import psycopg2

def main():
    try:
        with open("remove_duplicates.sql", "r") as file:
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