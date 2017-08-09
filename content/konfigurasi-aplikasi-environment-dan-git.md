Title: File Konfigurasi dan Environment
Date: 2016-10-28 17:00
Tags: development
Slug: file-konfigurasi-dan-environment
Status: published
Author: egig

Bagi yang sedang belajar pengembangan aplikasi perangkat lunak terutama aplikasi berbasis web, penting untuk mengerti, lalu _care_ terhadap konfigurasi aplikasi. Apalagi sekarang sudah serba _cloud_, dan open, konfigurasi aplikasi harus diatur dengan hati-hati demi keamanan dan kemudahan pengembangan.

### File konfigurasi ?

Dikutip dari wikipedia:
> In computing, configuration files, or config files configure the parameters and initial settings for some computer program. The files are often human-editable plain text, and filename extensions of .ini, .cnf, .conf, .cfg, .cf and similar are often used.

Ya, file konfigurasi adalah file yang seringnya bisa di-edit oleh pengguna memberi informasi pada aplikasi, juga menginstrukrikan bagaimana aplikasi harus berjalan. Ekstensi file-nya bisa bermacam-macam, untuk bahasa pemrograman php, kita kenal dengan file konfigurasi 'php.ini', atau mysql dengan file 'my.cnf'.

### Kaitan dengan Environment ?

Setiap instalasi aplikasi harus punya Environment yang jelas. Environment, pada kasus kita, sederhananya adalah satu set tools termasuk sistem operasi dan machine/komputer dimana kita menjalankan dan atau mengembangkan aplikasi. Environment ini di identifikasi dengan nama. Nama Environment bisa apa saja disesuaikan dengan tujuannya, yang biasa digunakan adalah production, development, dan testing. nama environment lain yang sering terdengar ada local, staging, sandbox dan banyak lainnya.

Contoh, aplikasi yang sedang di-develop di pc kita, kita bisa menamai environment-nya sebagai 'development' atau 'local'.
Aplikasi yang digunakan oleh tester kita namai environment-nya sebagai "testing" atau "staging". Aplikasi yang terinstal live di-klien kita namai environment-nya sebagai 'production'.

Dalam pengembangan aplikasi sering kali kita menemukan konfigurasi yang dibedakan berdasarkan environment tersebut diatas. Dan setiap environment, mempunyai isi file konfigurasi yang berbeda-beda. Contoh yang sering kita temui dalam kehidupan sebagai pengembang aplikasi sehari-hari diantaranya adalah konfigurasi database.

Koneksi database pada Environment production sering kali berbeda dengan koneksi database pada development atau testing. Untuk itu kita harus punya file konfigurasi bebeda untuk tiap-tiap environment.

### Hal yang harus di perhatikan

Yang perlu di perhatikan adalah, sering kali kita sebagai programmer pemula tidak care tentang hal ini, dan punya satu file konfigurasi saja untuk semua environment. Ini adalah bad practice, karena secara tidak langsung menyebabkan pengembangan aplikasi menjadi tambah repot. Tiap programmer harus punya database dengan nama sama username dan password juga harus sama. Atau programer harus edit ulang file konfigurasi tersebut.

Kebiasaan tidak membedakan file konfigurasi juga dapat menyebabkan celah keamanan. Misalnya saja, ketika programmer mengembangkan aplikasi di komputer mereka, semua pesan error ditampilkan untuk memudahkan pengembangan. Tapi di production, pesan error harus disembunyikan karena bisa saja mengandung data data sensitif seperti username, password dan lainnya. Kebiasaan tidak membedakan file per-environment bisa dengan tidak sengaja menampilkan persan error pada environment production.

### Kesimpulan

File konfigurasi adalah file penting yang harus di-manage secara hati-hati. Jika kita sebagai programmer _care_ terhadap good practice, keamanan dan kelancaran pengembangan aplikasi, tentunya kita harus memahami dan _care_ terhadap hal file konfigurasi ini.

Referensi:

<https://en.wikipedia.org/wiki/Configuration_file>
