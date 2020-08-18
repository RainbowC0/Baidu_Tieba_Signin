# !/user/bin/env python
# -*- coding:utf-8 -*- 

import requests, re
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

def urlupread(dri){
	return dri.current_url.find('upread.ccdy.cn')==-1
}

def urlwxqq(dri){
	return dri.current_url.find('mp.weixin.qq.com')!=-1
}

def signin():
	#print('*' * 30 + '幸运冲冲冲每日参与' + '*' * 30)
	url = 'http://upread.ccdy.cn/lxshow.html?c=8E671739&r='
	ua='Mozilla/5.0 (Linux; Android 5.1; OPPO R7s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 MicroMessenger/7.0.12.1620(0x27000C34) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64'
	options = webdriver.FirefoxOptions()
	options.add_argument('-headless')
	profile = webdriver.FirefoxProfile()
	profile.set_preference('permissions.default.image',2)
	profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
	profile.set_preference('general.useragent.override',ua)
	browser = webdriver.Firefox(options=options,firefox_profile = profile)
	print(dir(browser))
	browser.get(url)
	n=0
	WebDriverWait(browser,10).until(urlwxqq)
	while browser.current_url.find('cpu.baidu.com')!=-1:
		srs=browser.page_source
		print(srs)
		browser.back()
		WebDriverWait(browser,10).until(urlupread)
		n+=1
	browser.close()
	print(n)

if __name__ == '__main__':
	signin()
