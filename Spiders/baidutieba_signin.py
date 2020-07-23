# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/2/27--19:24
__author__ = 'Henry'

'''
项目:百度贴吧一键签到
目标网址:https://tieba.baidu.com/
内容:实现一键将关注的贴吧全部签到
'''

import requests, re
import hashlib
import sys
from urllib import parse

def encodeData(data):
        '''主要是计算sign的值'''
        SIGN_KEY='tiebaclient!!!'
        s=''
        keys=data.keys()
        #print(sorted(keys))
        for i in sorted(keys):
            s+=str(i)+'='+str(data[i])
        sign=hashlib.md5((s+SIGN_KEY).encode('utf-8')).hexdigest().upper()
        #print(sign)
        data.update({'sign':str(sign)})
        return data

def signin():
    print('*' * 30 + '百度贴吧签到小助手' + '*' * 30)
    cookie = sys.argv[1]
    BDUSS = re.search(r"BDUSS=([0-9A-Za-z~\\-]*);",cookie)
    #input('请输入您登录百度贴吧后获取的Cookie值:')
    url = 'https://tieba.baidu.com/mo/q/newmoindex'
    headers = {
        'Cookie': cookie,
        'User-Agent':'bdtb for Android 9.1.0.0'
        #'Mozilla/5.0 (Linux; Android 5.1; OPPO R7s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 tieba/9.1.0.0 subType/mini'
    }
    html = requests.get(url, headers=headers).json()
    print(html)
    print('正在进行贴吧签到...')
    num = 0
    for i in html["data"]["like_forum"]:
        url = 'http://c.tieba.baidu.com/c/c/forum/sign'
        form = {
        "BDUSS":BDUSS[1],
        "_client_id":"wappc_1595418910913_863",
        "_client_type":"2",
        "_client_version":"9.1.0.0",
        "_phone_imei":"869411025969204",
        "cuid":"9313BAE7943B4443E95A5EA22A296057|O",
        "cuid_galaxy2":"9313BAE7943B4443E95A5EA22A296057|O",
        "fid":i["forum_id"],
        "kw":str(i["forum_name"]),
        "net_type":1,
        "tbs":str(html["data"]["itb_tbs"])}
        d=encodeData(form)
        d=parse.urlencode(d)
        d=d.encode("utf-8")
        htm = requests.post(url,data=d, headers=headers).json()
        print(htm)
        if htm['error_code'] == '160002':
            print('[' + i["forum_name"] + '吧]:' + '亲，此贴吧您之前已经签过了哦!')
        if htm['error_code'] == '0':
            print('[' + str(i["forum_name"]) + '吧]:' + '签到成功! 经验+'+htm['user_info']['sign_bonus_point'])
            num += 1
    print('\n')
    print('恭喜您,贴吧签到成功!一共签到' + str(num) + '个贴吧!')


if __name__ == '__main__':
    signin()
