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

        if moeda_origem == moeda_destino:
            return 1

        # --- Try to get data from API

        url = "https://economia.awesomeapi.com.br/last/{}-{}"

        formatted_url = url.format(moeda_origem, moeda_destino)

        response = requests.get(formatted_url)

        if response.status_code == 200:
            return float(response.json()["{}{}".format(moeda_origem, moeda_destino)]["bid"])

        # --- Try to get reverse data from API
        
        formatted_url = url.format(moeda_destino, moeda_origem)

        response = requests.get(formatted_url)

        if response.status_code == 200:
            return 1 / float(response.json()["{}{}".format(moeda_destino, moeda_origem)]["bid"])

        # --- Try to get it through USD

        try:
            origin_usd = Currency.currency(moeda_origem, "USD")
            dest_usd = Currency.currency("USD", moeda_destino)

            return origin_usd * dest_usd
        except:
            return None