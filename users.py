import csv
import os

import numpy as np
import pandas as pd
import requests

url = "https://httpbin.org/post"

def post_request(filename):

    data= pd.read_csv(filename)
    df = pd.DataFrame(data, columns=['first_name', 'second_name', 'Age'])
    print(df)

    for index, row in df.iterrows():
        f_name = row[0]
        s_name = row[1]
        a_age = row[2]

        payload = {"first_name": f_name, "second_name":s_name, "age": a_age}
        # print(payload)

        req = requests.post(url, data=payload)

        print(req.text)

post_request("users.csv")