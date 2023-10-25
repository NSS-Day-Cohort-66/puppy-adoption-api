import sqlite3

class Agency():
    def __init__(self):
        self.id = 0
        self.name = ""
        self.address = ""
        self.phone_number = ""
        self.email_address = ""
        self.database_path = "./puppies.db"

    def create(self, id, name, address, phone_number, email_address):
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email_address = email_address
        return self

    def get_single(self, id):
        sql = """

        """

        with sqlite3.connect(self.database_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            db_cursor.execute(sql, (pk,))
            return db_cursor.fetchone()

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
        with sqlite3.connect(self.database_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            db_cursor.execute(sql)
            rows = db_cursor.fetchall()

            agencies = []

            for row in rows:
                new_agency = self.create(row['id'], row['name'], row['address'],
                           row['phone_number'], row['email_address'])

                agencies.append(new_agency.__dict__)

            # return a list of Agency objects
            return agencies