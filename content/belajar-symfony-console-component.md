Title: Belajar Symfony Console Component
Date: 2016-05-24 16:55
Author: egig
Category: Uncategorized
Tags: symfony
Slug: belajar-symfony-console-component
Status: published

> Untuk memudahkan, kita harus sudah paham dulu penggunaan Composer dan
> konsep autoload-nya composer.

Symfony Console Component adalah component atau library dari symfony
yang bisa kita gunakan untuk memudahkan pembuatan program CLI (Command
Line Interface) menggunakan PHP. Untuk lebih lengkapnya silahkan merujuk
pada
<http://symfony.com/doc/current/components/console/introduction.html>

Membuat Program Sederhana

1\. Buka Terminal/CMD  
2. Buat folder project, untuk kali ini kita beri nama
symfony-console-quickstart

    mkdir symfony-console-quickstart
    cd symfony-console-quickstart

3\. Install dependensi yang di butuhkan

    composer require symfony/console

Perintah diatas akan mendownload dependensi (Symfony Console Component)
ke dalam folder vendor dan mencatatnya di file composer.json.
(Perhatikan ada folder baru vendor dan file baru composer.json dan
composer.lock setelah menjalankan command diatas)

4\. Buat file php untuk program yang akan kita buat, misal kita beri nama
`console.php`.

Paste-kan kode program berikut:


    #!/usr/bin/env php
    run();

5\. Sekarang, program CLI sudah bisa kita jalankan

    php console.php

output:

    Console Tool

    Usage:
      command [options] [arguments]

    Options:
      -h, --help            Display this help message
      -q, --quiet           Do not output any message
      -V, --version         Display this application version
          --ansi            Force ANSI output
          --no-ansi         Disable ANSI output
      -n, --no-interaction  Do not ask any interactive question
      -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output,
     2 for more verbose output and 3 for debug

    Available commands:
      help  Displays help for a command
      list  Lists commands

Jika dilihat dari output di atas di bagian "Available commands", command
atau perintah yang tersedia baru ada "help" dan "list" artinya kita
masih belum bisa berbuat banyak selain menampilkan bantuan (help) dan
dafter perintah yang tersedia (list).

Untuk itu kita akan coba menambahkan command/perintah sederhana, "hanya"
untuk menjalankan server built in php lalu membuka browser.

1\. buat file class `StartServerCommand.php` di folder project, paste
code berikut:

    setName('server:start')
                ->setDescription('Open built in PHP server and open browser');
        }

        // execute
        protected function execute(InputInterface $input, OutputInterface $output)
        {   
            $command = PHP_BINARY." -S localhost:8000";
            $output->writeln("Running server");

            system("start http://localhost:8000");      
            system($command);
        }
    }

2\. Setelah itu, kita harus edit program console kita (console.php)
menjadi:

    #!/usr/bin/env php
    add(new StartServerCommand());
    $application->run();

Program console siap dijalankan:

    php console.php server:start
