# FairOS-Python-SDK
A simple, elegant Python SDK for FairOS, you can easily use it to interactive with [FairOS-API](https://docs.fairos.fairdatasociety.org/api/)


# Requirements
- Python 3.8+
- [FairOS http service](https://docs.fairos.fairdatasociety.org/docs/)

# How to install

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

# API Doc

- [3 Main Classes](/docs/api_doc.md)

# Contributor

- [jusonalien](https://github.com/jusonalien)

# License

[MIT](/LICENSE)