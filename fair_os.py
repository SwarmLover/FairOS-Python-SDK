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
        kwargs.setdefault('json', json)
        kwargs.setdefault('headers', headers)

        response = requests.request(*args, **kwargs)
        # print(response.status_code)
        # print(response.url)
        # print(response.text)
        # print((response.cookies))
        # print(dict(response.raw.headers))
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
    
    def user_is_loggined(self, user_name:str):
        
        uri = f'/v1/user/isloggedin?user_name={user_name}'

        response = self._http_request(url=self.basic_url+uri, headers=self.http_headers, request_type='get')
        return response.json()

    def user_import(self):
        pass



    
    def pod_new(self, pod_name, password):
        uri = '/v1/pod/new'
        json = {
            'pod_name': pod_name,
            'password': password,
        }
        response = self._http_request(url=self.basic_url+uri, json=json, headers=self.http_headers)
        return response.json()

    def dir_ls(self, dir_path):
        uri = '/v1/dir/ls'

        data = {
            'dir': (None,dir_path)
        }
        
        headers = {
            'Cookie': self.login_cookie,
            'Content-Type':'multipart/form-data',
        }
        response = self._http_request(url=self.basic_url+uri,json=data, headers=headers, request_type='get')

        return response.json()