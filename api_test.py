import requests
import jsonpath
import json

def doLogin():
	url = "http://user.fiidee.inet/admin/doLogin"
	params = {"Cookie": "SESSION=MTk1ZmRlOTItNzdmYy00NDY4LTg0ZjctNGQzMGI3YjIyYzk2"}
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	payload = {
		"username": "admin",
		"password": "kf1tY3psYOLk8fTv8lLYQAtb5mr0SIMGIis4VSPmw3j6ABrnCTX26qUBT/EPFpb8DWA0NSNpFqcC6+ARLXlfmmfgQJNY8J0uxiXcZNjMd8+lw4wr+fOOfbvUqcW6a2bwtX/rghiogurUcaoW6oSZmGRWbKoPtU1/ZF4mwRuYUG0=",
		"platid": "sys",
		"op": "login"
	}

	results = requests.post(url, data=payload, headers=headers).json()
	# print(results)
	res = jsonpath.jsonpath(results, '$..ssoUrls[7]')
	return res[0]

def get_JSESSIONID():
	url = doLogin()
	r = requests.get(url)
	headers = r.headers
	cookie = headers['Set-Cookie']
	JSESSIONID = cookie.split(';')[0]
	return JSESSIONID

print(doLogin())
url = "http://mondax.fiidee.inet/admin/market/price/summary"
cookie = get_JSESSIONID();
print(type(cookie))
print(cookie)

header = {'Cookie': cookie}
res = requests.get(url=url,headers=header).json()
print(res)