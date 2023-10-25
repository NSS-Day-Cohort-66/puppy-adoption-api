import sqlite3

DB_PATH = "./puppies.db"

class Agency:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.address = ""
        self.phone_number = ""
        self.email_address = ""
        self.animal_count = 0

    def create(self, id, name, address, phone_number, email_address, animal_count):
        agency = Agency()
        agency.id = id
        agency.name = name
        agency.address = address
        agency.phone_number = phone_number
        agency.email_address = email_address
        agency.animal_count = animal_count
        return agency

    def get_single(self, pk):
        sql = """
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
            AND a.id = ?
        GROUP BY
            c.id
        """
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            db_cursor.execute(sql, (pk,))
            row = db_cursor.fetchone()

        new_agency = self.create(
            row["id"],
            row["name"],
            row["address"],
            row["phone_number"],
            row["email_address"],
            row["animal_count"],
        )
        return new_agency.__dict__

    def get_all(self):
        sql = """
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
        """
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            db_cursor.execute(sql)
            rows = db_cursor.fetchall()

            agencies = []

            for row in rows:
                new_agency = self.create(
                    row["id"],
                    row["name"],
                    row["address"],
                    row["phone_number"],
                    row["email_address"],
                    row["animal_count"],
                )

                agencies.append(new_agency.__dict__)

            # return a list of Agency objects
            return agencies
