# !/user/bin/env python
# -*- coding:utf-8 -*- 

import requests, re
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def urlupread(dri):
	return dri.current_url.find('upread.ccdy.cn')==-1 and len(dri.find_elements_by_tag_name('script'))>2

def urlwxqq(dri):
	return dri.current_url.find('mp.weixin.qq.com')!=-1 and dri.find_element_by_id('moon_inline')!=None

def hasbody(dri):
	return len(dri.find_elements_by_tag_name('body'))>0

def signin():
	#print('*' * 30 + '幸运冲冲冲每日参与' + '*' * 30)
	headers={
		'User-Agent':'Mozilla/5.0 (Linux; Android 5.1; OPPO R7s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045318 Mobile Safari/537.36',
		'Cookie':sys.argv[1]
	}
	rslt=requests.post('https://c.29592.net/next/ViewTaskStart',headers=headers).json()
	print(rslt)
	if rslt['code']!=200 and rslt['code']!=110:
		rslt=requests.post('https://c.29592.net/next/ViewTaskStart',headers=headers).json()
		print(rslt)
	if rslt['code']==200 or rslt['code']==110:
		url = 'http://upread.ccdy.cn/lxshow.html?c=8E671739&r='
		ua='Mozilla/5.0 (Linux; Android 5.1; OPPO R7s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 MicroMessenger/7.0.12.1620(0x27000C34) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64'
		options = webdriver.FirefoxOptions()
		options.add_argument('-headless')
		options.add_argument('--ignore-certificate-errors')
		profile = webdriver.FirefoxProfile()
		profile.set_preference('permissions.default.image',2)
		profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
		profile.set_preference('general.useragent.override',ua)
		browser = webdriver.Firefox(options=options,firefox_profile = profile)
		browser.get(url)
		n=0
		WebDriverWait(browser,5).until(urlwxqq)
		while browser.current_url.find('cpu.baidu.com')==-1:
			print(len(browser.page_source))
			browser.back()
			WebDriverWait(browser,10).until(urlupread)
			n+=1
		WebDriverWait(browser,5).until(hasbody)
		browser.close()
		print(n)
		rslc=requests.post('https://c.29592.net/next/ViewTaskComplete',headers=headers).json()
		print(rslc['msg'])
	else:
		print(rslt['msg'])

if __name__ == '__main__':
	signin()
