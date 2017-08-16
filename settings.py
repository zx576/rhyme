# coding=utf-8
# author = zhouxin
# date = 2017.8.15

import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))

# 是否测试环境
TEST = False

# 根据测试环境确定数据库的选用
if TEST:
    DATABASE = 'test_rhyme.db'
else:
    DATABASE = 'rhyme.db'

# 歌单
MUSIClIST = [
        '799977314', '447516565', '808488091', '510860563', '714593343', '639741735',
        '557229147', '462399965', '808976784', '714778058', '776141176', '55433749',
        '155059572', '126482980', '110228333'
             ]

'''
红花会: 799977314
PGone : 447516565
VaVa : 808488091
艾福杰尼: 510860563
BooM黄旭: 714593343
Bridge: 639741735
GAI爷: 557229147
TizzyT: 462399965
JonyJ: 49527655
小青龙:808976784
辉子: 714778058
孙八一:776141176
谢帝: 55433749
马思维: 155059572
Mc光光:126482980
满舒克:110228333
'''

# 至少押几字
# 根据需求修改
RHYMENUM = 2

# 保存文件路径
# 根据自己喜好修改文件名
SAVETXT_2 = os.path.join(BASEDIR, 'rhymewords-2.txt')
SAVETXT_3 = os.path.join(BASEDIR, 'rhymewords-3.txt')
