# coding=utf-8
# author=zhouxin
# date=2017.8.15
# decription
# 使用 peewee 链接数据库, 建立一些models

from peewee import *
from settings import DATABASE
import os

db = SqliteDatabase(DATABASE)

# 歌词
class Lrc(Model):
    # 音乐ID
    music_id = IntegerField()
    # 音乐名
    music_name = CharField()
    # 歌手
    singer = CharField()
    # 歌词
    lrc = TextField()
    # 保留字段
    # 8.16 update re1 作为去重标记
    # re1 为　'd'　表示重复歌曲
    re1 = CharField(default='')
    re2 = CharField(default='')
    re3 = IntegerField(default=0)
    re4 = IntegerField(default=0)

    class Meta:
        database = db


# 押韵组合
class Rhyme(Model):

    # 组合  '3;2'  '10;5'
    integ = CharField()
    # 保留字段
    re1 = CharField(default='')
    re2 = CharField(default='')
    # 8.16 update　re3 用作计数
    re3 = IntegerField(default=0)
    re4 = IntegerField(default=0)

    class Meta:
        database = db

# 结果
class Word(Model):

    # 韵脚组合  '3;2'
    rhyme = CharField()
    # 对应单词
    word = CharField()
    # 保留字段
    re1 = CharField(default='')
    re2 = CharField(default='')
    # 8.16 update　re3 用作计数
    re3 = IntegerField(default=0)
    re4 = IntegerField(default=0)

    class Meta:
        database = db


class Dt:

    def __init__(self):

        self.tables = [Word, Lrc, Rhyme]

    def build(self):

        existed = os.path.exists(DATABASE)

        if not existed:
            db.connect()
            db.create_tables(self.tables)