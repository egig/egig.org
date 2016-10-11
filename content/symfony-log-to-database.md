Title: Symfony, Log to Database
Date: 2016-01-08 17:00
Author: egig
Category: Uncategorized
Slug: symfony-log-to-database
Status: published

Symfony sudah dilengkapi dengan component terkait dengan log:
[Monolog](https://github.com/Seldaek/monolog). Namun, symfony secara
default menyimpan log hanya pada filesystem dan tidak menyediakan fitur
penyimpanan log pada database. Karena memang tidak semua orang ingin
menyimpan log aplikasi pada database. In case, kita harus menambahkan
fitur semacam 'Catatan Sistem' pada aplikasi kita untuk menganalisa
kegiatan pengguna, sebagaimana yang pernah saya alami, berikut ini
sharing saya. Saya mencoba untuk menyimpan log pada database MySQL.
<!--more--> Untuk dapat menyimpan log pada database, kita harus membuat
Monolog handler baru. Tutorial membuat PDOHandler sudah tersedia:

<https://github.com/Seldaek/monolog/blob/master/doc/04-extending.md>.
Tapi kita akan merubahnya sedikit, karena symfony sudah dilengkapi
dengan component terkait database: Doctrine DBAL, maka kita tidak akan
menggunakan PDO tetapi menggunakan Doctrine DBAL, untuk itu handler yang
kita buat akan kita beri nama `DoctrineDBALHandler`.

    <?php
    // src/AppBundle/Monolog/Handler/DoctrineDBALHandler.php

    namespace AppBundle\Monolog\Handler;

    use Monolog\Logger;
    use Monolog\Handler\AbstractProcessingHandler;
    use Doctrine\DBAL\DriverManager;

    class DoctrineDBALHandler extends AbstractProcessingHandler
    {
        /**
         * Initialize state.
         *
         * @var boolean
         **/
        private $initialized = false;

        /**
         * Database connectin
         *
         * @var Doctrine\DBAL\Connection
         **/
        private $connection;

        /**
         * The statemenet.
         *
         * @var Doctrine\DBAL\Statement
         **/
        private $statement;

        /**
         * Table name.
         *
         * @var string
         **/
        private $logTable;

        /**
         * Handler constructor.
         *
         * @todo refactor this to be more clean
         **/

        public function __construct(
            $driver,
            $host,
            $dbname,
            $user,
            $password,
            $level = Logger::DEBUG,
            $bubble = true
            )
        {
            $param['driver'] = $driver;
            $param['host'] = $host;
            $param['dbname'] = $dbname;
            $param['user'] = $user;
            $param['password'] = $password;

            $this->connection = DriverManager::getConnection($param);

            parent::__construct($level, $bubble);
        }

        public function write(array $record)
        {
            if (!$this->initialized) {
                $this->initialize();
            }

            $this->statement->execute([
                'channel' => $record['channel'],
                'level' => $record['level'],
                'message' => $record['message'],
                'time' => $record['datetime']->format('U'),
            ]);
        }

        private function initialize()
        {
            $this->statement = $this->connection->prepare(
                'INSERT INTO '.$this->logTable.' (channel, level, message, time) VALUES (:channel, :level, :message, :time)'
            );

            $this->initialized = true;
        }
    }


Kita akan buat class diatas sebagai symfony service

    # app/config/services.yml

    services:
        monolog_dbal_handler:
            class: AppBundle\Directory\ClassName
            arguments: ["%database_driver%", "%database_host%", "%database_name%", "%database_user%", "%database_password%"]
     Setelah itu kita perlu mendaftarkan handler diatas pada konfigurasi.

    monolog:
        channels: [user_activity] # kita perlu menambahkan channel baru
        handlers:
            my_handler:
                type: service
                id: monolog_dbal_handler # Perhatikan nama service diatas
                channels: user_activity

Selesai. Sekarang kita sudah bisa menggunakan logger diatas, contoh penggunaannya di controller adalah sebagai berikut:


  $logger  = $this->get('monolog.logger.user_activity')

  $logger->error("Pengguna telah menyunting artikel");


Tentunya jangan lupa buat tabel di database dahulu:

    CREATE TABLE IF NOT EXISTS monolog (channel VARCHAR(255), level INTEGER, message LONGTEXT, time INTEGER UNSIGNED)

Demikian, semoga bermanfaat.
