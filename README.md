# TOKOWEE 🏪
## We always do and do things for you!
🔗🔗🔗Link to Toko Wee --> [Toko Wee](http://arzaka-raffan-tokowee.pbp.cs.ui.ac.id/)

Nama: Arzaka Raffan Mawardi
NPM: 2306152393
Kelas: PBP-D

### Tugas 2 PBP 2024/2025
---

### Pengimplementasian💡

### Membuat Sebuah Proyek Django Baru
- Pastikan Django sudah ter-install, lalu buat sebuah direktori lokal baru dengan nama yang sesuai dengan nama E-Commerce pilihan. Selanjutnya, pada direktori tersebut aktifkan virtual environment dan inisiasi projek baru Django dengan perintah django-admin startproject [nama_proyek]

### Membuat aplikasi dengan nama main pada proyek tersebut.
- Jalankan perintah python manage.py startapp main agar dapat membentuk sebuah direktori main di dalam folder proyek yang akan berisi fondasi proyek tersebut.

### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Dalam direktori [nama proyek], buka berakas urls.py lalu arahkan tampilan proyek ke direktori main dengan menggunakan variabel urlpatters.

### Membuat model pada aplikasi main dengan nama Product dan beberapa atribut wajib
- Buat sebuah class atau model di dalam models.py dalam direktori main dan isi class tersebut dengan atribut-atribut seperti nama item, deskripsi, harga, stok, dan kategori.

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi.
- dalam views.py, terdapat fungsi show_main yang akan dipanggil pada urls.py. Fungsinya adalah untuk melakukan request dan me-render template HTML yang nantinya akan menampilkan hal-hal seperti nama toko, harga barang, dan lain-lain

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
- Buat file urls.py di dalam direktori main, lalu petakan tampilan mana dari direktori main yang ingin ditampilkan dengan memanfaatkan fungsi show_main yang diimpor dari file views.py. Selanjutnya request dan render akan dilanjutkan di views.py

### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat
- Lakukan deployment ke dalam Pacil Web Service (PWS) dengan membuat proyek baru dalam PWS lalu tambahkan ALLOWED_HOST dalam file settings.py dengan URL Deployment PWS dan melakukan push ke PWS sehingga URL dapat diakses secara publik

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

### Jelaskan fungsi git dalam pengembangan perangkat lunak!
- Git merupakan sebuah alat software development yang memiliki fungsi sebagai sistem kontrol versi (version control system). Git dapat melacak perubahan, menyimpan, dan mengelola berbagai source code. Karena keunggulannya, Git menjadi media pilihan utama developer dalam berkolaborasi dalam pengembangan perangkat lunak.

### Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Framework Django seringkali dijadikan bahan pembelajaran pengembangan perangkat lunak karena beginner friendly, yakni mudah dipahami, dan juga mudah dipelajari. Struktur Model-View-Template (MVT) yang dipakai oleh Django menyajikan struktur yang terorganisir dan pemisahan yang jelas antar kepentingan sehingga banyak disukai oleh banyak orang. Dokumentasi yang lengkap serta komunitas yang aktif juga menjadi nilai plus bagi Django.

### Mengapa model pada Django disebut sebagai ORM?
- Model pada Django disebut sebagai Object Relational Mapping (ORM) adalah karena Django memetakan model-model python ke dalam tabel-tabel dalam database. Hal ini dapat memudahkan developer untuk mengakses dan memanipulasi data sehingga mempercepat proses pengembangan perangkat lunak.
