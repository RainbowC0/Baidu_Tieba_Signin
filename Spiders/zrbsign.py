# !/user/bin/env python
# -*- coding:utf-8 -*- 

import requests, re
import sys

def signin():
	print('*' * 30 + '众人帮每日自动打卡' + '*' * 30)
	cookie = sys.argv[1]
	url = 'http://m.zrb.net/api/units/DailyColock'
	headers = {
		'Cookie': cookie,
		'User-Agent':'Mozilla/5.0 (Linux; Android 9; Unspecified Device) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.0.0 Mobile Safari/537.36',
		'Accept':'application/json'
	}
	form = {'account':'15760207563','password':'4631727ABB07B5FEF574F3DC14FB9CC3'}
	#d=parse.urlencode(d)
	#d=d.encode("utf-8")
	rlt = requests.post(url,data=form,headers=headers).json();
	print(rlt['msg'])

if __name__ == '__main__':
	signin()
