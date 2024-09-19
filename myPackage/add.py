import math

def add(*args):
    result = 0
    for i in args:
        result = result + i
    return result


import pandas as pd
import pathlib as Path

def manpower_category( man_catg_filepath):
    data = []
    with open(man_catg_filepath, 'r') as f:
        header = f.readline().strip().split(',')
        print(header)
        for line in f:
            val = line.strip().split(',')
            data.append(dict(zip(header,val)))
    df = pd.DataFrame(data)
    df.set_index('Index',inplace=True)
    return df
