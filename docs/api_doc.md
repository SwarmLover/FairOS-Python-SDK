### API Document

In this sdk, we support 3 main classes, FairFS,FairKV,FairDocDB, below is the sdk demo

### FairFS

```
from fairospy.fair_fs import FairFS
ffs = FairFS(user_name='dd',passwd='dd',pod_name='pod_test_1', time_out=60)
print(ffs.ls('/data'))
print(ffs.mkdir('/data_test'))
print(ffs.rm_dir('/data_test'))
```

### FairKV

```
from fairospy.fair_kv import FairKV
pod_name = 'pod_test'
table_name = 'kv_table_test2333'
fkv = FairKV(user_name='dd',passwd='dd',pod_name=pod_name, time_out=60)
print(fkv.new_table(table_name=table_name,index_type='number'))
print(fkv.open_table(table_name=table_name))
print(fkv.ls_table())
print(fkv.del_table(table_name=table_name))
print(fkv.put(table_name=table_name, key='key1',value='value1'))
print(fkv.get(table_name=table_name, key='key1'))
print(fkv.get_data(table_name=table_name, key='key1',format='string'))
print(f"seek_key {fkv.seek_key(table_name=table_name, start_prefix=0,end_prefix=1,limit=1)}")
print(f"get_next {fkv.get_next(table_name=table_name)}")
print(f"loadcsv {fkv.loadcsv(table_name=table_name)}")
print(fkv.key_present(table_name=table_name, key='key1'))
print(fkv.del_val(table_name=table_name, key='key1'))
print(fkv.count_table(table_name=table_name))
print(fkv.get_data(table_name='kv_test_table_numbe_1', key='key1',format='string'))
print(fkv.del_table(table_name=table_name))
```

### FairDocDB

```
from fairospy.fair_doc_db import FairDocDB
pod_name = 'pod_test'
doc_db_name = 'doc_db_test2333'
fddb = FairDocDB(user_name='dd', passwd='dd', pod_name=pod_name, time_out=20)
print(fddb.create(table_name=doc_db_name, si="first_name=string,age=number,tags=map", mutable=True))
print(fddb.ls_doc_db())
print(fddb.open_doc_db(table_name=doc_db_name))
print(fddb.delete_doc_db(table_name=doc_db_name))
print(fddb.ls_doc_db())
```

