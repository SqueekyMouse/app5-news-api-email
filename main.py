import requests
#commit: access news titles and descriptions Sec27
#commit: make request, get dict with data, access the article Sec27

api_key='277ead44cf2a4b6390bdf077aceeb055'
url='https://newsapi.org/v2/everything?q=tesla&' \
    'from=2023-01-17&sortBy=publishedAt&' \
    'apiKey=277ead44cf2a4b6390bdf077aceeb055'

# make request
request=requests.get(url=url)
# content=request.text # this will be string!!!

# get dict with data
content=request.json() # thi will get a dict if its json!!!

# print(type(content))
# print(content['totalResults'])
# print(len(content['articles']))
# print(content['articles'][90]['title'])

## use debugger console to explore complex data!!!!

# access the article titles and description
for index,article in enumerate(content['articles']):
    print(article['title'])
    print(article['description'])
    if index>2:
        break
