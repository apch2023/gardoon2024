# IRAJ MIRZAZADEH
# VERSION 1.0
# PYTHON 3
# 2023/12/31
# HAPPY NEW YEAR 2024
# https://github.com/apch2023/gardoon2024.git

# نصب کتابخانه های مورد نیاز
# pip install python-telegram-bot
# pip install pyshorteners
# pip install requests 
# pip install beautifulsoup4
# pip install tweepy

from telegram import Bot
from weather import *
from goldenEye import *
from tagvim import *
import pyshorteners
import time
from twiBot import *
from hashtag import *

class gardooneh:
    def __init__(self):
        # مقداردهی اولیه
        self.key = tbKey  # کلید ربات تلگرام
        self.channel = '@channel_name'  # نام کانال تلگرام
        self.bot = Bot(token=self.key)  # ایجاد یک ربات تلگرام با استفاده از کلید
        self.db = diba()  # ایجاد یک دیتابیس
        self.pysh = pyshorteners.Shortener()  # ایجاد یک کوتاه کننده لینک
        self.tw=TwitterBot(APIKEY, APIKeySecret)  # ایجاد یک ربات توییتر

    def sendNews(self):
        nlinks = set()  # ایجاد یک مجموعه برای نگهداری لینک ها
        nList = []  # ایجاد یک لیست برای نگهداری خبرها
        # دریافت خبرها از وبسایت های مختلف
        nList = website1("website1")  + website2('website2')   + website3('website3') +website4('website4')
        for news in nList:
            try:
                links = self.db.seletor()  # دریافت لینک ها از دیتابیس
                for i in range(0, len(links)):
                    nlinks.add(links[i][0])  # اضافه کردن لینک به مجموعه لینک ها
                if news not in nlinks:  # اگر خبر در لینک ها نبود
                    tweet=f'{news}\n\n{hashtag(news)}'  # ایجاد یک توییت با خبر و هشتگ آن
                    try:
                        self.tw.send_tweet(tweet)  # ارسال توییت
                    except Exception as e:
                        pass

                    url = f'https://api.telegram.org/bot{self.key}/sendMessage'  # ایجاد یک درخواست برای ارسال پیام در تلگرام
                    params = {'chat_id': self.channel, 'text': self.pysh.tinyurl.short(news)}  # پارامترهای درخواست
                    response = requests.post(url, params=params)  # ارسال درخواست

                    self.db.inserter(news)  # اضافه کردن خبر به دیتابیس
                    
                    # چاپ نام وبسایت و زمان دریافت خبر
                    if "website1" in news:
                        print("website1   "+str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute))
                    elif "website2" in news:
                        print("website2      "+str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute))
                    elif "website3" in news:
                        print("website3     "+str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute))
                    elif "website4" in news:
                        print("website4 "+str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute))
                    else:
                        pass
                    time.sleep(60)  # مکث برای 60 ثانیه
                else:
                    pass

            except Exception as e:
                pass


if __name__ == "__main__":
    print('START       '+str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute))

    g = gardooneh()  # ایجاد یک نمونه از کلاس gardooneh
    t = tagvim()  # ایجاد یک نمونه از کلاس tagvim

    try:
        t.sendF()  # ارسال پیام
    except Exception as e:
        pass

    while True:
        try:
            g.sendNews()  # ارسال خبرها
        except Exception as e:
            pass
