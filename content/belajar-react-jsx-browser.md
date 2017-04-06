Title: Belajar React: JSX di Browser
Date: 2017-04-06 23:30
Author: egig
Category: Javascript
Tags: javascript, react
Slug: belajar-react-jsx-browser
Status: published


JSX tidak bisa dijalankan di browser begitu saja, karena browser, bahkan yang terbaru sekalipun, hanya mendukung javascript murni saja. Agar bisa menggunakan sintak JSX di browser, kita harus menggunakan librari lain yang bernana **Babel**.

### Apa itu Babel ?

> Babel is a JavaScript compiler.

Begitu kata website-nya, bisa dikunjungi di https://babeljs.io. **Babel** adalah javascript compiler. Secara teknis, Babel bisa kita gunakan untuk men-transformasi-kan  bahasa javascript modern (EcmaScript 6) dan atau JSX React menjadi javascript yang didukung oleh browser.

### Bagaimana menggunakan Bebel di Browser ?

Untuk menjalankan babel di browser, kita cukup memuat librari Babel langsung:

    <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.34/browser.min.js"></script>

    
Namun, text javascript yang ingin kita transformasikan, tidak lagi disertakan dengan HTML sebagai tipe `text/javascript`, melainkan sebagai tipe `text/babel`

Contoh:

    <script type="text/babel">
        const getMessage = () => "Hello World";
        document.getElementById('output').innerHTML = getMessage();
    </script>

Pada artikel sebelumnya dimana kita membuat program Hello World, kita belum menggunakan JSX.

    <!DOCTYPE html>
    <html>
      <head>
        <title>Sinau ReactJS</title>
      </head>
      <body>
    
        <!-- Element sederhana div dengan id 'app' -->
        <!-- Element ini diperlukan oleh react sebagai container -->
        <div id="app"></div>
    
        <!-- Load library React yang dibutuhkan -->
        <script src="https://unpkg.com/react@15/dist/react.min.js"></script>
        <script src="https://unpkg.com/react-dom@15/dist/react-dom.min.js"></script>
    
        <!-- Program -->
        <script type="text/javascript">
          var Hello  = function (props) {
            return React.createElement('div', null, 'Hello World');
          };
    
          ReactDOM.render(
            React.createElement(Hello, null, null),
            document.getElementById('app')
          );
        </script>
      </body>
    </html>
    
Mari kita rubah kode tersebut diatas menjadi menggunakan JSX.

1. Tambahkan script librari babel setelah librari react:

       
        <script src="https://unpkg.com/react@15/dist/react.min.js"></script>
        <script src="https://unpkg.com/react-dom@15/dist/react-dom.min.js"></script>
        <!-- Librari babel -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.34/browser.min.js"></script>
      


2. Gunakan JSX. Ganti kode berikut

        var Hello  = function (props) {
           return React.createElement('div', null, 'Hello World');
        };
    
        ReactDOM.render(
            React.createElement(Hello, null, null),
            document.getElementById('app')
         );
         
    menjadi:
    
        var Hello  = function (props) {
            return <div>Hello World</div>;
        };
   
        ReactDOM.render(
           <Hello />,
           document.getElementById('app')
        );
       
       
Hasil akhir:

    <!DOCTYPE html>
    <html>
    <head>
      <title>Sinau ReactJS: JSX</title>
    </head>
    <body>
    
    <!-- Element sederhana div dengan id 'app' -->
    <!-- Element ini diperlukan oleh react sebagai container -->
    <div id="app"></div>
    
    <!-- Load library React yang dibutuhkan -->
    <script src="https://unpkg.com/react@15/dist/react.min.js"></script>
    <script src="https://unpkg.com/react-dom@15/dist/react-dom.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.34/browser.min.js"></script>
    
    <!-- Program -->
    <script type="text/babel">
        var Hello  = function (props) {
            return <div>Hello World</div>;
        };
    
        ReactDOM.render(
            <Hello />,
            document.getElementById('app')
        );
    </script>
    </body>
    </html>
    
 Simpan dengan nama `2-jsx.html` dan buka di browser, maka akan tampil pesan sederhana "Hello World" seperti yang sudah kita lakukan sebelumnya.