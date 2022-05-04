CREATE TABLE Category(
    name        VARCHAR(32) PRIMARY KEY,
    description VARCHAR(512)
);

CREATE TABLE User(
    username VARCHAR(32) PRIMARY KEY,
    password VARCHAR(128) NOT NULL
    email    VARCHAR(512),
    website  TEXT
);

CREATE TABLE Post(
    
);