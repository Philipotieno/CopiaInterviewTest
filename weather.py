import csv
import os
from re import S

import numpy as np
import pandas as pd


def post_request(filename):

    df = pd.read_table(filename, sep="\s+", usecols=[0, 1, 2])

    df = pd.DataFrame(df, columns=['Dy', 'MxT', 'MnT'])

    # Clean data by removing *
    df["MnT"] = pd.to_numeric(df["MnT"].str.replace(r'*', '', regex=True))
    df["MxT"] = pd.to_numeric(df["MxT"].str.replace(r'*', '', regex=True))
    df["spread"] = df['MxT']-df['MnT']

    # Drop last row
    df.drop(df.tail(1).index,
            inplace=True)

    # Store the values of days and spread in dictionry
    datas = pd.Series(df.spread.values, index=df.Dy).to_dict()

    # Get maximum value
    max_value = max(datas, key=datas.get)

    print(max_value, datas[max_value])


post_request("weather.dat")
