import tweepy  # وارد کردن کتابخانه tweepy برای کار با توییتر
from KEY import *  # وارد کردن کلاس KEY
import datetime  # وارد کردن کتابخانه datetime برای کار با تاریخ و زمان

# تعریف کلاس TwitterBot
class TwitterBot:
    def __init__(self, APIKEY, APIKeySecret):
        auth = tweepy.OAuth2AppHandler(APIKEY, APIKeySecret)  # ایجاد یک نمونه از کلاس OAuth2AppHandler با استفاده از کلید API و رمز کلید API
        self.client = tweepy.Client(BerearToken,APIKEY,APIKeySecret,AccessToken,AccessTokenSecret)  # ایجاد یک نمونه از کلاس Client با استفاده از توکن Berear، کلید API، رمز کلید API، توکن دسترسی و رمز توکن دسترسی

    # تابع برای ارسال توییت
    def send_tweet(self, text):
        self.client.create_tweet(text=text)  # ایجاد یک توییت با متن مشخص شده
        print("Tweet       "+str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute))  # چاپ زمان کنونی
