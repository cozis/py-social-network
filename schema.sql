CREATE TABLE Category (
           name VARCHAR(32) PRIMARY KEY,
    description VARCHAR(512)
);

CREATE TABLE User (
     username VARCHAR(32) PRIMARY KEY,
     password VARCHAR(128) NOT NULL
    pvt_email VARCHAR(512),
    pub_email VARCHAR(512),
     website TEXT
);

CREATE TABLE Post (
          id INTEGER PRIMARY KEY,
    username VARCHAR(32), NOT NULL,
    category VARCHAR(32), 
       title VARCHAR(128) NOT NULL,
        body TEXT,
        link TEXT,
       time_ TIMESTAMP NOT NULL,
    FOREIGN KEY (username) REFERENCES User(username),
    FOREIGN KEY (category) REFERENCES Category(name),
    CHECK (body XOR link)
);

CREATE TABLE Reply (
        id   INTEGER PRIMARY KEY,
      post   INTEGER NOT NULL,
    parent   INTEGER,
      body      TEXT NOT NULL,
     time_ TIMESTAMP NOT NULL,
    FOREIGN KEY (post) REFERENCES Post(id),
    FOREIGN KEY (parent) REFERENCES Reply(id)
);
