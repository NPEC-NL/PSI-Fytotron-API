# MonitorValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.monitor_values import MonitorValues

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorValues from a JSON string
monitor_values_instance = MonitorValues.from_json(json)
# print the JSON string representation of the object
print(MonitorValues.to_json())

# convert the object into a dict
monitor_values_dict = monitor_values_instance.to_dict()
# create an instance of MonitorValues from a dict
monitor_values_from_dict = MonitorValues.from_dict(monitor_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


