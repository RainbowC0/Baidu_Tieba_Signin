# !/user/bin/env python
# -*- coding:utf-8 -*- 

import requests, re
import sys
import random

def signin():
	print('*' * 30 + '幸运冲冲冲每日参与' + '*' * 30)
	url = 'https://numberdatas.nainiupt.com/number/luckyNumber.do?chooseLuckyNumber'
	headers = {
		'User-Agent':'Mozilla/5.0 (Linux; Android 5.1; OPPO R7s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 MicroMessenger/7.0.12.1620(0x27000C34) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64',
		'Accept':'application/json'
	}
	pre_num=requests.post('https://numberdatas.nainiupt.com/number/luckyNumber.do?previousLuckyNumberInfo',headers=headers).json()['luckyNumber']
	print(pre_num)
	lki=0
	while True:
		lki=random.randint(1,9)
		if lki!=pre_num:
			break;
	print(lki)
	form = re.sub('luckyNumber=[1-9]','luckyNumber='+str(lki),sys.argv[1])
        print(form)
	rlt = requests.post(url,data=form,headers=headers).json()
	print(rlt['status'])

if __name__ == '__main__':
	signin()
