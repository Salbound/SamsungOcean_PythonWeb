DROP TABLE IF EXISTS entradas;
CREATE TABLE entradas (
  id INTEGER PRIMARY KEY autoincrement,
  titulo STRING NOT NULL,
  texto STRING NOT NULL
);