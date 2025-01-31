from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

dagparams = DefaultDagParams()

## 2个候选
result = dag(dagparams, ('pin'), path_num=3)
for item in result:
    print(item.score, item.path)
''' 输出
0.08117536840088911 ['你不知道', '的是']
0.04149191639287887 ['你不知道', '的诗']
'''

## 2个候选，使用对数打分
# result = dag(dagparams, ('ni', 'bu', 'zhi', 'dao', 'de', 'shi'), path_num=2, log=True)
# for item in result:
#     print(item.score, item.path)
''' 输出
-2.5111434226494866 ['你不知道', '的是']
-3.1822566564324477 ['你不知道', '的诗']
'''

## 1个候选
# print( dag(dagparams, ['ti', 'chu', 'le', 'bu', 'cuo', 'de', 'jie', 'jve', 'fang', 'an'], path_num=1) )
'''输出
[< score=0.0017174549839096384, path=['提出了', '不错', '的', '解决方案'] >]
'''