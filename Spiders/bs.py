# !/user/bin/env python
# -*- coding:utf-8 -*- 

'''
项目:bilibili一键签到
目标网址:https://m.bilibili.com
'''

import sys
import requests, re


def signin():
    print('*' * 30 + 'bilibili自动签到' + '*' * 30)
    cookie = sys.argv[1]
    #input('请输入您登录百度贴吧后获取的Cookie值:')
    url = 'https://m.bilibili.com/'
    headers = {
        'Cookie': cookie,
        'User-Agent':'Mozilla/5.0 (Linux; Android 9; Unspecified Device) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3764.0 Mobile Safari/537.36'
    }
    html = requests.get(url, headers=headers).text
    print(html)

if __name__ == '__main__':
    signin()
