import sqlite3

DB_PATH = "./puppies.db"

class Agency:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.address = ""
        self.phone_number = ""
        self.email_address = ""
        self.number_of_puppies = 0

    def create(self, id, name, address, phone_number, email_address, number_of_puppies = 0):
        agency = Agency()
        agency.id = id
        agency.name = name
        agency.address = address
        agency.phone_number = phone_number
        agency.email_address = email_address
        agency.number_of_puppies = number_of_puppies
        return agency

    def get_single(self, pk):
        sql = """
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
            AND c.id = ?
        """
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            db_cursor.execute(sql, (pk,))
            rows = db_cursor.fetchall()

            puppies = []

            for row in rows:
                if row['animal_id'] is not None:
                    this_puppy = {
                        "id": row['animal_id'],
                        "name": row['animal_name'],
                        "age": row['animal_age']
                    }
                    puppies.append(this_puppy)

            new_agency = self.create(
                rows[0]["id"],
                rows[0]["name"],
                rows[0]["address"],
                rows[0]["phone_number"],
                rows[0]["email_address"],
                len(puppies),
            )

            new_agency.puppies = puppies
            return new_agency.__dict__


        # [
        #     {
        #         "id": 1,
        #         "name": "Whatever Center",
        #         "puppies": [
        #             {
        #                 "id": 4,
        #                 "name": "Scooter",
        #                 "age": 5
        #             },
        #             ...
        #         ]
        #     }
        # ]

    def get_all(self):
        sql = """
        SELECT
            c.id,
            c.address,
            c.name,
            c.phone_number,
            c.email_address,
            COUNT(a.id) AS number_of_puppies
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
                    row["number_of_puppies"],
                )

                agencies.append(new_agency.__dict__)

            # return a list of Agency objects
            return agencies
