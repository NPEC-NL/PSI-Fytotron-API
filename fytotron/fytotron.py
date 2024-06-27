"""Fytotron API """
import fytotron.swagger_client as swagger_client
import fytotron.models as models

REQUEST_TIMEOUT = 60

class Fytotron_API():
    """Wrapper around the automatically  generated swagger client.
       return class instances instead of dictionaries."""
    def __init__(self, server: str, poort: int, token: str = ''):
        """
        Parameters
        ----------
            server: str
                URL of the server
            poort: int
                poortnumber of the Fytotron server
            token: str
                Token to authenticate with the server
        Return
        ----------
            -
        """
        self.configuration = swagger_client.Configuration()
        self.configuration.host = f'{server}:{poort}/fyto/rest'
        if token != '':
            self.configuration.api_key['X-Auth-Token'] = token
        self.api_instance = swagger_client.FytotronApi(
            swagger_client.ApiClient(self.configuration))

    def get_all_values(self) -> models.VariableWrapper:
        """
        Parameters
        ----------
            -
        Return
        ----------
            VariableWrapper
                List of variables
        """
        api_response = self.api_instance.info(_request_timeout=REQUEST_TIMEOUT)
        return models.VariableWrapper.from_dict(api_response)

    def get_current_value(self, name: str) -> int:
        """
        Get the current value of a variable
        Parameters
        ----------
            name: str
                Name of the parameter to get the value
        Return
        ----------
            int
                This endpoints returns an integer, not a json
        """
        return self.api_instance.getvar(name, _request_timeout=REQUEST_TIMEOUT)

    def set_setpoint(self, name, value) -> None:
        """
        Get the current value of a variable
        Parameters
        ----------
            name: str
                Name of the parameter to get the value
        Return
        ----------
            -
        """
        self.api_instance.setvar(name, value, _request_timeout=REQUEST_TIMEOUT)

    def get_monitor_values(self) -> models.MonitorValuesWrapper:
        """
        Get the current status of all the monitored variables
        Parameters
        ----------
            -
        Return
        ----------
            MonitorValuesWrapper
                list of monitoring values

        """
        api_response = self.api_instance.monitor(_request_timeout=REQUEST_TIMEOUT)
        return models.MonitorValuesWrapper.from_dict(api_response)
