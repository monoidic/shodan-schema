#!/usr/bin/env python3

import json
import configparser
import datetime
import traceback
import itertools

import shodan
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index

from template import ShodanBanner, stringized_paths
from transformations import all_transformations

from typing import List, Dict, Any, TextIO, Callable, Set
from functools import partial

FilterFunc = Callable[['Filters', Dict[str, Any]], bool]

def make_l_decorator(l: List[FilterFunc]) -> Callable[[FilterFunc], FilterFunc]:
    def ret(f: FilterFunc) -> FilterFunc:
        l.append(f)
        return f

    return ret

# Collection of all of the filters to be used for
class Filters(object):
    filters: List[FilterFunc] = []

    def __init__(self, conf: configparser.ConfigParser) -> None:
        self.conf: Dict[str, Set[str]] = {section: set(json.loads(conf[section]['all'])) for section in ('services', 'devices', 'tags', 'sections', 'products')}

    add_filter = make_l_decorator(filters)

    @add_filter
    def has_vulns(self, datum: Dict[str, Any]) -> bool:
        '''Reported service has known vulnerabilities'''
        return 'vulns' in datum

#    @add_filter
    def has_filtered_service(self, datum: Dict[str, Any]) -> bool:
        '''A service which should preferably not be public for security reasons'''
        # TODO way too many false positives
        return datum['shodan']['module'] in self.conf['services']

    @add_filter
    def has_filtered_section(self, datum: Dict[str, Any]) -> bool:
        '''Hopefully a version of the above with less false positives'''
        return bool(datum.keys() & self.conf['sections'])

    @add_filter
    def has_filtered_tag(self, datum: Dict[str, Any]) -> bool:
        '''The service has been marked with an undesirable tag'''
        return 'tags' in datum and bool(set(datum['tags']) & self.conf['tags'])

    @add_filter
    def open_recursive_dns(self, datum: Dict[str, Any]) -> bool:
        '''Permits DNS amplification attacks'''
        return datum['transport'] == 'udp' and 'dns' in datum and datum['dns']['recursive']

    @add_filter
    def expired_cert(self, datum: Dict[str, Any]) -> bool:
        '''Reported service has an expired TLS certificate'''
        return 'ssl' in datum and datum["ssl"]["cert"]["expired"]

    def check_any(self, datum: Dict[str, Any]) -> bool:
        '''Check if datum matches any filters; returns a boolean indicating whether it did'''
        return any(map(lambda f: f(self, datum), self.filters))

    def check_all(self, datum: Dict[str, Any]) -> List[str]:
        '''Check all filters, returns a tuple with the names of the matched filters'''
        return [f.__name__ for f in self.filters if f(self, datum)]

def add_banner(fd: TextIO, banner: Dict[str, Any]) -> None:
    json.dump(banner, fd)
    fd.write('\n')
    fd.flush()

def main() -> None:
    conf = configparser.ConfigParser()
    conf.read('filters.conf')
    f_obj = Filters(conf)

    with open('conf.json') as fd:
        j_conf = json.load(fd)

    elastic_conf = j_conf['elastic']


    with open('samples.json', 'a') as raw_samples, open('transformed_samples.json', 'a') as samples:
        while True:
            api = shodan.Shodan(conf['main']['api_key'])
            with Elasticsearch(
                hosts=elastic_conf['cluster'],
                http_auth=(elastic_conf['username'], elastic_conf['password'])
            ) as client:
                index_name = elastic_conf['index_name'] # + datetime.datetime.now().strftime('-%Y-%m-%d')
                index = Index(index_name, using=client)
                doc_class = index.document(ShodanBanner)

                try:
#                    for banner in api.stream.alert():
#                    for banner in api.stream.countries(['ee']):
                    for banner in api.stream.banners():
                        add_banner(raw_samples, banner)
                        banner = all_transformations(banner)
                        matched_filters = f_obj.check_all(banner)
                        banner['extra.filter_reason'] = ','.join(matched_filters)
                        banner['extra.filtered'] = bool(matched_filters)
                        add_banner(samples, banner)

                        # TODO can you force type transformation in ES itself?
#                        doc = doc_class(**banner)
#                        doc.save(using=client)
                except Exception as e:
                    print(f'{e=}')
                    traceback.print_exc()
#                    raise

if __name__ == '__main__':
    main()
