import requests  # وارد کردن کتابخانه requests برای ارسال درخواست های HTTP
import json  # وارد کردن کتابخانه json برای کار با اسناد JSON
from KEY import *  # وارد کردن کلاس KEY
import math  # وارد کردن کتابخانه math برای کار با عملیات ریاضی

# تابع برای تبدیل شرایط آب و هوایی به ایموجی
def weather_to_emoji(weather_condition):
    weather_emojis = {
        "Clear": "☀️🌗",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Snow": "❄️",
        "Thunderstorm": "⛈️",
        "Drizzle": "🌦️",
        "Mist": "🌫️",
        "Smoke": "💨",
        "Haze": "🌫️",
        "Dust": "💨",
        "Fog": "🌫️",
        "Sand": "💨",
        "Ash": "💨",
        "Squall": "🌬️",
        "Tornado": "🌪️"
    }

    emoji = weather_emojis.get(weather_condition)  # دریافت ایموجی مربوط به شرایط آب و هوایی
    return emoji  # برگرداندن ایموجی

# تابع برای دریافت آب و هوای یک شهر
def weather(city):
    try:
        url = f"https://api.codebazan.ir/weather/?city={city}"  # ایجاد یک URL برای دریافت آب و هوای شهر
        response = requests.get(url)  # ارسال یک درخواست GET به URL و دریافت پاسخ
        data = response.json()  # تبدیل پاسخ به JSON
        temperature=data['list'][0]['main']['temp']  # دریافت دما از داده ها
        wcon=data['list'][0]['weather'][0]['main']  # دریافت شرایط آب و هوایی از داده ها
        con = f"{city} دما {math.floor(temperature)}  {weather_to_emoji(wcon)}"  # ایجاد یک رشته با نام شهر، دما و ایموجی شرایط آب و هوایی
        return con  # برگرداندن رشته
    except Exception as e:
        return ""  # در صورت وجود خطا برگرداندن یک رشته خالی
