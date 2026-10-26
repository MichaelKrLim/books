CREATE TABLE IF NOT EXISTS books (
id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
title TEXT NOT NULL,
author TEXT NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS books_title_author_unique_idx ON books (title, author);
INSERT INTO books (title, author) VALUES
('The Gruffalo', 'Julia Donaldson'),
('Ada Twist, Scientist', 'Andrea Beaty'),
('The Girl Who Drank the Moon', 'Kelly Barnhill'),
('Dragons in a Bag', 'Zetta Elliott')
ON CONFLICT (title, author) DO NOTHING;
