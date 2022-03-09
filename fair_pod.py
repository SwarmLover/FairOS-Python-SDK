from logging import raiseExceptions
from fair_os import FairOs

class FairPod(object):

    def __init__(self, user_name, passwd) -> None:
        self.fair_os = FairOs()
        self.user_name = user_name
        self.passwd = passwd

        result = self.fair_os.user_login(user_name=user_name, passwd=passwd)
        if result['code'] != 200:
            raiseExceptions(f"user_login failed! {result}")
        
    
    def __del__(self):
        self.fair_os.user_logout()

    
    def create_pod(self, pod_name:str):

        result = self.fair_os.pod_new(pod_name=pod_name, password=self.passwd)

        return result

    def open_pod(self, pod_name:str):

        result = self.fair_os.pod_open(pod_name=pod_name, password=self.passwd)

        return result
    
    def ls_pod(self):

        return self.fair_os.pod_ls()

    def stat_pod(self, pod_name:str):

        return self.fair_os.pod_stat(pod_name=pod_name)