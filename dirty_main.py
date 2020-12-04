from datetime import datetime
from application.salary import *
from db.people import *

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    date = datetime.now()
    print(date)
    print(name, salary)