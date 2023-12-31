from diba import *  # وارد کردن کلاس diba
import requests  # وارد کردن کتابخانه requests برای ارسال درخواست های HTTP
from bs4 import BeautifulSoup  # وارد کردن کتابخانه BeautifulSoup برای تجزیه و تحلیل اسناد HTML

db=diba()  # ایجاد یک نمونه از کلاس diba

# تابع برای دریافت خبرها از وبسایت website1
def website1(url):
    vlist=[]  # ایجاد یک لیست برای نگهداری خبرها
    try:
        response = requests.get(url)  # ارسال یک درخواست GET به URL و دریافت پاسخ
        soup = BeautifulSoup(response.text, 'html.parser')  # تجزیه و تحلیل اسناد HTML
        links = db.seletor()  # دریافت لینک ها از دیتابیس
        for link in soup.find_all('a', class_='class'):  # پیدا کردن تمام تگ های a با کلاس مشخص شده
            link = str(url) + str(link.get('href'))  # ایجاد یک لینک با اضافه کردن URL به href
            if link not in links:  # اگر لینک در لینک ها نبود
                vlist.append(link)  # اضافه کردن لینک به لیست
    except Exception as e:
        pass 
    vlist = list(set(vlist))  # حذف تکراری ها از لیست
    return vlist  # برگرداندن لیست

# تابع برای دریافت خبرها از وبسایت website2
def website2(url):
    vlist=[]  # ایجاد یک لیست برای نگهداری خبرها
    try:
        response = requests.get(url)  # ارسال یک درخواست GET به URL و دریافت پاسخ
        soup = BeautifulSoup(response.text, 'html.parser')  # تجزیه و تحلیل اسناد HTML
        links = db.seletor()  # دریافت لینک ها از دیتابیس
        for link in soup.find_all('a', class_='class'):  # پیدا کردن تمام تگ های a با کلاس مشخص شده
            link = link.get('href')  # دریافت مقدار href
            if link not in links:  # اگر لینک در لینک ها نبود
                vlist.append(link)  # اضافه کردن لینک به لیست
    except Exception as e:
        pass 
    vlist = list(set(vlist))  # حذف تکراری ها از لیست
    return vlist  # برگرداندن لیست

# تابع برای دریافت خبرها از وبسایت website3
def website3(url):
    vlist=[]  # ایجاد یک لیست برای نگهداری خبرها
    try:
        response = requests.get(url)  # ارسال یک درخواست GET به URL و دریافت پاسخ
        soup = BeautifulSoup(response.text, 'html.parser')  # تجزیه و تحلیل اسناد HTML
        links = db.seletor()  # دریافت لینک ها از دیتابیس
        for link in soup.find_all('a', class_='class'):  # پیدا کردن تمام تگ های a با کلاس مشخص شده
            link = link.get('href')  # دریافت مقدار href
            if link not in links:  # اگر لینک در لینک ها نبود
                vlist.append(link)  # اضافه کردن لینک به لیست
    except Exception as e:
        pass 
    vlist = list(set(vlist))  # حذف تکراری ها از لیست
    return vlist  # برگرداندن لیست

# تابع برای دریافت خبرها از وبسایت website4
def website4(url):
    vlist=[]  # ایجاد یک لیست برای نگهداری خبرها
    try:
        response = requests.get(url)  # ارسال یک درخواست GET به URL و دریافت پاسخ
        soup = BeautifulSoup(response.text, 'html.parser')  # تجزیه و تحلیل اسناد HTML
        links = db.seletor()  # دریافت لینک ها از دیتابیس
        for link in soup.find_all('a', class_='class'):  # پیدا کردن تمام تگ های a با کلاس مشخص شده
            link = link.get('href')  # دریافت مقدار href
            if link not in links:  # اگر لینک در لینک ها نبود
                vlist.append(link)  # اضافه کردن لینک به لیست
    except Exception as e:
        pass 
    vlist = list(set(vlist))  # حذف تکراری ها از لیست
    return vlist  # برگرداندن لیست
