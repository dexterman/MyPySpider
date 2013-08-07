# coding: utf8

import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup

# 登录
signin_url = r'http://project.excellence.com.cn/redmine/login'
# 文档
documents_url = r'http://project.excellence.com.cn/redmine/projects/expass/documents'
# 文件
files_url = r'http://project.excellence.com.cn/redmine/projects/expass/files'

username = 'dengq'
password = r'415Egk\\789'


def SignIn():
	''' 模拟浏览器登录Project系统 '''

	# ---- 登录需要cookie支持，先打开浏览网页 ----
	cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())
	opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
	urllib2.install_opener(opener)
	content = urllib2.urlopen(signin_url).read()
	# print content

	# --- 登录Project系统 ----
	# 设置post方法参数
	postdata=urllib.urlencode({
	    'username': username,
	    'password': password,
	    'authenticity_token': '3560c8ad94e931cb953473ecd614632ed489f6e9',
	    'back_url': 'http://project.excellence.com.cn/redmine/',
	    'login': '登录 »'
	})
	# 伪装成浏览器访问
	headers = {
	    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
	}
	# 生成request请求
	req = urllib2.Request(
    	url = signin_url,
    	data = postdata
    	# ,headers = headers  # 不是不需的，某些网站会检查   反”反盗链”
	)
	# 返回response内容
	result = urllib2.urlopen(req).read()
	# print result


def DownloadDocuments():
	''' 下载文档栏目文件 '''
	req = urllib2.Request(
    	url = documents_url
    	# ,data = postdata
	)
	result = urllib2.urlopen(req).read()
	# print result

	pass


def DownloadFiles():
	''' 下载文件栏目文件 '''
	pass


if __name__ == '__main__':
	SignIn()
	DownloadDocuments()