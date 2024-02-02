# fytotron.swagger_client.FytotronApi

All URIs are relative to *https://localhost:44339/fyo/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getvar**](FytotronApi.md#getvar) | **GET** /getvar | Returns the current value of the variable
[**info**](FytotronApi.md#info) | **GET** /info | Returns all setpoints and actual values in the database.
[**monitor**](FytotronApi.md#monitor) | **GET** /monitor | Returns the current status of the fytotron
[**setvar**](FytotronApi.md#setvar) | **POST** /setvar | Set the setpoint value

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
api_instance = fytotron.swagger_client.FytotronApi()
name = 'name_example' # str | variable name

try:
    # Returns the current value of the variable
    api_response = api_instance.getvar(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FytotronApi->getvar: %s\n" % e)
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
api_instance = fytotron.swagger_client.FytotronApi()

try:
    # Returns all setpoints and actual values in the database.
    api_response = api_instance.info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FytotronApi->info: %s\n" % e)
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
api_instance = fytotron.swagger_client.FytotronApi()

try:
    # Returns the current status of the fytotron
    api_response = api_instance.monitor()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FytotronApi->monitor: %s\n" % e)
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
api_instance = fytotron.swagger_client.FytotronApi()
name = 'name_example' # str | variable name
value = 1.2 # float | value to se the variable to

try:
    # Set the setpoint value
    api_instance.setvar(name, value)
except ApiException as e:
    print("Exception when calling FytotronApi->setvar: %s\n" % e)
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

