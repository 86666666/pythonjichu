import requests
import asyncio
async def download_image(url):
    print(f'开始下载 {url}')
    loop=asyncio.get_event_loop() #设置事件循环
