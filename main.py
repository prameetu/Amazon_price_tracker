from bs4 import BeautifulSoup
import requests
import smtplib
import time


prices_list = []

def check_price():

    url = "https://www.amazon.in/Huami-Amazfit-Smart-Watch-Obsidian/dp/B07XLMY2HW/ref=sxin_9?ascsubtag=amzn1.osa.a87f6de8-839e-4bf7-a9de-71923400a7ae.A21TJRUUN4KGV.en_IN&creativeASIN=B07XLMY2HW&cv_ct_cx=mens+smart+watch&cv_ct_id=amzn1.osa.a87f6de8-839e-4bf7-a9de-71923400a7ae.A21TJRUUN4KGV.en_IN&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-gl-ranking&dchild=1&keywords=mens+smart+watch&linkCode=oas&pd_rd_i=B07XLMY2HW&pd_rd_r=c7cf74f8-7a05-4a3f-99c1-606e48ed46dd&pd_rd_w=AkLjk&pd_rd_wg=EVSjI&pf_rd_p=9711564d-930f-42d4-810f-a6eff7a95d66&pf_rd_r=2MAJJSSCX5EAA9P1CY4A&qid=1611472507&sr=1-2-5b72de9d-29e4-4d53-b588-61ea05f598f4&tag=timessyndicat-21"
    browser_agent = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

    product_page = requests.get(url,headers=browser_agent)

    soup = BeautifulSoup(product_page.content,"html.parser")
    #print(soup)

    page_title = soup.find(id = "productTitle").get_text()
    product_price = soup.find(id = "priceblock_dealprice").get_text()[2:7]
    product_price = product_price.replace(',', '')
    prices_list.append(int(product_price))
    return product_price

def send_email(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    password = input("Enter the password")
    server.login("prameetupadhyay@gmail.com",password)
    server.sendmail('prameetupadhyay@gmail.com','prameetu20@gmail.com',msg)

def price_decrease_check(price_list):
    if prices_list[-1] < prices_list[-2]:
        return True
    else:
        return False


count = 1

while True:
    current_price = check_price()
    if count > 1:
        flag = price_decrease_check(prices_list)
        if flag:
            decrease = prices_list[-1] - prices_list[-2]
            msg = f'The price of the item has decreased by {decrease} rupees>'
            send_email(msg)
    time.sleep(43200)
    count += 1