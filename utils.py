# coding = utf-8
# author = zhouxin
# date = 2017.8.15
# dexcription
# 一些调试阶段的工具函数

from models import Lrc, Word
import jieba.posseg as pseg
import re
import os
import json
from settings import BASEDIR

class Utils:

    def __init__(self):
        self.exclude = ['作词', '作曲', '混音', '编曲','歌词']

    # 删除某个 table 信息
    def delete_(self, ins):

        query = ins.delete().where(ins.re2 == '')
        query.execute()

    # 取词频较高的词汇
    # 同时可以筛选某类词性
    def get_most_common(self, num, f='n'):

        query = Word.select().where(Word.re3 > num)
        res = []
        for i in query:
            words = pseg.cut(i.word)
            for word, flag in words:
                # 筛选某类词性词汇
                if flag == f and word not in self.exclude:
                    res.append([i.word, i.re3])
            #
        res.sort(key=lambda x:x[1], reverse=True)
        # for i in res:
        #     print(i)
        return res

    def save_words_freq(self, txtname, num, ins, f='n'):

        dir = os.path.join(BASEDIR, txtname)
        res = self.get_most_common(num, f)
        dct = {}
        dct[ins] = res
        print(dct)
        # dct = dict(tuple(res))
        with open(dir, 'w',)as f:
            f.write(json.dumps(dct))


    # 查看兄弟出现次数
    # 验证数据有效性
    def get_total_num_lrc(self):
        query = Lrc.select().where(Lrc.re1 == '')
        pt = re.compile('兄弟')
        count = 0
        for i in query:
            # print(type(i.lrc))
            r = re.findall(pt, i.lrc)
            if r:
                count += 1
                print(count, i.music_name, i.music_id, i.singer, r)

        print(count)

    def deduplicate(self):

        query = Lrc.select().where(Lrc.re1 == '')
        for i in query:
            name = i.music_name
            songs = Lrc.select().where(Lrc.music_name == name)
            if len(songs) > 1:
                for j in songs[1:]:
                    j.re1 = 'd'
                    j.save()


if __name__ == '__main__':
    ul = Utils()
    # ul.delete_(Word)
    # ul.delete_(Rhyme)
    # ul.get_most_common(10)
    # ul.get_total_num_lrc()
    # ul.deduplicate()
    ul.save_words_freq('words-frequency-n.txt', 10, 'words', 'n')
    # ul.open_txt()