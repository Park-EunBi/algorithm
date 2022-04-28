from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests
import datetime


# 53페이지 매장 개수가 10보다 작아서 인덱스 오류 나는데 그거 해결하기
def yoger_store(result):
    result_test = []
    for page in range(1, 3):
        yoger_url = f'https://www.yogerpresso.co.kr/store/store_sub01.html?page={page}&is_search=&s_sido=&s_sigungu=&s_key=&s_parking=&s_wifi=&s_new=&s_delivery=&s_allday='
        print(yoger_url)

        response = requests.get(yoger_url)

        if (response.status_code == 200):
            html = response.content
            soupYoger = BeautifulSoup(html, 'html.parser')

            tag_ul = soupYoger.select('div.m_con')
            for info in tag_ul:
                store_info = info.find_all('span')
                store_name = store_info[1].text.strip()
                # store_info = store_info.text
                store_address = store_info[2].text.strip()
                result.append([store_name] + [store_address])
                result_test.append([store_name, store_address])

                '''
                for num in range(10):

                    ul = tag_ul[num].find_all('span')

                    store_name = ul[1].text.strip()
                    store_addr = ul[2].text.strip()

                    result.append([store_name] + [store_addr])
                    result_test.append([store_name, store_addr])

            '''
    return


def main():
    result = []

    print('yoger store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    yoger_store(result)  # [CODE 1] 호출
    yoger_tbl = pd.DataFrame(result, columns=('store', 'address'))
    yoger_tbl.to_csv('yoger.csv', encoding='cp949', mode='w', index=False)


if __name__ == '__main__':
    main()