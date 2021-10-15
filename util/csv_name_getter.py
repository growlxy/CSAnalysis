import os
import re


def get_csv_name():
    list = []
    fl = os.listdir(f'{os.path.dirname(os.getcwd())}\\analysis')
    for i in fl:
        if 'result' in i:
            i = re.split('_result.csv', i)
            list.append(i[0])

    return list
