__author__ = 'Z50-70'

from requests import request
from bs4 import BeautifulSoup
import time


def main():
    url = 'https://nkdev.ru:8443/'
    prev = ''
    with open('prevLink.txt', 'r', encoding='utf-8') as f:
        prev = f.read()
    print(prev)
    while True:
        t = request('GET', url).text
        '''with open('test.html', 'w', encoding='utf-8') as f:
            f.write(t)'''
        prev = parse(t, prev)
        time.sleep(60)



def parse(text, prev):

    soup = BeautifulSoup(text, "lxml")
    links = [link.get("href") for link in soup.find_all("a")]
    print("last: " + str(soup.find('td').string.split(' ')[0]))

    if prev != links[0]:
        print('New massage')
        if input("Have you read them?\n").lower() == 'y':
            with open('prevLink.txt', 'w', encoding='utf-8') as f:
                f.write(links[0])
    else:
        print('No mew message')
    return links[0]

main()
