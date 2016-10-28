Title: Symfony, Mengenal Compiler Pass
Date: 2016-02-05 17:41
Author: egig
Category: Uncategorized
Slug: symfony-mengenal-compiler-pass
Status: draft

Ya, kita harus mengenal dulu apa itu service pada Symfony. Service bisa
dianalogikan sebagai librari php lainnya yang punya fungsi tertentu,
misal seperti Mailer atau Database library, namun diintegrasikan pada
symfony dengan cara tersendiri.

Katakan kita membuat suatu service pada file konfigurasi
`app/config/services.yml`, misal:

    twitter_api_client:
        class: ..

Pada penggunaannya, symfony akan membuat suatu container, dan
konfigurasi yml diatas akan di-compile ke dalam code php kurang lebih
sebagai berikut:

    $twitterApiClient = new...

See ? tampak seperti penggunaan OOP biasa.

Namun, bayangkan, ketika service diatas dibuat, misal kita ingin
melakukan sesuatu misal set api key sebelum service benar-benar siap
digunakan ?

\$twitterApiClient-setApiKey()

Maka disinilah compiler pass kita perlukan. Jadi, compiler pass adalah
semacam mekanisme untuk memanipulasi Container sebelum atau pada saat
di-compile.

Kode

Kita harus menambahkan compiler diatas pada saat 'build' container. Kita
bisa menambahkannya pada bundle.
