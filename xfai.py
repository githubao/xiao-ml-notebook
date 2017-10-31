#!/usr/bin/env python
# encoding: utf-8

"""
@description: 讯飞api

@author: pacman
@time: 2017/10/30 20:46
"""

import requests
import time
from base64 import b64encode
from hashlib import md5
import json
import os
import random

url = 'https://api.xfyun.cn/v1/aiui/v1/text_semantic'


def run():
    with open('C:\\Users\\BaoQiang\\Desktop\\bdai.txt', 'r', encoding='utf-8') as f:
        data = f.readline()
        json_data = json.loads(data)

    fw = open('C:\\Users\\BaoQiang\\Desktop\\xunfei-intent-test.txt', 'w', encoding='utf-8')

    filepath = 'C:\\Users\\BaoQiang\\Desktop\\simi-test'
    for filename in os.listdir(filepath):
        full_file = os.path.join(filepath, filename)

        source = filename.replace('.txt', '')

        with open(full_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    line = line.strip()
                    ques, degree = line.split('\t')

                    result_json = get_single(json_data, ques)

                    fw.write('{}\t{}\t{}\t{}\n'.format(source, ques, result_json, degree))
                    fw.flush()

                    time.sleep(random.random())

                except Exception as e:
                    print(e)
                    print(line)

        print('process file: {} complete'.format(full_file))

    fw.close()


def get_single(json_data, text):
    headers = {}

    text_b64 = b64encode(text.encode()).decode()
    headers['X-Appid'] = json_data['appId']
    headers['X-Param'] = b64encode(json.dumps({"scene": "main", 'userid': 321}).encode()).decode()
    headers['X-CurTime'] = '{}'.format(int(time.time()))

    src = '{}{}{}text={}'.format(json_data['apiKey'], headers['X-CurTime'], headers['X-Param'], text_b64)
    headers['X-CheckSum'] = get_md5(src)

    response = requests.post(url, headers=headers, data={'text': text_b64})
    print(headers)

    return response.text


def get_md5(src):
    return md5(src.encode()).hexdigest()


def tmp():
    res = b64encode('json: {"scene":"main"}'.encode()).decode()
    print(res)


def main():
    run()
    # tmp()


if __name__ == '__main__':
    main()
