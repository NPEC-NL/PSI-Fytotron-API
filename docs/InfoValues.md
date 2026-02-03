# InfoValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from fytotron.models.info_values import InfoValues

# TODO update the JSON string below
json = "{}"
# create an instance of InfoValues from a JSON string
info_values_instance = InfoValues.from_json(json)
# print the JSON string representation of the object
print(InfoValues.to_json())

# convert the object into a dict
info_values_dict = info_values_instance.to_dict()
# create an instance of InfoValues from a dict
info_values_from_dict = InfoValues.from_dict(info_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


