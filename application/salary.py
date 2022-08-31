def calculate_salary(days, daily_rate):
    salary = f'{days * daily_rate} RUB'
    return salary


if __name__ == '__main__':
    print(calculate_salary(10, 1500))
