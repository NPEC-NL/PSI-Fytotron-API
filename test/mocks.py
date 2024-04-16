"""Example replies from the calls """
from unittest.mock import MagicMock


class ConfigMock(MagicMock):
    host: str = ""

class ApiClientMock():
    def __init__(self):
        self.info = MagicMock(return_value=MOCK_RETURN_INFO)
        self.getvar = MagicMock(return_value=MOCK_RETURN_GETVAR)
        self.setvar = MagicMock()
        self.monitor = MagicMock(return_value=MOCK_RETURN_MONITOR)


MOCK_RETURN_INFO = [
    {
        "Max": 85.0,
        "Min": 40,
        "Name": "RH_Set",
        "Unit": "%",
        "Value": 70
    },
    {
        "Max": 42.0,
        "Min": 4,
        "Name": "T_Set",
        "Unit": "C",
        "Value": 22
    },
    {
        "Max": 3000,
        "Min": 350,
        "Name": "CO2_Set",
        "Unit": "ppm",
        "Value": 400
    },
    {
        "Max": 3276.7,
        "Min": -3276.8,
        "Name": "T_Actual",
        "Unit": "C",
        "Value": 22.4
    },
    {
        "Max": 32767,
        "Min": -32768,
        "Name": "RH_Actual",
        "Unit": "%",
        "Value": 69
    },
    {
        "Max": 32767,
        "Min": -32768,
        "Name": "CO2_Actual",
        "Unit": "ppm",
        "Value": 450
    }
]

MOCK_RETURN_GETVAR = 22
MOCK_RETURN_MONITOR = [
    {
        "Caption": "PLC Comunication",
        "Message": "",
        "State": "ok"
    },
    {
        "Caption": "FC Comunication",
        "Message": "",
        "State": "ok"
    },
    {
        "Caption": "FC Hardware",
        "Message": "",
        "State": "ok"
    },
    {
        "Caption": "Power lost",
        "Message": "",
        "State": "ok"
    },
    {
        "Caption": "Power restored",
        "Message": "",
        "State": "ok"
    },
    {
        "Caption": "CO2 reg. overlimit",
        "Message": "CO2 out of range, overlimit",
        "State": "error"
    },
    {
        "Caption": "CO2 reg. underlimit",
        "Message": "",
        "State": "ok"
    }
]
