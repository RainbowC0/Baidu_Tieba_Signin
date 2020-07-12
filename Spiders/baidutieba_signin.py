# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/2/27--19:24

'''
项目:百度贴吧一键签到
目标网址:https://tieba.baidu.com/
内容:实现一键将关注的贴吧全自动签到
'''

import sys
import requests, re


def signin():
    print('*' * 30 + '百度贴吧签到小助手' + '*' * 30)
    cookie = sys.argv[1]
    url = 'https://tieba.baidu.com/'
    headers = {
        'Cookie': cookie,
        'User-Agent': 'bdtb for Android 8.0.8.0'
    }
    html = requests.get(url, headers=headers).text
    tieba = re.findall(r'lp=1030">(.*?)</a>', html)
    #tieba = tieba[:int(len(tieba) / 2)]
    print('正在进行贴吧签到...')
    num = 0
    for i in tieba:
        #i = i.replace('\\\\', '\\').encode('latin-1').decode('unicode_escape')
        url = 'http://tieba.baidu.com/sign/add'
        form = {'ie': 'utf-8',
                'kw': i,  # 要签到的贴吧名
                'tbs': '7dc070643ef556f71594255318'}
        html = requests.post(url, data=form, headers=headers).json()
        if html['no'] == 1101:
            print('[' + i + '吧]:' + '亲，此贴吧您之前已经签过了哦!')
        if html['error'] == '' or html['no'] == 0:
            print('[' + i + '吧]:' + '签到成功! 经验+'+str(html['cont_sign_num']))
            num += 1
    print('\n')
    print('恭喜您,贴吧签到成功!一共签到' + str(num) + '个贴吧!')


if __name__ == '__main__':
    signin()
