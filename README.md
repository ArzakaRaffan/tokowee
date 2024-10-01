# TOKOWEE 🏪
## We always do and do things for you!
🔗🔗🔗Link to Toko Wee --> [Toko Wee](http://arzaka-raffan-tokowee.pbp.cs.ui.ac.id/)

## Tugas 4 PBP 2024/2025

## Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
Perbedaan `HttpResponseRedirect()` dan `redirect()` terletak pada jenis pengembalian (_redirect_)-nya. `HttpResponseRedirect()` hanya dapat mengantarkan client ke url tertentu sementara fungsi `redirect()` merupakan fungsi yang lebih fleksibel karena argumen yang diterima bisa berbentuk `models`, `view`, atau `url` sehingga fungsi ini mudah digunakan dan lebih banyak digunakan dibanding `HttpResponseRedirect()`.

## Jelaskan cara kerja penghubungan model `Product` dengan `User`
Penghubungan antara model `Product` dan `User` dilakukan di model class `Product` dimana akan di-import `User` dari django dan selanjutnya user tersebut akan diberikan sebuah foreign key untuk dapat meng-_assign_ suatu produk menjadi milik user setiap kali user melakukan login. 
Berikut adalah cara pengimplementasiannya:
``` python
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication dan authorization dalam Django memiliki beberapa perbedaan. Authentication mengatur masalah verifikasi data _credential_ yang dimiliki oleh user. Authentication akan memverifikasi apakah username dan password yang diinput saat login sesuai atau tidak dengan yang dimiliki di database. Jika sesuai maka pengguna akan diautentikasi. Untuk Authorization, maksudnya adalah pemberian akses kepada pengguna yang sudah login. Saat user login dan ingin mengakses sebuah data, maka akan dilakukan authorization mengenai izin yang sesuai. Jika user diberikan izin untuk mengakses, maka data dapat diakses. Dalam Django, fitur authentication disediakan oleh Django dalam bentuk model `User` dan `AuthenticationForm` serta diatur oleh `AuthenticationMiddleware`. Sedangkan authorization, Django mengaturnya dalam sistem izin dan juga group-group. Contoh authorization adalah decorator @login_required yang mengatur sebuah fungsi dapat dijalankan ketika user sudah login saja (akses terbatas).

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Setelah user melakukan login dan berhasil memverifikasi kredensial mereka, Django akan membuat _session_ untuk pengguna tersebut. _Session_ berguna untuk menyimpan informasi-informasi selama sesi login dari User. Session ini dipetakan kepada pengguna melalui ID unik yang disimpan di cookie pada browser pengguna. Setiap user melakukan permintaan atau _request_, session ID akan dikirimkan kembali ke server melalui cookie. Cookie berguna dalam penyimpanan data preferensi website dari pengguna, melacak aktivitas pengguna, dan juga menyimpan data sementara. Tidak semua cookies aman digunakan, beberapa cookies yang tidak diatur dengan benar akan berakibat fatal. Cookies yang tidak dienkripsi dapat dicuri oleh penjahat jika pengguna mengakses website dari url yang tidak aman (HTTP). Lalu terdapat cookies yang tidak di-set ke **secure** atau **HTTP-Only** yang dapat dengan mudah diserang dan dicuri.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Buat sebuah page untuk registrasi user   
Buat fungsi register dengan memanfaatkan `UserCreationForm` yang sudah disediakan oleh django. Dalam `views.py`, buat fungsi register yang meminta input yakni username dan password dalam bentuk form:
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully registered!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'create_account.html', context)
```
Lalu sambungkan dengan sebuah `.html` file sebagai templates atau tampilan kepada user. Jangan lupa untuk menambahkan url `/register` ke dalam `urls.py`:
```python
from main.views imoport register
urlpatterns = [
    ...
    path('register/', register, name='register'),
    ...
```

### Buat page untuk login User
dalam `views.py` import terlebih dahulu fungsi `AuthenticationForm` agar dapat menyocokkan data yang di-input dengan yang ada di database dan juga fungsi `login` dari library Django. Lalu buat fungsi `login_user` untuk dapat menerima dan menyocokkan data:
```python
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)
```
Sambungkan dengan file `.html` baru bernama `login.html` agar page login memiliki visual. Terakhir jangan lupa untuk import fungsi `login_user` ke `urls.py` agar dapat diakses via url yang dikehendaki

### Buat Fungsi Logout
Import fungsi logout dari library Django dan buat fungsi logout di `views.py`:
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Tambahkan url untuk logout ke `urls.py` agar dapat diakses dengan menjalankan fungsi `logout_user` di `views.py`, jangan lupa import fungsi tersebut dari `views.py`. Selanjutnya dalam `main.html`, sertakan sebuah button yang ketike ditekan akan menuju ke url yang sudah ditetapkan agar selanjutnya dapat menjalankan fungsi logout_user untuk me-_request_ logout.

### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Lakukan register, login, lalu lakukan pengisian data dari model-model yang telah dibuat

### Menghubungkan User dengan Model (Product)
Buat foreign key untuk user pada `models.py` agar dapat menghubungkan suatu produk dengan suatu User:
```python
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
...
```
Setiap User menambahkan item atau product pada akunnya, simpan informasi tersebut ke User yang berkaitan dengan mwngubah fungsi `create_product` yang terdapat pada `views.py`. Lalu, pada fungsi `show_main`, restriksi data dengan hanya menampilkan data yang dimiliki oleh user tersebut saja. Selanjutnya lakukan migrasi agar data ini dapat tersimpan dan siap untuk menampung data-data dan informasi pengguna maupun produk-produk di dalamnya.

### Membuat informasi last login dari cookies
Untuk membuat sebuah informasi last login, kita harus dapat menangkap waktu ketika user login. Maka dari itu, dibutuhkan import `time` dan juga `HttpResponsRedirect`. Setelah itu, set sebuah catatan ketika user log in dengan menambahkan hal berikut pada login_user:
```python
...
if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
...
```
Agar dapat dipakai dan ditampilkan ke `main.html`, informasi mengenai last login ini harus ditambahkan ke `context` di dalam fungsi `show_main`:
```python
def show_main(request):
...
context = {
...
'last_login': request.COOKIES['last_login'],
...
}
```

setelah menambahkan cookies, jangan lupa untuk menghapus informasi last login ini ketika user logout, lalu selanjutnya tampilkan informasi ini pada `main.html`

# Archive Tugas 📚
---

## Tugas 3 PBP 2024/2025 📖📖📖 

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam pengembangan sebuah platform, data delivery sangat diperlukan karena data delivery bertanggung jawab dalam pengiriman, penerimaan, dan pengelolaan data. Sistem data delivery ini juga merupakan sistem yang sangat efisien dan cepat dalam konteks pengelolaan data sehingga sangat diperlukan. Tanpa adanya sistem data delivery, pengguna tidak akan bisa merasakan pengelolaan data dalam platform yang aman, efisien, dan juga cepat.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, jenis penyajian data yang lebih baik adalah JSON. Hal ini dikarenakan JSON menyajikan data dengan lebih manusiawi (_readable_). Dalam pemrosesan data,JSON juga memiliki efisiensi yang lebih baik dibandingkan dengan XML. Selanjutnya, JSON memiliki ukuran data yang lebih kecil sehingga penyajiannya dapat dilakukan dengan cepat dan juga tepat. XML sebenarnya tidak seburuk itu, namun penyajiannya lebih lambat dibanding JSON karena ukuran datanya yang lebih besar.
JSON lebih populer dibanding XML juga didukung oleh alasan-alasan di atas. Selain itu, banyak pengembang perangkat lunak yang mem-_build website_-nya dengan menggunakan JavaScript dimana JSON sudah secara alami terintegrasi dengan JSON.

## Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Jika dilakukan _ctrl + click_ pada method `is_valid()`, hal berikutlah yang muncul:
```python
   def is_valid(self):
        """Return True if the form has no errors, or False otherwise."""
        return self.is_bound and not self.errors
```
method is_valid() memeriksa apakah form yang di-_submit_ merupakan data yang valid atau tidak. Method ini akan mengembalikan _boolean True_ apabila form tidak terdapat data yang error, dapat dilihat dari bagian `return self.isbound and not self.errors`. Sehingga pemrosesan data pada projek dapat berjalan secara lancar dan tidak ada data-data yang menyebabkan projek error. Hasil validasi ini selanjutnya akan diproses untuk diolah kembali dalam proses selanjutnya.

## Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` dalam Django merupakan sebuah token unik dan berfungsi dalam keamanan yang di-_generate_ oleh server dan ada di setiap form yang menggunakan metode POST. Setiap kali form dikirimkan, Django akan meng-_cross-check_ apakah token yang di-_request_ sesuai dengan yang dimiliki oleh pengguna. Jika tidak menambahkan `csrf_token`, app atau web jadi mudah diserang dimana penyerang dapat melakukan _request_ palsu atas nama pengguna. Jika kejadian tersebut terjadi, server dapat mengikuti perintah-perintah yang dilakukan oleh penyerang atas nama pengguna dan melakukan hal-hal yang tidak bertanggung jawab pada data dan app atau website itu sendiri

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  ### 1. Menambahkan kerangka _default_ views
  Membuat sebuah default views sebagai kerangka yang akan digunakan oleh setiap halaman website yang lainnya dengan membuat `base.html` di direktori utama dan mendaftarkannya ke dalam `settings.py`. Jangan lupa, untuk setiap berkas `.html` di baris paling atasnya akan meng-_extend_ `base.html` tersebut dengan menggunakan kode: ` {% extends 'base.html' %}`\
  ### 2. Membuat form input sehingga bisa ditampilkan
  Buat berkas baru dalam aplikasi _main_ untuk dapat menginput _form_, yakni `forms.py`. Form ini dapat menerima input dan juga membuat product baru lengkap dengan atribut-atribut yang sudah ditentukan. Jangan lupa meng-_import_ kelas Product dari `models.py` Berikut adalah isi dari `forms.py`: 
  ```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['itemName', 'itemDescription', 'itemPrice', 'itemStock', 'itemCategory', 'itemImageURL']
  ```
  fields berisi atribut-atribut yang dimiliki oleh class Product, contohnya yakni itemName, itemDescription, dan lain-lain\
  Selanjutnya dalam `views.py`, buat sebuah fungsi yang menerima parameter _request_ sehingga dapat menambahkan data Product\
  ```python
  def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)
  ```
  Update fungsi `show_main` terutama di bagian `context` agar dapat menyambungkan `views.py` dengan `models.py` menjadi:
  ```python
  def show_main(request):
    products =  Product.objects.all()
    context = {
        'products': products
            }

    return render(request, "main.html", context)
  ```
  `Product.object.all()` digunakan untuk mengambil semua `Product` yang terdapat dalam database. Sehingga data-data atau atribut-atribut yang dipunyai oleh class Product dapat digunakan di dalam berkas `.html`\
  Lalu, buat berkas `.html` baru yang fungsinya untuk menjadi _page_ pengisian data. Jangan lupa untuk menambahkan routing ke _file_ tersebut di dalam `urls.py` dalam direktori main. Selanjutnya, data siap untuk ditampilkan di dalam `main.html`.
  ### 3. Membuat sebuah penyajian data dalam bentuk XML dan juga JSON
  Pada `views.py`, import `HttpResponse` dan `serializers` agar bisa mengembalikan respons berupa data. Lalu, buat beberapa fungsi untuk menampilakn data dalam bentuk XML dan juga JSON.
  ```python
  def show_xml(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
  
  def show_json(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```
Selanjutnya, untuk dapat menyajikan data XML dan JSON berdasarkan ID datanya, dapat dibuat beberapa fungsi tambahan berikut:
  ```python
  def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

  def show_json_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```
Terakhir, buat routing dengan menambahkan path url ke dalam `urlpatterns` dalam `urls.py` agar dapat mengakses fungsi-fungsi yang sudah diimplementasikan di atas:
```python
  urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ...
    ]
```
## Mengakses keempat URL mnggunakan Postman
- XML
![image](https://github.com/user-attachments/assets/f0ed1cbf-ac8f-4ec4-a74a-ffcc887591ed)

- JSON
![image](https://github.com/user-attachments/assets/3fd15c18-0932-4be5-9e97-fc57f832e2b0)

- XML by ID
![image](https://github.com/user-attachments/assets/fdff89e8-4eed-465d-905e-edfcb5a40957)

- JSON by ID
![image](https://github.com/user-attachments/assets/b47bec7a-73c8-48be-9b1b-11f53735257c)

---

## Tugas 2 PBP 2024/2025 📃
### Membuat Sebuah Proyek Django Baru 🤖
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

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html 🏢
![baganPBP](https://github.com/user-attachments/assets/edf17d58-cdc7-42d2-a205-bb5dd7c60b77)

### Jelaskan fungsi git dalam pengembangan perangkat lunak!💪
- Git merupakan sebuah alat software development yang memiliki fungsi sebagai sistem kontrol versi (version control system). Git dapat melacak perubahan, menyimpan, dan mengelola berbagai source code. Karena keunggulannya, Git menjadi media pilihan utama developer dalam berkolaborasi dalam pengembangan perangkat lunak.

### Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? ⛅
- Framework Django seringkali dijadikan bahan pembelajaran pengembangan perangkat lunak karena beginner friendly, yakni mudah dipahami, dan juga mudah dipelajari. Struktur Model-View-Template (MVT) yang dipakai oleh Django menyajikan struktur yang terorganisir dan pemisahan yang jelas antar kepentingan sehingga banyak disukai oleh banyak orang. Dokumentasi yang lengkap serta komunitas yang aktif juga menjadi nilai plus bagi Django.

### Mengapa model pada Django disebut sebagai ORM? 🥼
- Model pada Django disebut sebagai Object Relational Mapping (ORM) adalah karena Django memetakan model-model python ke dalam tabel-tabel dalam database. Hal ini dapat memudahkan developer untuk mengakses dan memanipulasi data sehingga mempercepat proses pengembangan perangkat lunak.

---

Nama: Arzaka Raffan Mawardi\
NPM: 2306152393\
Kelas: PBP-D
