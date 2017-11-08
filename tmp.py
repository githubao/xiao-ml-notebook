#!/usr/bin/env python
# encoding: utf-8

"""
@description: 数据文件处理

@author: pacman
@time: 2017/11/7 13:39
"""

import json

root_path = 'C:\\Users\\BaoQiang\\Desktop\\'

input_file = '{}/xunfei-intent-out.txt'.format(root_path)
output_file = '{}/xunfei-intent-out2.txt'.format(root_path)


def run():
    with open(input_file, 'r', encoding='utf-8') as f, \
            open(output_file, 'w', encoding='utf-8') as fw:
        for line in f:
            ques, cate, data = line.strip().split('\t')
            json_data = json.loads(data)

            try:
                text = json_data['data']['answer']['text']
                service = json_data['data']['service']
            except:
                service = '_'
                text = '_'

            fw.write('{}\t{}\t{}\t{}\n'.format(cate, ques, service, text))


def main():
    run()


if __name__ == '__main__':
    main()
