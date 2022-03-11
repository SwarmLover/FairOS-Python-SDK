#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.fair_os import FairOs
from core.base_obj import FairBase

class FairKV(FairBase):

    def __init__(self, user_name, 
        passwd,
        pod_name,
        basic_url='http://localhost:9090', 
        time_out=20) -> None:

        self.fair_os = FairOs()
        assert user_name
        self.user_name = user_name
        assert passwd
        self.passwd = passwd
        assert pod_name
        self.pod_name = pod_name

        result = self.fair_os.user_login(user_name=user_name, passwd=passwd)
        if result['code'] != 200:
            raise Exception(f"user_login failed! {result}")
        
        self.login()
        self.open_pod()
        
    
    def __del__(self):
        self.close_pod()
        self.logout()
    
    def new_table(self, table_name, index_type):

        return self.fair_os.kv_new(pod_name=self.pod_name, table_name=table_name, indexType=index_type)
    
    def ls_table(self):

        return self.fair_os.kv_list_tables(pod_name=self.pod_name)
    
    def open_table(self, table_name):
        return self.fair_os.kv_open_table(pod_name=self.pod_name, table_name=table_name)

    def count_table(self, table_name):
        return self.fair_os.kv_count_table(pod_name=self.pod_name, table_name=table_name)
    
    def put(self, table_name, key, value):
        return self.fair_os.kv_put(pod_name=self.pod_name, table_name=table_name, key=key, value=value)

    def get(self, table_name, key):
        return self.fair_os.kv_get(pod_name=self.pod_name, table_name=table_name, key=key)
    
    def get_data(self, table_name, key, format='string'):
        """
        format: string or byte-string
        """
        return self.fair_os.kv_get_data(pod_name=self.pod_name, table_name=table_name, key=key, format=format)
    
    # def seek_key(self, table_name, start_prefix, end_prefix, limit):
    #     return self.fair_os.kv_seek_key(pod_name=self.pod_name, table_name=table_name, start_prefix=start_prefix, end_prefix=end_prefix, limit=limit)
    
    # def get_next(self, table_name):
    #     return self.fair_os.kv_get_next(pod_name=self.pod_name, table_name=table_name)

    def del_val(self,table_name, key):
        return self.fair_os.kv_delete(pod_name=self.pod_name, table_name=table_name, key=key)

    def del_table(self, table_name):

        return self.fair_os.kv_delete_table(pod_name=self.pod_name, table_name=table_name)
    
    # def loadcsv(self, table_name):
    #     return self.fair_os.kv_loadcsv(pod_name=self.pod_name, table_name=table_name)

    def key_present(self, table_name, key):
        return self.fair_os.kv_key_present(pod_name=self.pod_name, table_name=table_name, key=key)
    