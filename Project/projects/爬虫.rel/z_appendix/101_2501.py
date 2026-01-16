import os.path
import time
import pyautogui
import requests
from bs4 import BeautifulSoup


def download_pic(url, name):
    # 1、发送请求：准备单张图片的url
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    }
    # 2、获取数据：使用get请求
    response = requests.get(url, headers=headers)
    # 3、解析数据：无需解析
    # 4、保存数据：直接保存二进制数据到本地
    with open(name, 'wb') as file:
        file.write(response.content)


def get_many():
    # 爬取多个页面，用循环遍历
    for i in range(1, 10000):
        url = ('https://cn.bing.com/images/search?'
               'q=%e5%a4%a9%e7%ab%a5%e7%88%b1%e4%b8%bd%e4%b8%9d&qpvt='
               '%e5%a4%a9%e7%ab%a5%e7%88%b1%e4%b8%bd%e4%b8%9d&form=IGRE&first=1')

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        # 设置正确编码，解决乱码问题
        response.encoding = response.apparent_encoding
        html = response.text
        print(html)

        # 3、解析数据：在网页中找到图片链接
        # 经过分析，我们想要的img标签，都在 class属性为list的div标签中
        #      div class="list"  --->  ul  --->  li  ---> img
        soup = BeautifulSoup(html, "html.parser")
        div = soup.find('div', class_='ming')
        # print(div)

        # 从div标签中找到想要的img标签   alt=True保证找到的img标签包含alt属性
        img_list = div.find_all('img', alt=True)
        for img in img_list:
            print(img)
            name = './壁纸/' + img['alt'] + '.jpg'  # './壁纸/' 表示保存到文件夹中
            url = img['src']

            # 图片太多？创建一个文件夹，把图片放到文件夹里
            if not os.path.exists('壁纸'):  # 如果不存在 壁纸 文件夹
                os.mkdir('壁纸')            # 就创建

            # 调用函数下载图片
            download_pic(url, name)
            # 为了防止触发网站的反爬机制，每次爬取后，让程序休眠一段时间
            time.sleep(0.2)
            pyautogui.sleep(0.3)


get_many()
