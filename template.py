from elasticsearch_dsl import Document, Text, Nested, Boolean, Double, Object, Long

class ShodanBanner(Document):
    afp = Nested(properties={
        "afp_versions": Text(multi=True),
        "directory_names": Text(multi=True),
        "machine_type": Text(),
        "network_addresses": Text(multi=True), #nullable,
        "server_flags": Nested(properties={
            "copy_file": Boolean(),
            "flag_hex": Text(),
            "open_directory": Boolean(),
            "password_changing": Boolean(),
            "password_saving_prohibited": Boolean(),
            "reconnect": Boolean(),
            "server_messages": Boolean(),
            "server_notifications": Boolean(),
            "server_signature": Boolean(),
            "super_client": Boolean(),
            "tcp_ip": Boolean(),
            "utf8_server_name": Boolean(),
            "uuids": Boolean()
        }),
        "server_name": Text(),
        "server_signature": Text(),
        "uams": Text(multi=True),
        "utf8_server_name": Text()
    })
    android_debug_bridge = Nested(properties={
        "device": Text(),
        "features": Text(multi=True),
        "model": Text(),
        "name": Text()
    })
    asn = Text()
    bgp = Nested(properties={
        "messages": Nested(multi=True, properties={
            "asn": Long(),
            "bgp_identifier": Text(),
            "hold_time": Long(),
            "length": Long(),
            "type": Text(),
            "version": Long(),
            "error_code": Text(),
            "error_subcode": Text()
        })
    })
    cassandra = Nested(properties={
        "keyspaces": Text(multi=True),
        "name": Text(),
        "partitioner": Text(),
        "snitch": Text(),
        "version": Text()
    })
    checkpoint = Nested(properties={
        "firewall_host": Text(),
        "smartcenter_host": Text()
    })
    chromecast = Nested(properties={
        "build_info": Nested(properties={
            "build_type": Long(),
            "cast_build_revision": Text(),
            "cast_control_version": Long(),
            "release_track": Text(),
            "system_build_number": Text()
        }),
        "device_info": Nested(properties={
            "cloud_device_id": Text(),
            "device_name": Text(),
            "hotspot_bssid": Text(),
            "mac_address": Text(),
            "manufacturer": Text(),
            "model_name": Text(),
            "product_name": Text(),
            "public_key": Text(),
            "ssdp_udn": Text(),
            "uma_client_id": Text()
        }),
        "net": Nested(properties={
            "ethernet_connected": Boolean(),
            "ip_address": Text(),
            "online": Boolean()
        }),
        "version": Long(),
        "wifi": Nested(properties={
            "bssid": Text(),
            "ssid": Text()
        })
    })
    cloud = Nested(properties={
        "provider": Text(),
        "region": Text(), #nullable,
        "service": Text(), #nullable
    })
    coap = Nested(properties={
        "resources": Nested(properties={
            "/": Nested(properties={
                "ct": Text(),
                "title": Text()
            }),
            "/.well-known/core": Object(),
            "/api": Object(),
            "/api/v1": Object(),
            "/bs": Object(),
            "/dp": Object(),
            "/efento": Object(),
            "/efento/m": Object(),
            "/info": Object(),
            "/mirror": Object(),
            "/ndm/ci": Object(),
            "/ndm/dis": Object(),
            "/ndm/login": Object(),
            "/ndm/logout": Object(),
            "/qlink": Object(),
            "/qlink/ack": Nested(properties={
                "title": Text()
            }),
            "/qlink/addgw": Object(),
            "/qlink/netinfo": Object(),
            "/qlink/querygw": Object(),
            "/qlink/request": Nested(properties={
                "title": Text()
            }),
            "/qlink/searchack": Object(),
            "/qlink/searchdevice": Nested(properties={
                "title": Text()
            }),
            "/rd": Nested(properties={
                "rt": Text()
            }),
            "/register": Object(),
            "/station": Nested(properties={
                "ct": Object(), #nullable,
                "title": Text()
            }),
            "/uhp": Object(),
            "/uspagent": Nested(properties={
                "obs": Object(), #nullable
            })
        })
    })
    consul = Nested(properties={
        "ACLDatacenter": Text(),
        "ACLDefaultPolicy": Text(),
        "ACLDisabledTTL": Long(),
        "ACLDownPolicy": Text(),
        "ACLEnforceVersion8": Boolean(),
        "ACLTTL": Long(),
        "ACLTTLRaw": Text(),
        "Addresses": Nested(properties={
            "DNS": Text(),
            "HTTP": Text(),
            "HTTPS": Text(),
            "RPC": Text()
        }),
        "AdvertiseAddr": Text(),
        "AdvertiseAddrWan": Text(),
        "AdvertiseAddrs": Nested(properties={
            "RPC": Object(), #nullable,
            "RPCRaw": Text(),
            "SerfLan": Object(), #nullable,
            "SerfLanRaw": Text(),
            "SerfWan": Object(), #nullable,
            "SerfWanRaw": Text()
        }),
        "Autopilot": Nested(properties={
            "CleanupDeadServers": Object(), #nullable,
            "DisableUpgradeMigration": Object(), #nullable,
            "LastContactThresholdRaw": Text(),
            "MaxTrailingLogs": Object(), #nullable,
            "RedundancyZoneTag": Text(),
            "ServerStabilizationTimeRaw": Text(),
            "UpgradeVersionTag": Text()
        }),
        "BindAddr": Text(),
        "Bootstrap": Boolean(),
        "BootstrapExpect": Long(),
        "CAFile": Text(),
        "CAPath": Text(),
        "CertFile": Text(),
        "CheckDeregisterIntervalMin": Long(),
        "CheckReapInterval": Long(),
        "CheckUpdateInterval": Long(),
        "ClientAddr": Text(),
        "DNSConfig": Nested(properties={
            "AllowStale": Boolean(),
            "DisableCompression": Boolean(),
            "EnableTruncate": Boolean(),
            "MaxStale": Long(),
            "NodeTTL": Long(),
            "OnlyPassing": Boolean(),
            "RecursorTimeout": Long(),
            "ServiceTTL": Object(), #nullable,
            "UDPAnswerLimit": Long()
        }),
        "DNSRecursor": Text(),
        "DNSRecursors": Object(multi=True),
        "DataDir": Text(),
        "Datacenter": Text(),
        "DeprecatedHTTPAPIResponseHeaders": Object(), #nullable,
        "DeprecatedRetryJoinAzure": Nested(properties={
            "TagName": Text(),
            "TagValue": Text()
        }),
        "DeprecatedRetryJoinEC2": Nested(properties={
            "Region": Text(),
            "TagKey": Text(),
            "TagValue": Text()
        }),
        "DeprecatedRetryJoinGCE": Nested(properties={
            "CredentialsFile": Text(),
            "ProjectName": Text(),
            "TagValue": Text(),
            "ZonePattern": Text()
        }),
        "DevMode": Boolean(),
        "DisableAnonymousSignature": Boolean(),
        "DisableCoordinates": Boolean(),
        "DisableHostNodeID": Boolean(),
        "DisableKeyringFile": Boolean(),
        "DisableRemoteExec": Boolean(),
        "DisableUpdateCheck": Boolean(),
        "Domain": Text(),
        "EnableACLReplication": Boolean(),
        "EnableDebug": Boolean(),
        "EnableScriptChecks": Boolean(),
        "EnableSyslog": Boolean(),
        "EnableUI": Boolean(),
        "EncryptVerifyIncoming": Boolean(),
        "EncryptVerifyOutgoing": Boolean(),
        "HTTPConfig": Nested(properties={
            "BlockEndpoints": Object(), #nullable,
            "ResponseHeaders": Object(), #nullable
        }),
        "KeyFile": Text(),
        "LeaveOnTerm": Boolean(),
        "Limits": Nested(properties={
            "RPCMaxBurst": Long(),
            "RPCRate": Double()
        }),
        "LogLevel": Text(),
        "NodeID": Text(),
        "NodeName": Text(),
        "NonVotingServer": Boolean(),
        "Performance": Nested(properties={
            "RaftMultiplier": Long()
        }),
        "PidFile": Text(),
        "Ports": Nested(properties={
            "DNS": Long(),
            "HTTP": Long(),
            "HTTPS": Long(),
            "RPC": Long(),
            "SerfLan": Long(),
            "SerfWan": Long(),
            "Server": Long()
        }),
        "Protocol": Long(),
        "RaftProtocol": Long(),
        "ReconnectTimeoutLan": Long(),
        "ReconnectTimeoutLanRaw": Text(),
        "ReconnectTimeoutWan": Long(),
        "ReconnectTimeoutWanRaw": Text(),
        "RejoinAfterLeave": Boolean(),
        "RetryIntervalRaw": Text(),
        "RetryIntervalWanRaw": Text(),
        "RetryJoinWan": Object(multi=True),
        "RetryMaxAttempts": Long(),
        "RetryMaxAttemptsWan": Long(),
        "Revision": Text(),
        "Segment": Text(),
        "Segments": Object(), #nullable,
        "SerfLanBindAddr": Text(),
        "SerfWanBindAddr": Text(),
        "Server": Boolean(),
        "ServerName": Text(),
        "SessionTTLMin": Long(),
        "SessionTTLMinRaw": Text(),
        "SkipLeaveOnInt": Boolean(),
        "StartJoin": Object(multi=True),
        "StartJoinWan": Object(multi=True),
        "SyslogFacility": Text(),
        "TLSCipherSuitesRaw": Text(),
        "TLSMinVersion": Text(),
        "TLSPreferServerCipherSuites": Boolean(),
        "TaggedAddresses": Nested(properties={
            "lan": Text(),
            "wan": Text()
        }),
        "Telemetry": Nested(properties={
            "CirconusAPIApp": Text(),
            "CirconusAPIURL": Text(),
            "CirconusBrokerID": Text(),
            "CirconusBrokerSelectTag": Text(),
            "CirconusCheckDisplayName": Text(),
            "CirconusCheckForceMetricActivation": Text(),
            "CirconusCheckID": Text(),
            "CirconusCheckInstanceID": Text(),
            "CirconusCheckSearchTag": Text(),
            "CirconusCheckSubmissionURL": Text(),
            "CirconusCheckTags": Text(),
            "CirconusSubmissionInterval": Text(),
            "DisableHostname": Boolean(),
            "DogStatsdAddr": Text(),
            "DogStatsdTags": Object(), #nullable,
            "FilterDefault": Boolean(),
            "PrefixFilter": Object(), #nullable,
            "StatsdAddr": Text(),
            "StatsiteAddr": Text(),
            "StatsitePrefix": Text()
        }),
        "TranslateWanAddrs": Boolean(),
        "UIDir": Text(),
        "UnixSockets": Nested(properties={
            "Grp": Text(),
            "Perms": Text(),
            "Usr": Text()
        }),
        "VerifyIncoming": Boolean(),
        "VerifyIncomingHTTPS": Boolean(),
        "VerifyIncomingRPC": Boolean(),
        "VerifyOutgoing": Boolean(),
        "VerifyServerHostname": Boolean(),
        "Version": Text(),
        "VersionPrerelease": Text(),
        "Watches": Object(), #nullable
    })
    couchdb = Nested(properties={
        "couchdb": Text(),
        "dbs": Text(multi=True),
        "features": Text(multi=True),
        "git_sha": Text(),
        "http_headers": Text(),
        "uuid": Text(),
        "vendor": Nested(properties={
            "name": Text(),
            "version": Text()
        }),
        "version": Text()
    })
    cpe = Text(multi=True)
    cpe23 = Text(multi=True)
    data = Text()
    device = Text()
    devicetype = Text()
    dns = Nested(properties={
        "recursive": Boolean(),
        "resolver_hostname": Text(), #nullable,
        "resolver_id": Text(), #nullable,
        "software": Text(), #nullable
    })
    domains = Text(multi=True)
    elastic = Nested(properties={
        "cluster": Nested(properties={
            "_nodes": Nested(properties={
                "failed": Long(),
                "successful": Long(),
                "total": Long()
            }),
            "cluster_name": Text(),
            "cluster_uuid": Text(),
            "indices": Nested(properties={
                "analysis": Nested(properties={
                    "analyzer_types": Nested(multi=True, properties={
                        "count": Long(),
                        "index_count": Long(),
                        "name": Text()
                    }),
                    "built_in_analyzers": Nested(multi=True, properties={
                        "count": Long(),
                        "index_count": Long(),
                        "name": Text()
                    }),
                    "built_in_char_filters": Object(multi=True),
                    "built_in_filters": Nested(multi=True, properties={
                        "count": Long(),
                        "index_count": Long(),
                        "name": Text()
                    }),
                    "built_in_tokenizers": Nested(multi=True, properties={
                        "count": Long(),
                        "index_count": Long(),
                        "name": Text()
                    }),
                    "char_filter_types": Nested(multi=True, properties={
                        "count": Long(),
                        "index_count": Long(),
                        "name": Text()
                    }),
                    "filter_types": Nested(multi=True, properties={
                        "count": Long(),
                        "index_count": Long(),
                        "name": Text()
                    }),
                    "tokenizer_types": Nested(multi=True, properties={
                        "count": Long(),
                        "index_count": Long(),
                        "name": Text()
                    })
                }),
                "completion": Nested(properties={
                    "size_in_bytes": Long()
                }),
                "count": Long(),
                "docs": Nested(properties={
                    "count": Long(),
                    "deleted": Long()
                }),
                "fielddata": Nested(properties={
                    "evictions": Long(),
                    "memory_size_in_bytes": Long()
                }),
                "filter_cache": Nested(properties={
                    "evictions": Long(),
                    "memory_size_in_bytes": Long()
                }),
                "id_cache": Nested(properties={
                    "memory_size_in_bytes": Long()
                }),
                "mappings": Nested(properties={
                    "field_types": Nested(multi=True, properties={
                        "count": Long(),
                        "index_count": Long(),
                        "name": Text()
                    })
                }),
                "percolate": Nested(properties={
                    "current": Long(),
                    "memory_size": Text(),
                    "memory_size_in_bytes": Long(),
                    "queries": Long(),
                    "time_in_millis": Long(),
                    "total": Long()
                }),
                "query_cache": Nested(properties={
                    "cache_count": Long(),
                    "cache_size": Long(),
                    "evictions": Long(),
                    "hit_count": Long(),
                    "memory_size_in_bytes": Long(),
                    "miss_count": Long(),
                    "total_count": Long()
                }),
                "segments": Nested(properties={
                    "count": Long(),
                    "doc_values_memory_in_bytes": Long(),
                    "file_sizes": Object(),
                    "fixed_bit_set_memory_in_bytes": Long(),
                    "index_writer_max_memory_in_bytes": Long(),
                    "index_writer_memory_in_bytes": Long(),
                    "max_unsafe_auto_id_timestamp": Long(), #signed int64 overflow,
                    "memory_in_bytes": Long(),
                    "norms_memory_in_bytes": Long(),
                    "points_memory_in_bytes": Long(),
                    "stored_fields_memory_in_bytes": Long(),
                    "term_vectors_memory_in_bytes": Long(),
                    "terms_memory_in_bytes": Long(),
                    "version_map_memory_in_bytes": Long()
                }),
                "shards": Nested(properties={
                    "index": Nested(properties={
                        "primaries": Nested(properties={
                            "avg": Double(),
                            "max": Long(),
                            "min": Long()
                        }),
                        "replication": Nested(properties={
                            "avg": Double(),
                            "max": Double(),
                            "min": Double()
                        }),
                        "shards": Nested(properties={
                            "avg": Double(),
                            "max": Long(),
                            "min": Long()
                        })
                    }),
                    "primaries": Long(),
                    "replication": Double(),
                    "total": Long()
                }),
                "store": Nested(properties={
                    "reserved_in_bytes": Long(),
                    "size_in_bytes": Long(),
                    "throttle_time_in_millis": Long()
                }),
                "versions": Nested(multi=True, properties={
                    "index_count": Long(),
                    "primary_shard_count": Long(),
                    "total_primary_bytes": Long(),
                    "version": Text()
                })
            }),
            "nodes": Nested(properties={
                "count": Nested(properties={
                    "client": Long(),
                    "coordinating_only": Long(),
                    "data": Long(),
                    "data_cold": Long(),
                    "data_content": Long(),
                    "data_frozen": Long(),
                    "data_hot": Long(),
                    "data_only": Long(),
                    "data_warm": Long(),
                    "ingest": Long(),
                    "master": Long(),
                    "master_data": Long(),
                    "master_only": Long(),
                    "ml": Long(),
                    "remote_cluster_client": Long(),
                    "total": Long(),
                    "transform": Long(),
                    "voting_only": Long()
                }),
                "discovery_types": Nested(properties={
                    "single-node": Long(),
                    "zen": Long()
                }),
                "fs": Nested(properties={
                    "available_in_bytes": Long(),
                    "disk_io_op": Long(),
                    "disk_io_size_in_bytes": Long(),
                    "disk_queue": Text(),
                    "disk_read_size_in_bytes": Long(),
                    "disk_reads": Long(),
                    "disk_service_time": Text(),
                    "disk_write_size_in_bytes": Long(),
                    "disk_writes": Long(),
                    "free_in_bytes": Long(),
                    "spins": Text(),
                    "total_in_bytes": Long()
                }),
                "ingest": Nested(properties={
                    "number_of_pipelines": Long(),
                    "processor_stats": Nested(properties={
                        "attachment": Nested(properties={
                            "count": Long(),
                            "current": Long(),
                            "failed": Long(),
                            "time_in_millis": Long()
                        }),
                        "convert": Nested(properties={
                            "count": Long(),
                            "current": Long(),
                            "failed": Long(),
                            "time_in_millis": Long()
                        }),
                        "gsub": Nested(properties={
                            "count": Long(),
                            "current": Long(),
                            "failed": Long(),
                            "time_in_millis": Long()
                        }),
                        "remove": Nested(properties={
                            "count": Long(),
                            "current": Long(),
                            "failed": Long(),
                            "time_in_millis": Long()
                        }),
                        "rename": Nested(properties={
                            "count": Long(),
                            "current": Long(),
                            "failed": Long(),
                            "time_in_millis": Long()
                        }),
                        "script": Nested(properties={
                            "count": Long(),
                            "current": Long(),
                            "failed": Long(),
                            "time_in_millis": Long()
                        }),
                        "set": Nested(properties={
                            "count": Long(),
                            "current": Long(),
                            "failed": Long(),
                            "time_in_millis": Long()
                        })
                    })
                }),
                "jvm": Nested(properties={
                    "max_uptime_in_millis": Long(),
                    "mem": Nested(properties={
                        "heap_max_in_bytes": Long(),
                        "heap_used_in_bytes": Long()
                    }),
                    "threads": Long(),
                    "versions": Nested(multi=True, properties={
                        "count": Long(),
                        "version": Text(),
                        "vm_name": Text(),
                        "vm_vendor": Text(),
                        "vm_version": Text(),
                        "bundled_jdk": Boolean(),
                        "using_bundled_jdk": Boolean()
                    })
                }),
                "network_types": Nested(properties={
                    "http_types": Nested(properties={
                        "filter-jetty": Long(),
                        "netty4": Long(),
                        "security4": Long()
                    }),
                    "transport_types": Nested(properties={
                        "com.amazon.opendistroforelasticsearch.security.ssl.http.netty.OpenDistroSecuritySSLNettyTransport": Long(),
                        "netty4": Long(),
                        "security4": Long()
                    })
                }),
                "os": Nested(properties={
                    "allocated_processors": Text(), #multiple types: int, str,
                    "architectures": Nested(multi=True, properties={
                        "arch": Text(),
                        "count": Long()
                    }),
                    "available_processors": Text(), #multiple types: int, str,
                    "cpu": Nested(multi=True, properties={
                        "cache_size_in_bytes": Long(),
                        "cores_per_socket": Long(),
                        "count": Long(),
                        "mhz": Long(),
                        "model": Text(),
                        "total_cores": Long(),
                        "total_sockets": Long(),
                        "vendor": Text()
                    }),
                    "mem": Nested(properties={
                        "free_in_bytes": Long(),
                        "free_percent": Long(),
                        "total_in_bytes": Long(),
                        "used_in_bytes": Long(),
                        "used_percent": Long()
                    }),
                    "names": Nested(multi=True, properties={
                        "count": Long(),
                        "name": Text()
                    }),
                    "pretty_names": Nested(multi=True, properties={
                        "count": Long(),
                        "pretty_name": Text()
                    })
                }),
                "packaging_types": Nested(multi=True, properties={
                    "count": Long(),
                    "flavor": Text(),
                    "type": Text()
                }),
                "plugins": Nested(multi=True, properties={
                    "classname": Text(),
                    "description": Text(),
                    "elasticsearch_version": Text(),
                    "extended_plugins": Object(multi=True),
                    "has_native_controller": Boolean(),
                    "java_version": Text(),
                    "name": Text(),
                    "version": Text(),
                    "jvm": Boolean(),
                    "site": Boolean(),
                    "url": Text(),
                    "isolated": Boolean()
                }),
                "process": Nested(properties={
                    "cpu": Nested(properties={
                        "percent": Long()
                    }),
                    "open_file_descriptors": Nested(properties={
                        "avg": Long(),
                        "max": Long(),
                        "min": Long()
                    })
                }),
                "versions": Text(multi=True)
            }),
            "status": Text(),
            "timestamp": Long()
        }),
        "indices": Nested(multi=True, properties={
            "identifier": Text(),
            "primaries": Nested(properties={
                "docs": Nested(properties={
                    "count": Long(),
                    "deleted": Long()
                }),
                "indexing": Nested(properties={
                    "delete_current": Long(),
                    "delete_time_in_millis": Long(),
                    "delete_total": Long(),
                    "index_current": Long(),
                    "index_failed": Long(),
                    "index_time_in_millis": Long(),
                    "index_total": Long(),
                    "is_throttled": Boolean(),
                    "noop_update_total": Long(),
                    "throttle_time_in_millis": Long()
                }),
                "store": Nested(properties={
                    "reserved_in_bytes": Long(),
                    "size_in_bytes": Long(),
                    "throttle_time_in_millis": Long()
                }),
                "completion": Nested(properties={
                    "size_in_bytes": Long()
                }),
                "fielddata": Nested(properties={
                    "evictions": Long(),
                    "memory_size_in_bytes": Long()
                }),
                "flush": Nested(properties={
                    "periodic": Long(),
                    "total": Long(),
                    "total_time_in_millis": Long()
                }),
                "get": Nested(properties={
                    "current": Long(),
                    "exists_time_in_millis": Long(),
                    "exists_total": Long(),
                    "missing_time_in_millis": Long(),
                    "missing_total": Long(),
                    "time_in_millis": Long(),
                    "total": Long()
                }),
                "merges": Nested(properties={
                    "current": Long(),
                    "current_docs": Long(),
                    "current_size_in_bytes": Long(),
                    "total": Long(),
                    "total_auto_throttle_in_bytes": Long(),
                    "total_docs": Long(),
                    "total_size_in_bytes": Long(),
                    "total_stopped_time_in_millis": Long(),
                    "total_throttled_time_in_millis": Long(),
                    "total_time_in_millis": Long()
                }),
                "query_cache": Nested(properties={
                    "cache_count": Long(),
                    "cache_size": Long(),
                    "evictions": Long(),
                    "hit_count": Long(),
                    "memory_size_in_bytes": Long(),
                    "miss_count": Long(),
                    "total_count": Long()
                }),
                "recovery": Nested(properties={
                    "current_as_source": Long(),
                    "current_as_target": Long(),
                    "throttle_time_in_millis": Long()
                }),
                "refresh": Nested(properties={
                    "external_total": Long(),
                    "external_total_time_in_millis": Long(),
                    "listeners": Long(),
                    "total": Long(),
                    "total_time_in_millis": Long()
                }),
                "request_cache": Nested(properties={
                    "evictions": Long(),
                    "hit_count": Long(),
                    "memory_size_in_bytes": Long(),
                    "miss_count": Long()
                }),
                "search": Nested(properties={
                    "fetch_current": Long(),
                    "fetch_time_in_millis": Long(),
                    "fetch_total": Long(),
                    "open_contexts": Long(),
                    "query_current": Long(),
                    "query_time_in_millis": Long(),
                    "query_total": Long(),
                    "scroll_current": Long(),
                    "scroll_time_in_millis": Long(),
                    "scroll_total": Long(),
                    "suggest_current": Long(),
                    "suggest_time_in_millis": Long(),
                    "suggest_total": Long()
                }),
                "segments": Nested(properties={
                    "count": Long(),
                    "doc_values_memory_in_bytes": Long(),
                    "file_sizes": Object(),
                    "fixed_bit_set_memory_in_bytes": Long(),
                    "index_writer_memory_in_bytes": Long(),
                    "max_unsafe_auto_id_timestamp": Long(),
                    "memory_in_bytes": Long(),
                    "norms_memory_in_bytes": Long(),
                    "points_memory_in_bytes": Long(),
                    "stored_fields_memory_in_bytes": Long(),
                    "term_vectors_memory_in_bytes": Long(),
                    "terms_memory_in_bytes": Long(),
                    "version_map_memory_in_bytes": Long()
                }),
                "translog": Nested(properties={
                    "earliest_last_modified_age": Long(),
                    "operations": Long(),
                    "size_in_bytes": Long(),
                    "uncommitted_operations": Long(),
                    "uncommitted_size_in_bytes": Long()
                }),
                "warmer": Nested(properties={
                    "current": Long(),
                    "total": Long(),
                    "total_time_in_millis": Long()
                })
            }),
            "total": Nested(properties={
                "docs": Nested(properties={
                    "count": Long(),
                    "deleted": Long()
                }),
                "indexing": Nested(properties={
                    "delete_current": Long(),
                    "delete_time_in_millis": Long(),
                    "delete_total": Long(),
                    "index_current": Long(),
                    "index_failed": Long(),
                    "index_time_in_millis": Long(),
                    "index_total": Long(),
                    "is_throttled": Boolean(),
                    "noop_update_total": Long(),
                    "throttle_time_in_millis": Long()
                }),
                "store": Nested(properties={
                    "reserved_in_bytes": Long(),
                    "size_in_bytes": Long(),
                    "throttle_time_in_millis": Long()
                }),
                "completion": Nested(properties={
                    "size_in_bytes": Long()
                }),
                "fielddata": Nested(properties={
                    "evictions": Long(),
                    "memory_size_in_bytes": Long()
                }),
                "flush": Nested(properties={
                    "periodic": Long(),
                    "total": Long(),
                    "total_time_in_millis": Long()
                }),
                "get": Nested(properties={
                    "current": Long(),
                    "exists_time_in_millis": Long(),
                    "exists_total": Long(),
                    "missing_time_in_millis": Long(),
                    "missing_total": Long(),
                    "time_in_millis": Long(),
                    "total": Long()
                }),
                "merges": Nested(properties={
                    "current": Long(),
                    "current_docs": Long(),
                    "current_size_in_bytes": Long(),
                    "total": Long(),
                    "total_auto_throttle_in_bytes": Long(),
                    "total_docs": Long(),
                    "total_size_in_bytes": Long(),
                    "total_stopped_time_in_millis": Long(),
                    "total_throttled_time_in_millis": Long(),
                    "total_time_in_millis": Long()
                }),
                "query_cache": Nested(properties={
                    "cache_count": Long(),
                    "cache_size": Long(),
                    "evictions": Long(),
                    "hit_count": Long(),
                    "memory_size_in_bytes": Long(),
                    "miss_count": Long(),
                    "total_count": Long()
                }),
                "recovery": Nested(properties={
                    "current_as_source": Long(),
                    "current_as_target": Long(),
                    "throttle_time_in_millis": Long()
                }),
                "refresh": Nested(properties={
                    "external_total": Long(),
                    "external_total_time_in_millis": Long(),
                    "listeners": Long(),
                    "total": Long(),
                    "total_time_in_millis": Long()
                }),
                "request_cache": Nested(properties={
                    "evictions": Long(),
                    "hit_count": Long(),
                    "memory_size_in_bytes": Long(),
                    "miss_count": Long()
                }),
                "search": Nested(properties={
                    "fetch_current": Long(),
                    "fetch_time_in_millis": Long(),
                    "fetch_total": Long(),
                    "open_contexts": Long(),
                    "query_current": Long(),
                    "query_time_in_millis": Long(),
                    "query_total": Long(),
                    "scroll_current": Long(),
                    "scroll_time_in_millis": Long(),
                    "scroll_total": Long(),
                    "suggest_current": Long(),
                    "suggest_time_in_millis": Long(),
                    "suggest_total": Long()
                }),
                "segments": Nested(properties={
                    "count": Long(),
                    "doc_values_memory_in_bytes": Long(),
                    "file_sizes": Object(),
                    "fixed_bit_set_memory_in_bytes": Long(),
                    "index_writer_memory_in_bytes": Long(),
                    "max_unsafe_auto_id_timestamp": Long(),
                    "memory_in_bytes": Long(),
                    "norms_memory_in_bytes": Long(),
                    "points_memory_in_bytes": Long(),
                    "stored_fields_memory_in_bytes": Long(),
                    "term_vectors_memory_in_bytes": Long(),
                    "terms_memory_in_bytes": Long(),
                    "version_map_memory_in_bytes": Long()
                }),
                "translog": Nested(properties={
                    "earliest_last_modified_age": Long(),
                    "operations": Long(),
                    "size_in_bytes": Long(),
                    "uncommitted_operations": Long(),
                    "uncommitted_size_in_bytes": Long()
                }),
                "warmer": Nested(properties={
                    "current": Long(),
                    "total": Long(),
                    "total_time_in_millis": Long()
                })
            }),
            "uuid": Text()
        }),
        "nodes": Nested(properties={
            "_nodes": Nested(properties={
                "failed": Long(),
                "successful": Long(),
                "total": Long()
            }),
            "cluster_name": Text(),
            "nodes": Nested(multi=True, properties={
                "attributes": Nested(properties={
                    "ml.enabled": Text(),
                    "ml.machine_memory": Text(),
                    "ml.max_open_jobs": Text(),
                    "xpack.installed": Text(),
                    "transform.node": Text(),
                    "ml.max_jvm_size": Text(),
                    "host": Text()
                }),
                "build_flavor": Text(),
                "build_hash": Text(),
                "build_type": Text(),
                "host": Text(),
                "http": Nested(properties={
                    "bound_address": Text(multi=True), #single or multi,
                    "max_content_length_in_bytes": Long(),
                    "publish_address": Text()
                }),
                "identifier": Text(),
                "ingest": Nested(properties={
                    "processors": Nested(multi=True, properties={
                        "type": Text()
                    })
                }),
                "ip": Text(),
                "jvm": Nested(properties={
                    "gc_collectors": Text(multi=True),
                    "input_arguments": Text(multi=True),
                    "mem": Nested(properties={
                        "direct_max_in_bytes": Long(),
                        "heap_init_in_bytes": Long(),
                        "heap_max_in_bytes": Long(),
                        "non_heap_init_in_bytes": Long(),
                        "non_heap_max_in_bytes": Long()
                    }),
                    "memory_pools": Text(multi=True),
                    "pid": Long(),
                    "start_time_in_millis": Long(),
                    "using_compressed_ordinary_object_pointers": Text(),
                    "version": Text(),
                    "vm_name": Text(),
                    "vm_vendor": Text(),
                    "vm_version": Text(),
                    "bundled_jdk": Boolean(),
                    "using_bundled_jdk": Boolean(), #nullable
                }),
                "modules": Nested(multi=True, properties={
                    "classname": Text(),
                    "description": Text(),
                    "elasticsearch_version": Text(),
                    "extended_plugins": Text(multi=True),
                    "has_native_controller": Boolean(),
                    "java_version": Text(),
                    "name": Text(),
                    "version": Text(),
                    "licensed": Boolean(),
                    "type": Text(),
                    "requires_keystore": Boolean(),
                    "isolated": Boolean(),
                    "jvm": Boolean(),
                    "site": Boolean()
                }),
                "name": Text(),
                "os": Nested(properties={
                    "allocated_processors": Long(),
                    "arch": Text(),
                    "available_processors": Text(), #multiple types: int, str,
                    "name": Text(),
                    "pretty_name": Text(),
                    "refresh_interval_in_millis": Long(),
                    "version": Text(),
                    "cpu": Nested(properties={
                        "cache_size_in_bytes": Long(),
                        "cores_per_socket": Long(),
                        "mhz": Long(),
                        "model": Text(),
                        "total_cores": Text(), #multiple types: int, str,
                        "total_sockets": Text(), #multiple types: int, str,
                        "vendor": Text()
                    }),
                    "mem": Nested(properties={
                        "total_in_bytes": Long()
                    }),
                    "swap": Nested(properties={
                        "total_in_bytes": Long()
                    })
                }),
                "plugins": Nested(multi=True, properties={
                    "classname": Text(),
                    "description": Text(),
                    "elasticsearch_version": Text(),
                    "extended_plugins": Text(multi=True),
                    "has_native_controller": Boolean(),
                    "java_version": Text(),
                    "name": Text(),
                    "version": Text(),
                    "requires_keystore": Boolean(),
                    "isolated": Boolean(),
                    "jvm": Boolean(),
                    "site": Boolean(),
                    "url": Text()
                }),
                "process": Nested(properties={
                    "id": Long(),
                    "mlockall": Boolean(),
                    "refresh_interval_in_millis": Long(),
                    "max_file_descriptors": Long()
                }),
                "roles": Text(multi=True),
                "settings": Nested(properties={
                    "bootstrap": Nested(properties={
                        "memory_lock": Text(),
                        "mlockall": Text()
                    }),
                    "client": Nested(properties={
                        "type": Text()
                    }),
                    "cluster": Nested(properties={
                        "name": Text(),
                        "election": Nested(properties={
                            "strategy": Text()
                        }),
                        "initial_master_nodes": Text(multi=True), #single or multi,
                        "routing": Nested(properties={
                            "allocation": Nested(properties={
                                "disk": Nested(properties={
                                    "threshold_enabled": Text()
                                })
                            })
                        }),
                        "remote": Nested(properties={
                            "connect": Text()
                        })
                    }),
                    "http": Nested(properties={
                        "type": Nested(properties={
                            "__set_values": Text(),
                            "default": Text()
                        }),
                        "type.default": Text(),
                        "cors": Nested(properties={
                            "allow-headers": Text(),
                            "allow-methods": Text(),
                            "allow-origin": Text(),
                            "enabled": Text(),
                            "allow-credentials": Text()
                        }),
                        "port": Text(),
                        "host": Text(),
                        "jsonp": Nested(properties={
                            "enable": Text()
                        }),
                        "max_initial_line_length": Text(),
                        "compression": Text(),
                        "max_content_length": Text()
                    }),
                    "network": Nested(properties={
                        "host": Text(),
                        "bind_host": Text(),
                        "publish_host": Text()
                    }),
                    "node": Nested(properties={
                        "attr": Nested(properties={
                            "ml": Nested(properties={
                                "enabled": Text(),
                                "machine_memory": Text(),
                                "max_open_jobs": Text(),
                                "max_jvm_size": Text()
                            }),
                            "xpack": Nested(properties={
                                "installed": Text()
                            }),
                            "transform": Nested(properties={
                                "node": Text()
                            }),
                            "host": Text()
                        }),
                        "name": Text(),
                        "master": Text(),
                        "pidfile": Text(),
                        "data": Text(),
                        "ingest": Text(),
                        "max_local_storage_nodes": Text(),
                        "ml": Text(),
                        "voting_only": Text()
                    }),
                    "path": Nested(properties={
                        "home": Text(),
                        "logs": Text(),
                        "data": Text(multi=True), #single or multi,
                        "plugins": Text(),
                        "work": Text(),
                        "repo": Text(multi=True),
                        "conf": Text()
                    }),
                    "transport": Nested(properties={
                        "features": Nested(properties={
                            "x-pack": Text()
                        }),
                        "type": Nested(properties={
                            "__set_values": Text(),
                            "default": Text()
                        }),
                        "type.default": Text(),
                        "host": Text(),
                        "tcp": Nested(properties={
                            "port": Text()
                        })
                    }),
                    "discovery": Nested(properties={
                        "seed_hosts": Text(multi=True), #single or multi,
                        "type": Text(),
                        "zen": Nested(properties={
                            "minimum_master_nodes": Text(),
                            "ping": Nested(properties={
                                "unicast": Nested(properties={
                                    "hosts": Text(multi=True), #single or multi
                                }),
                                "multicast": Nested(properties={
                                    "enabled": Text()
                                })
                            })
                        }),
                        "seed_providers": Text(),
                        "initial_state_timeout": Text()
                    }),
                    "pidfile": Text(),
                    "foreground": Text(),
                    "name": Text(),
                    "script": Nested(properties={
                        "groovy": Nested(properties={
                            "sandbox": Nested(properties={
                                "enabled": Text()
                            })
                        }),
                        "painless": Nested(properties={
                            "regex": Nested(properties={
                                "enabled": Text()
                            })
                        }),
                        "disable_dynamic": Text()
                    }),
                    "indices": Nested(properties={
                        "memory": Nested(properties={
                            "index_buffer_size": Text(),
                            "min_index_buffer_size": Text()
                        }),
                        "fielddata": Nested(properties={
                            "cache": Nested(properties={
                                "size": Text()
                            })
                        })
                    }),
                    "thread_pool": Nested(properties={
                        "bulk": Nested(properties={
                            "queue_size": Text()
                        }),
                        "index": Nested(properties={
                            "queue_size": Text()
                        }),
                        "search": Nested(properties={
                            "queue_size": Text()
                        })
                    }),
                    "xpack": Nested(properties={
                        "security": Nested(properties={
                            "enabled": Text(),
                            "authc": Nested(properties={
                                "realms": Nested(properties={
                                    "file": Nested(properties={
                                        "file1": Nested(properties={
                                            "order": Text()
                                        })
                                    }),
                                    "native": Nested(properties={
                                        "native1": Nested(properties={
                                            "order": Text()
                                        })
                                    })
                                }),
                                "reserved_realm": Nested(properties={
                                    "enabled": Text()
                                })
                            }),
                            "http": Nested(properties={
                                "ssl": Nested(properties={
                                    "enabled": Text()
                                })
                            }),
                            "transport": Nested(properties={
                                "ssl": Nested(properties={
                                    "enabled": Text()
                                })
                            }),
                            "audit": Nested(properties={
                                "enabled": Text()
                            })
                        }),
                        "ml": Nested(properties={
                            "enabled": Text()
                        }),
                        "license": Nested(properties={
                            "self_generated": Nested(properties={
                                "type": Text()
                            })
                        }),
                        "monitoring": Nested(properties={
                            "enabled": Text()
                        })
                    }),
                    "config": Nested(properties={
                        "ignore_system_properties": Text(),
                        "__set_values": Text()
                    }),
                    "action": Nested(properties={
                        "auto_create_index": Text(),
                        "destructive_requires_name": Text()
                    }),
                    "gateway": Nested(properties={
                        "recover_after_nodes": Text(),
                        "expected_nodes": Text(),
                        "recover_after_time": Text()
                    }),
                    "config.ignore_system_properties": Text(),
                    "index": Nested(properties={
                        "number_of_replicas": Text(),
                        "analysis": Nested(properties={
                            "analyzer": Nested(properties={
                                "default_index": Nested(properties={
                                    "alias": Text(multi=True),
                                    "char_filter": Text(multi=True),
                                    "filter": Text(multi=True),
                                    "tokenizer": Text(),
                                    "type": Text()
                                }),
                                "default_search": Nested(properties={
                                    "alias": Text(multi=True),
                                    "char_filter": Text(multi=True),
                                    "filter": Text(multi=True),
                                    "tokenizer": Text(),
                                    "type": Text()
                                })
                            }),
                            "char_filter": Nested(properties={
                                "ru": Nested(properties={
                                    "mappings": Text(multi=True),
                                    "type": Text()
                                })
                            }),
                            "filter": Nested(properties={
                                "custom_word_delimiter": Nested(properties={
                                    "catenate_all": Text(),
                                    "catenate_numbers": Text(),
                                    "catenate_words": Text(),
                                    "generate_number_parts": Text(),
                                    "generate_word_parts": Text(),
                                    "preserve_original": Text(),
                                    "split_on_case_change": Text(),
                                    "split_on_numerics": Text(),
                                    "type": Text()
                                }),
                                "stopwords_ru": Nested(properties={
                                    "ignore_case": Text(),
                                    "stopwords": Text(multi=True),
                                    "type": Text()
                                })
                            }),
                            "tokenizer": Nested(properties={
                                "nGram": Nested(properties={
                                    "max_gram": Text(),
                                    "min_gram": Text(),
                                    "type": Text()
                                })
                            })
                        }),
                        "number_of_shards": Text()
                    }),
                    "reindex": Nested(properties={
                        "remote": Nested(properties={
                            "whitelist": Text(multi=True)
                        })
                    })
                }),
                "thread_pool": Nested(multi=True, properties={
                    "core": Long(),
                    "identifier": Text(),
                    "keep_alive": Text(),
                    "max": Long(),
                    "queue_size": Text(), #multiple types: int, str,
                    "type": Text(),
                    "size": Long(),
                    "min": Long()
                }),
                "total_indexing_buffer": Long(),
                "transport": Nested(properties={
                    "bound_address": Text(multi=True), #single or multi,
                    "profiles": Object(),
                    "publish_address": Text()
                }),
                "transport_address": Text(),
                "version": Text(),
                "aggregations": Nested(properties={
                    "adjacency_matrix": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "auto_date_histogram": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "avg": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "boxplot": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "cardinality": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "children": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "composite": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "date_histogram": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "date_range": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "diversified_sampler": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "extended_stats": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "filter": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "filters": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "geo_bounds": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "geo_centroid": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "geo_distance": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "geohash_grid": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "geotile_grid": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "global": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "histogram": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "ip_range": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "matrix_stats": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "max": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "median_absolute_deviation": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "min": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "missing": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "nested": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "parent": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "percentile_ranks": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "percentiles": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "range": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "rare_terms": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "rate": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "reverse_nested": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "sampler": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "scripted_metric": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "significant_terms": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "significant_text": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "stats": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "string_stats": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "sum": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "t_test": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "terms": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "top_hits": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "top_metrics": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "value_count": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "variable_width_histogram": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "weighted_avg": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "geo_line": Nested(properties={
                        "types": Text(multi=True)
                    }),
                    "multi_terms": Nested(properties={
                        "types": Text(multi=True)
                    })
                }),
                "build": Text(),
                "http_address": Text(),
                "network": Nested(properties={
                    "primary_interface": Nested(properties={
                        "address": Text(),
                        "mac_address": Text(),
                        "name": Text()
                    }),
                    "refresh_interval_in_millis": Long()
                })
            })
        }),
        "total": Nested(properties={
            "completion": Nested(properties={
                "size_in_bytes": Long()
            }),
            "docs": Nested(properties={
                "count": Long(),
                "deleted": Long()
            }),
            "fielddata": Nested(properties={
                "evictions": Long(),
                "memory_size_in_bytes": Long()
            }),
            "flush": Nested(properties={
                "periodic": Long(),
                "total": Long(),
                "total_time_in_millis": Long()
            }),
            "get": Nested(properties={
                "current": Long(),
                "exists_time_in_millis": Long(),
                "exists_total": Long(),
                "missing_time_in_millis": Long(),
                "missing_total": Long(),
                "time_in_millis": Long(),
                "total": Long()
            }),
            "indexing": Nested(properties={
                "delete_current": Long(),
                "delete_time_in_millis": Long(),
                "delete_total": Long(),
                "index_current": Long(),
                "index_failed": Long(),
                "index_time_in_millis": Long(),
                "index_total": Long(),
                "is_throttled": Boolean(),
                "noop_update_total": Long(),
                "throttle_time_in_millis": Long()
            }),
            "merges": Nested(properties={
                "current": Long(),
                "current_docs": Long(),
                "current_size_in_bytes": Long(),
                "total": Long(),
                "total_auto_throttle_in_bytes": Long(),
                "total_docs": Long(),
                "total_size_in_bytes": Long(),
                "total_stopped_time_in_millis": Long(),
                "total_throttled_time_in_millis": Long(),
                "total_time_in_millis": Long()
            }),
            "query_cache": Nested(properties={
                "cache_count": Long(),
                "cache_size": Long(),
                "evictions": Long(),
                "hit_count": Long(),
                "memory_size_in_bytes": Long(),
                "miss_count": Long(),
                "total_count": Long()
            }),
            "recovery": Nested(properties={
                "current_as_source": Long(),
                "current_as_target": Long(),
                "throttle_time_in_millis": Long()
            }),
            "refresh": Nested(properties={
                "external_total": Long(),
                "external_total_time_in_millis": Long(),
                "listeners": Long(),
                "total": Long(),
                "total_time_in_millis": Long()
            }),
            "request_cache": Nested(properties={
                "evictions": Long(),
                "hit_count": Long(),
                "memory_size_in_bytes": Long(),
                "miss_count": Long()
            }),
            "search": Nested(properties={
                "fetch_current": Long(),
                "fetch_time_in_millis": Long(),
                "fetch_total": Long(),
                "open_contexts": Long(),
                "query_current": Long(),
                "query_time_in_millis": Long(),
                "query_total": Long(),
                "scroll_current": Long(),
                "scroll_time_in_millis": Long(),
                "scroll_total": Long(),
                "suggest_current": Long(),
                "suggest_time_in_millis": Long(),
                "suggest_total": Long()
            }),
            "segments": Nested(properties={
                "count": Long(),
                "doc_values_memory_in_bytes": Long(),
                "file_sizes": Object(),
                "fixed_bit_set_memory_in_bytes": Long(),
                "index_writer_memory_in_bytes": Long(),
                "max_unsafe_auto_id_timestamp": Long(),
                "memory_in_bytes": Long(),
                "norms_memory_in_bytes": Long(),
                "points_memory_in_bytes": Long(),
                "stored_fields_memory_in_bytes": Long(),
                "term_vectors_memory_in_bytes": Long(),
                "terms_memory_in_bytes": Long(),
                "version_map_memory_in_bytes": Long()
            }),
            "store": Nested(properties={
                "reserved_in_bytes": Long(),
                "size_in_bytes": Long(),
                "throttle_time_in_millis": Long()
            }),
            "translog": Nested(properties={
                "earliest_last_modified_age": Long(),
                "operations": Long(),
                "size_in_bytes": Long(),
                "uncommitted_operations": Long(),
                "uncommitted_size_in_bytes": Long()
            }),
            "warmer": Nested(properties={
                "current": Long(),
                "total": Long(),
                "total_time_in_millis": Long()
            })
        })
    })
    etcd = Nested(properties={
        "api": Text(),
        "clientURLs": Text(multi=True),
        "dbSize": Long(),
        "id": Text(), #multiple types: int, str,
        "leaderInfo": Nested(properties={
            "leader": Text(),
            "startTime": Text(),
            "uptime": Text()
        }),
        "name": Text(),
        "peerURLs": Text(multi=True),
        "recvAppendRequestCnt": Long(),
        "sendAppendRequestCnt": Long(),
        "startTime": Text(),
        "state": Text(),
        "version": Text()
    })
    ethereum_rpc = Nested(properties={
        "accounts": Text(multi=True),
        "client": Text(),
        "compiler": Text(),
        "hashrate": Text(),
        "platform": Text(),
        "version": Text()
    })
    ethernetip = Nested(properties={
        "command": Long(),
        "command_length": Long(),
        "command_status": Long(),
        "device_type": Text(), #multiple types: int, str,
        "encapsulation_length": Long(),
        "ip": Text(),
        "item_count": Long(),
        "options": Long(),
        "product_code": Long(),
        "product_name": Text(),
        "product_name_length": Long(),
        "raw": Text(),
        "revision_major": Long(),
        "revision_minor": Long(),
        "sender_context": Text(),
        "serial": Long(),
        "session": Long(),
        "socket_addr": Text(),
        "state": Long(),
        "status": Long(),
        "type_id": Long(),
        "vendor_id": Text(), #multiple types: int, str,
        "version": Long()
    })
    ftp = Nested(properties={
        "anonymous": Boolean(),
        "features": Nested(multi=True, properties={
            "identifier": Text(),
            "parameters": Text(multi=True)
        }),
        "features_hash": Long(), #nullable
    })
    hash = Long()
    hostnames = Text(multi=True)
    hp_ilo = Nested(properties={
        "cuuid": Text(),
        "ilo_firmware": Text(),
        "ilo_serial_number": Text(),
        "ilo_type": Text(),
        "ilo_uuid": Text(),
        "nics": Nested(multi=True, properties={
            "description": Text(),
            "ip_address": Text(),
            "location": Text(),
            "mac_address": Text(),
            "port": Text(),
            "status": Text()
        }),
        "product_id": Text(),
        "serial_number": Text(),
        "server_type": Text(),
        "uuid": Text()
    })
    html = Text()
    http = Nested(properties={
        "components": Nested(multi=True, properties={
            "categories": Object(multi=True),
            "identifier": Text()
        }),
        "favicon": Nested(properties={
            "data": Text(),
            "hash": Long(),
            "location": Text()
        }),
        "host": Text(),
        "html": Text(), #nullable,
        "html_hash": Long(), #nullable,
        "location": Text(),
        "redirects": Nested(multi=True, properties={
            "data": Text(),
            "host": Text(),
            "location": Text(),
            "html": Text()
        }),
        "robots": Text(), #nullable,
        "robots_hash": Long(), #nullable,
        "securitytxt": Text(), #nullable,
        "securitytxt_hash": Long(), #nullable,
        "server": Text(), #nullable,
        "sitemap": Text(), #nullable,
        "sitemap_hash": Long(), #nullable,
        "title": Text(), #nullable,
        "waf": Text()
    })
    ibm_db2 = Nested(properties={
        "db2_version": Text(),
        "external_name": Text(),
        "instance_name": Text(),
        "server_platform": Text()
    })
    id = Text()
    influxdb = Nested(properties={
        "bind_address": Text(), #nullable,
        "build": Text(),
        "databases": Text(multi=True),
        "go_arch": Text(),
        "go_max_procs": Long(),
        "go_os": Text(),
        "go_version": Text(),
        "network_hostname": Text(),
        "uptime": Text(),
        "version": Text()
    })
    info = Text()
    ip = Long()
    ip_camera = Nested(properties={
        "alias_name": Text(),
        "app_version": Text(),
        "brand": Text(),
        "build": Text(),
        "client_version": Text(),
        "ddns_host": Text(),
        "hardware_version": Text(),
        "id": Text(),
        "ip_address": Text(),
        "mac_address": Text(),
        "model": Text(),
        "name": Text(),
        "product": Text(),
        "server_version": Text(),
        "system_version": Text(),
        "version": Text()
    })
    ip_str = Text()
    ipv6 = Text()
    isakmp = Nested(properties={
        "aggressive": Nested(properties={
            "exchange_type": Long(),
            "flags": Nested(properties={
                "authentication": Boolean(),
                "commit": Boolean(),
                "encryption": Boolean()
            }),
            "initiator_spi": Text(),
            "length": Long(),
            "msg_id": Text(),
            "next_payload": Long(),
            "responder_spi": Text(),
            "vendor_ids": Text(multi=True),
            "version": Text()
        }),
        "exchange_type": Long(),
        "flags": Nested(properties={
            "authentication": Boolean(),
            "commit": Boolean(),
            "encryption": Boolean()
        }),
        "initiator_spi": Text(),
        "length": Long(),
        "msg_id": Text(),
        "next_payload": Long(),
        "responder_spi": Text(),
        "vendor_ids": Text(multi=True),
        "version": Text()
    })
    iscsi = Nested(properties={
        "targets": Nested(multi=True, properties={
            "addresses": Text(multi=True),
            "name": Text()
        })
    })
    isp = Text(), #nullable
    knx = Nested(properties={
        "device": Nested(properties={
            "friendly_name": Text(),
            "knx_address": Text(),
            "mac": Text(),
            "multicast_address": Text(),
            "serial": Text()
        }),
        "supported_services": Nested(properties={
            "core": Text(),
            "device_management": Text(),
            "object_server": Text(),
            "remote_config": Text(),
            "routing": Text(),
            "tunneling": Text()
        })
    })
    lantronix = Nested(properties={
        "gateway": Text(),
        "ip": Text(),
        "mac": Text(),
        "password": Text(),
        "type": Text(),
        "version": Text()
    })
    location = Nested(properties={
        "area_code": Object(), #nullable,
        "city": Text(), #nullable,
        "country_code": Text(), #nullable,
        "country_code3": Object(), #nullable,
        "country_name": Text(), #nullable,
        "dma_code": Object(), #nullable,
        "latitude": Double(), #nullable,
        "longitude": Double(), #nullable,
        "postal_code": Object(), #nullable,
        "region_code": Text(), #nullable
    })
    mac = Nested(multi=True, properties={
        "address": Text(),
        "assignment": Text(),
        "date": Text(),
        "org": Text(),
        "__set_values": Object(), #nullable
    })
    minecraft = Nested(properties={
        "description": Text(),
        "favicon": Text(),
        "forgeData": Nested(properties={
            "channels": Nested(multi=True, properties={
                "required": Boolean(),
                "res": Text(),
                "version": Text()
            }),
            "fmlNetworkVersion": Long(),
            "mods": Nested(multi=True, properties={
                "modId": Text(),
                "modmarker": Text()
            })
        }),
        "modinfo": Nested(properties={
            "modList": Nested(multi=True, properties={
                "modid": Text(),
                "version": Text()
            }),
            "type": Text()
        }),
        "players": Nested(properties={
            "max": Long(),
            "online": Long(),
            "sample": Nested(multi=True, properties={
                "id": Text(),
                "name": Text()
            })
        }),
        "version": Nested(properties={
            "name": Text(),
            "protocol": Long()
        })
    })
    mitsubishi_q = Nested(properties={
        "cpu": Text()
    })
    mongodb = Nested(properties={
        "authentication": Boolean(),
        "buildInfo": Nested(properties={
            "OpenSSLVersion": Text(),
            "allocator": Text(),
            "bits": Long(),
            "buildEnvironment": Nested(properties={
                "cc": Text(),
                "ccflags": Text(),
                "cppdefines": Text(),
                "cxx": Text(),
                "cxxflags": Text(),
                "distarch": Text(),
                "distmod": Text(),
                "linkflags": Text(),
                "target_arch": Text(),
                "target_os": Text()
            }),
            "compilerFlags": Text(),
            "debug": Boolean(),
            "gitVersion": Text(),
            "javascriptEngine": Text(),
            "loaderFlags": Text(),
            "maxBsonObjectSize": Long(),
            "modules": Text(multi=True),
            "ok": Double(),
            "openssl": Nested(properties={
                "compiled": Text(),
                "running": Text()
            }),
            "psmdbVersion": Text(),
            "storageEngines": Text(multi=True),
            "sysInfo": Text(),
            "targetMinOS": Text(),
            "version": Text(),
            "versionArray": Long(multi=True)
        }),
        "listDatabases": Nested(properties={
            "databases": Nested(multi=True, properties={
                "collections": Text(multi=True),
                "empty": Boolean(),
                "name": Text(),
                "sizeOnDisk": Double()
            }),
            "ok": Double(),
            "totalSize": Double()
        }),
        "serverStatus": Nested(properties={
            "advisoryHostFQDNs": Text(multi=True),
            "asserts": Nested(properties={
                "msg": Long(),
                "regular": Long(),
                "rollovers": Long(),
                "user": Long(),
                "warning": Long()
            }),
            "backgroundFlushing": Nested(properties={
                "average_ms": Double(),
                "flushes": Long(),
                "last_finished": Text(),
                "last_ms": Long(),
                "total_ms": Long()
            }),
            "connections": Nested(properties={
                "active": Long(),
                "available": Long(),
                "current": Long(),
                "totalCreated": Long()
            }),
            "cursors": Nested(properties={
                "clientCursors_size": Long(),
                "note": Text(),
                "pinned": Long(),
                "timedOut": Long(),
                "totalNoTimeout": Long(),
                "totalOpen": Long()
            }),
            "dur": Nested(properties={
                "commits": Long(),
                "commitsInWriteLock": Long(),
                "compression": Double(),
                "earlyCommits": Long(),
                "journaledMB": Double(),
                "timeMs": Nested(properties={
                    "commits": Long(),
                    "commitsInWriteLock": Long(),
                    "dt": Long(),
                    "prepLogBuffer": Long(),
                    "remapPrivateView": Long(),
                    "writeToDataFiles": Long(),
                    "writeToJournal": Long()
                }),
                "writeToDataFilesMB": Double()
            }),
            "extra_info": Nested(properties={
                "availPageFileMB": Long(),
                "heap_usage_bytes": Long(),
                "note": Text(),
                "page_faults": Double(), #upgraded to float,
                "ramMB": Long(),
                "totalPageFileMB": Long(),
                "usagePageFileMB": Long()
            }),
            "freeMonitoring": Nested(properties={
                "state": Text()
            }),
            "globalLock": Nested(properties={
                "activeClients": Nested(properties={
                    "readers": Long(),
                    "total": Long(),
                    "writers": Long()
                }),
                "currentQueue": Nested(properties={
                    "readers": Long(),
                    "total": Long(),
                    "writers": Long()
                }),
                "lockTime": Long(),
                "totalTime": Long()
            }),
            "host": Text(),
            "indexCounters": Nested(properties={
                "accesses": Long(),
                "hits": Long(),
                "missRatio": Double(),
                "misses": Long(),
                "resets": Long()
            }),
            "localTime": Text(),
            "locks": Nested(multi=True, properties={
                "acquireCount": Nested(properties={
                    "W": Long(),
                    "r": Long(),
                    "w": Long(),
                    "R": Long()
                }),
                "acquireWaitCount": Nested(properties={
                    "r": Long(),
                    "W": Long(),
                    "w": Long(),
                    "R": Long()
                }),
                "identifier": Text(),
                "timeAcquiringMicros": Nested(properties={
                    "r": Long(),
                    "W": Long(),
                    "w": Long(),
                    "R": Long()
                }),
                "timeLockedMicros": Nested(properties={
                    "r": Long(),
                    "w": Long(),
                    "R": Long(),
                    "W": Long()
                })
            }),
            "logicalSessionRecordCache": Nested(properties={
                "activeSessionsCount": Long(),
                "lastSessionsCollectionJobCursorsClosed": Long(),
                "lastSessionsCollectionJobDurationMillis": Long(),
                "lastSessionsCollectionJobEntriesEnded": Long(),
                "lastSessionsCollectionJobEntriesRefreshed": Long(),
                "lastSessionsCollectionJobTimestamp": Text(),
                "lastTransactionReaperJobDurationMillis": Long(),
                "lastTransactionReaperJobEntriesCleanedUp": Long(),
                "lastTransactionReaperJobTimestamp": Text(),
                "sessionsCollectionJobCount": Long(),
                "transactionReaperJobCount": Long()
            }),
            "mem": Nested(properties={
                "bits": Long(),
                "mapped": Long(),
                "mappedWithJournal": Long(),
                "resident": Long(),
                "supported": Boolean(),
                "virtual": Long()
            }),
            "metrics": Nested(properties={
                "commands": Nested(multi=True, properties={
                    "failed": Long(),
                    "identifier": Text(),
                    "total": Long(),
                    "__set_values": Long(),
                    "shardedfinish": Nested(properties={
                        "failed": Long(),
                        "total": Long()
                    })
                }),
                "cursor": Nested(properties={
                    "open": Nested(properties={
                        "noTimeout": Long(),
                        "pinned": Long(),
                        "total": Long()
                    }),
                    "timedOut": Long()
                }),
                "document": Nested(properties={
                    "deleted": Long(),
                    "inserted": Long(),
                    "returned": Long(),
                    "updated": Long()
                }),
                "getLastError": Nested(properties={
                    "wtime": Nested(properties={
                        "num": Long(),
                        "totalMillis": Long()
                    }),
                    "wtimeouts": Long()
                }),
                "operation": Nested(properties={
                    "fastmod": Long(),
                    "idhack": Long(),
                    "scanAndOrder": Long(),
                    "writeConflicts": Long()
                }),
                "query": Nested(properties={
                    "updateOneOpStyleBroadcastWithExactIDCount": Long(),
                    "upsertReplacementCannotTargetByQueryCount": Long()
                }),
                "queryExecutor": Nested(properties={
                    "scanned": Long(),
                    "scannedObjects": Long()
                }),
                "record": Nested(properties={
                    "moves": Long()
                }),
                "repl": Nested(properties={
                    "apply": Nested(properties={
                        "attemptsToBecomeSecondary": Long(),
                        "batchSize": Long(),
                        "batches": Nested(properties={
                            "num": Long(),
                            "totalMillis": Long()
                        }),
                        "ops": Long()
                    }),
                    "buffer": Nested(properties={
                        "count": Long(),
                        "maxSizeBytes": Long(),
                        "sizeBytes": Long()
                    }),
                    "executor": Nested(properties={
                        "counters": Nested(properties={
                            "cancels": Long(),
                            "eventCreated": Long(),
                            "eventWait": Long(),
                            "scheduledDBWork": Long(),
                            "scheduledNetCmd": Long(),
                            "scheduledWork": Long(),
                            "scheduledWorkAt": Long(),
                            "scheduledXclWork": Long(),
                            "schedulingFailures": Long(),
                            "waits": Long()
                        }),
                        "eventWaiters": Long(),
                        "networkInterface": Text(),
                        "pool": Nested(properties={
                            "inProgressCount": Long()
                        }),
                        "queues": Nested(properties={
                            "dbWorkInProgress": Long(),
                            "exclusiveInProgress": Long(),
                            "free": Long(),
                            "networkInProgress": Long(),
                            "ready": Long(),
                            "sleepers": Long()
                        }),
                        "shuttingDown": Boolean(),
                        "unsignaledEvents": Long()
                    }),
                    "initialSync": Nested(properties={
                        "completed": Long(),
                        "failedAttempts": Long(),
                        "failures": Long()
                    }),
                    "network": Nested(properties={
                        "bytes": Long(),
                        "getmores": Nested(properties={
                            "num": Long(),
                            "totalMillis": Long()
                        }),
                        "ops": Long(),
                        "readersCreated": Long()
                    }),
                    "oplog": Nested(properties={
                        "insert": Nested(properties={
                            "num": Long(),
                            "totalMillis": Long()
                        }),
                        "insertBytes": Long()
                    }),
                    "preload": Nested(properties={
                        "docs": Nested(properties={
                            "num": Long(),
                            "totalMillis": Long()
                        }),
                        "indexes": Nested(properties={
                            "num": Long(),
                            "totalMillis": Long()
                        })
                    })
                }),
                "storage": Nested(properties={
                    "freelist": Nested(properties={
                        "search": Nested(properties={
                            "bucketExhausted": Long(),
                            "requests": Long(),
                            "scanned": Long()
                        })
                    })
                }),
                "ttl": Nested(properties={
                    "deletedDocuments": Long(),
                    "passes": Long()
                })
            }),
            "network": Nested(properties={
                "bytesIn": Double(), #upgraded to float,
                "bytesOut": Double(), #upgraded to float,
                "compression": Nested(properties={
                    "snappy": Nested(properties={
                        "compressor": Nested(properties={
                            "bytesIn": Long(),
                            "bytesOut": Long()
                        }),
                        "decompressor": Nested(properties={
                            "bytesIn": Long(),
                            "bytesOut": Long()
                        })
                    })
                }),
                "numRequests": Long(),
                "physicalBytesIn": Long(),
                "physicalBytesOut": Long(),
                "serviceExecutorTaskStats": Nested(properties={
                    "executor": Text(),
                    "threadsRunning": Long()
                })
            }),
            "ok": Double(),
            "opLatencies": Nested(properties={
                "commands": Nested(properties={
                    "latency": Long(),
                    "ops": Long()
                }),
                "reads": Nested(properties={
                    "latency": Long(),
                    "ops": Long()
                }),
                "transactions": Nested(properties={
                    "latency": Long(),
                    "ops": Long()
                }),
                "writes": Nested(properties={
                    "latency": Long(),
                    "ops": Long()
                })
            }),
            "opReadConcernCounters": Nested(properties={
                "available": Long(),
                "linearizable": Long(),
                "local": Long(),
                "majority": Long(),
                "none": Long(),
                "snapshot": Long()
            }),
            "opcounters": Nested(properties={
                "command": Long(),
                "delete": Long(),
                "getmore": Long(),
                "insert": Long(),
                "query": Long(),
                "update": Long()
            }),
            "opcountersRepl": Nested(properties={
                "command": Long(),
                "delete": Long(),
                "getmore": Long(),
                "insert": Long(),
                "query": Long(),
                "update": Long()
            }),
            "pid": Long(),
            "process": Text(),
            "recordStats": Nested(multi=True, properties={
                "accessesNotInMemory": Long(),
                "identifier": Text(),
                "pageFaultExceptionsThrown": Long(),
                "__set_values": Long()
            }),
            "storageEngine": Nested(properties={
                "name": Text(),
                "persistent": Boolean(),
                "readOnly": Boolean(),
                "supportsCommittedReads": Boolean(),
                "supportsSnapshotReadConcern": Boolean()
            }),
            "tcmalloc": Nested(properties={
                "generic": Nested(properties={
                    "current_allocated_bytes": Long(),
                    "heap_size": Long()
                }),
                "tcmalloc": Nested(properties={
                    "aggressive_memory_decommit": Long(),
                    "central_cache_free_bytes": Long(),
                    "current_total_thread_cache_bytes": Long(),
                    "formattedString": Text(),
                    "max_total_thread_cache_bytes": Long(),
                    "pageheap_commit_count": Long(),
                    "pageheap_committed_bytes": Long(),
                    "pageheap_decommit_count": Long(),
                    "pageheap_free_bytes": Long(),
                    "pageheap_reserve_count": Long(),
                    "pageheap_scavenge_count": Long(),
                    "pageheap_total_commit_bytes": Long(),
                    "pageheap_total_decommit_bytes": Long(),
                    "pageheap_total_reserve_bytes": Long(),
                    "pageheap_unmapped_bytes": Long(),
                    "spinlock_total_delay_ns": Long(),
                    "thread_cache_free_bytes": Long(),
                    "total_free_bytes": Long(),
                    "transfer_cache_free_bytes": Long()
                })
            }),
            "transactions": Nested(properties={
                "currentActive": Long(),
                "currentInactive": Long(),
                "currentOpen": Long(),
                "retriedCommandsCount": Long(),
                "retriedStatementsCount": Long(),
                "totalAborted": Long(),
                "totalCommitted": Long(),
                "totalStarted": Long(),
                "transactionsCollectionWriteCount": Long()
            }),
            "transportSecurity": Nested(properties={
                "1.0": Long(),
                "1.1": Long(),
                "1.2": Long(),
                "1.3": Long(),
                "unknown": Long()
            }),
            "uptime": Double(),
            "uptimeEstimate": Double(), #upgraded to float,
            "uptimeMillis": Long(),
            "version": Text(),
            "wiredTiger": Nested(properties={
                "LSM": Nested(properties={
                    "application work units currently queued": Long(),
                    "merge work units currently queued": Long(),
                    "rows merged in an LSM tree": Long(),
                    "sleep for LSM checkpoint throttle": Long(),
                    "sleep for LSM merge throttle": Long(),
                    "switch work units currently queued": Long(),
                    "tree maintenance operations discarded": Long(),
                    "tree maintenance operations executed": Long(),
                    "tree maintenance operations scheduled": Long(),
                    "tree queue hit maximum": Long()
                }),
                "async": Nested(properties={
                    "current work queue length": Long(),
                    "maximum work queue length": Long(),
                    "number of allocation state races": Long(),
                    "number of flush calls": Long(),
                    "number of operation slots viewed for allocation": Long(),
                    "number of times operation allocation failed": Long(),
                    "number of times worker found no work": Long(),
                    "total allocations": Long(),
                    "total compact calls": Long(),
                    "total insert calls": Long(),
                    "total remove calls": Long(),
                    "total search calls": Long(),
                    "total update calls": Long()
                }),
                "block-manager": Nested(properties={
                    "blocks pre-loaded": Long(),
                    "blocks read": Long(),
                    "blocks written": Long(),
                    "bytes read": Double(), #upgraded to float,
                    "bytes written": Double(), #upgraded to float,
                    "bytes written for checkpoint": Double(), #upgraded to float,
                    "mapped blocks read": Long(),
                    "mapped bytes read": Long()
                }),
                "cache": Nested(properties={
                    "application threads page read from disk to cache count": Long(),
                    "application threads page read from disk to cache time (usecs)": Long(),
                    "application threads page write from cache to disk count": Long(),
                    "application threads page write from cache to disk time (usecs)": Double(), #upgraded to float,
                    "bytes belonging to page images in the cache": Long(),
                    "bytes belonging to the cache overflow table in the cache": Long(),
                    "bytes belonging to the lookaside table in the cache": Long(),
                    "bytes currently in the cache": Long(),
                    "bytes dirty in the cache cumulative": Double(), #upgraded to float,
                    "bytes not belonging to page images in the cache": Long(),
                    "bytes read into cache": Long(),
                    "bytes written from cache": Double(), #upgraded to float,
                    "cache overflow cursor application thread wait time (usecs)": Long(),
                    "cache overflow cursor internal thread wait time (usecs)": Long(),
                    "cache overflow score": Long(),
                    "cache overflow table entries": Long(),
                    "cache overflow table insert calls": Long(),
                    "cache overflow table max on-disk size": Long(),
                    "cache overflow table on-disk size": Long(),
                    "cache overflow table remove calls": Long(),
                    "checkpoint blocked page eviction": Long(),
                    "eviction calls to get a page": Long(),
                    "eviction calls to get a page found queue empty": Long(),
                    "eviction calls to get a page found queue empty after locking": Long(),
                    "eviction currently operating in aggressive mode": Long(),
                    "eviction empty score": Long(),
                    "eviction passes of a file": Long(),
                    "eviction server candidate queue empty when topping up": Long(),
                    "eviction server candidate queue not empty when topping up": Long(),
                    "eviction server evicting pages": Long(),
                    "eviction server populating queue, but not evicting pages": Long(),
                    "eviction server skipped very large page": Long(),
                    "eviction server slept, because we did not make progress with eviction": Long(),
                    "eviction server unable to reach eviction goal": Long(),
                    "eviction state": Long(),
                    "eviction walk target pages histogram - 0-9": Long(),
                    "eviction walk target pages histogram - 10-31": Long(),
                    "eviction walk target pages histogram - 128 and higher": Long(),
                    "eviction walk target pages histogram - 32-63": Long(),
                    "eviction walk target pages histogram - 64-128": Long(),
                    "eviction walks abandoned": Long(),
                    "eviction walks gave up because they restarted their walk twice": Long(),
                    "eviction walks gave up because they saw too many pages and found no candidates": Long(),
                    "eviction walks gave up because they saw too many pages and found too few candidates": Long(),
                    "eviction walks reached end of tree": Long(),
                    "eviction walks started from root of tree": Long(),
                    "eviction walks started from saved location in tree": Long(),
                    "eviction worker thread active": Long(),
                    "eviction worker thread created": Long(),
                    "eviction worker thread evicting pages": Long(),
                    "eviction worker thread removed": Long(),
                    "eviction worker thread stable number": Long(),
                    "failed eviction of pages that exceeded the in-memory maximum": Long(),
                    "failed eviction of pages that exceeded the in-memory maximum count": Long(),
                    "failed eviction of pages that exceeded the in-memory maximum time (usecs)": Long(),
                    "files with active eviction walks": Long(),
                    "files with new eviction walks started": Long(),
                    "force re-tuning of eviction workers once in a while": Long(),
                    "hazard pointer blocked page eviction": Long(),
                    "hazard pointer check calls": Long(),
                    "hazard pointer check entries walked": Long(),
                    "hazard pointer maximum array length": Long(),
                    "in-memory page passed criteria to be split": Long(),
                    "in-memory page splits": Long(),
                    "internal pages evicted": Long(),
                    "internal pages split during eviction": Long(),
                    "leaf pages split during eviction": Long(),
                    "lookaside score": Long(),
                    "lookaside table entries": Long(),
                    "lookaside table insert calls": Long(),
                    "lookaside table remove calls": Long(),
                    "maximum bytes configured": Double(), #upgraded to float,
                    "maximum page size at eviction": Long(),
                    "modified pages evicted": Long(),
                    "modified pages evicted by application threads": Long(),
                    "operations timed out waiting for space in cache": Long(),
                    "overflow pages read into cache": Long(),
                    "overflow values cached in memory": Long(),
                    "page split during eviction deepened the tree": Long(),
                    "page written requiring cache overflow records": Long(),
                    "page written requiring lookaside records": Long(),
                    "pages currently held in the cache": Long(),
                    "pages evicted because they exceeded the in-memory maximum": Long(),
                    "pages evicted because they exceeded the in-memory maximum count": Long(),
                    "pages evicted because they exceeded the in-memory maximum time (usecs)": Long(),
                    "pages evicted because they had chains of deleted items": Long(),
                    "pages evicted because they had chains of deleted items count": Long(),
                    "pages evicted because they had chains of deleted items time (usecs)": Long(),
                    "pages evicted by application threads": Long(),
                    "pages queued for eviction": Long(),
                    "pages queued for urgent eviction": Long(),
                    "pages queued for urgent eviction during walk": Long(),
                    "pages read into cache": Long(),
                    "pages read into cache after truncate": Long(),
                    "pages read into cache after truncate in prepare state": Long(),
                    "pages read into cache requiring cache overflow entries": Long(),
                    "pages read into cache requiring cache overflow for checkpoint": Long(),
                    "pages read into cache requiring lookaside entries": Long(),
                    "pages read into cache skipping older cache overflow entries": Long(),
                    "pages read into cache skipping older lookaside entries": Long(),
                    "pages read into cache with skipped cache overflow entries needed later": Long(),
                    "pages read into cache with skipped cache overflow entries needed later by checkpoint": Long(),
                    "pages read into cache with skipped lookaside entries needed later": Long(),
                    "pages requested from the cache": Long(),
                    "pages seen by eviction walk": Long(),
                    "pages selected for eviction unable to be evicted": Long(),
                    "pages split during eviction": Long(),
                    "pages walked for eviction": Long(),
                    "pages written from cache": Long(),
                    "pages written requiring in-memory restoration": Long(),
                    "percentage overhead": Long(),
                    "tracked bytes belonging to internal pages in the cache": Double(), #upgraded to float,
                    "tracked bytes belonging to leaf pages in the cache": Double(), #upgraded to float,
                    "tracked bytes belonging to overflow pages in the cache": Long(),
                    "tracked dirty bytes in the cache": Long(),
                    "tracked dirty pages in the cache": Long(),
                    "unmodified pages evicted": Long()
                }),
                "capacity": Nested(properties={
                    "background fsync file handles considered": Long(),
                    "background fsync file handles synced": Long(),
                    "background fsync time (msecs)": Long(),
                    "threshold to call fsync": Long(),
                    "throttled bytes read": Long(),
                    "throttled bytes written for checkpoint": Long(),
                    "throttled bytes written for eviction": Long(),
                    "throttled bytes written for log": Long(),
                    "throttled bytes written total": Long(),
                    "time waiting due to total capacity (usecs)": Long(),
                    "time waiting during checkpoint (usecs)": Long(),
                    "time waiting during eviction (usecs)": Long(),
                    "time waiting during logging (usecs)": Long(),
                    "time waiting during read (usecs)": Long()
                }),
                "concurrentTransactions": Nested(properties={
                    "read": Nested(properties={
                        "available": Long(),
                        "out": Long(),
                        "totalTickets": Long()
                    }),
                    "write": Nested(properties={
                        "available": Long(),
                        "out": Long(),
                        "totalTickets": Long()
                    })
                }),
                "connection": Nested(properties={
                    "auto adjusting condition resets": Long(),
                    "auto adjusting condition wait calls": Long(),
                    "detected system time went backwards": Long(),
                    "files currently open": Long(),
                    "memory allocations": Double(), #upgraded to float,
                    "memory frees": Double(), #upgraded to float,
                    "memory re-allocations": Long(),
                    "pthread mutex condition wait calls": Double(), #upgraded to float,
                    "pthread mutex shared lock read-lock calls": Long(),
                    "pthread mutex shared lock write-lock calls": Long(),
                    "total fsync I/Os": Long(),
                    "total read I/Os": Long(),
                    "total write I/Os": Long()
                }),
                "cursor": Nested(properties={
                    "cached cursor count": Long(),
                    "cursor close calls that result in cache": Long(),
                    "cursor create calls": Long(),
                    "cursor insert calls": Long(),
                    "cursor modify calls": Long(),
                    "cursor next calls": Long(),
                    "cursor operation restarted": Long(),
                    "cursor prev calls": Long(),
                    "cursor remove calls": Long(),
                    "cursor reserve calls": Long(),
                    "cursor reset calls": Long(),
                    "cursor restarted searches": Long(),
                    "cursor search calls": Long(),
                    "cursor search near calls": Long(),
                    "cursor sweep buckets": Long(),
                    "cursor sweep cursors closed": Long(),
                    "cursor sweep cursors examined": Long(),
                    "cursor sweeps": Long(),
                    "cursor update calls": Long(),
                    "cursors cached on close": Long(),
                    "cursors reused from cache": Long(),
                    "open cursor count": Long(),
                    "truncate calls": Long()
                }),
                "data-handle": Nested(properties={
                    "connection candidate referenced": Long(),
                    "connection data handles currently active": Long(),
                    "connection dhandles swept": Long(),
                    "connection sweep candidate became referenced": Long(),
                    "connection sweep dhandles closed": Long(),
                    "connection sweep dhandles removed from hash list": Long(),
                    "connection sweep time-of-death sets": Long(),
                    "connection sweeps": Long(),
                    "connection time-of-death sets": Long(),
                    "session dhandles swept": Long(),
                    "session sweep attempts": Long()
                }),
                "lock": Nested(properties={
                    "checkpoint lock acquisitions": Long(),
                    "checkpoint lock application thread wait time (usecs)": Long(),
                    "checkpoint lock internal thread wait time (usecs)": Long(),
                    "commit timestamp queue lock application thread time waiting (usecs)": Long(),
                    "commit timestamp queue lock application thread time waiting for the dhandle lock (usecs)": Long(),
                    "commit timestamp queue lock internal thread time waiting (usecs)": Long(),
                    "commit timestamp queue lock internal thread time waiting for the dhandle lock (usecs)": Long(),
                    "commit timestamp queue read lock acquisitions": Long(),
                    "commit timestamp queue write lock acquisitions": Long(),
                    "dhandle lock application thread time waiting (usecs)": Long(),
                    "dhandle lock application thread time waiting for the dhandle lock (usecs)": Long(),
                    "dhandle lock internal thread time waiting (usecs)": Long(),
                    "dhandle lock internal thread time waiting for the dhandle lock (usecs)": Long(),
                    "dhandle read lock acquisitions": Long(),
                    "dhandle write lock acquisitions": Long(),
                    "handle-list lock acquisitions": Long(),
                    "handle-list lock application thread wait time (usecs)": Long(),
                    "handle-list lock eviction thread wait time (usecs)": Long(),
                    "handle-list lock internal thread wait time (usecs)": Long(),
                    "metadata lock acquisitions": Long(),
                    "metadata lock application thread wait time (usecs)": Long(),
                    "metadata lock internal thread wait time (usecs)": Long(),
                    "read timestamp queue lock application thread time waiting (usecs)": Long(),
                    "read timestamp queue lock application thread time waiting for the dhandle lock (usecs)": Long(),
                    "read timestamp queue lock internal thread time waiting (usecs)": Long(),
                    "read timestamp queue lock internal thread time waiting for the dhandle lock (usecs)": Long(),
                    "read timestamp queue read lock acquisitions": Long(),
                    "read timestamp queue write lock acquisitions": Long(),
                    "schema lock acquisitions": Long(),
                    "schema lock application thread wait time (usecs)": Long(),
                    "schema lock internal thread wait time (usecs)": Long(),
                    "table lock acquisitions": Long(),
                    "table lock application thread time waiting for the table lock (usecs)": Long(),
                    "table lock internal thread time waiting for the table lock (usecs)": Double(), #upgraded to float,
                    "table read lock acquisitions": Long(),
                    "table write lock acquisitions": Long(),
                    "txn global lock application thread time waiting (usecs)": Long(),
                    "txn global lock application thread time waiting for the dhandle lock (usecs)": Long(),
                    "txn global lock internal thread time waiting (usecs)": Long(),
                    "txn global lock internal thread time waiting for the dhandle lock (usecs)": Long(),
                    "txn global read lock acquisitions": Long(),
                    "txn global write lock acquisitions": Long()
                }),
                "log": Nested(properties={
                    "busy returns attempting to switch slots": Long(),
                    "consolidated slot closures": Long(),
                    "consolidated slot join active slot closed": Long(),
                    "consolidated slot join races": Long(),
                    "consolidated slot join transitions": Long(),
                    "consolidated slot joins": Long(),
                    "consolidated slot transitions unable to find free slot": Long(),
                    "consolidated slot unbuffered writes": Long(),
                    "failed to find a slot large enough for record": Long(),
                    "force archive time sleeping (usecs)": Long(),
                    "force checkpoint calls slept": Long(),
                    "log buffer size increases": Long(),
                    "log bytes of payload data": Double(), #upgraded to float,
                    "log bytes written": Double(), #upgraded to float,
                    "log files manually zero-filled": Long(),
                    "log flush operations": Double(), #upgraded to float,
                    "log force write operations": Double(), #upgraded to float,
                    "log force write operations skipped": Double(), #upgraded to float,
                    "log read operations": Long(),
                    "log records compressed": Long(),
                    "log records not compressed": Long(),
                    "log records too small to compress": Long(),
                    "log release advances write LSN": Long(),
                    "log scan operations": Long(),
                    "log scan records requiring two reads": Long(),
                    "log server thread advances write LSN": Long(),
                    "log server thread write LSN walk skipped": Long(),
                    "log sync operations": Long(),
                    "log sync time duration (usecs)": Double(), #upgraded to float,
                    "log sync_dir operations": Long(),
                    "log sync_dir time duration (usecs)": Long(),
                    "log write operations": Long(),
                    "logging bytes consolidated": Double(), #upgraded to float,
                    "maximum log file size": Long(),
                    "number of pre-allocated log files to create": Long(),
                    "pre-allocated log files not ready and missed": Long(),
                    "pre-allocated log files prepared": Long(),
                    "pre-allocated log files used": Long(),
                    "record size exceeded maximum": Long(),
                    "records processed by log scan": Long(),
                    "slot close lost race": Long(),
                    "slot close unbuffered waits": Long(),
                    "slot closures": Long(),
                    "slot join atomic update races": Long(),
                    "slot join calls atomic updates raced": Long(),
                    "slot join calls did not yield": Long(),
                    "slot join calls found active slot closed": Long(),
                    "slot join calls slept": Long(),
                    "slot join calls yielded": Long(),
                    "slot join found active slot closed": Long(),
                    "slot joins yield time (usecs)": Long(),
                    "slot transitions unable to find free slot": Long(),
                    "slot unbuffered writes": Long(),
                    "slots selected for switching that were unavailable": Long(),
                    "total in-memory size of compressed records": Double(), #upgraded to float,
                    "total log buffer size": Long(),
                    "total size of compressed records": Double(), #upgraded to float,
                    "written slots coalesced": Long(),
                    "yields waiting for previous log file close": Long()
                }),
                "perf": Nested(properties={
                    "file system read latency histogram (bucket 1) - 10-49ms": Long(),
                    "file system read latency histogram (bucket 2) - 50-99ms": Long(),
                    "file system read latency histogram (bucket 3) - 100-249ms": Long(),
                    "file system read latency histogram (bucket 4) - 250-499ms": Long(),
                    "file system read latency histogram (bucket 5) - 500-999ms": Long(),
                    "file system read latency histogram (bucket 6) - 1000ms+": Long(),
                    "file system write latency histogram (bucket 1) - 10-49ms": Long(),
                    "file system write latency histogram (bucket 2) - 50-99ms": Long(),
                    "file system write latency histogram (bucket 3) - 100-249ms": Long(),
                    "file system write latency histogram (bucket 4) - 250-499ms": Long(),
                    "file system write latency histogram (bucket 5) - 500-999ms": Long(),
                    "file system write latency histogram (bucket 6) - 1000ms+": Long(),
                    "operation read latency histogram (bucket 1) - 100-249us": Long(),
                    "operation read latency histogram (bucket 2) - 250-499us": Long(),
                    "operation read latency histogram (bucket 3) - 500-999us": Long(),
                    "operation read latency histogram (bucket 4) - 1000-9999us": Long(),
                    "operation read latency histogram (bucket 5) - 10000us+": Long(),
                    "operation write latency histogram (bucket 1) - 100-249us": Long(),
                    "operation write latency histogram (bucket 2) - 250-499us": Long(),
                    "operation write latency histogram (bucket 3) - 500-999us": Long(),
                    "operation write latency histogram (bucket 4) - 1000-9999us": Long(),
                    "operation write latency histogram (bucket 5) - 10000us+": Long()
                }),
                "reconciliation": Nested(properties={
                    "fast-path pages deleted": Long(),
                    "page reconciliation calls": Long(),
                    "page reconciliation calls for eviction": Long(),
                    "pages deleted": Long(),
                    "split bytes currently awaiting free": Long(),
                    "split objects currently awaiting free": Long()
                }),
                "session": Nested(properties={
                    "open cursor count": Long(),
                    "open session count": Long(),
                    "session query timestamp calls": Long(),
                    "table alter failed calls": Long(),
                    "table alter successful calls": Long(),
                    "table alter unchanged and skipped": Long(),
                    "table compact failed calls": Long(),
                    "table compact successful calls": Long(),
                    "table create failed calls": Long(),
                    "table create successful calls": Long(),
                    "table drop failed calls": Long(),
                    "table drop successful calls": Long(),
                    "table rebalance failed calls": Long(),
                    "table rebalance successful calls": Long(),
                    "table rename failed calls": Long(),
                    "table rename successful calls": Long(),
                    "table salvage failed calls": Long(),
                    "table salvage successful calls": Long(),
                    "table truncate failed calls": Long(),
                    "table truncate successful calls": Long(),
                    "table verify failed calls": Long(),
                    "table verify successful calls": Long()
                }),
                "thread-state": Nested(properties={
                    "active filesystem fsync calls": Long(),
                    "active filesystem read calls": Long(),
                    "active filesystem write calls": Long()
                }),
                "thread-yield": Nested(properties={
                    "application thread time evicting (usecs)": Long(),
                    "application thread time waiting for cache (usecs)": Long(),
                    "connection close blocked waiting for transaction state stabilization": Long(),
                    "connection close yielded for lsm manager shutdown": Long(),
                    "data handle lock yielded": Long(),
                    "get reference for page index and slot time sleeping (usecs)": Long(),
                    "log server sync yielded for log write": Long(),
                    "page access yielded due to prepare state change": Long(),
                    "page acquire busy blocked": Long(),
                    "page acquire eviction blocked": Long(),
                    "page acquire locked blocked": Long(),
                    "page acquire read blocked": Long(),
                    "page acquire time sleeping (usecs)": Long(),
                    "page delete rollback time sleeping for state change (usecs)": Long(),
                    "page delete rollback yielded for instantiation": Long(),
                    "page reconciliation yielded due to child modification": Long(),
                    "reference for page index and slot yielded": Long(),
                    "tree descend one level yielded for split page index update": Long()
                }),
                "transaction": Nested(properties={
                    "Number of prepared updates": Long(),
                    "Number of prepared updates added to cache overflow": Long(),
                    "Number of prepared updates resolved": Long(),
                    "commit timestamp queue entries walked": Long(),
                    "commit timestamp queue insert to empty": Long(),
                    "commit timestamp queue inserts to head": Long(),
                    "commit timestamp queue inserts to tail": Long(),
                    "commit timestamp queue inserts total": Long(),
                    "commit timestamp queue length": Long(),
                    "number of named snapshots created": Long(),
                    "number of named snapshots dropped": Long(),
                    "prepared transactions": Long(),
                    "prepared transactions committed": Long(),
                    "prepared transactions currently active": Long(),
                    "prepared transactions rolled back": Long(),
                    "query timestamp calls": Long(),
                    "read timestamp queue entries walked": Long(),
                    "read timestamp queue insert to empty": Long(),
                    "read timestamp queue inserts to head": Long(),
                    "read timestamp queue inserts total": Long(),
                    "read timestamp queue length": Long(),
                    "rollback to stable calls": Long(),
                    "rollback to stable updates aborted": Long(),
                    "rollback to stable updates removed from cache overflow": Long(),
                    "rollback to stable updates removed from lookaside": Long(),
                    "set timestamp calls": Long(),
                    "set timestamp commit calls": Long(),
                    "set timestamp commit updates": Long(),
                    "set timestamp oldest calls": Long(),
                    "set timestamp oldest updates": Long(),
                    "set timestamp stable calls": Long(),
                    "set timestamp stable updates": Long(),
                    "transaction begins": Long(),
                    "transaction checkpoint currently running": Long(),
                    "transaction checkpoint generation": Long(),
                    "transaction checkpoint max time (msecs)": Long(),
                    "transaction checkpoint min time (msecs)": Long(),
                    "transaction checkpoint most recent time (msecs)": Long(),
                    "transaction checkpoint scrub dirty target": Long(),
                    "transaction checkpoint scrub time (msecs)": Long(),
                    "transaction checkpoint total time (msecs)": Long(),
                    "transaction checkpoints": Long(),
                    "transaction checkpoints skipped because database was clean": Long(),
                    "transaction failures due to cache overflow": Long(),
                    "transaction fsync calls for checkpoint after allocating the transaction ID": Long(),
                    "transaction fsync calls for checkpoint before allocating the transaction ID": Long(),
                    "transaction fsync duration for checkpoint after allocating the transaction ID (usecs)": Double(), #upgraded to float,
                    "transaction fsync duration for checkpoint before allocating the transaction ID (usecs)": Double(), #upgraded to float,
                    "transaction range of IDs currently pinned": Long(),
                    "transaction range of IDs currently pinned by a checkpoint": Long(),
                    "transaction range of IDs currently pinned by named snapshots": Long(),
                    "transaction range of timestamps currently pinned": Long(),
                    "transaction range of timestamps pinned by a checkpoint": Long(),
                    "transaction range of timestamps pinned by the oldest timestamp": Long(),
                    "transaction sync calls": Long(),
                    "transactions committed": Long(),
                    "transactions rolled back": Long(),
                    "update conflicts": Long()
                }),
                "uri": Text()
            }),
            "writeBacksQueued": Boolean()
        })
    })
    mqtt = Nested(properties={
        "code": Long(),
        "messages": Nested(multi=True, properties={
            "payload": Text(), #nullable,
            "topic": Text()
        })
    })
    msrpc = Nested(properties={
        "actual_count": Long(),
        "entries": Nested(multi=True, properties={
            "annotation_length": Long(),
            "annotation_offset": Long(),
            "object": Text(),
            "referent_id": Long(),
            "tower": Nested(properties={
                "ip_address": Text(),
                "length": Long(),
                "num_floors": Long(),
                "tcp_port": Long(),
                "uuid": Text(),
                "ncalrpc": Text(),
                "ncacn_np": Text(),
                "netbios": Text(),
                "ncacn_http": Long(),
                "udp_port": Long()
            })
        }),
        "max_count": Long(),
        "num_entries": Long(),
        "offset": Long()
    })
    mssql = Nested(properties={
        "dns_computer_name": Text(),
        "dns_domain_name": Text(),
        "dns_forest_name": Text(),
        "flags": Text(),
        "netbios_computer_name": Text(),
        "netbios_domain_name": Text(),
        "os_version": Text(),
        "target_realm": Text(),
        "timestamp": Long()
    })
    nats = Nested(properties={
        "auth_required": Boolean(),
        "go": Text(),
        "host": Text(),
        "max_payload": Long(),
        "port": Long(),
        "server_id": Text(),
        "ssl_required": Boolean(),
        "tls_required": Boolean(),
        "tls_verify": Boolean(),
        "version": Text()
    })
    ndmp = Nested(properties={
        "devices": Nested(multi=True, properties={
            "fs_logical_device": Text(),
            "fs_physical_device": Text(),
            "fs_type": Text()
        })
    })
    netbios = Nested(properties={
        "mac": Text(),
        "names": Nested(multi=True, properties={
            "flags": Long(),
            "name": Text(),
            "suffix": Long()
        }),
        "networks": Text(multi=True),
        "raw": Text(multi=True),
        "server_name": Text(),
        "servername": Text(), #nullable,
        "username": Text(), #nullable
    })
    netgear = Nested(properties={
        "description": Text(),
        "firewall_version": Text(),
        "firmware_version": Text(),
        "first_use_date": Text(),
        "model_name": Text(),
        "serial_number": Text(),
        "smartagent_version": Text(),
        "vpn_version": Text()
    })
    ntp = Nested(properties={
        "LANTIME": Text(),
        "clk_jitter": Text(), #multiple types: float, str,
        "clk_wander": Text(), #multiple types: float, str,
        "clock": Text(),
        "clock_offset": Double(),
        "delay": Double(),
        "digest": Text(),
        "expire": Long(),
        "flags": Text(),
        "frequency": Text(), #multiple types: float, str,
        "host": Text(),
        "jitter": Double(),
        "leap": Long(),
        "leapsec": Long(),
        "mintc": Long(),
        "monlist": Nested(properties={
            "__set_values": Object(), #nullable,
            "connections": Text(multi=True),
            "more": Boolean()
        }),
        "noise": Double(),
        "offset": Text(), #multiple types: float, str,
        "peer": Long(),
        "phase": Double(),
        "poll": Long(),
        "precision": Long(),
        "processor": Text(),
        "refid": Text(), #multiple types: int, str,
        "reftime": Text(), #multiple types: float, str,
        "root_delay": Double(),
        "root_dispersion": Double(),
        "rootdelay": Text(), #multiple types: float, str,
        "rootdisp": Text(), #multiple types: float, str,
        "rootdispersion": Double(),
        "signature": Text(),
        "stability": Text(), #multiple types: float, str,
        "state": Long(),
        "stratum": Long(),
        "sys_jitter": Text(), #multiple types: float, str,
        "system": Text(),
        "tai": Text(), #multiple types: int, str,
        "tc": Long(),
        "version": Text(), #multiple types: int, str
    })
    openflow = Nested(properties={
        "supported_versions": Text(multi=True),
        "version": Text()
    })
    openwebnet = Nested(properties={
        "date_and_time": Text(),
        "device_type": Text(),
        "distribution_version": Text(),
        "firmware_version": Text(),
        "ip_address": Text(),
        "kernel_version": Text(),
        "mac_address": Text(),
        "net_mask": Text(),
        "systems": Nested(properties={
            "automation": Long(),
            "burglar_alarm": Long(),
            "heating": Long(),
            "lighting": Long(),
            "power_management": Long()
        }),
        "uptime": Text()
    })
    opts = Nested(properties={
        "afp": Nested(properties={
            "AFP Versions": Text(multi=True),
            "Directory Names": Text(multi=True),
            "Machine Type": Text(),
            "Server Flags": Nested(properties={
                "Copy File": Boolean(),
                "Flags Hex": Text(),
                "Open Directory": Boolean(),
                "Password Changing": Boolean(),
                "Password Saving Prohibited": Boolean(),
                "Reconnect": Boolean(),
                "Server Messages": Boolean(),
                "Server Notifications": Boolean(),
                "Server Signature": Boolean(),
                "Super Client": Boolean(),
                "TCP/IP": Boolean(),
                "UTF-8 Server Name": Boolean(),
                "UUIDs": Boolean()
            }),
            "Server Name": Text(),
            "Server Signature": Text(),
            "UAMs": Text(multi=True),
            "UTF-8 Server Name": Text()
        }),
        "amqp": Nested(properties={
            "encoded": Text(),
            "locales": Text(),
            "mechanisms": Text(),
            "server_properties": Nested(properties={
                "capabilities": Nested(properties={
                    "basic.nack": Boolean(),
                    "consumer_cancel_notify": Boolean(),
                    "exchange_exchange_bindings": Boolean(),
                    "publisher_confirms": Boolean()
                }),
                "copyright": Text(),
                "information": Text(),
                "platform": Text(),
                "product": Text(),
                "version": Text()
            }),
            "version_major": Long(),
            "version_minor": Long()
        }),
        "bacnet": Nested(properties={
            "bbmd": Nested(multi=True, properties={
                "ip": Text(),
                "port": Long()
            }),
            "fdt": Nested(multi=True, properties={
                "ip": Text(),
                "port": Long(),
                "timeout": Long(),
                "ttl": Long()
            })
        }),
        "bitcoin": Nested(properties={
            "addresses": Object(multi=True),
            "handshake": Nested(multi=True, properties={
                "checksum": Text(),
                "command": Text(),
                "from_addr": Nested(properties={
                    "ipv4": Text(),
                    "ipv6": Text(),
                    "port": Long(),
                    "services": Long(),
                    "timestamp": Object(), #nullable
                }),
                "lastblock": Long(),
                "length": Long(),
                "magic_number": Text(),
                "nonce": Long(), #signed int64 overflow,
                "relay": Boolean(),
                "services": Long(),
                "timestamp": Long(),
                "to_addr": Nested(properties={
                    "ipv4": Text(),
                    "ipv6": Text(),
                    "port": Long(),
                    "services": Long(),
                    "timestamp": Object(), #nullable
                }),
                "user_agent": Text(),
                "version": Long()
            })
        }),
        "buildinfo": Text(),
        "command": Long(),
        "command_length": Long(),
        "command_status": Long(),
        "couchdb": Nested(properties={
            "error": Text(),
            "reason": Text()
        }),
        "data": Text(),
        "device_type": Text(), #multiple types: int, str,
        "dhcp": Nested(properties={
            "broadcast": Boolean(),
            "chaddr": Text(),
            "ciaddr": Text(),
            "file": Text(),
            "giaddr": Text(),
            "options": Object(),
            "secs": Text(),
            "siaddr": Text(),
            "sname": Text(),
            "xid": Text(),
            "yiaddr": Text()
        }),
        "dvr": Text(),
        "encapsulation_length": Long(),
        "hdfs_namenode": Nested(properties={
            "BlockPoolId": Text(),
            "BlockPoolUsedSpace": Long(),
            "CacheCapacity": Long(),
            "CacheUsed": Long(),
            "ClusterId": Text(),
            "CompileInfo": Text(),
            "CorruptFiles": Text(),
            "DeadNodes": Text(),
            "DecomNodes": Text(),
            "DistinctVersionCount": Long(),
            "DistinctVersions": Nested(multi=True, properties={
                "key": Text(),
                "value": Long()
            }),
            "Files": Object(multi=True),
            "Free": Long(),
            "JournalTransactionInfo": Text(),
            "LiveNodes": Text(),
            "NNStarted": Text(),
            "NNStartedTimeInMillis": Long(),
            "NameDirStatuses": Text(),
            "NameJournalStatus": Text(),
            "NodeUsage": Text(),
            "NonDfsUsedSpace": Long(),
            "NumberOfMissingBlocks": Long(),
            "NumberOfMissingBlocksWithReplicationFactorOne": Long(),
            "NumberOfSnapshottableDirs": Long(),
            "PercentBlockPoolUsed": Double(),
            "PercentRemaining": Double(),
            "PercentUsed": Double(),
            "RollingUpgradeStatus": Object(), #nullable,
            "Safemode": Text(),
            "SoftwareVersion": Text(),
            "Threads": Long(),
            "Total": Long(),
            "TotalBlocks": Long(),
            "TotalFiles": Long(),
            "UpgradeFinalized": Boolean(),
            "Used": Long(),
            "Version": Text(),
            "modelerType": Text(),
            "name": Text()
        }),
        "heartbleed": Text(),
        "ip": Text(),
        "item_count": Long(),
        "ldap": Nested(properties={
            "SupportedLDAPVersion": Text(multi=True),
            "altServer": Text(multi=True),
            "configurationNamingContext": Text(),
            "currentTime": Text(),
            "dNSHostName": Text(),
            "defaultNamingContext": Text(),
            "dnsHostName": Text(),
            "domainFunctionality": Text(),
            "dsServiceName": Text(),
            "errorMessage": Text(),
            "forestFunctionality": Text(),
            "highestCommittedUSN": Text(),
            "isGlobalCatalogReady": Text(),
            "isSynchronized": Text(),
            "ldapServiceName": Text(),
            "namingContexts": Text(multi=True), #single or multi,
            "namingcontexts": Text(multi=True), #single or multi,
            "resultCode": Text(),
            "rootDomainNamingContext": Text(),
            "schemaNamingContext": Text(),
            "serverName": Text(),
            "subSchemaSubEntry": Text(),
            "subSchemaSubentry": Text(),
            "subschemaSubentry": Text(),
            "subschemasubentry": Text(),
            "supportedCapabilities": Text(multi=True),
            "supportedControl": Text(multi=True), #single or multi,
            "supportedExtension": Text(multi=True), #single or multi,
            "supportedLDAPPolicies": Text(multi=True),
            "supportedLDAPVersion": Text(multi=True), #single or multi,
            "supportedLDAPversion": Text(multi=True),
            "supportedSASLMechanisms": Text(multi=True), #single or multi,
            "supportedcontrol": Text(multi=True),
            "supportedextension": Text(multi=True),
            "supportedldapversion": Text(multi=True),
            "supportedsaslmechanisms": Text(multi=True), #single or multi
        }),
        "listDatabases": Text(),
        "mac": Text(),
        "minecraft": Nested(properties={
            "description": Text(),
            "favicon": Text(),
            "forgeData": Nested(properties={
                "channels": Nested(multi=True, properties={
                    "required": Boolean(),
                    "res": Text(),
                    "version": Text()
                }),
                "fmlNetworkVersion": Long(),
                "mods": Nested(multi=True, properties={
                    "modId": Text(),
                    "modmarker": Text()
                })
            }),
            "modinfo": Nested(properties={
                "modList": Nested(multi=True, properties={
                    "modid": Text(),
                    "version": Text()
                }),
                "type": Text()
            }),
            "players": Nested(properties={
                "max": Long(),
                "online": Long(),
                "sample": Nested(multi=True, properties={
                    "id": Text(),
                    "name": Text()
                })
            }),
            "version": Nested(properties={
                "name": Text(),
                "protocol": Long()
            })
        }),
        "modbus": Nested(multi=True, properties={
            "response": Text(multi=True),
            "uid": Long()
        }),
        "names": Nested(multi=True, properties={
            "flags": Long(),
            "name": Text(),
            "suffix": Long()
        }),
        "ntp": Nested(properties={
            "more": Boolean()
        }),
        "options": Long(),
        "product_code": Long(),
        "product_name": Text(),
        "product_name_length": Long(),
        "raw": Text(),
        "revision_major": Long(),
        "revision_minor": Long(),
        "s7": Nested(properties={
            "dst_tsap": Text(),
            "identities": Nested(properties={
                "Basic Firmware": Nested(properties={
                    "raw": Text(),
                    "value": Text()
                }),
                "Basic Hardware": Nested(properties={
                    "raw": Text(),
                    "value": Text()
                }),
                "Copyright": Nested(properties={
                    "raw": Text(),
                    "value": Text()
                }),
                "Module": Nested(properties={
                    "raw": Text(),
                    "value": Text()
                }),
                "Module name": Nested(properties={
                    "raw": Text(),
                    "value": Text()
                }),
                "Module type": Nested(properties={
                    "raw": Text(),
                    "value": Text()
                }),
                "PLC name": Nested(properties={
                    "raw": Text(),
                    "value": Text()
                }),
                "Plant identification": Nested(properties={
                    "raw": Text(),
                    "value": Text()
                }),
                "Reserved for operating system": Nested(properties={
                    "raw": Text(),
                    "value": Text()
                }),
                "Serial number of memory card": Nested(properties={
                    "raw": Text(),
                    "value": Text()
                }),
                "Serial number of module": Nested(properties={
                    "raw": Text(),
                    "value": Text()
                }),
                "Unknown (129)": Nested(properties={
                    "raw": Text(),
                    "value": Text()
                })
            }),
            "src_tsap": Text()
        }),
        "samsung_tv": Nested(properties={
            "Capabilities": Nested(multi=True, properties={
                "location": Text(),
                "name": Text(),
                "port": Text()
            }),
            "CountryCode": Text(),
            "DUID": Text(),
            "DeviceID": Text(),
            "DeviceName": Text(),
            "DialURI": Text(),
            "FirmwareVersion": Text(),
            "IP": Text(),
            "Model": Text(),
            "ModelDescription": Text(),
            "ModelName": Text(),
            "NetworkType": Text(),
            "Resolution": Text(),
            "SSID": Text(),
            "ServiceURI": Text(),
            "SmartHubAgreement": Text(),
            "UDN": Text()
        }),
        "screenshot": Nested(properties={
            "data": Text(),
            "hash": Long(),
            "labels": Text(multi=True),
            "mime": Text(),
            "text": Text()
        }),
        "sender_context": Text(),
        "serial": Long(),
        "serverStatus": Text(),
        "session": Long(),
        "socket_addr": Text(),
        "state": Long(),
        "status": Long(),
        "steam-a2s": Nested(properties={
            "address": Text(),
            "app_id": Long(),
            "bots": Long(),
            "client_dll": Long(),
            "folder": Text(),
            "game": Text(),
            "game_port": Long(),
            "is_mod": Long(),
            "map": Text(),
            "max_players": Long(),
            "mod_size": Long(),
            "mod_version": Long(),
            "name": Text(),
            "os": Text(),
            "password": Long(),
            "players": Long(),
            "protocol": Long(),
            "secure": Long(),
            "server_only": Long(),
            "server_type": Text(),
            "spec_name": Text(),
            "spec_port": Long(),
            "steam_id": Long(),
            "tags": Text(),
            "url_download": Text(),
            "url_info": Text(),
            "version": Text(), #multiple types: int, str,
            "visibility": Long()
        }),
        "telnet": Nested(properties={
            "do": Text(multi=True),
            "dont": Text(multi=True),
            "will": Text(multi=True),
            "wont": Text(multi=True)
        }),
        "type_id": Long(),
        "vendor_id": Text(), #multiple types: int, str,
        "version": Long(),
        "vulns": Text(multi=True)
    })
    org = Text(), #nullable
    os = Text(), #nullable
    pcworx = Nested(properties={
        "firmware_date": Text(),
        "firmware_time": Text(),
        "firmware_version": Text(),
        "model_number": Text(),
        "plc_type": Text()
    })
    platform = Text()
    port = Long()
    product = Text()
    realport = Nested(properties={
        "name": Text(),
        "ports": Long()
    })
    redis = Nested(properties={
        "clients": Nested(properties={
            "__set_values": Nested(multi=True, properties={
                "addr": Text(),
                "age": Long(),
                "argv-mem": Long(),
                "cmd": Text(),
                "db": Long(),
                "events": Text(),
                "fd": Long(),
                "flags": Text(),
                "id": Long(),
                "idle": Long(),
                "multi": Long(),
                "name": Text(),
                "obl": Long(),
                "oll": Long(),
                "omem": Long(), #signed int64 overflow,
                "psub": Long(),
                "qbuf": Long(),
                "qbuf-free": Long(),
                "sub": Long(),
                "tot-mem": Long(),
                "user": Text(),
                "laddr": Text(),
                "redir": Long()
            }),
            "blocked_clients": Long(),
            "client_biggest_input_buf": Long(),
            "client_longest_output_list": Long(),
            "client_recent_max_input_buffer": Long(),
            "client_recent_max_output_buffer": Long(),
            "connected_clients": Long()
        }),
        "cluster": Nested(properties={
            "__set_values": Text(multi=True),
            "cluster_enabled": Long()
        }),
        "cpu": Nested(properties={
            "used_cpu_sys": Double(),
            "used_cpu_sys_children": Double(),
            "used_cpu_sys_main_thread": Double(),
            "used_cpu_user": Double(),
            "used_cpu_user_children": Double(),
            "used_cpu_user_main_thread": Double()
        }),
        "errorstats": Nested(properties={
            "errorstat_ERR": Text(),
            "errorstat_MISCONF": Text(),
            "errorstat_NOSCRIPT": Text(),
            "errorstat_READONLY": Text(),
            "errorstat_UNBLOCKED": Text()
        }),
        "keys": Nested(properties={
            "data": Text(multi=True),
            "more": Boolean()
        }),
        "keyspace": Nested(properties={
            "db0": Text(),
            "db1": Text(),
            "db3": Text()
        }),
        "memory": Nested(properties={
            "active_defrag_running": Long(),
            "allocator_active": Long(),
            "allocator_allocated": Long(),
            "allocator_frag_bytes": Long(),
            "allocator_frag_ratio": Double(),
            "allocator_resident": Long(),
            "allocator_rss_bytes": Long(),
            "allocator_rss_ratio": Double(),
            "lazyfree_pending_objects": Long(),
            "lazyfreed_objects": Long(),
            "maxmemory": Long(),
            "maxmemory_human": Text(),
            "maxmemory_policy": Text(),
            "mem_allocator": Text(),
            "mem_aof_buffer": Long(),
            "mem_clients_normal": Long(),
            "mem_clients_slaves": Long(),
            "mem_fragmentation_bytes": Long(),
            "mem_fragmentation_ratio": Double(),
            "mem_not_counted_for_evict": Long(),
            "mem_replication_backlog": Long(),
            "number_of_cached_scripts": Long(),
            "rss_overhead_bytes": Long(),
            "rss_overhead_ratio": Double(),
            "total_system_memory": Long(),
            "total_system_memory_human": Text(),
            "used_memory": Long(),
            "used_memory_dataset": Long(), #signed int64 overflow,
            "used_memory_dataset_perc": Text(),
            "used_memory_human": Text(),
            "used_memory_lua": Long(),
            "used_memory_lua_human": Text(),
            "used_memory_overhead": Long(),
            "used_memory_peak": Long(),
            "used_memory_peak_human": Text(),
            "used_memory_peak_perc": Text(),
            "used_memory_rss": Long(),
            "used_memory_rss_human": Text(),
            "used_memory_scripts": Long(),
            "used_memory_scripts_human": Text(),
            "used_memory_startup": Long()
        }),
        "modules": Object(),
        "ok": Object(),
        "persistence": Nested(properties={
            "aof_base_size": Long(),
            "aof_buffer_length": Long(),
            "aof_current_rewrite_time_sec": Long(),
            "aof_current_size": Long(),
            "aof_delayed_fsync": Long(),
            "aof_enabled": Long(),
            "aof_last_bgrewrite_status": Text(),
            "aof_last_cow_size": Long(),
            "aof_last_rewrite_time_sec": Long(),
            "aof_last_write_status": Text(),
            "aof_pending_bio_fsync": Long(),
            "aof_pending_rewrite": Long(),
            "aof_rewrite_buffer_length": Long(),
            "aof_rewrite_in_progress": Long(),
            "aof_rewrite_scheduled": Long(),
            "current_cow_size": Long(),
            "current_fork_perc": Text(),
            "current_save_keys_processed": Long(),
            "current_save_keys_total": Long(),
            "loading": Long(),
            "module_fork_in_progress": Long(),
            "module_fork_last_cow_size": Long(),
            "rdb_bgsave_in_progress": Long(),
            "rdb_changes_since_last_save": Long(),
            "rdb_current_bgsave_time_sec": Long(),
            "rdb_last_bgsave_status": Text(),
            "rdb_last_bgsave_time_sec": Long(),
            "rdb_last_cow_size": Long(),
            "rdb_last_save_time": Long()
        }),
        "replication": Nested(properties={
            "connected_slaves": Long(),
            "master_failover_state": Text(),
            "master_host": Text(),
            "master_last_io_seconds_ago": Long(),
            "master_link_down_since_seconds": Long(),
            "master_link_status": Text(),
            "master_port": Long(),
            "master_repl_meaningful_offset": Long(),
            "master_repl_offset": Long(),
            "master_replid": Text(), #multiple types: int, str,
            "master_replid2": Text(), #multiple types: int, str,
            "master_sync_in_progress": Long(),
            "repl_backlog_active": Long(),
            "repl_backlog_first_byte_offset": Long(),
            "repl_backlog_histlen": Long(),
            "repl_backlog_size": Long(),
            "role": Text(),
            "second_repl_offset": Long(),
            "slave0": Text(),
            "slave_priority": Long(),
            "slave_read_only": Long(),
            "slave_repl_offset": Long()
        }),
        "server": Nested(properties={
            "arch_bits": Long(),
            "atomicvar_api": Text(),
            "config_file": Text(),
            "configured_hz": Long(),
            "executable": Text(),
            "gcc_version": Text(),
            "hz": Long(),
            "io_threads_active": Long(),
            "lru_clock": Long(),
            "multiplexing_api": Text(),
            "os": Text(),
            "process_id": Long(),
            "process_supervised": Text(),
            "redis_build_id": Text(), #multiple types: int, str,
            "redis_git_dirty": Long(),
            "redis_git_sha1": Long(),
            "redis_mode": Text(),
            "redis_version": Text(),
            "run_id": Text(),
            "server_time_usec": Long(),
            "tcp_port": Long(),
            "uptime_in_days": Long(),
            "uptime_in_seconds": Long()
        }),
        "ssl": Nested(properties={
            "ssl_connections_to_current_certificate": Long(),
            "ssl_connections_to_previous_certificate": Long(),
            "ssl_current_certificate_not_after_date": Text(),
            "ssl_current_certificate_not_before_date": Text(),
            "ssl_current_certificate_serial": Long(),
            "ssl_enabled": Text()
        }),
        "stats": Nested(properties={
            "active_defrag_hits": Long(),
            "active_defrag_key_hits": Long(),
            "active_defrag_key_misses": Long(),
            "active_defrag_misses": Long(),
            "dump_payload_sanitizations": Long(),
            "evicted_keys": Long(),
            "expire_cycle_cpu_milliseconds": Long(),
            "expired_keys": Long(),
            "expired_stale_perc": Double(),
            "expired_time_cap_reached_count": Long(),
            "instantaneous_input_kbps": Double(),
            "instantaneous_ops_per_sec": Long(),
            "instantaneous_output_kbps": Double(),
            "io_threaded_reads_processed": Long(),
            "io_threaded_writes_processed": Long(),
            "keyspace_hits": Long(),
            "keyspace_misses": Long(),
            "latest_fork_usec": Long(),
            "migrate_cached_sockets": Long(),
            "pubsub_channels": Long(),
            "pubsub_patterns": Long(),
            "rejected_connections": Long(),
            "slave_expires_tracked_keys": Long(),
            "sync_full": Long(),
            "sync_partial_err": Long(),
            "sync_partial_ok": Long(),
            "total_commands_processed": Long(),
            "total_connections_received": Long(),
            "total_error_replies": Long(),
            "total_forks": Long(),
            "total_net_input_bytes": Long(),
            "total_net_output_bytes": Long(),
            "total_reads_processed": Long(),
            "total_writes_processed": Long(),
            "tracking_total_items": Long(),
            "tracking_total_keys": Long(),
            "tracking_total_prefixes": Long(),
            "unexpected_error_replies": Long()
        })
    })
    rip = Nested(properties={
        "addresses": Nested(multi=True, properties={
            "addr": Text(),
            "family": Text(),
            "metric": Long(),
            "next_hop": Object(), #nullable,
            "subnet": Object(), #nullable,
            "tag": Object(), #nullable
        }),
        "command": Long(),
        "version": Long()
    })
    ripple = Nested(properties={
        "peers": Nested(multi=True, properties={
            "ip": Text(),
            "public_key": Text(),
            "type": Text(),
            "uptime": Long(),
            "version": Text(),
            "complete_ledgers": Text(),
            "port": Text(), #multiple types: int, str
        })
    })
    rsync = Nested(properties={
        "authentication": Boolean(),
        "modules": Nested(multi=True, properties={
            "__set_values": Text(), #nullable,
            "identifier": Text()
        })
    })
    shodan = Nested(properties={
        "crawler": Text(),
        "id": Text(),
        "module": Text(),
        "options": Nested(properties={
            "hostname": Text(),
            "referrer": Text(),
            "scan": Text()
        }),
        "ptr": Boolean()
    })
    smb = Nested(properties={
        "anonymous": Boolean(),
        "capabilities": Text(multi=True),
        "os": Text(),
        "raw": Text(multi=True),
        "shares": Nested(multi=True, properties={
            "comments": Text(),
            "name": Text(),
            "special": Boolean(),
            "temporary": Boolean(),
            "type": Text(),
            "files": Nested(multi=True, properties={
                "directory": Boolean(),
                "name": Text(),
                "read-only": Boolean(),
                "size": Long()
            })
        }),
        "smb_version": Long(),
        "software": Text()
    })
    snmp = Nested(properties={
        "contact": Text(), #nullable,
        "description": Text(), #nullable,
        "location": Text(), #nullable,
        "name": Text(), #nullable,
        "objectid": Text(), #nullable,
        "ordescr": Text(),
        "orid": Text(),
        "orindex": Text(),
        "orlastchange": Text(),
        "oruptime": Text(),
        "services": Text(), #nullable,
        "uptime": Text(), #nullable
    })
    sonos = Nested(properties={
        "friendly_name": Text(),
        "hardware_version": Text(),
        "model_name": Text(),
        "model_number": Text(),
        "raw": Text(),
        "room_name": Text(),
        "serial_number": Text(),
        "software_version": Text(),
        "udn": Text()
    })
    ssh = Nested(properties={
        "cipher": Text(),
        "fingerprint": Text(),
        "hassh": Text(),
        "kex": Nested(properties={
            "compression_algorithms": Text(multi=True),
            "encryption_algorithms": Text(multi=True),
            "kex_algorithms": Text(multi=True),
            "kex_follows": Boolean(),
            "languages": Text(multi=True),
            "mac_algorithms": Text(multi=True),
            "server_host_key_algorithms": Text(multi=True),
            "unused": Long()
        }),
        "key": Text(),
        "mac": Text(),
        "type": Text()
    })
    ssl = Nested(properties={
        "acceptable_cas": Nested(multi=True, properties={
            "components": Nested(properties={
                "CN": Text(),
                "DC": Text(),
                "C": Text(),
                "O": Text(),
                "OU": Text(),
                "ST": Text(),
                "L": Text(),
                "emailAddress": Text(),
                "serialNumber": Text(),
                "UNDEF": Text(),
                "name": Text(),
                "businessCategory": Text(),
                "jurisdictionC": Text(),
                "jurisdictionST": Text(),
                "postalCode": Text(),
                "street": Text(),
                "mail": Text(),
                "telephoneNumber": Text(),
                "UID": Text(),
                "title": Text(),
                "SN": Text(),
                "role": Text(),
                "GN": Text(),
                "dnQualifier": Text(),
                "friendlyName": Text(),
                "description": Text(),
                "subjectAltName": Text(),
                "jurisdictionL": Text()
            }),
            "hash": Long(),
            "raw": Text()
        }),
        "alpn": Text(multi=True),
        "cert": Nested(properties={
            "expired": Boolean(),
            "expires": Text(),
            "extensions": Nested(multi=True, properties={
                "critical": Boolean(),
                "data": Text(),
                "name": Text()
            }),
            "fingerprint": Nested(properties={
                "sha1": Text(),
                "sha256": Text()
            }),
            "issued": Text(),
            "issuer": Nested(properties={
                "C": Text(),
                "CN": Text(),
                "DC": Text(),
                "GN": Text(),
                "L": Text(),
                "O": Text(),
                "OU": Text(),
                "SN": Text(),
                "ST": Text(),
                "UID": Text(),
                "UNDEF": Text(),
                "contentType": Text(),
                "description": Text(),
                "dnQualifier": Text(),
                "emailAddress": Text(),
                "emailProtection": Text(),
                "friendlyName": Text(),
                "generationQualifier": Text(),
                "houseIdentifier": Text(),
                "initials": Text(),
                "name": Text(),
                "postalCode": Text(),
                "pseudonym": Text(),
                "role": Text(),
                "serialNumber": Text(),
                "street": Text(),
                "subjectAltName": Text(),
                "telephoneNumber": Text(),
                "title": Text(),
                "unstructuredAddress": Text(),
                "unstructuredName": Text()
            }),
            "pubkey": Nested(properties={
                "bits": Long(),
                "type": Text()
            }),
            "serial": Long(), #signed int64 overflow,
            "sig_alg": Text(),
            "subject": Nested(properties={
                "C": Text(),
                "CN": Text(),
                "DC": Text(),
                "GN": Text(),
                "L": Text(),
                "O": Text(),
                "OU": Text(),
                "SN": Text(),
                "ST": Text(),
                "UID": Text(),
                "UNDEF": Text(),
                "businessCategory": Text(),
                "contentType": Text(),
                "description": Text(),
                "dnQualifier": Text(),
                "emailAddress": Text(),
                "emailProtection": Text(),
                "generationQualifier": Text(),
                "initials": Text(),
                "jurisdictionC": Text(),
                "jurisdictionL": Text(),
                "jurisdictionST": Text(),
                "mail": Text(),
                "name": Text(),
                "postOfficeBox": Text(),
                "postalCode": Text(),
                "pseudonym": Text(),
                "role": Text(),
                "serialNumber": Text(),
                "street": Text(),
                "subjectAltName": Text(),
                "telephoneNumber": Text(),
                "title": Text(),
                "unstructuredAddress": Text(),
                "unstructuredName": Text()
            }),
            "version": Long()
        }),
        "chain": Text(multi=True),
        "chain_sha256": Text(multi=True),
        "cipher": Nested(properties={
            "__set_values": Object(), #nullable,
            "bits": Long(),
            "name": Text(),
            "version": Text()
        }),
        "dhparams": Nested(properties={
            "__set_values": Object(), #nullable,
            "bits": Long(),
            "fingerprint": Text(),
            "generator": Text(), #multiple types: int, str,
            "prime": Text(),
            "public_key": Text()
        }),
        "ja3s": Text(), #nullable,
        "jarm": Text(),
        "ocsp": Nested(properties={
            "cert_status": Text(),
            "certificate_id": Nested(properties={
                "hash_algorithm": Text(),
                "issuer_name_hash": Text(),
                "issuer_name_key": Text(),
                "serial_number": Text()
            }),
            "next_update": Text(),
            "produced_at": Text(),
            "responder_id": Text(),
            "response_status": Text(),
            "signature_algorithm": Text(),
            "this_update": Text(),
            "version": Text()
        }),
        "tlsext": Nested(multi=True, properties={
            "id": Long(),
            "name": Text()
        }),
        "trust": Nested(properties={
            "browser": Nested(properties={
                "__set_values": Object(), #nullable,
                "apple": Boolean(),
                "microsoft": Boolean(),
                "mozilla": Boolean()
            }),
            "revoked": Nested(properties={
                "__set_values": Boolean(),
                "apple": Boolean(),
                "microsoft": Boolean(),
                "mozilla": Boolean()
            })
        }),
        "unstable": Text(multi=True),
        "versions": Text(multi=True)
    })
    steam_ihs = Nested(properties={
        "client_id": Text(),
        "connect_port": Long(),
        "enabled_services": Long(),
        "euniverse": Long(),
        "hostname": Text(),
        "instance_id": Text(),
        "ip_addresses": Text(multi=True),
        "is_64bit": Boolean(),
        "mac_addresses": Text(multi=True),
        "min_version": Long(),
        "os_type": Long(),
        "public_ip_address": Text(),
        "timestamp": Long(),
        "users": Nested(multi=True, properties={
            "auth_key_id": Long(),
            "steam_id": Text()
        }),
        "version": Long()
    })
    tacacs = Nested(properties={
        "flags": Long(),
        "length": Long(),
        "sequence": Long(),
        "session": Long(),
        "type": Long(),
        "version": Text()
    })
    tags = Text(multi=True)
    telnet = Nested(properties={
        "do": Text(multi=True),
        "dont": Text(multi=True),
        "will": Text(multi=True),
        "wont": Text(multi=True)
    })
    tibia = Nested(properties={
        "map": Nested(properties={
            "author": Text(),
            "height": Long(),
            "name": Text(),
            "width": Long()
        }),
        "monsters": Nested(properties={
            "total": Long()
        }),
        "motd": Object(),
        "npcs": Nested(properties={
            "total": Long()
        }),
        "owner": Nested(properties={
            "email": Text(),
            "name": Text()
        }),
        "players": Nested(properties={
            "max": Long(),
            "online": Long(),
            "peak": Long()
        }),
        "serverinfo": Nested(properties={
            "client": Double(),
            "ip": Text(),
            "location": Text(),
            "port": Long(),
            "server": Text(),
            "servername": Text(),
            "uptime": Long(),
            "url": Text(),
            "version": Double()
        })
    })
    timestamp = Text()
    title = Text()
    transport = Text()
    ubiquiti = Nested(properties={
        "hostname": Text(),
        "ip": Text(),
        "ip_alt": Text(),
        "mac": Text(),
        "mac_alt": Text(),
        "product": Text(),
        "version": Text()
    })
    unitronics_pcom = Nested(properties={
        "hardware_version": Text(),
        "model": Text(),
        "os_build": Long(),
        "os_version": Double(),
        "plc_name": Text(),
        "plc_unique_id": Long(),
        "uid_master": Long()
    })
    upnp = Nested(properties={
        "device_type": Text(),
        "friendly_name": Text(),
        "manufacturer": Text(),
        "manufacturer_url": Text(),
        "model_description": Text(),
        "model_name": Text(),
        "model_number": Text(),
        "model_url": Text(),
        "serial_number": Text(),
        "sub_devices": Nested(multi=True, properties={
            "device_type": Text(),
            "friendly_name": Text(),
            "manufacturer": Text(),
            "manufacturer_url": Text(),
            "model_description": Text(),
            "model_name": Text(),
            "model_number": Text(),
            "model_url": Text(),
            "serial_number": Text(),
            "sub_devices": Nested(multi=True, properties={
                "device_type": Text(),
                "friendly_name": Text(),
                "manufacturer": Text(),
                "manufacturer_url": Text(),
                "model_description": Text(),
                "model_name": Text(),
                "model_number": Text(),
                "model_url": Text(),
                "serial_number": Text(),
                "udn": Text(),
                "upc": Text()
            }),
            "udn": Text(),
            "upc": Text()
        }),
        "udn": Text(),
        "upc": Text()
    })
    version = Text()
    vmware = Nested(properties={
        "api_type": Text(),
        "api_version": Text(),
        "build": Text(),
        "full_name": Text(),
        "locale_build": Text(),
        "locale_version": Text(),
        "name": Text(),
        "os_type": Text(),
        "product_line_id": Text(),
        "vendor": Text(),
        "version": Text()
    })
    vulns = Nested(multi=True, properties={
        "cvss": Double(),
        "identifier": Text(),
        "references": Text(multi=True),
        "summary": Text(),
        "verified": Boolean()
    })


