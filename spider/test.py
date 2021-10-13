import os
import pandas as pd

from job_spider import getData


if __name__ == '__main__':
    kd = ['javascript', 'python', 'java', 'php', 'c++']
    getData(kd[4])
