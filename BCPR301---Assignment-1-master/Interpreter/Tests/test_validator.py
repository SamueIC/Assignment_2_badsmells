from unittest import TestCase
from Interpreter.validator import Validator
from datetime import datetime


class TestValidator(TestCase):

    def setUp(self):
        self.validator = Validator()

    def tearDown(self):
        del self.validator

    def test_empid_invalid(self):
        """
        Tests validating data
        """
        empid = "A12323123123"
        expected = False

        result = self.validator.check_empid(empid)
        self.assertEqual(expected, result)

    def test_empid_valid(self):
        """
        Tests validating data
        """
        empid = "Q666"
        expected = "Q666"

        result = self.validator.check_empid(empid)
        self.assertEqual(expected, result)

    def test_gender_true_female_letter(self):
        """
        Tests validating data
        """
        gender = "F"
        expected = "F"

        result = self.validator.check_gender(gender)
        self.assertEqual(expected, result)

    def test_gender_true_female_string(self):
        """
        Tests validating data
        """
        gender = "Female"
        expected = "F"

        result = self.validator.check_gender(gender)
        self.assertEqual(expected, result)

    def test_gender_true_male_string(self):
        """
        Tests validating data
        """
        gender = "male"
        expected = "M"

        result = self.validator.check_gender(gender)
        self.assertEqual(expected, result)

    def test_gender_false(self):
        """
        Tests validating data
        """
        gender = "transgender"
        expected = False

        result = self.validator.check_gender(gender)
        self.assertEqual(expected, result)

    def test_age_true(self):
        """
        Tests validating data
        """
        age = "23"
        expected = "23"

        result = self.validator.check_age(age)
        self.assertEqual(expected, result)

    def test_age_false(self):
        """
        Tests validating data
        """
        age = "213"
        expected = False

        result = self.validator.check_age(age)
        self.assertEqual(expected, result)

    def test_sales_true(self):
        """
        Tests validating data
        """
        sales = "123"
        expected = "123"

        result = self.validator.check_sales(sales)
        self.assertEqual(expected, result)

    def test_sales_false(self):
        """
        Tests validating data
        """
        sales = "1233"
        expected = False

        result = self.validator.check_sales(sales)
        self.assertEqual(expected, result)

    def test_BMI_true(self):
        """
        Tests validating data
        """
        BMI = "Normal"
        expected = "Normal"

        result = self.validator.check_BMI(BMI)
        self.assertEqual(expected, result)

    def test_BMI_lowercase(self):
        """
        Tests validating data
        """
        BMI = "overweight"
        expected = "Overweight"

        result = self.validator.check_BMI(BMI)
        self.assertEqual(expected, result)

    def test_BMI_false(self):
        """
        Tests validating data
        """
        BMI = "Fatty"
        expected = False

        result = self.validator.check_BMI(BMI)
        self.assertEqual(expected, result)

    def test_salary_true(self):
        """
        Tests validating data
        """
        salary = "456"
        expected = "456"

        result = self.validator.check_salary(salary)
        self.assertEqual(expected, result)

    def test_salary_false(self):
        """
        Tests validating data
        """
        salary = "456million"
        expected = False

        result = self.validator.check_salary(salary)
        self.assertEqual(expected, result)

    def test_birthday_true(self):
        """
        Tests validating data
        """
        birthday = "13/12/1994"
        expected = "13/12/1994"

        result = self.validator.check_birthday(birthday)
        self.assertEqual(expected, result)

    def test_birthday_false(self):
        """
        Tests validating data
        """
        birthday = "13-12-1994"

        result = self.validator.check_birthday(birthday)
        self.assertFalse(result)

    def test_xlxs_date(self):
        """"
        Tests static return function, test coverage purposes
        """
        expected = "13-12-1994"
        test_date = datetime(1994, 12, 13)
        result = Validator.xlsx_date(test_date)
        self.assertEquals(expected, result)

    def test_save_dict_valid(self):
        """
        Test static checker method
        """
        data2 = {0: {'ID': 'Q123', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', 'Salary': '12',
                     'Birthday': '01/01/1996'}}
        expected2 = {0: {'ID': 'Q123', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', 'Salary': '12',
                         'Birthday': '01/01/1996'}}
        result2 = self.validator.save_dict(data2)
        self.assertEqual(result2, expected2)
        # may need to tweak this method to accurately show coverage

    def test_z_save_dict_invalid(self):
        """
        Test static checker method
        """
        data1 = {0: {'ID': 'A1232', 'Gender': 'F', 'Age': '21', 'Sales': '101', 'BMI': 'Normal', 'Salary': '12',
                     'Birthday': '01/01/1996'},
                 1: {'ID': 'Q999', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', 'Salary': '12',
                     'Birthday': '01/01/1996'}
                 }
        expected1 = {1: {'ID': 'Q999', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', 'Salary': '12',
                         'Birthday': '01/01/1996'}
                     }
        result1 = self.validator.save_dict(data1)
        self.assertEqual(result1, expected1)

    def test_check_checker_invalid_id(self):
        """
        Test static checker method
        """
        data = {0: {'ID': 'A1232', 'Gender': 'F', 'Age': '21', 'Sales': '101', 'BMI': 'Normal', 'Salary': '12',
                    'Birthday': '01/01/1996'},
                1: {'ID': 'A123', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', 'Salary': '12',
                    'Birthday': '01/01/1996'}
                }
        expected = {1: {'ID': 'A123', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', 'Salary': '12',
                        'Birthday': '01/01/1996'}
                    }
        result = Validator.save_dict(data)
        print('result')
        print(result)
        self.assertEqual(result, expected)
