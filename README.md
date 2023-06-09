# آموزش راه اندازی رزبری پای پیکو ( Run raspberry pi pico )

سلام به همه توسعه دهندگان  
اگر به عنوان مقدمه بخواهم بیان کنم بنیاد رزبری پای مدل‌های کوچکی از برد توسعه خود به نام rasberry pi pico و rasberry pi pico w را ارائه داده است که مدل w دارای ماژول وای فای می‌باشد و همچنین برخلاف باقی رزبری پای‌ها قابلیت نصب سیستم عامل را ندارند و مشابه میکروکنترلر‌ها بر پایه تراشه RP2040 عمل می‌کنند. زبان برنامه نویسی که برای این نوع از بردها می‌توان استفاده کرد میکروپایتون و سی می‌باشد.

# معرفی پایه‌های رزبری پای

برای آشنا شدن با پایه‌های رزبری پای پیکو می‌توانید از عکس زیر استفاده کنید:

![alt text](https://raw.githubusercontent.com/afshinnasiri/Run_rasberry_pi_pico/main/raspberry-pi-pico-gpio-1024x600.png)


# راه اندازی و نصب میکروپایتون

ابتدا باید امکان شناسایی رزربری پای را برای ویندوز فراهم کنیم. در لینوکس معمولا مشکلی وجود ندارد و به همین خاطر در ویندوز ممکن است مشکل شناسایی به خصوص در ویندوز 7 پیش بیاد که باید امکان شناسایی رو فراهم کنیم. اصطلاحا می‌توانیم با وصل کردن میکرو usb به برد و اتصال به لپ تاپ و ... با پورت مجازی که به وجود خواهد آمد برنامه‌نویسی را انجام دهیم. ما باید برای پردازش کدها توسط چیپ آرم موجود در رزبری پای میکروپایتون را نصب کنیم. ابتدا وارد سایت‌های زیر می‌شویم (متناسب با مدل رزبری پای خود) و آخرین ورژن میکروپایتون با پسوند uf2 را از بخش Firmware و nightly builds دانلود می‌کنید و در سیستم خود ذخیره نگه می‌دارید که در ادامه به آن نیاز دارید و با فلش کردن از طریق بوت لودر UF2 میکروپایتون را نصب می‌کنید:
```
1. https://micropython.org/download/rp2-pico/
2. https://micropython.org/download/rp2-pico-w/
```

بعد از انجام مرحله بالا به سراغ برد بروید و ابتدا دکمه BOOTSEL را نگه دارید. سپس در حین نگه داشتن دکمه برد را با کابل usb به سیستم خود متصل کنید و دکمه را رها کنید. بعد از انجام اینکار اگر در my computer مشاهده کنید شبیه فلش مموری با اسم RPI-RP2 درایوی ساخته خواهد شد که فایل که از لینک قبل دانلود کردید در این داریو قرار دهید. بعد از انجام اینکار برد شما بوت و ریست می‌شود و کار تمام است میکروپایتون نصب شد! برد خود را همچنان به سیستم متصل نگه دارید چون حالا نوبت کدنویسی است.

# نحوه آپلود کدها روی برد و کدنویسی

بسیار عالی. حالا نوبت کدنویسی و اجرا پروژه‌ها است. برای کدنویسی نیاز به یک Python IDE دارید که نرم‌افزار Thonny برای اینکار مناسب است. از لینک زیر دانلود کنید و نصب کنید و ادامه مراحل را پیش بروید:
```
https://thonny.org/
```
بعداز نصب نرم افزار فوق، آن را اجرا کنید. از بخش پایین نرم‌افزار با پورت مجازی ایجاد شده می‌توانید برد خود را برای آپلود کد انتخاب کنید:
![alt text](https://raw.githubusercontent.com/afshinnasiri/Run_rasberry_pi_pico/main/selecrpi.png)

خب حالا که برد را انتخاب کردید شروع می‌کنیم به تست برد که روی برد یک LED وجود دارد که پین آن GP25 می‌باشد. به همین خاطر کدهای زیر برای چشمک زدن آن را در محیط نرم‌افزار وارد کنید و دکمه سبز رنگ Run را بزنید تا کد روی برد اجرا شود اجرا می‌کنیم:

```
from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
```
اگر کد را بررسی کنیم، ماژولی به نام machine وجود دارد که توابع مخصوص سخت افزار درون آن قرار گرفته است. led یک شی یا آبجکت است که کلاس Pin پین 25 را خروجی تعریف کرده است. حال از ماژول کلاس Timer هم برای ایجاد یک پریود زمانی برای چشمک زدن led در شی timer که ایجاد شده است استفاده می‌شود.

# مثال چراغ چشمک زن

حال یک مثال ساده از ساخت یک چراغ چشمک زدن را خواهیم داشت:

![alt text](https://raw.githubusercontent.com/afshinnasiri/Run_rasberry_pi_pico/main/Raspberry-Pi-Pico-blink-led.jpg)

از یک led و مقاومت 220 اهم استفاده می‌کنیم و مدار را به شکل زیر می‌بندیم. پین 13 به عنوان خروجی برای اتصال به led در نظر گرفته می‌شود. کد ما به صورت زیر خواهد بود که یک مشابه قبل شی led را می‌سازیم و پین مربوطه را خروجی تعریف می‌کنیم و در نهایت با یک حلقه بی‌نهایت و تابع sleep زمان خاموش و روشن شدن آن را تنظیم می‌کنیم و سپس در نرم‌افزار کد را وارد کرده و دکمه run را بزنید:

```
import time
from machine import Pin
led=Pin(13,Pin.OUT)       

while True:
  led.value(1)            #on
  time.sleep(0.5)
  led.value(0)            #off
  time.sleep(0.5)
```

## نکته:
می‌توانید کدهای خود را با پسوند .py ذخیره کنید و در برد رزبری خود قرار دهید.

موفق باشید!

