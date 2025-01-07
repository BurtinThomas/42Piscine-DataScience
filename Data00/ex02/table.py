import psycopg2
import os

def main():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="piscineds",
            user="tburtin",
            password="toto"
        )
        cur = conn.cursor()

        file = "data_2022_dec.csv"
        file_name_without_extension = os.path.splitext(file)[0]

        cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {file_name_without_extension} (
            event_time TIMESTAMP,
            event_type VARCHAR(50),
            product_id INT,
            price FLOAT,
            user_id INT,
            user_session INT
        );
        """)

        cur.close()
        conn.commit()
        conn.close()

    except Exception as error:
        print(f"{Exception.__name__} : {error}")


if __name__ == "__main__":
    main()