import unittest
import xmlrunner
import os
from unittest_parametrize import parametrize
from unittest_parametrize import ParametrizedTestCase
from unittest.mock import patch
from modules.units.units import Units

class TestUnits(ParametrizedTestCase):
    @parametrize(
        "origin, dest, value, expected_result, expected_api_return",
        [
            ("g", "lb", 1000,  2.2046226218487757, 2.2046226218487757),
            ("kg", "lb", 1, 2.2046226218487757, 2.2046226218487757),
            ("g", "oz", 1000, 35.273961949580412916, 35.273961949580412916),
            ("oz", "kg", 35.273961949580412916, 1, 1000),
            ("mg", "g", 1000, 1, 1),
        ],
    )
    @patch("modules.units.units.requests.post")
    def test_weight(self, mock_post, origin: str, dest: str, value: float, expected_result: float, expected_api_return: float) -> None:
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result-float": expected_api_return}
        mock_post.return_value = mock_response

        result = Units.weight(origin, dest, value)
        self.assertEqual(result, expected_result)
    
    @parametrize(
        "origin, dest, value, expected_result, expected_api_return",
        [
            ("C", "F", 0, 32, 32),
            ("F", "C", 32, 0, 0),
            ("K", "C", 273.15, 0, 0),
            ("C", "K", 0, 273.15, 0),
            ("F", "K", 32, 273.15, 0),
        ],
    )
    @patch("modules.units.units.requests.post")
    def test_temperature(self, mock_post, origin: str, dest: str, value: float, expected_result: float, expected_api_return: float) -> None:
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result-float": expected_api_return}
        mock_post.return_value = mock_response

        result = Units.temperature(origin, dest, value)
        self.assertEqual(result, expected_result)
    
    @parametrize(
        "origin, dest, value, expected_result, expected_api_return",
        [
            ("mi", "m", 1, 1609.344, 1609.344),
            ("m", "cm", 1, 100, 1),
            ("km", "mi", 1.6, 0.9941939075797344, 0.9941939075797344),
        ],
    )
    @patch("modules.units.units.requests.post")
    def test_distance(self, mock_post, origin: str, dest: str, value: float, expected_result: float, expected_api_return: float) -> None:
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result-float": expected_api_return}
        mock_post.return_value = mock_response

        result = Units.distance(origin, dest, value)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    # Ensure the directory exists
    output_dir = 'test-reports'
    os.makedirs(output_dir, exist_ok=True)
    
    # Run the tests
    runner = xmlrunner.XMLTestRunner(output=output_dir)
    unittest.main(testRunner=runner)
