from cmath import exp
from core.fair_os import FairOs
from core.base_obj import FairBase

class FairDocDB(FairBase):

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

    def create(self, table_name, si, mutable=True):
        return self.fair_os.doc_db_create(pod_name=self.pod_name, table_name=table_name, si=si, mutable=mutable)
    
    def ls_doc_db(self):
        return self.fair_os.doc_db_ls(pod_name=self.pod_name)

    def open_doc_db(self, table_name):
        return self.fair_os.doc_db_open(pod_name=self.pod_name, table_name=table_name)
    
    def count(self, table_name, expr):
        return self.fair_os.doc_count(pod_name=self.pod_name, table_name=table_name, expr=expr)

    def delete_doc_db(self, table_name):
        return self.fair_os.doc_db_delete(pod_name=self.pod_name, table_name=table_name)
    
    def find(self, table_name, expr, limit):
        return self.fair_os.doc_db_find(pod_name=self.pod_name, table_name=table_name, expr=expr, limit=limit)