# coding:utf-8
__author__ = 'fengshaomin'
__name__ = 'tuling'

import requests
import time

KEY = 'e06082d7fd0a4e4ca748833af327a536'


def get_tuling(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'itchar',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        # return r.get('text')
        result = r.get('text')
        if 'url' in r:
            result = result + '\n' + r.get('url')
        return result

    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return False


def test(data, msg=None, bot=None):
    return True


def respond(data, msg=None, bot=None):
    response = get_tuling(data)
    return response


if __name__ == '__main__':
    print(get_tuling('云盘的服务器有个地址ping不通'))
    # time.sleep(4)
    # get_response('北京')
