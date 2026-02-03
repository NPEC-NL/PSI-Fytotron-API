"""Example implementation"""
from os import getenv
from dotenv import load_dotenv

import fytotron


if __name__ == "__main__":
    load_dotenv()
    # Create an instance of the API class
    api = fytotron.FytotronApi(
        fytotron.ApiClient(
            fytotron.Configuration(
                host=getenv('URL'),
                api_key={'ApiKeyAuth': getenv('TOKEN')}
            )
        )
    )

    # Retreive all values
    variable_list = api.info()
    for var in variable_list:
        print(f"{var.name} max: {var.max}{var.unit}, \
                           min: {var.min}{var.unit}, \
                           value: {var.value}{var.unit}")

    # Retreive current value
    variable = 'T_Set'
    current_value = api.getvar(variable)
    print(f"{variable}, value: {current_value}")

    # Set setpoint, commented to prevent accidental execution
    # api.setvar('T_Set', 25)

    # Retreive monitoring values
    monitor_values = api.monitor()
    for var in monitor_values:
        print(f"{var.caption}: {var.state}, {var.message} ")
