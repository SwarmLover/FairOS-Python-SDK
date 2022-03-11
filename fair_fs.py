from core.fair_os import FairOs
from core.base_obj import FairBase

class FairFS(FairBase):
     
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

    def mkdir(self, dir_path):
        
        return self.fair_os.dir_mkdir(pod_name=self.pod_name, dir_path=dir_path)

    def rm_dir(self, dir_path):

        return self.fair_os.dir_remove(pod_name=self.pod_name, dir_path=dir_path)

    def ls(self,dir_path):
        
        return self.fair_os.dir_ls(pod_name=self.pod_name, dir_path=dir_path)


