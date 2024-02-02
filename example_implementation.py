"""Example implementation"""
from os import getenv
from dotenv import load_dotenv

from fytotron.fytotron import Fytotron_API


if __name__ == "__main__":
    load_dotenv()
    # Create an instance of the API class
    api = Fytotron_API(getenv('URL'), getenv('PORT'))

    # Retreive all values
    variable_list = api.get_all_values()

    for var in variable_list:
        print(f"{var.name} max: {var.max}{var.unit}, \
                           min: {var.min}{var.unit}, \
                           value: {var.value}{var.unit}")

    # Retreive current value
    variable = 'T_Set'
    current_value = api.get_current_value(variable)
    print(f"{variable}, value: {current_value}")

    # Set setpoint, commented to prevent accidental execution
    # api.set_setpoint('T_Set', 25)

    # Retreive monitoring values
    monitor_values = api.get_monitor_values()
    for var in monitor_values:
        print(f"{var.caption}: {var.state}, {var.message} ")
