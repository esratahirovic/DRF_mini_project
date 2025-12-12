TEKNİK MİMARİ DOKÜMANI — Mini Udemy + Mini Uber + JWT Auth Sistemi 

Geliştirme Ortamı 

Proje Ubuntu Linux üzerinde geliştirilmiştir. Belirtilen kurulum komutları Linux işletim sistemi uyumludur. 

Teknolojiler: 

Python 3.12 

Django + Django REST Framework 

SimpleJWT (Bearer Token Authentication) 

SQLite (demo amaçlı) 

Postman (API testleri) 

venv (sanal ortam) 

Kurulum Komutları 

Sanal ortam: 

python3 -m venv venv 
source venv/bin/activate 

Migrasyonlar: 

python manage.py makemigrations 
python manage.py migrate 

Mock veri üretimi: 

python mock/generate_mockdata.py 

Sunucuyu başlatma: 

python manage.py runserver 

Kullanılan Yapılar ve Nedenleri 

DRF → Hızlı ve modüler REST API geliştirme. 

SimpleJWT → Stateless, güvenli token tabanlı kimlik doğrulama. 

SQLite → Demo için hızlı ve sıfır kurulumlu veritabanı. 

Faker → Eğitmen, kullanıcı ve kurslar için sahte veri oluşturma. 

Rol Modeli 

Kullanıcı modeli genişletilerek 3 rol tanımlanmıştır: 

user: kurs satın alma, canlı ders talebi 

instructor: atanmış canlı dersleri görüntüleme 

admin: sistem yönetimi 

JWT ile tüm isteklerde kimlik doğrulama yapılır. 

Mini Udemy Sistemi (Kurs Satın Alma Akışı) 

Modeller: 

Course: başlık, açıklama, eğitmen, fiyat 

Purchase: kullanıcı, kurs, ödeme ID, durum, timestamp 

Akış: 

Kullanıcı JWT ile giriş yapar. 

/courses/purchase/ üzerinden course_id gönderilir. 

Mock ödeme servisi çalışır. 

Ödeme başarılı → Purchase kaydı oluşur. 

Kullanıcı satın aldığı kursları /courses/purchases/ ile görüntüler. 

Mini Uber Mantığı (Canlı Ders Eşleştirme) 

Model: LiveLessonRequest (öğrenci, eğitmen, durum) 

Eşleştirme: 
Basit algoritma ile ilk uygun eğitmen seçilir. 

Akış: 

Öğrenci /courses/live/request/ çağırır. 

Sistem eğitmen atar. 

Bildirim simülasyonu yapılır. 

Eğitmen /courses/live/instructor/ ile atamaları görür. 

Güvenlik ve Kimlik Doğrulama 

Tüm korumalı endpointler JWT Token gerektirir. 

request.user, token içeriğine göre otomatik belirlenir. 

Rol tabanlı erişim kontrolü view seviyesinde uygulanır. 
