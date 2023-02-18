import requests
from send_email import send_email
from datetime import datetime
#commit: date topic lang to url and conn err safe Sec28

date=datetime.now()

topic='tesla'
fdate=date.strftime('%Y-%m-%d')
api_key='277ead44cf2a4b6390bdf077aceeb055'

url='https://newsapi.orgi/v2/everything?'\
    f'q={topic}&from={fdate}&sortBy=publishedAt&'\
    f'apiKey={api_key}&'\
    'language=en'

# make request
try:
    request=requests.get(url=url)
# except Exception as e:
#     print(f'Error establishing conn to url:\n{url}\n\nException: {e}')
#     exit()
except:
    print(f'Error establishing conn to url:\n{url}')
    exit()

# get dict with data
content=request.json() # this will get a dict if its json!!!
## use debugger console to explore complex data!!!!

msg_body='Subject: Todays News\n'
# access the article titles and description, limit to 10
for article in content['articles'][:10]:
    # skip articles with title as None!!!
    if article['title'] is not None:
        msg_body=f"{msg_body}Title: {article['title']}\n"\
                f"Description: {article['description']}\n"\
                f"Link: {article['url']}\n\n"

# print(msg_body)
# encoding to fix error UnicodeEncodeError: 'ascii' codec can't encode character
msg_body=msg_body.encode('utf8')
if send_email(message=msg_body):
    print('Successfully sent mail!!!')
else:
    print("Mail failed!!!!")
