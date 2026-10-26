CREATE TABLE IF NOT EXISTS users (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

TRUNCATE TABLE users;

INSERT INTO books (title, author) VALUES
    ('Michel', 'asd;lfjk'),
    ('James', 'asdkljfe'),
    ('Layla', 'elkse'),
    ('Bill', '@£lkjsdkfjelLJ');
