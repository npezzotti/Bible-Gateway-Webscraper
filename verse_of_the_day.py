#!/usr/bin/env python3

'''Scrapes the verse of the day from Bible Gateway'''

import requests, webbrowser, bs4

URL = 'https://www.biblegateway.com'

def main():
  res = requests.get(URL)
  res.raise_for_status()

  soup = bs4.BeautifulSoup(res.text, features="html.parser")
  passage = soup.find('div', { 'class': 'passage-box' })

  title = passage.find('span', { 'class': 'citation' }).text
  content = passage.find('div', { 'id': 'verse-text' }).text
  
  print('\n\033[1m\033[04m' + title + ':\033[0m\n')
  print(content)

  should_open = input("\n\033[01mOpen in Bible Gateway? (y/n) ")
  if should_open == 'y':
    href = passage.find('div', { 'class': 'verse-bar' }).a.get('href')
    webbrowser.open(URL + href)

if __name__ == '__main__':
  main()
