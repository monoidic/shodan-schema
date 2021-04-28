#!/usr/bin/env python3

import re
import itertools

from functools import partial
from typing import Dict, Any, List, Callable, Iterable, Tuple, Union

from template import stringized

_ntp_numbers_pattern = re.compile('^refid|[0-9-]+')
_remove_underscore_prefix = partial(re.compile('^_*').sub, '')

def _redis_fix(addr: Union[str, Tuple[str, int]]) -> str:
    if isinstance(addr, str):
        return addr
    elif addr[0].startswith('/'):
        return addr[0]
    else:
        return f'{addr[0]}:{addr[1]}'

# try to ensure stability (i.e if f(A) -> f(B), then f(B) -> f(B)
def transformations(banner: Dict[str, Any], stringize:bool=True) -> None:
    # move {key: values} based identifiers to [{values, key_value: key}, ...] to simplify the schema
    # values under 'mac' can be None, hence the **(v if v else {})
    for identifier, paths in [
        ('identifier', ['vulns', 'elastic.indices', 'elastic.nodes.nodes', 'elastic.nodes.nodes.thread_pool', 'ftp.features',
                        'http.components', 'mongodb.serverStatus.metrics.commands', 'mongodb.serverStatus.locks', 'mongodb.serverStatus.recordStats',
                        'rsync.modules']),
        ('address', ['mac']),
    ]:
        for split_path in map(lambda p: p.split('.'), paths):
            _transformations_recurse(banner, split_path, lambda d: [{**(v if v and isinstance(v, dict) else ({} if isinstance(v, dict) else {'__set_values': v})), identifier: k} for k, v in d.items()])

    # remove keys like 52644862-1952644862
    if 'ntp' in banner:
        banner['ntp'] = {k: v for k, v in banner['ntp'].items() if k == 'refid' or _ntp_numbers_pattern.sub('', k)}

    f_field_map: List[Tuple[Callable[[Any], Any], Iterable[str]]] = [
        (_redis_fix, ('redis.clients.addr',)),
        (lambda e: float(e) if e else 0.0, ('vulns.cvss',)), # can be None
    ]
    if stringize:
        f_field_map.append((lambda e: str(e), stringized))

    for f, field_paths in f_field_map:
        for field_path in map(lambda s: s.split('.'), field_paths):
            _transformations_recurse(banner, field_path, f)


def _transformations_recurse(element: Dict[str, Any], remaining_path: List[str], f: Callable[[Any], Any]) -> None:
    section = remaining_path[0]
    if not isinstance(element, dict) or section not in element:
        return # section not included as a child of this node
    next_e = element[section]
    next_path = remaining_path[1:]
    if not next_path: # is final node
        try:
            element[section] = f(next_e)
        except:
            print(f'{remaining_path=} {f=} {element=}')
            raise
    else: # is not final node
        if isinstance(next_e, list):
            for e in next_e:
                _transformations_recurse(e, next_path, f)
        else:
            _transformations_recurse(next_e, next_path, f)


def clear_empty_keys(banner: Any) -> Any: # gets rid of empty keys
    mapping: Dict[type, Callable[[], Any]] = {
        list: lambda: [clear_empty_keys(e) for e in banner],
        dict: lambda: {k: clear_empty_keys(v) for k, v in banner.items() if k},
    }
    f = mapping.get(type(banner), lambda: banner)
    return f()

def all_transformations(banner: Dict[str, Any], stringize:bool=True) -> Dict[str, Any]:
    # toggle stringize off on on template generation
    banner = clear_empty_keys(banner)
    banner = {_remove_underscore_prefix(k): v for k, v in banner.items()}
    transformations(banner, stringize)
    return banner
