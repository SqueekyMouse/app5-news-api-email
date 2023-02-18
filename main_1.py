import requests
from send_email import send_email
#commit: sent email with news titles and desc Sec27

topic='tesla'
api_key='277ead44cf2a4b6390bdf077aceeb055'
url=f'https://newsapi.org/v2/everything?q={topic}&'\
    'from=2023-01-18&sortBy=publishedAt&'\
    f'apiKey={api_key}&'\
    'language=en'

# make request
request=requests.get(url=url)

# get dict with data
content=request.json() # thi will get a dict if its json!!!
## use debugger console to explore complex data!!!!

msg_body='Subject: Todays News\n\n'
# msg_body=''
# access the article titles and description
for index,article in enumerate(content['articles']):
    if index>10:
        break
    # skip articles with title as None!!!
    if article['title'] is not None:
        msg_body=f"{msg_body}Title: {article['title']}\n"\
                f"Description: {article['description']}\n"\
                f"Link: {article['url']}\n\n"

# print(msg_body)
# encoding to fix error UnicodeEncodeError: 'ascii' codec can't encode character
msg_body=msg_body.encode('utf8')
send_email(message=msg_body)
