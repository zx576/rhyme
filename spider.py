# coding=utf-8
# author = zhouxin
# date = 2017.8.15

import requests
import queue
import threading
import time
from settings import MUSIClIST
from models import Lrc, Dt
import re


'''
url = 'http://music.163.com/api/artist/albums/1049144?id=1049144&offset=0&total=true&limit=5'
url2 = 'http://music.163.com/api/playlist/detail?id=402614161'
url3 = 'http://music.163.com/api/song/lyric?os=pc&id=411988938&lv=-1&kv=-1&tv=-1'
hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'}

def get_wy(url):

    req = requests.get(url)
    # print(req.json())
    dt = req.json()
    pt = re.compile(r'\[.*\]')

    s = dt['lrc']['lyric']
    new_s = re.sub(pt, '',s)
    print(new_s)
    # tracks = dt['result']['tracks']
    # for i in tracks:
    #     print(i['artists'][0]['name'], i['name'], i['id'])


get_wy(url3)
'''

class WySpider:

    def __init__(self):

        self.mlist = MUSIClIST
        self.q = queue.Queue()
        self.mlisturl = 'http://music.163.com/api/playlist/detail?id={}'
        self.lrcurl = 'http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'
        self.pt = re.compile(r'\[.*\]')
        self.db = Dt().build()
        self.hd = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}

    # 多线程获取歌曲 id
    def _get_music_id(self):

        for id in self.mlist:
            u = self.mlisturl.format(id)
            self._enq_music_id(u)

    # 请求歌单,将歌曲 id 入队
    def _enq_music_id(self, url):

        req = requests.get(url, headers=self.hd)
        req.raise_for_status()
        dt = req.json()
        tracks = dt['result']['tracks']
        for i in tracks:
            # print(i['name'], i['id'])
            self.q.put([i['artists'][0]['name'], i['name'], i['id']])

    # 多线程获取歌词
    def _get_lrc(self):

        while True:
            print(self.q.qsize())
            if self.q.empty():
                break
            if threading.active_count() > 5:
                time.sleep(3)
                continue
            m_info = self.q.get()
            try:
                t = threading.Thread(target=self._save_lrc, args=(m_info,))
                t.start()
                t.join()
            except:
                self.q.put(m_info)

    # 请求歌词信息,保存
    def _save_lrc(self, info):

        singer, name, id = info
        # 去重
        try:
            Lrc.get(Lrc.music_id == int(id))
            Lrc.get(Lrc.music_name == name)
            return
        except:
            pass

        u = self.lrcurl.format(id)
        req = requests.get(u, headers=self.hd)
        dt = req.json()
        s = dt['lrc']['lyric']
        new_s = re.sub(self.pt, '', s)

        Lrc.create(
            music_id=int(id),
            music_name=name,
            singer=singer,
            lrc=new_s
        )

    def main(self):
        self._get_music_id()
        self._get_lrc()


if __name__ == '__main__':
    wy = WySpider()
    wy.main()
