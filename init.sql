-- Creating table for junctions
CREATE TABLE junctions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Creating table for professions
CREATE TABLE professions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Creating table for professionals (riders or other professions)
CREATE TABLE professionals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

-- Creating linking table for junctions, professions, and professionals
CREATE TABLE junction_professionals (
    id SERIAL PRIMARY KEY,
    junction_id INTEGER NOT NULL REFERENCES junctions(id),
    profession_id INTEGER NOT NULL REFERENCES professions(id),
    professional_id INTEGER NOT NULL REFERENCES professionals(id),
    UNIQUE (junction_id, profession_id, professional_id)
);

-- Inserting dummy data for junctions
INSERT INTO junctions (name) VALUES
    ('Central Junction'),
    ('Market Square'),
    ('Station Road');

-- Inserting dummy data for professions
INSERT INTO professions (name) VALUES
    ('Keke Rider'),
    ('Bike Rider');

-- Inserting dummy data for professionals
INSERT INTO professionals (name, phone_number) VALUES
    ('John Doe', '+2348012345678'),
    ('Jane Smith', '+2348098765432'),
    ('Mike Johnson', '+2348055555555'),
    ('Sarah Adams', '+2348077777777');

-- Inserting dummy data for junction_professionals
INSERT INTO junction_professionals (junction_id, profession_id, professional_id) VALUES
    (1, 1, 1), -- John Doe as Keke Rider at Central Junction
    (1, 2, 2), -- Jane Smith as Bike Rider at Central Junction
    (2, 1, 3), -- Mike Johnson as Keke Rider at Market Square
    (2, 2, 4), -- Sarah Adams as Bike Rider at Market Square
    (3, 1, 1), -- John Doe as Keke Rider at Station Road
    (3, 2, 4); -- Sarah Adams as Bike Rider at Station Road