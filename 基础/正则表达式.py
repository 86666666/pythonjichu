import re
print(re.search(r'[1-9]\d{5}','bit-100081'))#函数式用法，一次性使用
#面向对象的用法：编译后多次操作
pat=re.compile(r'[1-9]\d{5}')
ui=pat.search('bit-100081')
print(ui.group(0))
print(ui.string)
print(ui.re)
print(ui)
