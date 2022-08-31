from datetime import datetime
from pprint import pprint


from application import salary
from application.db import people

if __name__ == '__main__':
    pprint(people.get_employees())
    print(salary.calculate_salary(10, 2000))
    print(datetime.now())
