import csv

def get_info(info_path):
    info = {}
    with open(info_path, 'r', encoding='utf-8') as infoF:
        ret = list(csv.reader(infoF))[1:]
        for item in ret:
            word = item[0]
            mp3 = item[1]
            explain = item[2]
            
            if word in info:
                info[word].append({
                    'mp3': mp3,
                    'explain': explain,
                })
            else:
                info[word] = [{
                    'mp3': mp3,
                    'explain': explain,
                }]
    return info


def set_info(info_path, info_dict):
    with open(info_path, 'w', encoding='utf-8') as infoF:
        infoF.write('word,mp3,explain\n')
        for word in info_dict.keys():
            items = info_dict[word]
            for item in items:
                infoF.write('%s,%s,%s\n' % (word, item['mp3'], item['explain']))

