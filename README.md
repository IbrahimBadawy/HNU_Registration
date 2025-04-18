# ✅ README.md

## HNU_Registration — Helwan University Admission System

نظام تسجيل وتقديم إلكتروني لطلاب جامعة حلوان يشمل:

- تسجيل الطلاب (اسم، بريد، كلمة مرور)
- تعبئة استمارة بيانات تفصيلية (7 خطوات)
- رفع مستندات PDF أو صور
- تتبع حالة الطلب (قيد المراجعة، مقبول، مرفوض)
- دفع إلكتروني عبر رابط خارجي
- لوحة تحكم للأدمن:
  - عرض وقبول/رفض الطلبات
  - فلترة حسب الكلية أو الحالة
  - تصدير الطلبات Excel
  - توليد PDF للطلب
  - عرض تقارير إحصائية

## طريقة التشغيل

### 1. تشغيل Backend (Django)

```bash
cd helwan-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 2. تشغيل Frontend (Vue 3 + Vite)

```bash
cd frontend
npm install
npm run dev
```
