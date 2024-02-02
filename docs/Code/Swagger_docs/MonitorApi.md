# fytotron.swagger_client.MonitorApi

All URIs are relative to *https://localhost:44339/fyo/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**monitor**](MonitorApi.md#monitor) | **GET** /monitor | Returns the current status of the fytotron

# **monitor**
> JsonMonitorResult monitor()

Returns the current status of the fytotron

### Example
```python
from __future__ import print_function
import time
import swagger_client
from fytotron.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fytotron.swagger_client.MonitorApi()

try:
    # Returns the current status of the fytotron
    api_response = api_instance.monitor()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonMonitorResult**](JsonMonitorResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