stringized = [
    "elastic.cluster.nodes.os.allocated_processors",
    "elastic.cluster.nodes.os.available_processors",
    "elastic.nodes.nodes.os.available_processors",
    "elastic.nodes.nodes.os.cpu.total_cores",
    "elastic.nodes.nodes.os.cpu.total_sockets",
    "elastic.nodes.nodes.thread_pool.queue_size",
    "etcd.id",
    "ethernetip.device_type",
    "ethernetip.vendor_id",
    "ntp.clk_jitter",
    "ntp.clk_wander",
    "ntp.frequency",
    "ntp.offset",
    "ntp.refid",
    "ntp.reftime",
    "ntp.rootdelay",
    "ntp.rootdisp",
    "ntp.stability",
    "ntp.sys_jitter",
    "ntp.tai",
    "ntp.version",
    "opts.device_type",
    "opts.steam-a2s.version",
    "opts.vendor_id",
    "redis.replication.master_replid",
    "redis.replication.master_replid2",
    "redis.server.redis_build_id",
    "ripple.peers.port",
    "ssl.dhparams.generator",
]


floated = [
    "mongodb.serverStatus.extra_info.page_faults",
    "mongodb.serverStatus.network.bytesIn",
    "mongodb.serverStatus.network.bytesOut",
    "mongodb.serverStatus.uptimeEstimate",
    "mongodb.serverStatus.wiredTiger.block-manager.bytes read",
    "mongodb.serverStatus.wiredTiger.block-manager.bytes written",
    "mongodb.serverStatus.wiredTiger.block-manager.bytes written for checkpoint",
    "mongodb.serverStatus.wiredTiger.cache.application threads page write from cache to disk time (usecs)",
    "mongodb.serverStatus.wiredTiger.cache.bytes dirty in the cache cumulative",
    "mongodb.serverStatus.wiredTiger.cache.bytes written from cache",
    "mongodb.serverStatus.wiredTiger.cache.maximum bytes configured",
    "mongodb.serverStatus.wiredTiger.cache.tracked bytes belonging to internal pages in the cache",
    "mongodb.serverStatus.wiredTiger.cache.tracked bytes belonging to leaf pages in the cache",
    "mongodb.serverStatus.wiredTiger.connection.memory allocations",
    "mongodb.serverStatus.wiredTiger.connection.memory frees",
    "mongodb.serverStatus.wiredTiger.connection.pthread mutex condition wait calls",
    "mongodb.serverStatus.wiredTiger.lock.table lock internal thread time waiting for the table lock (usecs)",
    "mongodb.serverStatus.wiredTiger.log.log bytes of payload data",
    "mongodb.serverStatus.wiredTiger.log.log bytes written",
    "mongodb.serverStatus.wiredTiger.log.log flush operations",
    "mongodb.serverStatus.wiredTiger.log.log force write operations",
    "mongodb.serverStatus.wiredTiger.log.log force write operations skipped",
    "mongodb.serverStatus.wiredTiger.log.log sync time duration (usecs)",
    "mongodb.serverStatus.wiredTiger.log.logging bytes consolidated",
    "mongodb.serverStatus.wiredTiger.log.total in-memory size of compressed records",
    "mongodb.serverStatus.wiredTiger.log.total size of compressed records",
    "mongodb.serverStatus.wiredTiger.transaction.transaction fsync duration for checkpoint after allocating the transaction ID (usecs)",
    "mongodb.serverStatus.wiredTiger.transaction.transaction fsync duration for checkpoint before allocating the transaction ID (usecs)",
]


