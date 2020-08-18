# !/user/bin/env python
# -*- coding:utf-8 -*- 

import requests, re
import sys
from selenium import webdriver

def signin():
	#print('*' * 30 + '幸运冲冲冲每日参与' + '*' * 30)
	url = 'http://upread.ccdy.cn/lxshow.html?c=8E671739&r='
	headers = {
		'User-Agent':'Mozilla/5.0 (Linux; Android 5.1; OPPO R7s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 MicroMessenger/7.0.12.1620(0x27000C34) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64'
	}
	options = webdriver.FirefoxOptions()
	options.add_argument('-headless')
	profile = webdriver.FirefoxProfile()
	profile.set_preference('permissions.default.image', 2)
	profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
	#profile.set_preference('javascript.enabled', 'false')
	browser = webdriver.Firefox(options=options,firefox_profile = profile)
	#查看拥有的各种方法、属性
	print(dir(browser))
	browser.get(url)
	srs=browser.page_source
	print(srs)
	browser.close()

if __name__ == '__main__':
	signin()
