
from abc import ABCMeta, abstractmethod

from .fair_os import FairOs


class FairBase(object):

    __metaclass__ = ABCMeta

    def __init__(self, user_name, passwd, pod_name, basic_url, time_out) -> None:

        assert user_name
        self.user_name = user_name

        assert passwd
        self.passwd = passwd

        assert pod_name
        self.pod_name = pod_name

        assert basic_url
        self.basic_url = basic_url if basic_url else 'http://localhost:9090'

        assert time_out
        self.time_out = time_out if time_out else 10

        self.fair_os = FairOs(basic_url=self.basic_url, time_out=self.time_out)
        
    def login(self):
        result = self.fair_os.user_login(user_name=self.user_name, passwd=self.passwd)
        if result['code'] != 200:
            raise Exception(f"user_login failed! {result}")
    
    def logout(self):
        result = self.fair_os.user_logout()
        if result['code'] != 200:
            raise Exception(f"user_logout failed! {result}")

    
    
    def open_pod(self):
        result = self.fair_os.pod_open(pod_name=self.pod_name, password=self.passwd)
        if result.get('code') != 200:
            raise Exception(f"open pod failed {result}")
    
    def close_pod(self):
        result = self.fair_os.pod_close(pod_name=self.pod_name)
        if result.get('code') != 200:
            raise Exception(f"close pod failed {result}")

    
    
    def change_pod(self, pod_name):
        
        self.fair_os.pod_close(self.pod_name)
        self.pod_name = pod_name
        self.open_pod(self.pod_name)