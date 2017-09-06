## 分析说唱歌手歌词,提取押韵词汇

#### 结果

本项目一共分析了 459 首不重复的歌曲，歌手与网易歌单ID分别为：

- 红花会: 799977314
- PGone : 447516565
- VaVa : 808488091
- 艾福杰尼: 510860563
- BooM黄旭: 714593343
- Bridge: 639741735
- GAI爷: 557229147
- TizzyT: 462399965
- JonyJ: 49527655
- 小青龙:808976784
- 辉子: 714778058
- 孙八一:776141176
- 谢帝: 55433749
- 马思维: 155059572
- Mc光光:126482980
- 满舒克:110228333

以上 ID 为手动在网易云上查找获取。

分析过后共产生了 21206 个词汇
以及 2845 个韵脚


#### 文件说明已经项目运行流程

settings.py

一些通用的设置,涵盖了数据库名 歌单ID 最后的产出文件名

models.py

数据库设置文件
使用 peewee 建立需要的表和字段

rhyme_index.py

包含预设的韵脚

spider.py

爬歌词文件,分两部进行
1. 爬取每个歌单内歌曲名 ID
2. 爬取每个歌曲歌词 保存到数据库

analysis.py

分析歌词

1. 逐行导入歌词
2. 使用 jieba 切割歌词为词汇,同时也取每行歌词后两词添加到歌词中
3. 使用 rhyme_index 文件中的预设韵脚匹配词汇
4. 匹配后保存到数据库

extract.py

根据韵脚提取押韵词汇,集合到一个 txt 文件中

utils.py

调试阶段使用的工具函数

rhymewords-2.txt/ rhymewords-3.txt 分别包含双押以及三押以上词汇
words-frequency-n.txt / words-frequency-v.txt 分别为名词以及动词词频排行榜

#### 自定义运行流程

自定义分析歌词,可以按照以下顺序运行

1. 自定义 settings.py 中的设置
2. 运行 spider.py 文件
3. 运行 analysis.py 文件
4. 运行 extract.py 文件

到此,可到当前文件夹下查看生成的 txt 文件, analysis.py 的运行时间可能稍长,耐心等待.
注意: 如果需对歌词重新分析,只需运行 utils.py 文件即可,该文件会删除现有的分析结果,但不会删除已经下载的歌词.

#### 技术细节

1、请求网易云 api 接口

本项目使用到了歌单接口,以及歌词接口,使用方法如下:

请求**歌单**

分别去请求我们手动获取的歌单 ID， 得到歌单内所有歌曲的 ID

```python

import requests
# 实际使用时修改歌单 id 即可
url = 'http://music.163.com/api/playlist/detail?id=402614161'
req = requests.get(url)
data = req.json()
print(data)

```

请求 **歌词**

从上一步请求歌单的结果中可以提取歌单内所以歌曲的ID，继续请求获取歌词

```python

import requests
# 实际使用时修改歌曲 id 即可
url = 'http://music.163.com/api/song/lyric?os=pc&id=411988938&lv=-1&kv=-1&tv=-1'
req = requests.get(url)
data = req.json()
print(data)

```

2、peewee 处理数据库部分

[点我: 官方文档](http://docs.peewee-orm.com/en/latest/)

如果你也厌倦了写原生的 sql 语句,在简单的项目中, 使用 peewee 是较好的选择.

简单的建表流程如下

```python

from peewee import *
db = SqliteDatabase('peewee.db')
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
    class Meta:
        database = db

db.connect()
db.create_tables([Lrc])

```
运行以上代码就在 peewee.db 数据库文件中建立好了一张表.更详细的用法参考文档,以及本项目中的代码

3 jieba 分词处理

[点我:官方地址](https://github.com/fxsjy/jieba)

jieba 是一个非常好用的中文分词库,简单的示例代码如下

```python

import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

'''
结果:

【全模式】: 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学

【精确模式】: 我/ 来到/ 北京/ 清华大学

'''
```

4 xpinyin 转换文字为拼音

[点我:官方文档](https://github.com/lxneng/xpinyin)
xpinyin 是一个中文文字拼音转换库,使用方法如下

```linux

>>> from xpinyin import Pinyin
>>> p = Pinyin()
>>> # default splitter is `-`
>>> p.get_pinyin(u"上海")
'shang-hai'

```
