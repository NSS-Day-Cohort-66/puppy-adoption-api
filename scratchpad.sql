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


SELECT
    c.id AS center_id,
    c.address AS center_address,
    c.name AS center_name,
    c.phone_number AS center_phone,
    c.email_address AS center_email,
    a.id AS animal_id,
    a.name AS animal_name,
    a.age AS animal_age,
    a.image_url AS animal_image_url
FROM
    Center c
LEFT JOIN
    Animal a ON c.id = a.center_id
-- Exclude animals that have been adopted
LEFT JOIN
    Adoption ad ON a.id = ad.animal_id
WHERE
    ad.id IS NULL
;



























SELECT
    c.id,
    c.address,
    c.name,
    c.phone_number,
    c.email_address,
    a.id animal_id,
    a.name animal_name,
    a.age animal_age,
    a.center_id animal_center_id
FROM
    Center c
LEFT JOIN
    Animal a ON c.id = a.center_id
LEFT JOIN
    Adoption ad ON a.id = ad.animal_id
WHERE
    ad.id IS NULL
    AND c.id = 3
;