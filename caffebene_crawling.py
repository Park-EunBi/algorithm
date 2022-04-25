from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests
import datetime


def caffe_store(result):
    result_test = []
    caffebene_url = 'http://caffebene.com/store/local.html'
    print(caffebene_url)

    response = requests.get(caffebene_url)

    if (response.status_code == 200):
        html = response.content
        soupcaffe = BeautifulSoup(html, 'html.parser')
        tag_ul = soupcaffe.select('div.store-search-body > ul > li > div > h4 > a ')
        tag_ul2 = soupcaffe.select('div.store-search-body > ul > li > div > p ')

        # print(tag_ul)

        for num in range(0, 251):
            store_info = list(tag_ul[num])
            store_name = store_info[0].text
            store_info2 = list(tag_ul2)
            store_addr = store_info2[num * 2].text
            store_tel = store_info2[num * 2 + 1].text

            # print(store_name)
            # print(store_addr)
            # print(store_tel)

            result.append([store_name] + [store_addr] + [store_tel])
            result_test.append([store_name, store_addr, store_tel])

def main():
    result = []

    print('caffeBene store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    caffe_store(result)  # [CODE 1] 호출
    caffe_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    caffe_tbl.to_csv('caffebene.csv', encoding='cp949', mode='w', index=True)


if __name__ == '__main__':
    main()