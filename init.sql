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
    ('Janruwa Junction'),
    ('Kamazou Junction'),
    ('Mahuta Junction'),
    ('Karji Junction');

-- Inserting dummy data for professions
INSERT INTO professions (name) VALUES
    ('Keke Rider'),
    ('Bike Rider');

-- Inserting dummy data for professionals
INSERT INTO professionals (name, phone_number) VALUES
    ('John Doe', '+2348012345678'),
    ('James Smith', '+2348098765432'),
    ('Mike Johnson', '+2348055555555'),
    ('Samuel Adams', '+2348077777777'),
    ('Chibuike Okonkwo', '+2348033333333'),
    ('Ibrahim Hassan', '+2348066666666'),
    ('Oluwaseun Adeleke', '+2348044444444'),
    ('Chinua Achebe', '+2348099999999'),
    ('Babatunde Adeyemi', '+2348022222222'),
    ('Babajide Ogunleye', '+2348011111111'),
    ('Michael Williams', '+2348013579246'),
    ('David Brown', '+2348024681357'),
    ('Robert Taylor', '+2348035792468'),
    ('Daniel Wilson', '+2348046813579'),
    ('Joseph Anderson', '+2348057924680'),
    ('Christopher Lee', '+2348068135792'),
    ('Emmanuel Okafor', '+2348079246813'),
    ('Chidi Nnamdi', '+2348090357924'),
    ('Yusuf Mohammed', '+2348001234567'),
    ('Abubakar Sani', '+2348012345670');

-- Inserting dummy data for junction_professionals
INSERT INTO junction_professionals (junction_id, profession_id, professional_id) VALUES
    (1, 1, 1),  -- John Doe as Keke Rider at Janruwa Junction
    (1, 2, 2),  -- James Smith as Bike Rider at Janruwa Junction
    (1, 1, 3),  -- Mike Johnson as Keke Rider at Janruwa Junction
    (1, 2, 4),  -- Samuel Adams as Bike Rider at Janruwa Junction
    (1, 1, 5),  -- Chibuike Okonkwo as Keke Rider at Janruwa Junction
    (2, 1, 6),  -- Ibrahim Hassan as Keke Rider at Kamazou Junction
    (2, 2, 7),  -- Oluwaseun Adeleke as Bike Rider at Kamazou Junction
    (2, 1, 8),  -- Chinua Achebe as Keke Rider at Kamazou Junction
    (2, 2, 9),  -- Babatunde Adeyemi as Bike Rider at Kamazou Junction
    (2, 1, 10), -- Babajide Ogunleye as Keke Rider at Kamazou Junction
    (3, 1, 11), -- Michael Williams as Keke Rider at Mahuta Junction
    (3, 2, 12), -- David Brown as Bike Rider at Mahuta Junction
    (3, 1, 13), -- Robert Taylor as Keke Rider at Mahuta Junction
    (3, 2, 14), -- Daniel Wilson as Bike Rider at Mahuta Junction
    (3, 1, 15), -- Joseph Anderson as Keke Rider at Mahuta Junction
    (4, 1, 16), -- Christopher Lee as Keke Rider at Karji Junction
    (4, 2, 17), -- Emmanuel Okafor as Bike Rider at Karji Junction
    (4, 1, 18), -- Chidi Nnamdi as Keke Rider at Karji Junction
    (4, 2, 19), -- Yusuf Mohammed as Bike Rider at Karji Junction
    (4, 1, 20);  -- Abubakar Sani as Keke Rider at Karji Junction