int64_overflow = [
    "elastic.cluster.indices.segments.max_unsafe_auto_id_timestamp",
    "opts.bitcoin.handshake.nonce",
    "redis.clients.__set_values.omem",
    "redis.memory.used_memory_dataset",
    "ssl.cert.serial",
]


nullable = [
    "afp.network_addresses",
    "cloud.region",
    "cloud.service",
    "coap.resources./station.ct",
    "coap.resources./uspagent.obs",
    "consul.AdvertiseAddrs.RPC",
    "consul.AdvertiseAddrs.SerfLan",
    "consul.AdvertiseAddrs.SerfWan",
    "consul.Autopilot.CleanupDeadServers",
    "consul.Autopilot.DisableUpgradeMigration",
    "consul.Autopilot.MaxTrailingLogs",
    "consul.DNSConfig.ServiceTTL",
    "consul.DeprecatedHTTPAPIResponseHeaders",
    "consul.HTTPConfig.BlockEndpoints",
    "consul.HTTPConfig.ResponseHeaders",
    "consul.Segments",
    "consul.Telemetry.DogStatsdTags",
    "consul.Telemetry.PrefixFilter",
    "consul.Watches",
    "dns.resolver_hostname",
    "dns.resolver_id",
    "dns.software",
    "elastic.nodes.nodes.jvm.using_bundled_jdk",
    "ftp.features_hash",
    "http.html",
    "http.html_hash",
    "http.robots",
    "http.robots_hash",
    "http.securitytxt",
    "http.securitytxt_hash",
    "http.server",
    "http.sitemap",
    "http.sitemap_hash",
    "http.title",
    "influxdb.bind_address",
    "isp",
    "location.area_code",
    "location.city",
    "location.country_code",
    "location.country_code3",
    "location.country_name",
    "location.dma_code",
    "location.latitude",
    "location.longitude",
    "location.postal_code",
    "location.region_code",
    "mac.__set_values",
    "mqtt.messages.payload",
    "netbios.servername",
    "netbios.username",
    "ntp.monlist.__set_values",
    "opts.bitcoin.handshake.from_addr.timestamp",
    "opts.bitcoin.handshake.to_addr.timestamp",
    "opts.hdfs_namenode.RollingUpgradeStatus",
    "org",
    "os",
    "rip.addresses.next_hop",
    "rip.addresses.subnet",
    "rip.addresses.tag",
    "rsync.modules.__set_values",
    "snmp.contact",
    "snmp.description",
    "snmp.location",
    "snmp.name",
    "snmp.objectid",
    "snmp.services",
    "snmp.uptime",
    "ssl.cipher.__set_values",
    "ssl.dhparams.__set_values",
    "ssl.ja3s",
    "ssl.trust.browser.__set_values",
]


single_and_multi = [
    "elastic.nodes.nodes.http.bound_address",
    "elastic.nodes.nodes.settings.cluster.initial_master_nodes",
    "elastic.nodes.nodes.settings.path.data",
    "elastic.nodes.nodes.settings.discovery.seed_hosts",
    "elastic.nodes.nodes.settings.discovery.zen.ping.unicast.hosts",
    "elastic.nodes.nodes.transport.bound_address",
    "opts.ldap.namingContexts",
    "opts.ldap.namingcontexts",
    "opts.ldap.supportedControl",
    "opts.ldap.supportedExtension",
    "opts.ldap.supportedLDAPVersion",
    "opts.ldap.supportedSASLMechanisms",
    "opts.ldap.supportedsaslmechanisms",
]
