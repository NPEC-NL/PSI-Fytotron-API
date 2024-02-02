# fytotron.swagger_client.SetvarApi

All URIs are relative to *https://localhost:44339/fyo/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setvar**](SetvarApi.md#setvar) | **POST** /setvar | Set the setpoint value

# **setvar**
> setvar(name, value)

Set the setpoint value

### Example
```python
from __future__ import print_function
import time
import swagger_client
from fytotron.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fytotron.swagger_client.SetvarApi()
name = 'name_example' # str | variable name
value = 1.2 # float | value to se the variable to

try:
    # Set the setpoint value
    api_instance.setvar(name, value)
except ApiException as e:
    print("Exception when calling SetvarApi->setvar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| variable name | 
 **value** | **float**| value to se the variable to | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

