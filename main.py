from datetime import datetime
from application import salary as s
from application import people as p


if __name__ == "__main__":
    s.calculate_salary()
    p.get_employees()
    print(f'it`s too late! \n{datetime.now()}')

