#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: pacman
@time: 2017/11/7 16:28
"""

import redis
import sys


def remove():
    redis_prefix = 'apikey_scripts_'

    client = redis.Redis(host='10.46.64.52', port=6390, db=0, password='nlpturing2016')

    api_key = sys.argv[1]
    key = redis_prefix + api_key

    print('before: {}'.format(client.get(key)[:100]))

    client.delete(key)

    print('after: {}'.format(client.get(key)))


def main():
    remove()


if __name__ == '__main__':
    main()
