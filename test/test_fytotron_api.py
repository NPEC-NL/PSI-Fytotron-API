"""Fytotron API tests"""
import unittest
from unittest.mock import patch, MagicMock

import mocks
# Add the parent folder to the path
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from fytotron import fytotron


@patch('fytotron.fytotron.swagger_client.FytotronApi', return_value=mocks.ApiClientMock())
class MyTestCase(unittest.TestCase):

    def test_init(self, api_mock):
        """Test the class instantiation"""
        with patch('fytotron.fytotron.swagger_client.Configuration', return_value=MagicMock()) as mock_context:
            with patch('fytotron.fytotron.swagger_client.ApiClient', return_value=mocks.ApiClientMock()):
                api = fytotron.Fytotron_API('test', '33')
            mock_context.assert_called_once()
            self.assertEqual(mock_context.return_value.host, 'test:33/fyto/rest')

    def test_get_all_values(self, api_mock):
        api = fytotron.Fytotron_API('test', '33')
        reply = api.get_all_values()

        self.assertEqual(len(reply), len(mocks.MOCK_RETURN_INFO))
        self.assertEqual(reply[0].max, mocks.MOCK_RETURN_INFO[0]['Max'])
        self.assertEqual(reply[0].min, mocks.MOCK_RETURN_INFO[0]['Min'])
        self.assertEqual(reply[0].name, mocks.MOCK_RETURN_INFO[0]['Name'])
        self.assertEqual(reply[0].unit, mocks.MOCK_RETURN_INFO[0]['Unit'])
        self.assertEqual(reply[0].value, mocks.MOCK_RETURN_INFO[0]['Value'])

    def test_get_current_value(self, api_mock):
        api = fytotron.Fytotron_API('test', '33')
        reply = api.get_current_value('test')

        api.api_instance.getvar.assert_called_once()
        self.assertEqual(api.api_instance.getvar.call_args[0][0], 'test')
        self.assertEqual(reply, mocks.MOCK_RETURN_GETVAR)

    def test_set_setpoint(self, api_mock):
        api = fytotron.Fytotron_API('test', '33')
        api.set_setpoint('test', 33)

        api.api_instance.setvar.assert_called_once()
        var, value = api.api_instance.setvar.call_args[0]
        self.assertEqual(var, 'test')
        self.assertEqual(value, 33)

    def test_get_monitor_values(self, api_mock):
        api = fytotron.Fytotron_API('test', '33')
        reply = api.get_monitor_values()

        api.api_instance.monitor.assert_called_once()
        self.assertEqual(len(reply), len(mocks.MOCK_RETURN_MONITOR))
        self.assertEqual(reply[0].caption, mocks.MOCK_RETURN_MONITOR[0]['Caption'])
        self.assertEqual(reply[0].message, mocks.MOCK_RETURN_MONITOR[0]['Message'])
        self.assertEqual(reply[0].state, mocks.MOCK_RETURN_MONITOR[0]['State'])


if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = MyTestCase()
    test_case.test_init()
    test_case.test_get_all_values()
    test_case.test_get_current_value()
    test_case.test_set_setpoint()
    test_case.test_get_monitor_values()
