#!/usr/bin/env python3

import json

import analyze # located in this repo
from typing import Dict, Any, Iterable, Tuple, Union, List, Set

template_str = {
    int: 'Long', # TODO figure out if anything should be Long
    str: 'Text',
    float: 'Double',
    bool: 'Boolean',
}

class Single(object): # TODO
    pass

class Reason(object):
    def __init__(self, t: type, s: str) -> None:
        self.t = t
        self.s = s

class Nested(object):
    def __init__(self, multi: bool, properties: Dict[str, Any], level: int) -> None:
        self.multi = multi
        self.properties = properties
        self.level = level

    def __str__(self) -> str: # TODO handle comments better
        multi_str = "multi=True" if self.multi else ""
        if len(self.properties) == 0:
            return f'Object({multi_str})'
        prefix = f'Nested({multi_str + ", " if multi_str else ""}properties={{\n{self.level*4*" "}'
        sep = ',\n' + self.level * 4 * ' '
        end = '\n' + (self.level-1) * 4 * ' ' + '})'
        return prefix + sep.join([f'"{k}": {v}' for k, v in self.properties.items()]) + end

    def __getitem__(self, key:str) -> Any:
        return self.properties[key]

    def __setitem__(self, key:str, value:Any) -> None:
        self.properties[key] = value

enumerations = {
    'stringized': [],
    'floated': [],
    'int64_overflow': [],
    'nullable': [],
    'single_and_multi': [],
}

def templatize(obj: Union[List[Any], Dict[str, Any]], level:int=1, multi:bool=False, current_path:Tuple[str, ...]=()) -> Union[Nested, str]:
    multi_str = 'multi=True' if multi else ""
    extra_comments = []
    if isinstance(obj, list):
        types: Set[Any] = {type(e) for e in obj}
        if type(None) in types:
            enumerations['nullable'].append('.'.join(current_path))
            extra_comments.append('nullable')
            types.remove(type(None))

        if types == {int, float}: # upgrade to float
            enumerations['floated'].append('.'.join(current_path))
            extra_comments.append('upgraded to float')
            types.remove(int)
        elif int in types: # check for anything not fitting in a signed int64
            if any((isinstance(e, int) and e.bit_length() > 63) for e in obj):
                enumerations['int64_overflow'].append('.'.join(current_path))
                extra_comments.append('signed int64 overflow')

        if types == {list}: # elements appear as lists in original structure
            return str(templatize([e for l in obj for e in l], level, True, current_path)) + (', #' + '; '.join(extra_comments) if extra_comments else '')
        elif types == {dict}:
            merged: Dict[str, Any] = {}
            for e in obj:
                analyze.recursive_copy(e, merged)
            return str(templatize(analyze.unfreeze(merged), level, multi, current_path)) + (', #' + '; '.join(extra_comments) if extra_comments else '')
        elif list in types and len(types) == 2 or len(types) == 1:
            if list in types:
                multi_str = 'multi=True'
                enumerations['single_and_multi'].append('.'.join(current_path))
                extra_comments.append('single or multi')
                types.remove(list)
            return template_str[types.pop()] + f'({multi_str})' + (', #' + '; '.join(extra_comments) if extra_comments else '')
#        elif any(isinstance(e, Reason) for e in types):
#            r = [e for e in types if isinstance(e, Reason)][0]
#            if r.t is str:
#                stringized.append('.'.join(current_path))
#            return template_str[r.t] + f'({multi_str}), # {r.s}'
        elif str in types and not types & {list, dict}: # upgrade to string
            enumerations['stringized'].append('.'.join(current_path))
            extra_comments.append('multiple types: ' + ', '.join(sorted(map(lambda e: e.__name__, types))))
            return template_str[str] + f'({multi_str}), #' + '; '.join(extra_comments)
        elif len(types) == 0:
            return f'Object({multi_str})' + (', #' + '; '.join(extra_comments) if extra_comments else '')
        else:
            raise ValueError(f'multiple types {types=} {obj=}')

    elif isinstance(obj, dict):
        return Nested(properties={k: templatize(v, level+1, current_path=current_path + (k,)) for k, v in obj.items()}, level=level, multi=multi)
    else:
        raise ValueError(f'{type(obj)=} {obj=}')

def main() -> None:
    with open('results.json') as fd:
        data = json.load(fd)

    print('loaded')

    root = templatize(data)
    del data

    print('templatized')

    with open('template.py', 'w') as fd:
        fd.write('from elasticsearch_dsl import Document, Text, Nested, Boolean, Double, Object, Long\n\n'
                 'class ShodanBanner(Document):\n')

        for k, v in root.properties.items():
            fd.write(f'    {k} = {v}\n')

        for name, l in enumerations.items():
            fd.write(f'\n\n{name} = [\n')
            for s in l:
                fd.write(f'    "{s}",\n')
            fd.write(']\n')

    print('written')

if __name__ == '__main__':
    main()
