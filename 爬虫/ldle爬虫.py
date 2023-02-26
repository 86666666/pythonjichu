from selenium import webdriver
url=('https://www.baidu.com')
path=('C:\\Users\86666\AppData\Local\Programs\Python\Python37\chromedriver.exe')
dr=webdriver.Chrome()
dr.get(url)
print(dr.title)
