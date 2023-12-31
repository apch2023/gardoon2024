from collections import Counter  # وارد کردن کلاس Counter برای شمارش تکراری ها
import re  # وارد کردن کتابخانه re برای کار با عبارات منظم

# تابع برای پیدا کردن دو مورد پرتکرار در یک لیست
def most_frequent(lst):
    counter = Counter(lst)  # شمارش تعداد تکراری ها در لیست
    try:
        hashtags=[item for item, count in counter.most_common(2)]  # پیدا کردن دو مورد پرتکرار
        th=''  # ایجاد یک رشته خالی
        for items in hashtags:  # برای هر مورد در مورد های پرتکرار
            th+='#'+items+' '  # اضافه کردن مورد به رشته با یک هشتگ
        hashtags=th  # ذخیره رشته در متغیر hashtags
        return hashtags  # برگرداندن hashtags
    except Exception as e:
        return '#retweet'  # در صورت وجود خطا برگرداندن '#retweet'
    

# تابع برای ایجاد هشتگ از یک لینک
def hashtag(link):
    if 'website1' in link:  # اگر 'website1' در لینک بود
        link=link.replace('website1','')  # حذف 'website1' از لینک
    elif 'website1_sub' in link:  # اگر 'website1_sub' در لینک بود
        link=link.replace('website1_sub','')  # حذف 'website1_sub' از لینک
    elif 'website2' in link:  # اگر 'website2' در لینک بود
        link=link.replace('website2','')  # حذف 'website2' از لینک
    elif 'website2_sub' in link:  # اگر 'website2_sub' در لینک بود
        link=link.replace('website2_sub','')  # حذف 'website2_sub' از لینک
    elif 'website3' in link:  # اگر 'website3' در لینک بود
        link=link.replace('website3','')  # حذف 'website3' از لینک
    elif 'website4' in link:  # اگر 'website4' در لینک بود
        link=link.replace('website4','')  # حذف 'website4' از لینک
    link=re.sub('[0-9/\\-]', ' ', link)  # جایگزین کردن اعداد، خط فاصله و خط مایل با فاصله
    link=link.split(' ')  # تقسیم لینک به چندین قسمت با استفاده از فاصله
    link = [item for item in link if len(item)>=4]  # حذف کلمات کوتاه تر از 4 حرف
    return most_frequent(link)  # برگرداندن دو مورد پرتکرار
