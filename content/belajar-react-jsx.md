Title: Belajar React: JSX
Date: 2017-04-05 23:30
Author: egig
Category: Javascript
Tags: javascript, react
Slug: belajar-react-jsx
Status: published

Pada pembahasan [sebelumnya](http://egig.org/2017/04/belajar-react-hello-world.html) kita membuat React component dengan cara sebagai berikut.

    var Hello  = function (props) {
        return React.createElement('div', null, 'Hello World');
    };

Perhatikan bahwa kita menggunakan fungsi `React.createElement`. Fungsi tersebut digunakan untuk membuat elemen html yang kita butuhkan untuk membuat sebuah komponen. Contoh, kita ingin membuat komponen, yang jika dituliskan dengan html, atau jika di-render menjadi html, akan menjadi seperti berikut berikut:


    <div>
        <p>Paragraph Text</p>
        <button>
            Button Text    
        </button>
    <div>


Menggunakan React dengan vanilla javascript, komponen tersebut dapat ditulis sebagai berikut:

    var KomponenSaya = function(props) {
        var el = React.createElement(
          'div',
          null,
          React.createElement('p', null, 'Paragraph Text'),
          React.createElement('button', null, 'Button Text')
        )
        
        return el;
    }


Perhatikan kode diatas, kita menuliskan satu `React.createElement` untuk setiap elemen yang dibutuhkan, jadi total 3 kali `React.createElement`.

Pada aplikasinya di dunia nyata, kita akan membuat ratusan atau bahkan mungkin ribuan element. Menuliskan elemen-elemen tersebut menggunakan `React.createElement` akan terasa bodoh dan sangat berat. Untuk itu, para Engineer Facebook, membuat sebuah ekstensi dari bahasa pemrograman Javascript yang di beri nama JSX.

JSX kependekan dari Javascript-XML. Dimana kita bisa menyisipkan atau menggunakan sintak menyerupai XML ke dalam bahasa pemrograman javascript, Contoh:


    var helloText  = <span> Hello </span>;
    var submitBtn = <button> Kiraim <button>;


Karena sintak HTML juga menyerupai XML, maka kita bisa menuliskan HTML juga pada JSX dengan beberapa pengecualian yang mungkin nanti akan kita bahas. Untuk saat ini, yang terpenting kita sudah tahu bahwa kita bisa menuliskan tag-tag HTML pada JSX. Dengan demikian, kita bisa menuliskan script diatas menjadi seperti berikut.

    var KomponenSaya = function(props) {
        var el = (
            <div>
                <p>Paragraph Text</p>
                <button>
                    Button Text    
                </button>
            <div>
        );   
        return el;
    }