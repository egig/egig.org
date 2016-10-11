Title: Frontend Development
Date: 2015-07-20 17:00
Author: egig
Category: Uncategorized
Slug: frontend-development
Status: published

Pernah satu ketika saya, atau juga anda mungkin, men-download template
website gratis, atau premium, template nya terdiri dari halaman html
statis, yang setiap halaman completely terpisah dari halaman lain. Jadi
setiap halaman punya konten yang berbeda tapi punya navigasi, header dan
footer yang sama, dan itu seperti(atau bisa saja memang) di hard-coded
semua. Bagaimana seseorang membuatnya ? ya, saya langsung terpikir
semacam static site generator, yang memang sekarang sudah banyak
tersedia di internet semisal Jekyll dan lainnya.

<!--more-->

Saya kebanyakan berurusan sama hal-hal backend php, jadi agak
ketinggalan tentang web tech, bahkan baru beberapa minggu kemarin saya
mendengar tentang EcmaScript6. Tapi sampai juga pada saat dimana saya
harus berurusan dengan hal tersebut. Untuk Hoby project saya,
Drafterbit, saya kepikiran bagaimana memisahkan concern antara
development interface dengan logic nya, untuk itu saya experimentally
memutuskan untuk membuat repositori terpisah untuk UI development-nya.

Awalnya saya terpikir untuk menggunakan assamble, static site generator
untuk nodejs, tetapi saya rasa saya ingin/harus melakukan sesuatu yang
lain: belajar hal baru tentang frontend development.

[]()

### Sass

Bagi yang belum tahu, Sass adalah CSS Preprocessor, jadi dengan CSS
Preprocessor ini, kita bisa membuat css dengan lebih terstruktur, jadi
kita bisa punya variable, nested selector dan sebagainya. Sebenarnya
sudah lama saya ingin belajar CSS Preprocessor, tapi belum juga sempat.
Pada saat ini saya belum tahu apakah Sass atau Less yang lebih baik
untuk saya, tapi sebagai pemula, saya percaya saja pada arikel ini:
<https://css-tricks.com/sass-vs-less/>

[]()

### Typescript or Cofeescript ? or just Javascript ?

Beberapa orang mengeluhkan struktur bahasa pemrograman Javascript yang
kurang baik, sehingga dibuatlah bahasa 'perantara' yang lebih
progammer-friendly, diantaranya yang saya tahu adalah Typescript dan
Cofeescript. Jadi mana yang harus kita gunakan ? keduanya tidak harus.
Personally saya lebih memilih menggunakan pure javascript malah. Jika
anda sehari-harinya di lingkungan Windows, maka anda mungkin ingin
menggunakan Typescript karena syntaknya yang hampir mirip Java/C\#.

[]()

### Nunjucks

Jadi bagaimana para template developer membuat halaman-halaman template
yang masing masing terpisah(tidak saling terkait) itu ? Pastinya harus
menggunakan templating system dan semacam generator. Template engine
untuk nodejs yang baru-baru ini saya tahu adalah Nunjucks. Nunjucks
adalah template engine hasil porting dari Jinja(template engine untuk
python) yang dibuat oleh komunitas mozilla. Dilihat dari dokumentasi
nya, saya rasa Nunjucks keren juga. Oh ya, syntak nya juga kurang lebih
mirip dengan Twig(Template engine untuk PHP).

[]()

### Gulp

Beberapa waktu lalu saya sempat mempelajari Grunt dan menggunakannya di
salah satu project. Tidak berbeda dengan pendahulunya, Grunt, Gulp juga
adalah automation tool, tapi, menurut saya, sedikit lebih keren.
Syntaknya lebih simple. Dengan Gulp inilah kita, sebagai frontend
developer bekerja: meng-compile scss menjadi css, Typescript jadi
javascript, generate template dan sebagainya.

Demikian, Sass, pure js, Nunjucks dan Gulp adalah tools yang saya
gunakan untuk frontend development saya. Tulisan ini sebagai catatan dan
kesenangan pribadi saja, mudah-mudahan setidaknya memberi
keyword-keyword baru untuk selanjutnya pembaca gali kembali.
Terimakasih.
