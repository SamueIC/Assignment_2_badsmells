from unittest import TestCase

from validator import Validator


class TestValidator(TestCase):

    def tests_invalid_id(self):
        """
        Tests invalid ID
        """
        test_data = {0: {"1D": "A123", "Gender": "F", "Age": "23", "Sales": "789", "BMI": "Normal", "Salary": "200",
                         "Birthday": "24/06/1994"},
                     1: {"1D": "11111", "Gender": "M", "Age": "28", "Sales": "444", "BMI": "Normal", "Salary": "420",
                         "Birthday": "24/06/1989"}}

        expected = {0: {"1D": "A123", "Gender": "F", "Age": "23", "Sales": "789", "BMI": "Normal", "Salary": "200",
                        "Birthday": "24/06/1994"}, }

        result = Validator.save_dict(test_data)
        print(result)
        print("result ^^^^")
        print(expected)
        print("expected^^^")
        self.assertEqual(expected, result)