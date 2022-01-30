import csv
import os
from playsound import playsound
from random import randint


CURR_PATH = os.path.dirname(os.path.realpath(__file__))


def readWord(filename):
    words = {}
    with open(filename, 'r', encoding='utf-8') as inf:
        ret = list(csv.reader(inf))[1:]
        for item in ret:
            wid = item[0]
            word = item[1]
            inter = item[2]
            words[wid] = {
                'word': word,
                'inter': inter,
                'count': 0,
            }
    return words


def readCount(filename, words):
    with open(filename, 'r', encoding='utf-8') as inf:
        ret = list(csv.reader(inf))
        for item in ret:
            wid = item[0]
            count = int(item[1])
            if wid in words:
                words[wid]['count'] = count
            else:
                print('有无词条计数id: ', wid)


def saveCount(wid, wordDict, filename):
    wordDict[wid]['count'] += 1

    with open(filename, 'w', encoding='utf-8') as outf:
        for k in wordDict.keys():
            item = wordDict[k]
            outf.write('%s,%d\n' % (item['wid'], item['count']))


def memorize(countFile, wordDict):
    while True:
        readCount(countFile, wordDict)

        countKeyDict = {}
        for wid in wordDict.keys():
            item = wordDict[wid]
            item['wid'] = wid
            if item['count'] in countKeyDict:
                countKeyDict[item['count']].append(item)
            else:
                countKeyDict[item['count']] = [item]

        minKey = min(countKeyDict.keys())
        idx = randint(0, len(countKeyDict[minKey])-1)
        target = countKeyDict[minKey][idx]
        
        print('[ %s ] : %s \t %s' % (target['word'], target['inter'], target['wid']))

        soudFiles = os.listdir('mp3')
        targetSound = target['wid']+'.mp3'
        if targetSound in soudFiles:
            playsound(CURR_PATH+'\\mp3\\'+targetSound)
        
        inp = input()
        if inp == '1':
            saveCount(target['wid'], wordDict, countFile)


words = readWord('wordlist.csv')
memorize('count.csv', words)
