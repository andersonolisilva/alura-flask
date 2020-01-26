CREATE TABLE jogo (
      id int(11) NOT NULL AUTO_INCREMENT,
      nome varchar(50) NOT NULL,
      categoria varchar(40) NOT NULL,
      console varchar(20) NOT NULL,
      PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE usuario (
      id varchar(8) COLLATE utf8_bin NOT NULL,
      nome varchar(20) COLLATE utf8_bin NOT NULL,
      senha varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;