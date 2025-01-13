import psycopg2
from table import create_table

def main():
    try:
        create_table("data_2023_feb.csv", "customers")
        with open("customers_table.sql", "r") as file:
            query = file.read()

        conn = psycopg2.connect(
            host="localhost",
            database="piscineds",
            user="tburtin",
            password="toto"
        )
        cur = conn.cursor()
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
    except Exception as error:
        print(f"{Exception.__name__} : {error}")

if __name__ == "__main__":
    main()

#SELECT * FROM item where product_id = 5846774;
#SELECT COUNT(*) FROM customers;