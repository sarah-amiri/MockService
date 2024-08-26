<p style="direction:rtl;text-align:justify;">
برنامه ی MockService تنها به منظور ایجاد داده ی mock ایجاد شده است. برای اجرای آن ابتدا پکیج های فایل requirements.txt را نصب و سپس برنامه را با دستور
</p>
<code>
uvicorn app.main:app –port 8000
</code>
<p style="direction:rtl;text-align:justify;">
اجرا کنید. بعد از اجرا از طریق آدرس <code>http://localhost:8000/docs</code> به صفحه ی سواگر برنامه دسترسی خواهید داشت.
</p><br>
<ol style="direction:rtl">
این برنامه شامل سه اندپوینت زیر است:
<li style="margin-bottom:15px;">
<b>/customers/</b>
<p style="text-align:justify;">لیستی از کد ملی های موجود در سیستم را به شما خواهد داد</p>
</li>
<li style="margin-bottom:15px;">
<b>/customers/{customer_id}/</b>
<p style="text-align:justify;">
با دادن customer_id (کد ملی) اطلاعات بیشتری از مشتری از جمله بانک هایی که مشتری در آن حساب دارد را به شما خواهد داد. اجرای این ریکوئست ممکن است تا ۴ ثانیه طول بکشد.
</p>
</li>
<li>
<b>/customers/{customer_id}/{bank_name}/transactions/</b>
<p style="text-align:justify;">
لیستی از تراکنش های مشتری در بانک مربوطه را به شما خواهد داد. ریسپانس این اندپوینت بصورت رندوم ۱ تا ۱۰ ثانیه طول خواهد کشید. همچنین گاهی ممکن است با خطای ۵۰۳ روبرو شوید که به معنی این است که سرویس موقتا در دسترس نمی باشد و باید دوباره تلاش کنید.
</p>
</li>
 </ol>
