CREATE TABLE IF NOT EXISTS books (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL
);

TRUNCATE TABLE books;

INSERT INTO books (title, author) VALUES
    ('The Gruffalo', 'Julia Donaldson'),
    ('Ada Twist, Scientist', 'Andrea Beaty'),
    ('The Girl Who Drank the Moon', 'Kelly Barnhill'),
    ('Dragons in a Bag', 'Zetta Elliott');
