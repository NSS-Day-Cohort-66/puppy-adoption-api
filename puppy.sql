CREATE TABLE Center (
    id INTEGER PRIMARY KEY,
    address TEXT,
    name TEXT,
    phone_number TEXT,
    email_address TEXT
);

CREATE TABLE Animal (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    image_url TEXT,
    center_id INTEGER,
    FOREIGN KEY (center_id) REFERENCES Center(id)
);

CREATE TABLE Adopter (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone_number TEXT,
    address TEXT
);

CREATE TABLE Adoption (
    id INTEGER PRIMARY KEY,
    animal_id INTEGER,
    adopter_id INTEGER,
    date_of_adoption DATE,
    FOREIGN KEY (animal_id) REFERENCES Animal(id),
    FOREIGN KEY (adopter_id) REFERENCES Adopter(id)
);


-- Adding 4 centers
INSERT INTO Center (address, name, phone_number, email_address) VALUES
('123 Main St, CityA', 'Center A', '123-456-7890', 'a@center.com'),
('456 Park Ave, CityB', 'Center B', '987-654-3210', 'b@center.com'),
('789 West St, CityC', 'Center C', '234-567-8901', 'c@center.com'),
('012 North Ave, CityD', 'Center D', '345-678-9012', 'd@center.com');

-- Adding 10 adopters
INSERT INTO Adopter (name, phone_number, address) VALUES
('John Doe', '111-222-3333', '10 Elm St'),
('Jane Smith', '222-333-4444', '20 Oak St'),
('Bob Brown', '333-444-5555', '30 Maple St'),
('Alice White', '444-555-6666', '40 Birch St'),
('Charlie Green', '555-666-7777', '50 Cedar St'),
('Daisy Blue', '666-777-8888', '60 Fir St'),
('Eve Black', '777-888-9999', '70 Pine St'),
('Frank Red', '888-999-0000', '80 Spruce St'),
('Grace Yellow', '999-000-1111', '90 Ash St'),
('Henry Purple', '000-111-2222', '100 Cherry St');

-- Adding 8 puppies to each center
-- Center A
INSERT INTO Animal (name, age, image_url, center_id) VALUES
('Buddy', 1, 'https://dog.ceo/api/breeds/image/random', 1),
('Bella', 1, 'https://dog.ceo/api/breeds/image/random', 1),
('Charlie', 1, 'https://dog.ceo/api/breeds/image/random', 1),
('Lucy', 1, 'https://dog.ceo/api/breeds/image/random', 1),
('Max', 1, 'https://dog.ceo/api/breeds/image/random', 1),
('Luna', 1, 'https://dog.ceo/api/breeds/image/random', 1),
('Rocky', 1, 'https://dog.ceo/api/breeds/image/random', 1),
('Daisy', 1, 'https://dog.ceo/api/breeds/image/random', 1);

-- Center B
INSERT INTO Animal (name, age, image_url, center_id) VALUES
('Milo', 1, 'https://dog.ceo/api/breeds/image/random', 2),
('Zoe', 1, 'https://dog.ceo/api/breeds/image/random', 2),
('Toby', 1, 'https://dog.ceo/api/breeds/image/random', 2),
('Stella', 1, 'https://dog.ceo/api/breeds/image/random', 2),
('Oscar', 1, 'https://dog.ceo/api/breeds/image/random', 2),
('Sadie', 1, 'https://dog.ceo/api/breeds/image/random', 2),
('Finn', 1, 'https://dog.ceo/api/breeds/image/random', 2),
('Molly', 1, 'https://dog.ceo/api/breeds/image/random', 2);

-- Center C
INSERT INTO Animal (name, age, image_url, center_id) VALUES
('Rusty', 1, 'https://dog.ceo/api/breeds/image/random', 3),
('Rosie', 1, 'https://dog.ceo/api/breeds/image/random', 3),
('Teddy', 1, 'https://dog.ceo/api/breeds/image/random', 3),
('Ruby', 1, 'https://dog.ceo/api/breeds/image/random', 3),
('Jake', 1, 'https://dog.ceo/api/breeds/image/random', 3),
('Sophie', 1, 'https://dog.ceo/api/breeds/image/random', 3),
('Cody', 1, 'https://dog.ceo/api/breeds/image/random', 3),
('Lily', 1, 'https://dog.ceo/api/breeds/image/random', 3);

-- Center D
INSERT INTO Animal (name, age, image_url, center_id) VALUES
('Oliver', 1, 'https://dog.ceo/api/breeds/image/random', 4),
('Chloe', 1, 'https://dog.ceo/api/breeds/image/random', 4),
('Zeus', 1, 'https://dog.ceo/api/breeds/image/random', 4),
('Riley', 1, 'https://dog.ceo/api/breeds/image/random', 4),
('Murphy', 1, 'https://dog.ceo/api/breeds/image/random', 4),
('Angel', 1, 'https://dog.ceo/api/breeds/image/random', 4),
('Duke', 1, 'https://dog.ceo/api/breeds/image/random', 4),
('Missy', 1, 'https://dog.ceo/api/breeds/image/random', 4);

-- 2 random adoptions
-- Adopting Buddy by John Doe
INSERT INTO Adoption (animal_id, adopter_id, date_of_adoption) VALUES
(1, 1, '2023-10-25');

-- Adopting Bella by Jane Smith
INSERT INTO Adoption (animal_id, adopter_id, date_of_adoption) VALUES
(2, 2, '2023-10-25');


SELECT
    a.id,
    a.name,
    ad.id
FROM Animal a
LEFT JOIN Adoption ad ON ad.animal_id = a.id
;


SELECT
    c.id,
    c.address,
    c.name,
    c.phone_number,
    c.email_address,
    COUNT(a.id) AS animal_count
FROM
    Center c
LEFT JOIN
    Animal a ON c.id = a.center_id
LEFT JOIN
    Adoption ad ON a.id = ad.animal_id
WHERE
    ad.id IS NULL
GROUP BY
    c.id
;
