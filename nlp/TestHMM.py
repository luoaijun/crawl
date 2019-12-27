from Pinyin2Hanzi import DefaultHmmParams
from Pinyin2Hanzi import viterbi

hmmparams = DefaultHmmParams()

## 2个候选
result = viterbi(hmm_params=hmmparams, observations=('ni', 'zhi', 'bu', 'zhi', 'dao'), path_num = 2)
for item in result:
    print(item.score, item.path)
'''输出
1.3155294593897203e-08 ['你', '知', '不', '知', '道']
3.6677865125992192e-09 ['你', '只', '不', '知', '道']
'''

## 2个候选，使用对数打分
result = viterbi(hmm_params=hmmparams, observations=('ni', 'zhi', 'bu', 'zhi', 'dao'), path_num = 2, log = True)
for item in result:
    print(item.score, item.path)
'''输出
-18.14644152864202 ['你', '知', '不', '知', '道']
-19.423677486918002 ['你', '只', '不', '知', '道']
'''

## 2个候选，使用对数打分
# result = viterbi(hmm_params=hmmparams, observations=('ni', 'zhii', 'bu', 'zhi', 'dao'), path_num = 2, log = True)
# for item in result:
#     print(item.score, item.path)
# 发生KeyError，`zhii`不规范