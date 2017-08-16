# coding=utf-8
# author = zhouxin
# date = 2017.8.15
# dexcription
# 分析词汇

from rhyme_index import RhymeDct
from models import Lrc, Word, Rhyme
from settings import RHYMENUM
import xpinyin
import jieba

class AnaRhyme:

    def __init__(self):

        self.pin = xpinyin.Pinyin()
        # 标记是否在循环中
        self.mark = True

    def _analysis_one(self, lrc):

        lrc_list = lrc.split('\n')
        n_lrc = lrc.replace('\n', '').replace(' ', '')
        jieba_l = self._jieba_words(n_lrc)

        for l in lrc_list:
            # 跳过字数不够的词
            if len(l) <= RHYMENUM:
                continue

            # # 切片取得押韵字数
            n = RHYMENUM * (-1)
            q_words = l[n:]
            jieba_l.append(q_words)

        for words in set(jieba_l):
            if len(words) < RHYMENUM:
                continue
            r = self._analysis_words(words)
            if r:
                # 词汇去重
                try:
                    w = Word.get(Word.word == words)
                    w.re3 += 1
                    w.save()
                except:
                    Word.create(
                        rhyme=r,
                        word=words
                    )
                    # print(words)
                # 韵脚去重
                try:
                    ry = Rhyme.get(Rhyme.integ == r)
                    ry.re3 += 1
                    ry.save()
                except:
                    Rhyme.create(
                        integ=r
                    )
                    # print(r)

    # jieba 分析歌词行
    def _jieba_words(self, l):
        lst = jieba.cut(l)
        return [i for i in lst if len(i) > 1]

    #
    def _analysis_words(self, words):

        word_py = self.pin.get_pinyin((u'{}'.format(words)))
        lst_words = word_py.split('-')
        r = []
        for i in lst_words:

            while True:
                if not i:
                    break
                token = RhymeDct.get(i, None)
                if token:
                    r.append(token)
                    break
                i = i[1:]
        if len(r) == len(words):
            return '-'.join(r)


    def main(self):

        query = Lrc.select()
        for i in query:
            lrc = i.lrc
            self._analysis_one(lrc)

    def t2(self):

        # print(next(self._extract()))
        # print('==========')
        # print(next(self._extract()))
        t = Lrc.get(Lrc.music_id == 493752191)
        print(t)
        # t = Lrc.select()
        # for i in t:
        #     print(i.music_id)

if __name__ == '__main__':
    ana = AnaRhyme()
    ana.main()