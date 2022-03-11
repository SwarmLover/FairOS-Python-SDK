from .fair_os import FairOs

class FairPod(object):

    def __init__(self, user_name, 
        passwd,
        basic_url='http://localhost:9090', 
        time_out=20) -> None:
        
        self.fair_os = FairOs()
        self.user_name = user_name
        self.passwd = passwd

        result = self.fair_os.user_login(user_name=user_name, passwd=passwd)
        if result['code'] != 200:
            raise Exception(f"user_login failed! {result}")
        
    
    def __del__(self):
        self.fair_os.user_logout()

    
    def create_pod(self, pod_name:str):

        result = self.fair_os.pod_new(pod_name=pod_name, password=self.passwd)

        return result

    def open_pod(self, pod_name:str):

        result = self.fair_os.pod_open(pod_name=pod_name, password=self.passwd)

        return result
    
    
    def sync_pod(self, pod_name:str):
        
        return self.fair_os.pod_sync(pod_name)
    
    def close_pod(self, pod_name:str):

        return self.fair_os.pod_close(pod_name)
    
    def delete_pod(self, pod_name:str):

        return self.fair_os.pod_delete(pod_name=pod_name, passwd=self.passwd)
    
    def ls_pod(self):
    
        return self.fair_os.pod_ls()

    def stat_pod(self, pod_name:str):

        return self.fair_os.pod_stat(pod_name=pod_name)