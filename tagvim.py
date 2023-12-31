from KEY import *  # وارد کردن کلاس KEY
from diba import *  # وارد کردن کلاس diba
from telegram import Bot, InputFile  # وارد کردن کلاس های Bot و InputFile از کتابخانه telegram
import datetime  # وارد کردن کتابخانه datetime برای کار با تاریخ و زمان
from weather import *  # وارد کردن کلاس weather
import pyshorteners  # وارد کردن کتابخانه pyshorteners برای کوتاه کردن لینک ها

# تعریف کلاس tagvim
class tagvim:
    def __init__(self):
        self.key = tbKey  # کلید ربات تلگرام
        self.channel = '@channel_name'  # نام کانال تلگرام
        self.bot = Bot(token=self.key)  # ایجاد یک ربات تلگرام با استفاده از کلید
        self.db=diba()  # ایجاد یک نمونه از کلاس diba
        self.pysh = pyshorteners.Shortener()  # ایجاد یک کوتاه کننده لینک
        self.image=self.pysh.tinyurl.short('image_web_link')  # کوتاه کردن لینک تصویر

    # تابع برای ارسال پیام
    def sendF(self):
        now = datetime.datetime.now()  # دریافت زمان کنونی
        current_time = datetime.datetime.now()  # دریافت زمان کنونی
        time_str = now.strftime("%H:%M")  # تبدیل زمان به رشته
        date_str = now.strftime("%Y-%m-%d")  # تبدیل تاریخ به رشته
        w1=weather(city=f"تبریز")  # دریافت آب و هوای تبریز
        w2=weather(city=f"تهران")  # دریافت آب و هوای تهران
        w3=weather(city=f"مشهد")  # دریافت آب و هوای مشهد
        w4=weather(city=f"ساری")  # دریافت آب و هوای ساری
        w5=weather(city=f"رشت")  # دریافت آب و هوای رشت
        # ایجاد یک رشته برای ارسال به تلگرام
        caption = f"{self.image}\nDate : {date_str}\nTime : {time_str}\n{w1}\n{w2}\n{w3}\n{w4}\n{w5}\n"
        print("Tagvim      "+str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute))  # چاپ زمان کنونی
        url = f'https://api.telegram.org/bot{self.key}/sendMessage'  # ایجاد یک درخواست برای ارسال پیام در تلگرام
        params = {'chat_id': self.channel, 'text': caption}  # پارامترهای درخواست
        response = requests.post(url, params=params)  # ارسال درخواست
