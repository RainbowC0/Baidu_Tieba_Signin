# !/user/bin/env python
# -*- coding:utf-8 -*- 

import requests, re
import sys

def signin():
	print('*' * 30 + '众人帮每日自动打卡' + '*' * 30)
	cookie = sys.argv[3]
	url = 'https://c.29592.net/api/units/DailyColock'
	headers = {
		'Cookie': cookie,
		'User-Agent':'Mozilla/5.0 (Linux; Android 5.1; OPPO R7s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 Html5Plus/1.0',
		'Accept':'application/json'
	}
	form = {'account':sys.argv[1],'password':sys.argv[2]}
	#d=parse.urlencode(d)
	#d=d.encode("utf-8")
	rlt = requests.post(url,data=form,headers=headers).json();
	print(rlt['msg'])

if __name__ == '__main__':
	signin()
