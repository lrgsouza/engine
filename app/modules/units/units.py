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
        
        if unidade_origem == unidade_destino:
            return 1
        
        # If unit is kg, g or mg converto to gram before, API only accepts gram
        valor = float(valor)
        altered_origin_unit = ""
        if unidade_origem == "kg":
            unidade_origem = "g"
            altered_origin_unit = "kg"
            valor = valor * 1000
        elif unidade_origem == "mg":
            unidade_origem = "g"
            altered_origin_unit = "mg"
            valor = valor / 1000

        #If destiny unit is kg, g or mg, results needs to be reconvert from gram
        altered_destiny_unit = ""
        if unidade_destino == "kg":
            unidade_destino = "g"
            altered_destiny_unit = "kg"
        elif unidade_destino == "mg":
            unidade_destino = "g"
            altered_destiny_unit = "mg"

        # Tries to convert the units using the API

        response = requests.post(Units.url, data={
            "from-value": valor,
            "from-type": units_map[unidade_origem],
            "to-type": units_map[unidade_destino]
        }, headers=Units.request_header)

        if response.status_code == 200:
            result = float(response.json()["result-float"])

            #Check altered units to reconvert the result

            if altered_destiny_unit == "kg":
                result = result / 1000
            elif altered_destiny_unit == "mg":
                result = result * 1000
        
            return result
        
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
        
        if unidade_origem == unidade_destino:
            return 1

        # If unit is Kelvin, converto to Celsius before, API only accepts Celsius
        valor = float(valor)
        altered_origin_unit = ""
        if unidade_origem == "K":
            unidade_origem = "C"
            altered_origin_unit = "K"
            valor = valor - 273.15

        #If destiny unit is Kelvin, results needs to be reconvert from Celsius to Kelvin
        altered_destiny_unit = ""
        if unidade_destino == "K":
            unidade_destino = "C"
            altered_destiny_unit = "K"



        # Tries to convert the units using the API

        response = requests.post(Units.url, data={
            "from-value": valor,
            "from-type": units_map[unidade_origem],
            "to-type": units_map[unidade_destino]
        }, headers=Units.request_header)

        if response.status_code == 200:
            result = float(response.json()["result-float"])

            #Check altered units to reconvert the result

            if altered_destiny_unit == "K":
                result = result + 273.15
            
            return result

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
        
        if unidade_origem == unidade_destino:
            return 1

        # If origin unit is km, cm or mm convert to to meter before, API only accepts meter
        valor = float(valor)
        altered_origin_unit = ""

        if unidade_origem == "km":
            unidade_origem = "m"
            altered_origin_unit = "km"
            valor = valor * 1000
        elif unidade_origem == "cm":
            unidade_origem = "m"
            altered_origin_unit = "cm"
            valor = valor / 100
        elif unidade_origem == "mm":
            unidade_origem = "m"
            altered_origin_unit = "mm"
            valor = valor / 1000

        #if destiny unit is km cm or mm, convert back from meter, API returns meter
        altered_destiny_unit = ""
        if unidade_destino == "km":
            unidade_destino = "m"
            altered_destiny_unit = "km"
        elif unidade_destino == "cm":
            unidade_destino = "m"
            altered_destiny_unit = "cm"
        elif unidade_destino == "mm":
            unidade_destino = "m"
            altered_destiny_unit = "mm"



        # Tries to convert the units using the API

        response = requests.post(Units.url, data={
            "from-value": valor,
            "from-type": units_map[unidade_origem],
            "to-type": units_map[unidade_destino]
        }, headers=Units.request_header)

        if response.status_code == 200:
            result = response.json()["result-float"]

            #Check altered units to reconvert the result
            
            if altered_destiny_unit == "km":
                result = result / 1000
            elif altered_destiny_unit == "cm":
                result = result * 100
            elif altered_destiny_unit == "mm":
                result = result * 1000

            return result
        else:
            return None

