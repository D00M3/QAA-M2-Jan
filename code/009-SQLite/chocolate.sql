-- SQL file that will make an SQL table and put some data into it

-- Create a table if this one doesn't already exist
CREATE TABLE IF NOT EXISTS chocolate (
    choc_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    flavour VARCHAR(30) NOT NULL, 
    weight_gr INTEGER NOT NULL,
    fairtrade BOOLEAN NOT NULL 
);

INSERT INTO chocolate (flavour, weight_gr, fairtrade) 
VALUES ('Salted Caramel', 60, true);

INSERT INTO chocolate (flavour, weight_gr, fairtrade) 
VALUES ('Strawberry', 92, false);

INSERT INTO chocolate (flavour, weight_gr, fairtrade) 
VALUES ('Dark', 80, true);