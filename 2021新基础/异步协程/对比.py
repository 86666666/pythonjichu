
#普通循环方式下载，遇到网络io只能等待上一个请求下载完成之后，继续下载下一个图片
import requests

def download_image(url):
    print(f'开始下载：{url}')
    response=requests.get(url)
    print('下载完成')
    #文件名称
    file_name=url.split('_')[-1] #取出来url最后一个下划线右边的字符串作为文件名称
    with open(file_name,'wb') as p:
        p.write(response.content) #respnse.content是二进制形式

url_list = [
          'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
          'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
          'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
      ]
for item in url_list:
    download_image(item)


#异步协程的方式

