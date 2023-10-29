CREATE TABLE stores (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nom TEXT NOT NULL
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    store_id INTEGER NOT NULL, 
    nom TEXT NOT NULL, 
    unitats INTEGER NOT NULL,
    FOREIGN KEY (store_id) REFERENCES stores(id)
);

INSERT INTO stores(nom) VALUES ("Mercadona");
INSERT INTO stores(nom) VALUES ("Lidl");
INSERT INTO stores(nom) VALUES ("Aldi");
INSERT INTO stores(nom) VALUES ("Condis");

CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL UNIQUE, role TEXT NOT NULL, password TEXT NOT NULL);
-- Les contrasenyes són patata
INSERT INTO users (email, role, password) VALUES ('voltaire@mir.com', 'viewer', 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4');
INSERT INTO users (email, role, password) VALUES ('edison@mir.com', 'editor', 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4');
