from pprint import pprint


def get_employees():
    staff = [{'per_num': '005', 'name': 'Григорий', 'surname': 'Велосипедов'},
             {'per_num': '006', 'name': 'Анастасия', 'surname': 'Самокатова'}]
    return staff


if __name__ == '__main__':
    pprint(get_employees())
