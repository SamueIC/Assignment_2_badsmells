import re
from copy import deepcopy


class Validator:
    def __init__(self):
        self.temp_dict = dict()
        self.valid_dict = dict()
        self.empid = "^[A-Z][\d]{3}$"
        self.gender = "^(M|F)$"
        self.age = "^[\d]{2}$"
        self.sales = "^[\d]{3}$"
        self.bmi = "^(Normal|Overweight|Obesity|Underweight)$"
        self.salary = "^([\d]{2}|[\d]{3})$"
        self.birthday = "^(0[1-9]|[1-2][0-9]|3(0|1))(/)(0[1-9]|1[0-2])(/)(19|20)[0-9]{2}$"

    def check_all(self, new_value, new_key):
        """
        :param new_value:
        :param new_key:
        :return:
        >>> v = Validator()
        >>> v.checker({'ID': 'Q999', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', 'Salary': '12',\
                     'Birthday': '01/01/1996'})
        True
        """
        new_key = getattr(self, new_key)
        new_value = str(new_value)
        # Remove invalid delims
        new_value = self.fix_bday_delims(new_value)
        # Fix long-hand gender notation
        new_value = self.fix_gender(new_value)
        # Match all standard RegEx
        match = re.match(new_key, new_value)
        # Check this functions correctly and is in correct call order
        match_bmi = self.fix_bmi(new_value)

        if match:
            return new_value
        elif match_bmi is True:
            new_value = new_value.capitalize()
            return new_value
        else:
            new_value = False
            return new_value

    @staticmethod
    def fix_bmi(new_bmi):
        match = re.match("^(normal|overweight|obesity|underweight)$", new_bmi)
        if match:
            return True
        else:
            return False

    @staticmethod
    def fix_gender(new_gender):
            match = re.match("^(m|M)ale$", new_gender)
            fmatch = re.match("^(f|F)emale$", new_gender)
            if match:
                new_gender = "M"
            elif fmatch:
                new_gender = "F"
            return new_gender

    @staticmethod
    def fix_bday_delims(new_birthday):
        invalid_delims = "^(|/\\.:;,_)$"
        for i in invalid_delims:
            new_birthday = new_birthday.replace(i, "/")
        return new_birthday

    @staticmethod
    def xlsx_date(a_date):
        return a_date.date().strftime("%d-%m-%Y")

    def checker(self, row):
        for key, value in row.items():
            if key == "ID" or "EMPID" or "Gender" or "Age" or "Sales" or "Salary" or "Birthday" or "BMI":
                if key == "ID":
                    key2 = "empid"
                else:
                    key2 = key.lower()  # THIS IS A HACK FIX
                if self.check_all(value, key2) is False:
                    result = False
                    return result
                else:
                    self.push_value(key, self.check_all(value, key2))
            else:
                result = False
                return result

    def save_dict(self, loaded_dict):
        for empno, row in loaded_dict.items():
            b = self.checker(row)
            if b is False:
                print("Error at entry: " + str(empno))
            else:
                self.push_row(empno)
        return self.return_dict()

    def push_value(self, key, val):
        self.temp_dict[key] = val

    def push_row(self, empno):
        print("Adding Row " + str(empno))
        temp = deepcopy(self.temp_dict)
        self.valid_dict[empno] = temp
        print(self.valid_dict[empno])

    def return_dict(self):
        return self.valid_dict
