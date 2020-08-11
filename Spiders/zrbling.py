# !/user/bin/env python
# -*- coding:utf-8 -*- 

import requests, re
import sys

def signin():
	print('*' * 30 + '众人帮每日自动打卡' + '*' * 30)
	cookie = sys.argv[3]
	url = 'http://m.zrb.net/api/units/LingDailyBonus'
	headers = {
		'Cookie': cookie,
		'User-Agent':'Mozilla/5.0 (Linux; Android 9; Unspecified Device) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.0.0 Mobile Safari/537.36',
		'Accept':'application/json'
	}
	form = {'account':sys.argv[1],'password':sys.argv[2]}
	#d=parse.urlencode(d)
	#d=d.encode("utf-8")
	rlt = requests.post(url,data=form,headers=headers).json();
	print(rlt['msg'])

if __name__ == '__main__':
	signin()
