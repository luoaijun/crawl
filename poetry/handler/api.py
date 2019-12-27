# -*- coding: utf-8 -*-
import json

import tornado.ioloop
import tornado.web

from compose_poem import gen_poem, pretty_print_poem
from poems.model import rnn_model
from poems.poems import process_poems
import numpy as np


class poetry(tornado.web.RequestHandler):

    def get(self):
        """get请求"""
        word = self.get_argument('word') + " end"
        num = self.get_argument('num')
        print(tuple(word.split(" ")))
        begin_char = input('## please input the first character:')
        poem = gen_poem(begin_char)
        list = []
        for item in poem:
            result = {item.score, item.path}
            list.append(result)
            print(item.score, item.path)
        self.write(json.dumps(poem))

application = tornado.web.Application([(r"/pinyinDAG", poetry)])


def run():
    application.listen(20086)
    tornado.ioloop.IOLoop.instance().start()
