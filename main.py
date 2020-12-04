from datetime import datetime
from application.salary import calculate_salary
from db.people import get_employees

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    date = datetime.now()
    print(date)
