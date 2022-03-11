#!/usr/bin/env python
# -*- coding: utf-8 -*-

from importlib.metadata import files
import json
from urllib import request
import requests


class FairOs(object):

    def __init__(self, basic_url='http://localhost:9090', time_out=20) -> None:
        pass
        self.time_out = time_out
        self.basic_url = basic_url
        self.http_headers = {
            'Content-Type': 'application/json'
        }
        self.login_cookie = ''

    def _http_request(self, url, json={}, headers={}, request_type='post', *args, **kwargs):
        
        kwargs.setdefault('url', url)
        kwargs.setdefault('method', request_type)
        kwargs.setdefault('timeout', self.time_out)
        if json:
            kwargs.setdefault('json', json)
        kwargs.setdefault('headers', headers)

        response = requests.request(*args, **kwargs)
        # print(response.status_code)
        # print(response.url)
        # print(response.headers)
        # print(response.text)
        # print((response.cookies))
        # print(response.request.headers)
        # print(response.request.)
        # print(response.request.body)
        return response

    def user_sign_up(self, user_name:str, passwd:str,mnemonic=''):
        
        uri = '/v1/user/signup'
        json = {
            'user_name': user_name,
            'password': passwd,
        }
        if mnemonic:
            json.update({'mnemonic': mnemonic})
        headers = {
            'Content-Type': 'application/json'
        }

        return self._http_request(url=self.basic_url+uri, json=json, headers=headers)

    def user_login(self,user_name:str, passwd:str):
        """
        {'message': 'user logged-in successfully', 'code': 200}
        """
        
        uri = '/v1/user/login'
        json = {
            'user_name': user_name,
            'password': passwd,
        }

        response = self._http_request(url=self.basic_url+uri, json=json, headers=self.http_headers)

        header_dic = dict(response.raw.headers)
        login_cookie = header_dic['Set-Cookie']
        # login_cookie = ''
        self.login_cookie = login_cookie
        self.http_headers.update({'Cookie': login_cookie})
        
        return response.json()

    def user_import(self, user_name, password, eth_address):
        uri = '/v1/user/import'
        json = {
            'user_name': user_name,
            'password': password,
            'address': eth_address
        }

        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers)
        return response.json()
    
    def user_present(self, user_name):
        uri = '/v1/user/present'
        json = {
            'user_name': user_name
        }
        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers,request_type='get')
        return response.json()
    
    def user_logout(self):
        """
        {'message': 'user logged out successfully', 'code': 200}
        """
        uri = '/v1/user/logout'

        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers)
        return response.json()
    
    def user_is_loggined(self, user_name:str):
        """
        {'loggedin': True}
        """
        uri = f'/v1/user/isloggedin?user_name={user_name}'

        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers, request_type='get')
        return response.json()


    def user_export(self):
        uri = '/v1/user/export'
        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers, request_type='post')
        return response.json()


    def pod_receiveinfo(self, file_sharing_reference):
        uri = '/v1/pod/receiveinfo'
        json = {
            'reference':file_sharing_reference
        }
        response = self._http_request(url=self.basic_url+uri, json=json, headers=self.http_headers)
        return response.json()
    
    def pod_receive(self,file_sharing_reference):
        """
        make a pod public and share it with others
        """
        uri = '/v1/pod/receive'
        json = {
            'reference':file_sharing_reference
        }
        response = self._http_request(url=self.basic_url+uri, json=json, headers=self.http_headers)
        return response.json()

    def pod_new(self, pod_name, password):
        uri = '/v1/pod/new'
        json = {
            'pod_name': pod_name,
            'password': password,
        }
        response = self._http_request(url=self.basic_url+uri, json=json, headers=self.http_headers)
        return response.json()
    
    def pod_open(self, pod_name, password):
        """
        {'message': 'pod opened successfully', 'code': 200}
        """
        uri = '/v1/pod/open'
        json = {
            'pod_name': pod_name,
            'password': password,
        }
        response = self._http_request(url=self.basic_url+uri, json=json, headers=self.http_headers)
        return response.json()

    def pod_sync(self, pod_name:str):
        """
        Syncs the latest contents of the pod from Swarm
        """
        uri = '/v1/pod/sync'
        json = {
            'pod_name': pod_name,
        }
        response = self._http_request(url=self.basic_url+uri, json=json, headers=self.http_headers)
        return response.json()
    
    def pod_share(self, pod_name, password):
        """
        Shared a pod
        """
        uri = '/v1/pod/share'
        json = {
            'pod_name': pod_name,
            'password': password
        }
        response = self._http_request(url=self.basic_url+uri, json=json, headers=self.http_headers)
        return response.json()

    def pod_close(self, pod_name:str):
        """
        {'message': 'pod closed successfully', 'code': 200}
        """
        uri = '/v1/pod/close'
        json = {
            'pod_name': pod_name,
        }
        response = self._http_request(url=self.basic_url+uri, json=json, headers=self.http_headers)
        return response.json()

    def pod_delete(self, pod_name:str, passwd:str):
        """
        {'message': 'pod deleted successfully', 'code': 200}
        """
        uri = '/v1/pod/delete'
        json = {
            'pod_name': pod_name,
            'password': passwd,
        }
        response = self._http_request(url=self.basic_url+uri, json=json, headers=self.http_headers, request_type='delete')
        return response.json()
    
    def pod_ls(self):
        """
        {'pod_name': ['pod_test', 'pod_test_1'], 'shared_pod_name': []}
        """

        uri = '/v1/pod/ls'

        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers, request_type='get')
        return response.json()
    
    def pod_stat(self, pod_name:str):
        """ pod should be opened then can stat
        {'pod_name': 'pod_test_1', 'address': '2cd552ed3878c01834af6756eda697fc03aa0c51'}
        """
        
        uri = f"/v1/pod/stat?pod_name={pod_name}"
        # print(uri)
        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers, request_type='get')
        return response.json()

    def pod_present(self, pod_name):
        """
        Is Pod present
        """
        uri = '/v1/pod/present'
        json = {
            'pod_name': pod_name,
        }
        response = self._http_request(url=self.basic_url+uri, params=json ,headers=self.http_headers, request_type='get')
        return response.json()
    
    def dir_mkdir(self, pod_name,dir_path):
        """
        {'message': 'directory created successfully', 'code': 201}
        """
        uri = '/v1/dir/mkdir'

        data = {
            'pod_name': pod_name,
            'dir_path': dir_path
        }

        response = self._http_request(url=self.basic_url+uri,json=data, headers=self.http_headers, request_type='post')

        return response.json()
    
    def dir_remove(self,pod_name, dir_path):
        """
        remove a directory inside a pod
        """
        uri = '/v1/dir/rmdir'
        data = {
            'pod_name': pod_name,
            'dir_path': dir_path,
        }

        response = self._http_request(url=self.basic_url+uri,json=data, headers=self.http_headers, request_type='delete')

        return response.json()


    def dir_ls(self,pod_name,dir_path):
        
        uri = f'/v1/dir/ls?pod_name={pod_name}&dir_path={dir_path}'
        
        response = self._http_request(url=self.basic_url+uri,json={}, headers=self.http_headers, request_type='get')

        return response.json()
    
    def dir_stat(self, pod_name, dir_path):
        """
        Show a directory related information
        """

        uri = f'/v1/dir/stat?pod_name={pod_name}&dir_path={dir_path}'
    
        response = self._http_request(url=self.basic_url+uri,json={}, headers=self.http_headers, request_type='get')

        return response.json()
    
    def dir_present(self, pod_name, dir_path):
        """
        Is directory present
        """
        uri = f'/v1/dir/present?pod_name={pod_name}&dir_path={dir_path}'
    
        response = self._http_request(url=self.basic_url+uri,json={}, headers=self.http_headers, request_type='get')

        return response.json()


    def file_upload(self, pod_name, pod_dir, block_size, file_path):
        """
        upload a file to dfs

        file_list = ['file_name_1','file_name_2']
        {"username": ('username.txt', open('1.txt','r')), "password": (None, "abcd1234"),"location":('location.txt','福田区'),"picture":('1.jpg',open(r'C:\\Users\\1.jpg','rb'))}
        """
        uri = '/v1/file/upload'

        data = {
            'pod_name': pod_name,
            'dir_path': pod_dir,
            'block_size': block_size,
        }
        f = open(file_path, 'rb')
        # print(f"file_path {file_path} {f.read()}")
        files = {'files':open(file_path, 'rb')}
        # files = {'files': b'sdfsdfsdf'}
        headers = self.http_headers

        headers.update({'fairOS-dfs-Compression':'snappy'})
        del headers['Content-Type']

        response = self._http_request(url=self.basic_url+uri, headers=headers,params=data,files=files)

        return response.json()
    
    def file_download(self, pod_name, file_path):
        """
        Download a file from the pod tp the local dir
        """
        uri = '/v1/file/download'

        data = {
            'pod_name': pod_name,
            'file_path': file_path,
        }
 
        headers = self.http_headers

        response = self._http_request(url=self.basic_url+uri, headers=headers,params=data)

        return response.text
    
    def file_share(self,pod_name, pod_path_file, dest_user):
        """
        Share a file with another user
        """

        uri = '/v1/file/share'

        data = {
            'pod_name': pod_name,
            'pod_path_file': pod_path_file,
            'dest_user': dest_user,# eth address 
        }
 
        headers = self.http_headers

        response = self._http_request(url=self.basic_url+uri, headers=headers,params=data)

        return response.json()
    
    def file_receive(self, pod_name, sharing_ref, dir_path):
        """
        Receive file that was shared by another user
        """
        uri = '/v1/file/receive'

        data = {
            'pod_name': pod_name,
            'sharing_ref': sharing_ref,
            'dir_path': dir_path,# eth address 
        }

        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers,request_type='get',params=data)

        return response.json()
    
    def file_receive_info(self, pod_name, sharing_ref):
        """
        Receive file info that is being shared by another user
        """
        uri = '/v1/file/receiveinfo'

        data = {
            'pod_name': pod_name,
            'sharing_ref': sharing_ref,
        }

        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers,request_type='get',params=data)

        return response.json()

    def file_delete(self, pod_name, file_path):
        """
        Delete a file in the pod
        """
        uri = '/v1/file/delete'

        data = {
            'pod_name': pod_name,
            'file_path': file_path,
        }

        response = self._http_request(url=self.basic_url+uri, json=data,headers=self.http_headers,request_type='delete')

        return response.json()

    def file_stat(self, pod_name, file_path):
        """
        Get the information about a file in the pod
        """
        uri = '/v1/file/stat'

        data = {
            'pod_name': pod_name,
            'file_path': file_path,
        }

        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers,request_type='get', params=data)

        return response.json()
    
    def kv_new(self, pod_name, table_name, indexType):
        """
        Create a new key value table
        indexType: "string" | number
        """
        uri = '/v1/kv/new'

        data = {
            'pod_name': pod_name,
            'table_name': table_name,
            'indexType': indexType,
        }
        response = self._http_request(url=self.basic_url+uri, json=data, headers=self.http_headers)

        return response.json()
    
    def kv_list_tables(self, pod_name):
        """
        List all the Key Value tables of this pod
        """
        uri = '/v1/kv/ls'

        data = {
            'pod_name': pod_name
        }
        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers,request_type='get',params=data)

        return response.json()
    
    def kv_open_table(self, pod_name, table_name):
        """
        Opens a already created key value table
        """
        uri = '/v1/kv/open'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
        }
        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers, json=data)

        return response.json()
    
    def kv_count_table(self, pod_name, table_name):
        """
        Count KV pairs in a table
        """
        uri = '/v1/kv/count'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
        }
        response = self._http_request(url=self.basic_url+uri,json=data,headers=self.http_headers)

        return response.json()
    
    def kv_delete_table(self, pod_name, table_name):
        """
        Delete a KV table of a pod
        """
        uri = '/v1/kv/delete'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
        }
        response = self._http_request(url=self.basic_url+uri,json=data,headers=self.http_headers,request_type='delete')

        return response.json()
    
    def kv_put(self, pod_name, table_name, key, value):
        """
        Inserts a Key Value pair in the table
        """
        uri = '/v1/kv/entry/put'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
            'key': key,
            'value': value,
        }
        response = self._http_request(url=self.basic_url+uri,json=data,headers=self.http_headers)

        return response.json()
    
    def kv_get(self, pod_name, table_name,key):
        """
        Get value given a key
        """
        uri = '/v1/kv/entry/get'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
            'key': key,
        }
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers,request_type='get',params=data)

        return response.json()
    
    def kv_get_data(self, pod_name, table_name, key,format='string'):
        """
        format string or byte-string
        """
        uri = '/v1/kv/entry/get-data'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
            'key': key,
            'format': format
        }
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers,request_type='get',params=data)

        return response.json()

    def kv_delete(self, pod_name, table_name, key):
        """
        Delete a KV pair given a key
        """
        uri = '/v1/kv/entry/del'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
            'key': key,
        }
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers,json=data,request_type='delete')

        return response.json()
    
    def kv_seek_key(self, pod_name, table_name, start_prefix, end_prefix, limit=0):
        """
        Seek a KV pair given a key or its prefix
        """
        uri = '/v1/kv/seek'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
            'start_prefix': start_prefix,
            'end_prefix': end_prefix,
            'limit': limit,
        }
       
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers,json=data)

        return response.json()
    
    def kv_get_next(self, pod_name, table_name):
        uri = '/v1/kv/seek/next'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
        }
       
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers,request_type='get',params=data)

        return response.json()
    
    def kv_loadcsv(self, pod_name, table_name, memory=0):
        uri = '/v1/kv/loadcsv'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
        }

        if memory:
            data['memeory'] = memory
        headers = self.http_headers
        headers['Content-Type'] = 'multipart/form-data'
        response = self._http_request(url=self.basic_url+uri,headers=headers,params=data)

        return response.json()
    
    def kv_key_present(self, pod_name, table_name, key):
        uri = '/v1/kv/present'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
            'key': key,
        }
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers,params=data, request_type='get')

        return response.json()

    def doc_db_create(self, pod_name, table_name, si, mutable=True):
        """
        create a document DB with the given fields as indexes
        """
        uri = '/v1/doc/new'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
            'si': si,
            'mutable': mutable
        }

        response = self._http_request(url=self.basic_url+uri,json=data,headers=self.http_headers)

        return response.json()
    
    def doc_db_ls(self, pod_name):
        uri = '/v1/doc/ls'
        data = {
            'pod_name': pod_name,
        }

        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers, request_type='get',params=data)

        return response.json()
    
    def doc_db_open(self, pod_name, table_name):
        uri = '/v1/doc/open'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
        }

        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers, json=data,request_type='post')

        return response.json()
    
    def doc_count(self, pod_name, table_name, expr):
        uri = '/v1/doc/count'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
            'expr': expr,
        }
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers, json=data,request_type='post')

        return response.json()

    def doc_db_delete(self, pod_name, table_name):
        uri = '/v1/doc/delete'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
        }
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers, json=data,request_type='delete')

        return response.json()

    def doc_db_find(self, pod_name, table_name, expr, limit):
        uri = '/v1/doc/find'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
            'expr': expr,
            'limit': limit,
        }
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers, json=data,request_type='get')

        return response.json()
    
    def doc_db_load_json(self, pod_name, table_name):
        uri = '/v1/doc/loadjson'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
        }

        headers = self.http_headers

        # headers.update({'fairOS-dfs-Compression':'snappy'})
        headers['Content-Type'] = 'multipart/form-data'
        response = self._http_request(url=self.basic_url+uri,headers=headers, json=data)

        return response.json()
    
    def doc_db_index_json(self, pod_name, table_name, file):
        uri = '/v1/doc/indexjson'
        data  = {
            'pod_name': pod_name,
            'tabel_name': table_name,
            'file': file,
        }
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers, json=data)

        return response.json()
    
    def doc_insert(self, pod_name, table_name, doc):
        """
        Insert the document in the documentDB
        """
        uri = '/v1/doc/entry/put'
        data = {
            'pod_name': pod_name,
            'tabel_name': table_name,
            'doc': foc,
        }
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers, json=data)

        return response.json()
    
    def doc_get(self, pod_name, table_name, doc_id):
        """
        Get the document from the documentDB given the id
        """
        uri = '/v1/doc/entry/get'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
            'id': doc_id,
        }
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers, json=data, request_type='get')

        return response.json()
    
    def doc_del(self, pod_name, table_name, doc_id):
        """
        Get the document from the documentDB given the id
        """
        uri = '/v1/doc/entry/del'
        data = {
            'pod_name': pod_name,
            'table_name': table_name,
            'id': doc_id,
        }
        response = self._http_request(url=self.basic_url+uri,headers=self.http_headers, json=data, request_type='delete')

        return response.json()