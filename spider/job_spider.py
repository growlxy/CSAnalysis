import os
import random
import time

import pandas as pd
from requests import post

def getData():
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    cookies = open('cookie.txt').read()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cookie': cookies,
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    form_data = {
        'first': 'true',
        'pn': '1',
        'kd': 'python'
    }

    time.sleep(random.randint(1, 3))
    respone = post(url, headers=headers, data=form_data, timeout=3)

    result = extractData(respone)
    result.to_csv(f'{os.getcwd()}\\analysis\\result.csv', encoding='utf-8')

    return result

def extractData(respone):
    data_json = respone.json()
    positions = data_json['content']['positionResult']['result']
    data = []
    for position in positions:
        job = [
            position['positionId'],
            position['positionName'],
            position['companyId'],
            position['companyFullName'],
            position['companySize'],
            position['industryField'],
            position['financeStage'],
            position['firstType'],
            position['secondType'],
            position['thirdType'],
            position['city'],
            position['district'],
            position['salary'],
            position['workYear'],
            position['education'],
            position['positionAdvantage']
        ]
        data.append(job)

    columns = ['positionId', 'positionName', 'companyId', 'companyFullName', 'companySize', 'industryField', 'financeStage',
               'firstType', 'secondType', 'thirdType', 'city', 'district', 'salary', 'workYear', 'education', 'positionAdvantage']
    data = pd.DataFrame(data=data, columns=columns)

    return data

