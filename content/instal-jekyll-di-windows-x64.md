Title: Instal Jekyll Di Windows x64
Date: 2013-10-05 17:00
Author: egig
Category: Uncategorized
Slug: instal-jekyll-di-windows-x64
Status: published

> Update: There is more sophisticated article:  
>   
>   
> http://jekyll-windows.juthilo.com/

Seperti yang ikut-ikutan yah, instal Jekyll segala,  
padahal kan wordpress atau blogger juga ada, lebih gampang  
dan gratis juga. Ikut-ikutan di bidang teknologi itu harus  
kayaknya, se-enggaknya menurut saya. Kalo 'nggak gitu ya  
ketinggalan nantinya. Di samping itu, ini kan hobi saya,  
something new is something that must be fun. jadi inilah pengalaman
saya.

<!--more-->

[]()

### Cara Install Jekyll di Windows

Laptop saya ini pake windows 64 bit. Saya kira nggak bakal jauh  
beda sama yang 32 bit. Dari [jekyllrb.com](http://jekyllrb.com) :

> Jekyll is a simple, blog-aware, static site generator. It takes a
> template directory containing raw text files in various formats, runs
> it through Markdown (or Textile) and Liquid converters, and spits out
> a complete, ready-to-publish static website suitable for serving with
> your favorite web server.

Jadi, waktu itu saya pikir saya harus punya ruby di laptop saya. Dan
memang sudah.  
Instal ruby kayak instal software biasanya. Download di
<http://rubyinstaller.org/downloads/>  
terus tinggal `Double klik` dah itu instalan, laptop saya 64 bit, jadi
saya sebelumnya pilih yang Ruby 2.0.0-p247 (x64).  
Untuk windows yang 32 bit, jodohnya Ruby 2.0.0-p247 aja.

Setelah itu saya langsung install Jekyll dengan kode : (sok tahu banget)

    ~$ gem install jekyll

Tapi dapet error, errornya lupa saya nggag printscreen pokoknya isinya  
bilang kalo saya harus install DevKit buat ruby. Nah, temen-temen  
bisa download itu di <http://rubyinstaller.org/downloads/> juga.  
kalo yang 32 bit, pilih yang sebelumnya ada tulisan *For use with Ruby
2.0 (32bits version only):*

Setelah di Download, begini :

Double-klik file 7zip yang baru aja di download. Selanjutnya temen2 akan
diminta untuk pilih folder untuk extrak. Nah, **hati-hati !** soalnya
ini akan jadi instalasi permanen. Dan ribet lagi kalo mau dipindahin,
Jadi pilihlah folder yang tepat !.  
Setelah file selesai di ekstrak, ganti working direktori ke folder
tersebut, misal:

        ~$ cd DevKit

Jalankan perintah berikut

        ~$ ruby dk.rb init

Satu Lagi

        ~$ ruby dk.rb install

Setelah itu, baru temen2 bisa install Jekyll, prosessnya akan makan
waktu beberapa menit,  
apalagi kalo internetnya lemot. Langsung aja :

        ~$ gem install jekyll

Selesai !, Kalo semua langkah-langkah nya bener,  
harusnya temen2 udah bisa bikin aplikasi jekyll, misal :

    ~ $ gem install jekyll
    ~ $ jekyll new my-awesome-site
    ~ $ cd my-awesome-site
    ~/my-awesome-site $ jekyll serve

    # => Now browse to http://localhost:4000

Demikian. Jika ada pertanyaan, koreksi atau apapun, saya akan sangat
senang bila ada yang berkomentar.
