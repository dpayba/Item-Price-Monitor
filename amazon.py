import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = '*INSERT URL OF ITEM*'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:4])

    print(converted_price)
    print(title.strip())

    if(converted_price > 500):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YOUR EMAIL', 'ENTER_PASSWORD')

    subject = 'Price drop found'
    body = 'Check Amazon link *URL OF ITEM*'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'YOUR EMAIL',
        msg
    )
    print('Email Has Been Sent')

    server.quit()


while(True):
    check_price()
    time.sleep(86400)
