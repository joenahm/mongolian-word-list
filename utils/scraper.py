import requests
from bs4 import BeautifulSoup

def search_word_info(keyword):
    BASE_URL = 'http://www.bolor-toli.com/'
    # 访问主页面，取得音频和释义数据
    resp = requests.get('http://www.bolor-toli.com/dictionary/word?search=%s' % keyword)
    bs = BeautifulSoup(resp.content, 'html.parser')
    ret_table = bs.find(id='search_result_table')

    if ret_table:
        # 提取获得发音请求所需的2个数据
        trans_id = ''
        lang_id = ''
        explain = ''
        for item in ret_table.find_all('a', {'onclick': True}):
            if trans_id == '' and 'showSounds' in item.attrs['onclick']:
                # 拿到最后2个关键数据
                data = item.attrs['onclick'][:-1].split(',')[-2:]
                trans_id = data[0].strip()[1:-1]
                lang_id = data[1].strip()[1:-1]
                if trans_id != '' and lang_id != '' and explain != '':
                    break
            # 并且提取释义 
            if explain == '' and 'searchThisWord' in item.attrs['onclick']:
                explain = item.attrs['onclick'][:-1].split('\'')[1]
                if trans_id != '' and lang_id != '' and explain != '':
                    break

        # 获取发音数据
        sound_resp = requests.post('http://www.bolor-toli.com/dictionary/sounds', {
            'trans_id': trans_id,
            'lang_id': lang_id,
        })
        sound_bs = BeautifulSoup(sound_resp.content, 'html.parser')
        src = sound_bs.find('source').attrs['src']
        url = '%s%s' % (BASE_URL, src)
        
        return {
            'status': True,
            'url': url,
            'explain': explain,
        }
    else:
        print('未找到词[ %s ]的信息' % keyword)
        return {
            'status': False,
            'url': '',
            'explain': '',
        }


def download(url, target_path):
    content = requests.get(url).content
    file_name = url.split('/')[-1]
    with open('%s/%s' % (target_path, file_name), 'wb') as outF:
        outF.write(content)
    return file_name
