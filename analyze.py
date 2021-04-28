#!/usr/bin/env python3

import json
import collections
import collections.abc
import immutabledict

from transformations import all_transformations

from typing import Dict, Any, Callable, List, Tuple, Union, Set, cast
from abc import ABCMeta

def recursive_freeze(obj: Any) -> Any:
    for iface, f in _freeze_functions:
        if isinstance(obj, iface):
            return f(obj)
    raise ValueError(f'{type(obj)} {obj}')

_freeze_functions: List[Tuple[ABCMeta, Callable[[Any], Any]]] = [
    (collections.abc.Hashable, lambda e: e),
    (collections.abc.Mapping, lambda d: immutabledict.immutabledict({k: recursive_freeze(v) for k, v in d.items()})),
    (collections.abc.Sequence, lambda l: tuple(recursive_freeze(e) for e in l)),
]

def recursive_copy(source: Dict[str, Any], target: Dict[str, Union[Dict[str, Any], Set[Any]]]) -> None:
    try:
        for k, v in source.items():
            if isinstance(v, (str, int, float, bool, type(None))):
                target_set = target.setdefault(k, set())
                if not isinstance(target_set, set):
                    target_set = cast(Set[Any], target_set.setdefault('__set_values', set()))
                target_set.add(v)
            elif isinstance(v, list):
                add_to = target.setdefault(k, set())
                if not isinstance(add_to, set):
                    add_to = cast(Set[Any], add_to.setdefault('__set_values', set()))
#                    print(f'add_to not set {k=} {v=} {type(target)=}')
#                print(v)
#                if len(add_to) > 1000:
#                    return
                add_to.add(recursive_freeze(v))
            elif isinstance(v, dict):
                target_d = target.setdefault(k, {})
                if not isinstance(target_d, dict):
                    target_d = {'__set_values': target_d}
                    target[k] = target_d
                recursive_copy(source[k], target_d)
            else:
                raise ValueError(f'value {k=} {v=}')
    except Exception as e:
        print(f'some exception: {e=} {k=} {v=} {type(target)=}')
        raise

_mappings: List[Tuple[List[type], Callable[[Any], Any]]] = [
    ([int, float, str, bool, type(None)], lambda e: e),
    ([set, list, tuple], lambda d: sorted((unfreeze(e) for e in d), key=lambda e: str(e).lower())),
    ([dict, immutabledict.immutabledict], lambda d: {k: unfreeze(v) for k, v in d.items()}),
]
_unfreeze_map: Dict[type, Callable[[Any], Any]] = {t: f for t_l, f in _mappings for t in t_l}

def unfreeze(d: Any) -> Any:
    f = _unfreeze_map.get(type(d))
    if f is None:
        raise ValueError(str(type(d)))

    return f(d)

def immutable_default(e):
    if isinstance(e, (set, tuple)):
        return list(e)
    elif isinstance(e, immutabledict.immutabledict):
        return dict(e)
    else:
        raise ValueError(f'Unhandled type: {type(e)}')

def main() -> None:
    known_values: Dict[str, Any] = {}
    with open('samples.json') as fd:
        for i, line in enumerate(fd):
            try:
                datum = json.loads(line)
                datum = all_transformations(datum, False)
                recursive_copy(datum, known_values)
                print(i+1, end='\r')
            except json.decoder.JSONDecodeError:
                print('error on', i+1)

    print('samples merged')

    with open('results.json', 'w') as fd:
        json.dump(known_values, fd, indent=4, sort_keys=True, default=immutable_default)

    print('dumped')

if __name__ == '__main__':
    main()
