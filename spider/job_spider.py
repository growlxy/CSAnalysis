import os
import sys
import random
import time
from urllib.parse import quote

import pandas as pd
from requests import post
from cookie_spider import getCookie


def getData(kd):
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    for page in range(1, 31):
        if (page - 1) % 5 == 0:
            cookies = getCookie()
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': f'https://www.lagou.com/jobs/list_{quote(kd)}/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400'
        }
        form_data = {
            'first': 'false',
            'pn': page,
            'kd': kd
        }
        if page == 1:
            form_data['first'] = 'true'

        time.sleep(random.random() + random.randint(2, 3))
        respone = post(url, headers=headers, data=form_data, cookies=cookies, timeout=3)
        time.sleep(1.5)

        result = extractData(respone)
        print("\r", end="")
        print(f"爬取进度： {round(page / 30 * 100)}%： {'▋' * int(page / 30 * 100 // 2)}", end="")
        sys.stdout.flush()
        try:
            if result == None:
                print(f'\n爬取中断，只爬取了{page-1}页，请稍后再试')
                return None
        except ValueError:
            if page == 1:
                temp = result
            else:
                temp = pd.concat([temp, result], ignore_index=True)

    temp.to_csv(f'{os.path.dirname(os.getcwd())}\\analysis\\{kd}_result.csv', encoding='utf-8')

    print(f'\n{kd}爬取完成')


def extractData(respone):
    data_json = respone.json()
    try:
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
    except KeyError:
        print(data_json)
        return None

    return data
