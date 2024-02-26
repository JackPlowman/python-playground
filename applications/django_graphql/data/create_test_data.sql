INSERT INTO blog_author (id, name) VALUES (1, 'John Doe'),
(2, 'Jane Doe'),
(3, 'Jack Smith');

INSERT INTO blog_post (title, content, author_id) VALUES
('First post', 'This is the first post', 1),
('Second post', 'This is the second post', 1),
('Third post', 'This is the third post', 1),
('Fourth post', 'This is the fourth post', 2),
('Fifth post', 'This is the fifth post', 2),
('Sixth post', 'This is the sixth post', 3);
