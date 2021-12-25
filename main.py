from utils.scraper import search_word_info
from utils.scraper import download
from utils.info import get_info
from utils.info import set_info
import os
import random
from playsound import playsound

INFO_PATH = 'data/info.csv'
MP3_PATH = 'data/mp3'
CURR_PATH = os.path.dirname(os.path.realpath(__file__))



def memo(info, word):
    for item in info[word]:
        mp3 = item['mp3']
        explain = item['explain']
        print('[ %s ]: %s' % (word, explain))
        playsound('%s\\data\\mp3\\%s' % (CURR_PATH, mp3))


def search_word(info, keyword):
    if keyword in info:
        memo(info, keyword)
    else:
        # 下载
        ret = search_word_info(keyword)
        if ret['status']:
            file_path = download(ret['url'], MP3_PATH)
            info[keyword] = [{
                'mp3': file_path,
                'explain': ret['explain'],
            }]
        # 更新数据库
        set_info(INFO_PATH, info)
        # 重新获取
        info = get_info(INFO_PATH)
        # 背诵
        memo(info, keyword)


def random_get(info):
    words = list(info.keys())
    rand_idx = random.randint(0, len(words)-1)
    rand_word = words[rand_idx]
    
    memo(info, rand_word)


info = get_info(INFO_PATH)

while True:
    inp = input(': ')
    if (inp == ''):
        random_get(info)
    else:
        search_word(info, inp)
