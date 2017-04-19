#coding=utf-8

import os
import sys
# sys.path.append('..')

import aiml

# from tornado.options import options

__name__ = 'talkbot'
# print os.getcwd()
# root = 'e:/itchatrobot/'
root = os.getcwd()
aiml_set = os.path.join(root, 'aiml_set')
# aiml_set = 'd:/ai/aiml_set/'
talkbot_brain_path =  os.path.join(aiml_set, 'talkbot.brn')

talkbot_properties=dict(
        name='fengdazhuang',
        master='风大壮',
        birthday='',
        gender='男',
        city='北京',
        os='raspberry'
    )
# os.chdir(aiml_set)
class TalkBot(aiml.Kernel):
    def __init__(self):
        super(TalkBot, self).__init__()
        self.verbose('error')
        self.setTextEncoding('utf-8')
        if os.path.exists(talkbot_brain_path):
            self.bootstrap(brainFile=talkbot_brain_path)
        else:
            self.init_bot()
            self.saveBrain(talkbot_brain_path)

        for p in talkbot_properties:
            self.setBotPredicate(p, talkbot_properties[p])

    def init_bot(self):
        for f in os.listdir(aiml_set):
            if f.endswith('.aiml'):
                self.learn(os.path.join(aiml_set, f))

talkbot = TalkBot()
def test(data, msg=None, bot=None):
    return True

def respond(data, msg=None, bot=None):
    # print talkbot.respond(data)
    if '''Let's talk about math'''in talkbot.respond(data):
        return False
    else:
        return talkbot.respond(data).decode('utf-8')
# print(respond("说不说"))
# print(respond("调戏"))
# if __name__ == '__main__':
#
#     print(respond("说不说"))
