# coding=utf-8
# author = zhouxin
# date = 2017.8.15
# description
# 从已经分析好的数据库中提取出结果,保存为可读的 txt 文件

from models import Rhyme, Word
from settings import SAVETXT_2, SAVETXT_3
from rhyme_index import RhymeIndex

class Ext:

    def __init__(self):

        # print(SAVETXT)
        self.rdct = dict(RhymeIndex)

    def _get_words(self, integ):

        query = Word.select().where(Word.rhyme == integ)
        if len(query) < 2:
            return

        r = []
        for i in query:
            r.append((i.word, i.re3+1))

        return sorted(r, key=lambda x:x[1], reverse=True)

    # 保存到 txt　字数为 2 为一个文件
    # 3 以及以上的为一个文件
    def _save(self, r, NUM):

        if NUM == 2:
            with open(SAVETXT_2, 'a+')as f:
                f.write(str(r))
                f.write('\n')
        else:
            with open(SAVETXT_3, 'a+')as f:
                f.write(str(r))
                f.write('\n')


    def main(self):
        query = Rhyme.select()
        for i in query:
            rh = i.integ
            # print(rh)
            res = self._get_words(rh)
            # print(res)
            if res:
                lst_rh = rh.split('-')
                s = []
                for i in lst_rh:
                    pre = self.rdct.get(i)
                    s.append(str(pre))
                NUM = len(lst_rh)
                s = '-'.join(s)
                res = '韵脚:' + s + '\t' + '词汇:' + str(res)
                self._save(res, NUM)


if __name__ == '__main__':
    ex = Ext()
    ex.main()