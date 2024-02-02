""""Dataclasses for all the replies """
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Variable:
    max: float
    min: float
    name: str
    unit: str
    value: float

    @staticmethod
    def from_dict(obj: Any) -> 'Variable':
        return Variable(
            max=obj.get("Max"),
            min=obj.get("Min"),
            name=obj.get("Name"),
            unit=obj.get("Unit"),
            value=obj.get("Value"),
        )


@dataclass
class VariableWrapper:
    """value wrapper """
    values: List[Variable]

    @staticmethod
    def from_dict(obj: Any) -> List[Variable]:
        return [Variable.from_dict(y) for y in obj]


@dataclass
class MonitorValues:
    caption: str
    message: str
    state: str

    @staticmethod
    def from_dict(obj: Any) -> 'MonitorValues':
        _caption = str(obj.get("Caption"))
        _message = str(obj.get("Message"))
        _state = str(obj.get("State"))
        return MonitorValues(_caption, _message, _state)


@dataclass
class MonitorValuesWrapper:
    """value wrapper """
    values: List[MonitorValues]

    @staticmethod
    def from_dict(obj: Any) -> List[MonitorValues]:
        return [MonitorValues.from_dict(y) for y in obj]
