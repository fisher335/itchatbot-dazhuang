# coding=utf8
import itchat
from ai import get_response
import time
import logging
from datetime import datetime



@itchat.msg_register('Text')

def text_reply(msg):
    global ms
    ms= msg.fromUserName
    if u'查看日志' in msg['Text']:
        itchat.send_file(fileDir='logs/log.log', toUserName=msg['FromUserName'])
        # itchat.send(u'测试内容测试内容', toUserName=msg['FromUserName'])
        # itchat.send_image(fileDir='static/test.jpg',toUserName=msg['FromUserName'])
        # return u'你可以在这里了解他：https://github.com/littlecodersh'
    elif u'英雄名称' in msg['Text'] or u'获取文件' in msg['Text']:
        itchat.send_file(fileDir='static/hero.xls',
                         toUserName=msg['FromUserName'])
        # itchat.send('@fil@main.py', msg['FromUserName'])
        # itchat.send('@fil@static/hero.xls', msg['FromUserName'])
        return u'英雄的名称和简称请参考excel'
    elif u'获取图片' in msg['Text']:
        # itchat.send_msg(msg='test',toUserName=msg['FromUserName'])
        itchat.send_file(fileDir='static/hero.xls',
                         toUserName=msg['FromUserName'])
    # # itchat.send('@img@applaud.gif', msg['FromUserName'])  # there should be a picture
    elif u'电话' in msg['Text'] or u'手机' in msg['Text']:
        itchat.send_msg(get_response(msg['Text']),toUserName=msg['FromUserName'])
    else:
        ms = msg.fromUserName
        # return get_response(msg['Text']) or u'收到：' + msg['Text']
        itchat.send_msg(msg['Text'],'@99e92e57f8323524aee348c250847dae')


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def atta_reply(msg):
    return ({'Picture': u'图片', 'Recording': u'录音',
             'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
            u'已下载到本地')  # download function is: msg['Text'](msg['FileName'])


@itchat.msg_register(['Map', 'Card', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        return u'收到位置分享'
    elif msg['Type'] == 'Sharing':
        return u'收到分享' + msg['Text']
        # elif msg['Type'] == 'Note':
        return u'收到：' + msg['Text']
    elif msg['Type'] == 'Card':
        return u'收到好友信息：' + msg['Text']['Alias']


@itchat.msg_register('Text', isGroupChat=True)
def group_reply(msg):
    if msg['isAt']:
        a = msg['Text']
        # print a
        lo = a.find(u'\u2005')
        msg_rel = a[lo + 1:]
        if u'英雄介绍' in msg['Text']:
            return u'你可以在这里了解他：https://github.com/littlecodersh'
        elif u'英雄名称' in msg['Text'] or u'获取文件' in msg['Text']:
            # itchat.send('@fil@main.py', msg['FromUserName'])
            # itchat.send('@fil@static/hero.xls', msg['FromUserName'])
            itchat.send_file(fileDir='static/hero.xml', toUserName=msg['FromUserName'])
            # itchat.send('%s: %s' % (msg['Type'], msg['Type']), msg['FromUserName'])
            return u'英雄的名称和简称请参考excel'
        elif u'获取图片' in msg['Text']:
            # there should be a picture
            itchat.send('@img@applaud.gif', msg['FromUserName'])
        else:
            # print msg_rel
            itchat.send(u'@%s\u2005 %s' % (
                msg['ActualNickName'], get_response(msg_rel)), msg['FromUserName'])


#公众号微软小冰的回复转发
@itchat.msg_register('Text',isMpChat=True)
def group_reply(msg):
    itchat.send_msg(msg.text,ms)
    logging.warning(msg.text+'from xiaobing')



# TODO:增加群管理功能，自动加人 踢人
@itchat.msg_register('Note', isGroupChat=True)
def group_join_note(msg):
    print(msg)
    logging.warning(msg['Content'])
    logging.warning(msg['Text'])
    if u'邀请' in msg['Content'] or u'invited' in msg['Content']:
        str_content = msg['Content'];
        pos_start = str_content.find('"')
        pos_end = str_content.find('"', pos_start + 1)
        inviter = str_content[pos_start + 1:pos_end]
        rpos_start = str_content.rfind('"')
        rpos_end = str_content.rfind('"', 0, rpos_start)
        invitee = str_content[(rpos_end + 1): rpos_start]
        itchat.send_msg(u"@%s 欢迎来到本群[微笑]，感谢%s邀请。" % (invitee, inviter), msg['FromUserName'])


itchat.auto_login(True, enableCmdQR=False)
itchat.run(blockThread=False)
# 采用定时给文件助手发送消息的机制保证网页微信不退出，刷新时间为一小时
login_info = 'itchatbot has been login, time:' + \
             datetime.now().strftime('%Y-%m-%d:%H:%M:%S')
itchat.send(login_info, toUserName='filehelper')
while True:
    time.sleep(60 * 60)
    refresh_info = 'itchatbot has been refreshed, time:' + \
                   datetime.now().strftime('%Y-%m-%d:%H:%M:%S')
    itchat.send(refresh_info, toUserName='filehelper')
