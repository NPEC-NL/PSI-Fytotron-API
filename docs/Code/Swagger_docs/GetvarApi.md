# fytotron.swagger_client.GetvarApi

All URIs are relative to *https://localhost:44339/fyo/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getvar**](GetvarApi.md#getvar) | **GET** /getvar | Returns the current value of the variable

# **getvar**
> JsonGetvarResult getvar(name)

Returns the current value of the variable

### Example
```python
from __future__ import print_function
import time
import swagger_client
from fytotron.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fytotron.swagger_client.GetvarApi()
name = 'name_example' # str | variable name

try:
    # Returns the current value of the variable
    api_response = api_instance.getvar(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetvarApi->getvar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| variable name | 

### Return type

[**JsonGetvarResult**](JsonGetvarResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

