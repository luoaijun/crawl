# -*- coding: utf-8 -*-
import json

import tornado.ioloop
import tornado.web

from poetry.compose_poem import gen_poem
import tensorflow as tf
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag
from Pinyin2Hanzi import DefaultHmmParams
from Pinyin2Hanzi import viterbi
import jieba

dagparams = DefaultDagParams()
hmmparams = DefaultHmmParams()


class pinyinDAG(tornado.web.RequestHandler):

    def get(self):
        """get请求"""
        word = self.get_argument('word') + " end"
        num = self.get_argument('num')
        print(tuple(word.split(" ")))
        result = dag(dagparams, tuple(word.split(" ")), path_num=num)
        list = []
        for item in result:
            result = {item.score, item.path}
            list.append(result)
            print(item.score, item.path)
        self.write(json.dumps(list))


class pinyinHMM(tornado.web.RequestHandler):

    def get(self):
        """get请求"""
        word = self.get_argument('word') + " end"
        num = self.get_argument('num')
        list = []
        result = viterbi(hmm_params=hmmparams, observations=(tuple(word.split(" "))), path_num=num, log=True)
        for item in result:
            result = {item.score, item.path}
            list.append(result)
            print(item.score, item.path)
        self.write(json.dumps(list))


class jiebas(tornado.web.RequestHandler):
    def get(self):
        word = self.get_argument('word')
        seg_list = jieba.cut_for_search(word)
        print(seg_list)
        self.write(",".join(seg_list))

class test(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world，test success！")

class poery(tornado.web.RequestHandler):
    def get(self):
        tf.reset_default_graph()  # 清除默认图像的堆栈，并重置默认图
        begin_char =self.get_argument("word")
        poem = gen_poem(begin_char)
        self.write(poem)


application = tornado.web.Application([(r"/pinyinDAG", pinyinDAG),
                                       (r"/test", test),
                                       (r"/pinyinHMM", pinyinHMM),
                                       (r"/jieba", jiebas),
                                       (r"/poery", poery)])


def run():
    application.listen(20086)
    tornado.ioloop.IOLoop.instance().start()
