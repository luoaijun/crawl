# -*- coding: utf-8 -*-
import json

import tornado.ioloop
import tornado.web

from utils.MysqlUtils import MySQLUtils
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


application = tornado.web.Application([(r"/pinyinDAG", pinyinDAG),
                                       (r"/test", test),
                                       (r"/pinyinHMM", pinyinHMM),
                                       (r"/jieba", jiebas)])


def run():
    application.listen(20086)
    tornado.ioloop.IOLoop.instance().start()
