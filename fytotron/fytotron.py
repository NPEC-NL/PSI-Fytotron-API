"""Fytotron API """
import fytotron.swagger_client as swagger_client
import fytotron.models as models


class Fytotron_API():
    """Wrapper around the automatically  generated swagger client.
       return class instances instead of dictionaries."""
    def __init__(self, server, poort):
        self.configuration = swagger_client.Configuration()
        self.configuration.host = f'{server}:{poort}/fyto/rest'
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
        api_response = self.api_instance.info()
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
        return self.api_instance.getvar(name)

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
        self.api_instance.setvar(name, value)

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
        api_response = self.api_instance.monitor()
        return models.MonitorValuesWrapper.from_dict(api_response)
