#!/usr/bin/env python3

'''Searches Bible Gateway for relevant verses'''

import bs4, requests, sys

def main(args):
  URL = 'https://www.biblegateway.com/quicksearch/?search={}&resultspp=250'
  q = "psalms"
  if len(args) > 1:
    q = args[1]
  
  html = get_html(URL.format(q))

  soup = bs4.BeautifulSoup(html, "html.parser")
  search_results = soup.find('div', class_='search-result-list')
  
  if search_results is not None:
    verses = search_results.find_all('li', class_='bible-item')

    if len(verses) > 0:
      for v in verses:
        title = v.find('a', class_='bible-item-title')
        content = v.find('div', class_='bible-item-text')
        # Remove extra hyperlink text
        extra_text = v.find('div', class_='bible-item-extras')
        extra_text.extract()

        print(title.text, content.text)

def get_html(url):
  '''Returns the HTML for a given URL'''
  res = requests.get(url)
  res.raise_for_status()
  return res.text

if __name__ == '__main__':
  main(sys.argv)
