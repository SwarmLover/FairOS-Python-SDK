#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        response = self._http_request(url=self.basic_url+uri, json=json ,headers=self.http_headers, request_type='get')
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