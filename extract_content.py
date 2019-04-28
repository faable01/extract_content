import re
import requests
from bs4 import BeautifulSoup
import ssl
from concurrent.futures import ThreadPoolExecutor
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from readability.readability import Document
from extractcontent3 import ExtractContent

# InsecureRequestWarningを非表示にする
urllib3.disable_warnings(InsecureRequestWarning)

# 引数のURLのページにアクセス、メインコンテンツらしき文章を抽出する
def extract_content(url: str) -> str:
    h = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.1.2; ja-jp; SC-06D Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
    res = requests.get(url, headers=h, verify=False)
    
    # WEBページの文字コードを推測
    res.encoding = res.apparent_encoding
    if res.encoding != 'UTF-8' and res.encoding != 'utf-8':
        print(f'UTF-8以外の文字コードを検出：{res.encoding}')
        if res.encoding == 'Windows-1254':
            print('誤りだと思われる文字コード(Windows-1254)を検出しました。UTF-8に変換します。')
            res.encoding = 'UTF-8'
    
    html = res.text
    article = Document(html).summary()
    print(article)
    return article

# extractContent3で同上の処理を行う
def extract_content_3(url: str) -> str:
    h = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.1.2; ja-jp; SC-06D Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
    res = requests.get(url, headers=h, verify=False)
    
    # WEBページの文字コードを推測
    res.encoding = res.apparent_encoding
    if res.encoding != 'UTF-8' and res.encoding != 'utf-8':
        print(f'UTF-8以外の文字コードを検出：{res.encoding}')
        if res.encoding == 'Windows-1254':
            print('誤りだと思われる文字コード(Windows-1254)を検出しました。UTF-8に変換します。')
            res.encoding = 'UTF-8'
    
    html = res.text
    
    # extractContent3
    extractor = ExtractContent()
    
    # オプション値を指定する
    extractor.analyse(html)
    text, title = extractor.as_text()
    html, title = extractor.as_html()
    title = extractor.extract_title(html)
    print(text)
    print("")
    print(html)
    return text

#_________________________________________________
#
#実行処理
#-----------------------------
# # article = extract_content(r'https://travel.rakuten.co.jp/mytrip/ranking/spot-tokyo/')
# article = extract_content(r'https://macaro-ni.jp/30147')
# print(article)

extract_content_3(r'https://macaro-ni.jp/30147')