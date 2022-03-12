# FairOS-Python-SDK
A simple, elegant Python SDK for FairOS, you can use it to interactive with [FairOS-API](https://docs.fairos.fairdatasociety.org/api/) simply


# Requirements
- Python 3.8+
- FairOS http service

# How to use

```
pip install fairos-py-sdk
```

# Demo 

```
>>> from fairospy.fair_kv import FairKV

>>> fkv = FairKV(user_name='dd',passwd='dd',pod_name='pod_test',basic_url='http://localhost:9090', time_out=60)

>>> fkv.ls_table()
 
{'Tables': [{'table_name': 'test_kv',
   'indexes': ['StringIndex'],
   'type': 'KV Store'}]}
```

# License

[MIT](/LICENSE)