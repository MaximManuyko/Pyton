insert into users (first_name, email) values
('Gregory', 'gregory@google.com');
UPDATE users set email = 'johny@hotmail.com' WHERE first_name = 'John'
DELETE FROM users WHERE first_name = 'Alex';

INSERT INTO users (first_name, email) VALUES ('Gregory', 'gregory@google.com');
UPDATE users SET email = 'johny@hotmail.com' WHERE first_name = 'John';
DELETE FROM users WHERE first_name = 'Alex';