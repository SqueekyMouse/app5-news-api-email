import requests
from datetime import datetime

date=datetime.now()
print(date.strftime('%Y-%m-%d'))

def read_url():
    url='https://finance.yahoo.com'
    request=requests.get(url=url)
    content=request.text
    print(content)

def news_api_test():
    api_key='277ead44cf2a4b6390bdf077aceeb055'
    url='https://newsapi.org/v2/everything?q=tesla&' \
        'from=2023-01-17&sortBy=publishedAt&' \
        'apiKey=277ead44cf2a4b6390bdf077aceeb055'

    request=requests.get(url=url)
    # content=request.text # this will be string!!!
    content=request.json() # thi will get a dict if its json!!!
    # print(type(content))
    print(content['totalResults'])
    print(len(content['articles']))
    print(content['articles'][90]['title'])

    ## use debugger console to explore complex data!!!!
    for index,art in enumerate(content['articles']):
        print(art['title'])
        if index>3:
            break


