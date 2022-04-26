from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests
import datetime


def jawsfood_store(result):
    result_test = []
    jaws_url = 'http://www.jawsfood.co.kr/store/store_search.html'

    print(jaws_url)

    response = requests.get(jaws_url)

    if(response.status_code == 200):
        html = response.content
        soupJaws = BeautifulSoup(html, 'html.parser')

        data = soupJaws.select('#datalist > li')
        for d in data:
            info = d.find_all('p')
            store_name = info[0].text
            store_addr = info[1].text

            result.append([store_name] + [store_addr])
            result_test.append([store_name, store_addr])


'''
        store_info = soupJaws.select('#datalist > li > a > p')
        store_info = list(store_info)
        for num in range(219):
            store_name = store_info[num * 2].text
            store_address = store_info[num * 2 + 1].text

            print(store_name)
            print(store_address)

            result.append([store_name] + [store_address])
            result_test.append([store_name, store_address])

'''
def main():
    result = []

    print('jawsfood store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    jawsfood_store(result)  # [CODE 1] 호출
    jawsfood_tbl = pd.DataFrame(result, columns=('store', 'address'))
    jawsfood_tbl.to_csv('jawsfood.csv', encoding='utf-8', mode='w', index=True)
    # 오류 나서 utf-8로 인코딩 했는데 이러면 csv 파일이 망가짐


if __name__ == '__main__':
    main()