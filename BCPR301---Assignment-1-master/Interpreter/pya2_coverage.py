from coverage import Coverage
from Tests.test_validator import TestValidator

print(help(Coverage))

cov = Coverage()
cov.start()

a = TestValidator()
a.test_sales()
a.test_BMI()
a.test_gender()

cov.stop()
cov.html_report(directory='covhtml')
