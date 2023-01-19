CREATE TABLE IF NOT EXISTS penguins (
    penguin_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    fish_eaten INT NOT NULL, 
    dancing BOOLEAN NOT NULL,
    penguin_name VARCHAR(20) NOT NULL 
);

INSERT INTO penguins (fish_eaten, dancing, penguin_name) VALUES (12, true, 'Judy');
INSERT INTO penguins (fish_eaten, dancing, penguin_name) VALUES (15, true, 'Michael');
INSERT INTO penguins (fish_eaten, dancing, penguin_name) VALUES (7, false, 'Pingu');