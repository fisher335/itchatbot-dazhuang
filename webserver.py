#!/usr/bin/env python
# -*- coding: utf-8 -*-  @Author  : bjsasc
import os
import time

from flask import Flask, Response, render_template, request, send_file

app = Flask(__name__)


def alert(msg):
    return Response('<script type = "text/javascript"> alert("{}");location.href="/"</script>'.format(msg))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['POST'])
def login():
    if request.form.get('login') == 'shaomina':
        img_url = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'QR.png')
        resp = send_file(img_url)
        return resp
    else:
        return alert('密码错误')


@app.route('/reboot/', methods=['POST'])
def reboot():
    if request.form.get('reboot') == 'shaomina':
        os.system(
            'ps -ef | grep main.py | grep -v grep | cut -c 9-15 | xargs kill -s 9')

        return alert('重启服务成功,请扫描登录')
    else:
        return alert('密码错误')


if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8080, debug=False)
    app.run(host='0.0.0.0', port=8080, debug=False)
