# fytotron.swagger_client.InfoApi

All URIs are relative to *https://localhost:44339/fyo/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info**](InfoApi.md#info) | **GET** /info | Returns all setpoints and actual values in the database.

# **info**
> JsonInfoResult info()

Returns all setpoints and actual values in the database.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from fytotron.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fytotron.swagger_client.InfoApi()

try:
    # Returns all setpoints and actual values in the database.
    api_response = api_instance.info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonInfoResult**](JsonInfoResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

