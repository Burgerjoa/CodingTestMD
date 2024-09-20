#
# #텍스파일 쓰기
# f2=open("maincodes2.md","w")
# len=f2.write("asdasdasd")
# print("maincodes2.md:총%d바이트크기의 파일을 생성하였습니다."%len)
# f2.close()

import requests
from bs4 import BeautifulSoup
from unicodedata import category

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.acmicpc.net/problem/10757', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

aa = soup.select('#problem_tags')

print(aa)

