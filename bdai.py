#!/usr/bin/env python
# encoding: utf-8

"""
@description: 百度的ai接口

@author: pacman
@time: 2017/10/30 18:07
"""

import os
from aip import nlp
import time
import random
import json


def run():
    with open('C:\\Users\\BaoQiang\\Desktop\\bdai.txt','r',encoding='utf-8') as f:
        data = f.readline()
        json_data = json.loads(data)

    ai_nlp = nlp.AipNlp(apiKey=json_data['apiKey'], appId=json_data['appId'], secretKey=json_data['secretKey'])

    fw = open('C:\\Users\\BaoQiang\\Desktop\\baidu-simi-test.txt', 'w', encoding='utf-8')

    filepath = 'C:\\Users\\BaoQiang\\Desktop\\simi-test'
    for filename in os.listdir(filepath):
        full_file = os.path.join(filepath, filename)

        source = filename.replace('.txt', '')

        with open(full_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    line = line.strip()
                    ques, degree = line.split('\t')

                    json_data = ai_nlp.simnet(source, ques)
                    score = json_data['score']

                    fw.write('{}\t{}\t{:0.2f}\t{}\n'.format(source, ques, score * 100, degree))
                    fw.flush()

                    time.sleep(random.random())

                except Exception as e:
                    print(e)
                    print(line)

        print('process file: {} complete'.format(full_file))

    fw.close()


# def tmp():
#     s1 = '我很开心'
#     s2 = '我开心死了'
#
#     ai_nlp = nlp.AipNlp(apiKey=apiKey, appId=appId, secretKey=secretKey)
#
#     print(ai_nlp.simnet(s1, s2))


# def get_token():
#     dic = {'app_key': '', 'secret_key': '',
#            'grant_type': 'client_credentials', }
#
#     url = 'https://aip.baidubce.com/oauth/2.0/token'
#
#     response = requests.post(url, json=dic)
#
#     return response.json()



def main():
    run()


if __name__ == '__main__':
    main()
