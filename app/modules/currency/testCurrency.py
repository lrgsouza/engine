import unittest
from modules.currency.currency import Currency

from unittest_parametrize import parametrize
from unittest_parametrize import ParametrizedTestCase


class TestCurrency(ParametrizedTestCase):
    @parametrize(
        "origin, dest",
        [
            ("USD", "USD"),
            ("USD", "BRL"),
            ("USD", "EUR"),
            ("USD", "JPY"),
            ("USD", "CHF"),
            ("USD", "BTC"),
            ("USD", "ETH"),
            ("BRL", "USD"),
            ("BRL", "BRL"),
            ("BRL", "EUR"),
            ("BRL", "JPY"),
            ("BRL", "CHF"),
            ("BRL", "BTC"),
            ("BRL", "ETH"),
            ("EUR", "USD"),
            ("EUR", "BRL"),
            ("EUR", "EUR"),
            ("EUR", "JPY"),
            ("EUR", "CHF"),
            ("EUR", "BTC"),
            ("EUR", "ETH"),
            ("JPY", "USD"),
            ("JPY", "BRL"),
            ("JPY", "EUR"),
            ("JPY", "JPY"),
            ("JPY", "CHF"),
            ("JPY", "BTC"),
            ("JPY", "ETH"),
            ("CHF", "USD"),
            ("CHF", "BRL"),
            ("CHF", "EUR"),
            ("CHF", "JPY"),
            ("CHF", "CHF"),
            ("CHF", "BTC"),
            ("CHF", "ETH"),
            ("BTC", "USD"),
            ("BTC", "BRL"),
            ("BTC", "EUR"),
            ("BTC", "JPY"),
            ("BTC", "CHF"),
            ("BTC", "BTC"),
            ("BTC", "ETH"),
            ("ETH", "USD"),
            ("ETH", "BRL"),
            ("ETH", "EUR"),
            ("ETH", "JPY"),
            ("ETH", "CHF"),
            ("ETH", "BTC"),
            ("ETH", "ETH")
        ],
    )
    def test_currency(self, origin: str, dest: str) -> None:
        self.assertIsNotNone(Currency.currency(origin, dest))


if __name__ == '__main__':
    unittest.main()