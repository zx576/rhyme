# coding=utf-8
# author = zhouxin
# date = 2017.8.15


RhymeIndex = [('1', ['a', 'ia', 'ua']), ('2', ['ai', 'uai']), ('3', ['an', 'ian', 'uan']),
              ('4', ['ang', 'iang', 'uang']), ('5', ['ao', 'iao']), ('6', ['e', 'o', 'uo']), ('7', ['ei', 'ui']),
              ('8', ['en', 'in', 'un']), ('9', ['eng', 'ing', 'ong', 'iong']), ('10', ['er']), ('11', ['i']),
              ('12', ['ie', 'ye']), ('13', ['ou', 'iu']), ('14', ['u']), ('16', ['ue']), ('15', ['qu', 'xu', 'yu'])]

RhymeDct = {'ui': '7', 'uan': '3', 'ian': '3', 'iu': '13', 'en': '8', 'ue': '16', 'ing': '9', 'a': '1', 'ei': '7',
            'eng': '9', 'uo': '6', 'ye': '12', 'in': '8', 'ou': '13', 'ao': '5', 'uang': '4', 'ong': '9', 'ang': '4',
            'ai': '2', 'ua': '1', 'uai': '2', 'an': '3', 'iao': '5', 'ia': '1', 'ie': '12', 'iong': '9', 'i': '11',
            'er': '10', 'e': '6', 'u': '14', 'un': '8', 'iang': '4', 'o': '6', 'qu': '15', 'xu': '15', 'yu': '15'}


s = '''

    一、佳麻　 a ia ua　　　第十部　麻、佳半，部分入声

二、开来　 ai uai　　　　第五部　佳半、灰半

三、先寒　 an ian uan üan 第七部　寒删先元半十四部覃盐咸

四、江阳　 ang iang uang　第二部　江阳

五、逍遥　 ao iao　　　　　第八部　萧肴豪

六、国歌　 e o uo　　　　第九部　歌，部分入声

七、灰微　 ei ui　　　第三部　支微齐，部分入声

八、森林　 en in un ün　 第六部　真文元半，十三部　侵

九、冬青　 eng ing ong iong 第一部　东冬，十一部　庚青蒸

十、希奇（儿）i（er并入）　第三部　支微齐，部分入声

十一、诗词　i（整体认读）第三部　支微齐，部分入声

十二、别叠　ie (y)e 　　　　 部分入声，佳麻二韵部分字

十三、忧愁　ou iu　　　　 十二部　尤

十四、读书　u　　　　　　第四部　鱼虞，部分入声

十五、须臾　ü　　　　　　 第四部　鱼虞，部分入声

十六、绝学　üe　　　　　 部分入声



import re

def get_r(s):

    dct = []
    st = s.split('\n')
    pat = re.compile(r'[a-z]+')
    count = 1
    for i in st:
        if not i:
            continue
        r = re.findall(pat, i)
        dct.append((str(count), r))
        count += 1

    print(dct)
get_r(s)

def reb(lst):

    dct = {}
    for item in lst:

        for initem in item[1]:
            dct[initem] = item[0]

    print(dct)

reb(RhymeIndex)

'''


