import requests


class Units:
    # Default request parameters
    user_id = "matheusjulidori"
    api_key = "fcOygYhtbRMahLrjF6sdyzKLEZR5qA7THbNRXYMmBxYawXJZ"
    url = "https://neutrinoapi.net/convert"
    request_header = {
        "User-ID": user_id,
        "API-Key": api_key
    }

    @staticmethod
    def temperature_units():
        """
        Obtains the list of allowed temperature units.

        Returns:
            list: List of allowed temperature units.
        """
        return ["C", "F", "K"]
    
    @staticmethod
    def weight_units():
        """
        Obtains the list of allowed weight units.

        Returns:
            list: List of allowed weight units.
        """
        return ["kg", "g", "mg", "lb", "oz"]
    
    @staticmethod
    def distance_units():
        """
        Obtains the list of allowed distance units.

        Returns:
            list: List of allowed distance units.
        """
        return ["km", "m", "cm", "mm", "mi", "yd", "ft", "in"]

    @staticmethod
    def weight(unidade_origem, unidade_destino, valor):
        """
        Converts weight units.

        Args:
            unidade_origem (str): Source currency code.
            unidade_destino (str): Destination currency code.
            valor (str): Value to be converted.

        Returns:
            float: Exchange rate from source to destination currency.
        """

        # Allowed weight units

        allowed_units = ["kg", "g", "mg", "lb", "oz"]
        units_map = {
            "g": "Gram",
            "lb": "Pound",
            "oz": "Ounce"
        }

        if unidade_origem not in allowed_units or unidade_destino not in allowed_units:
            return None

        # If unit is kg, g or mg converto to gram before, API only accepts gram
        valor = float(valor)
        altered_unit = ""
        if unidade_origem == "kg":
            unidade_origem = "g"
            altered_unit = "kg"
            valor = valor * 1000
        elif unidade_origem == "mg":
            unidade_origem = "g"
            altered_unit = "mg"
            valor = valor / 1000

        if unidade_origem == unidade_destino:
            return 1

        # Tries to convert the units using the API

        response = requests.post(Units.url, data={
            "from-value": valor,
            "from-type": units_map[unidade_origem],
            "to-type": units_map[unidade_destino]
        }, headers=Units.request_header)

        if response.status_code == 200:
            if altered_unit == 'kg':
                return float(response.json()["result-float"]) / 1000
            elif altered_unit == 'mg':
                return float(response.json()["result-float"]) * 1000
            else:
                return float(response.json()["result-float"])
        else:
            return None

    @staticmethod
    def temperature(unidade_origem, unidade_destino, valor):
        """
        Converts temperature units.

        Args:
            unidade_origem (str): Source currency code.
            unidade_destino (str): Destination currency code.
            valor (str): Value to be converted.

        Returns:
            float: Exchange rate from source to destination currency.
        """

        # Allowed temperature units

        allowed_units = ["C", "F", "K"]
        units_map = {
            "C": "Celsius",
            "F": "Fahrenheit",
        }

        if unidade_origem not in allowed_units or unidade_destino not in allowed_units:
            return None

        # If unit is Kelvin, converto to Celsius before, API only accepts Celsius
        valor = float(valor)
        altered_unit = ""
        if unidade_origem == "K":
            unidade_origem = "C"
            altered_unit = "K"
            valor = valor - 273.15

        # Tries to convert the units using the API

        response = requests.post(Units.url, data={
            "from-value": valor,
            "from-type": units_map[unidade_origem],
            "to-type": units_map[unidade_destino]
        }, headers=Units.request_header)

        if response.status_code == 200:
            if altered_unit == 'K':
                return float(response.json()["result-float"]) + 273.15
            else:
                return float(response.json()["result-float"])
        else:
            return None

    @staticmethod
    def distance(unidade_origem, unidade_destino, valor):
        """
        Converts distance units.

        Args:
            unidade_origem (str): Source currency code.
            unidade_destino (str): Destination currency code.
            valor (str): Value to be converted.

        Returns:
            float: Exchange rate from source to destination currency.
        """

        # Allowed distance units

        allowed_units = ["km", "m", "cm", "mm", "mi", "yd", "ft", "in"]
        units_map = {
            "m": "Meter",
            "mi": "Mile",
            "yd": "Yard",
            "ft": "Feet",
            "in": "Inch"
        }

        if unidade_origem not in allowed_units or unidade_destino not in allowed_units:
            return None

        # If unit is km, cm or mm converto to meter before, API only accepts meter
        valor = float(valor)
        altered_unit = ""
        if unidade_origem == "km":
            unidade_origem = "m"
            altered_unit = "km"
            valor = valor * 1000
        elif unidade_origem == "cm":
            unidade_origem = "m"
            altered_unit = "cm"
            valor = valor / 100
        elif unidade_origem == "mm":
            unidade_origem = "m"
            altered_unit = "mm"
            valor = valor / 1000

        if unidade_origem == unidade_destino:
            return 1

        # Tries to convert the units using the API

        response = requests.post(Units.url, data={
            "from-value": valor,
            "from-type": units_map[unidade_origem],
            "to-type": units_map[unidade_destino]
        }, headers=Units.request_header)

        if response.status_code == 200:
            if altered_unit == 'km':
                return float(response.json()["result-float"]) / 1000
            elif altered_unit == 'cm':
                return float(response.json()["result-float"]) * 100
            elif altered_unit == 'mm':
                return float(response.json()["result-float"]) * 1000
            else:
                return float(response.json()["result-float"])
        else:
            return None
