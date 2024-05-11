import requests

class Currency:
    @staticmethod
    def codes():
        """
        Obtains currency codes.
        
        Returns:
            list: List of currency codes.
        """
        # These are some common currency codes.
        return ["USD", "BRL", "EUR", "JPY", "CHF", "BTC", "ETH"]
    
    @staticmethod
    def emojis():
        """
        Obtains currency emojis.
        
        Returns:
            dict: Dictionary of currency emojis.
        """
        return {
            "USD": ":dollar:",    # Dólar
            "BRL": ":flag_br:",   # Real Brasileiro
            "EUR": ":euro:",      # Euro
            "JPY": ":yen:",       # Iene Japonês
            "CHF": ":flag_ch:",             # Franco Suíço
            "BTC": ":coin:",                # Bitcoin
            "ETH": ":small_blue_diamond:"   # Ethereum
        }

        
        
    @staticmethod
    def currency(moeda_origem, moeda_destino):
        """
        Retrieves currency exchange rate.
        
        Args:
            moeda_origem (str): Source currency code.
            moeda_destino (str): Destination currency code.
        
        Returns:
            float: Exchange rate from source to destination currency.
        """
        # Endpoint URL
        url = "https://economia.awesomeapi.com.br/last/{}-{}"

        # Making the GET request
        response = requests.get(url.format(moeda_origem, moeda_destino))

        # Checking if the request was successful
        if response.status_code == 200:
            return float(response.json()[f"{moeda_origem}{moeda_destino}"]["bid"])
        
        elif moeda_origem == "USD" or moeda_destino == "USD":
            aux = moeda_destino
            moeda_destino = moeda_origem
            moeda_origem = aux

            return 1/float(requests.get(url.format(moeda_origem, moeda_destino)).json()[f"{moeda_origem}USD"]["bid"])

        elif response.status_code == 404:
            # If the specific exchange rate is not found, we try to calculate using USD as intermediate currency.
            
            # Exchange rate from source to USD
            source_to_usd = float(requests.get(url.format(moeda_origem, "USD")).json()[f"{moeda_origem}USD"]["bid"])

            # Exchange rate from USD to destination
            usd_to_destiny = float(requests.get(url.format("USD", moeda_destino)).json()[f"USD{moeda_destino}"]["bid"])

            # Conversion
            return source_to_usd * usd_to_destiny
        else:
            # If the request fails, print the status code
            print("Failed to retrieve exchange rate. Status code:", response.status_code)
            return None
