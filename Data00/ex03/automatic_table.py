import psycopg2
import pandas
import os

def create_table(file, cur):
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {file} (
            event_time TIMESTAMP,
            event_type VARCHAR(255),
            product_id INT,
            price FLOAT,
            user_id BIGINT,
            user_session VARCHAR(255)
        );
        """)

def insert_data_into_table(table_name, df, cur):
    insert_query = f"""
        INSERT INTO {table_name} (event_time, event_type, product_id, price, user_id, user_session)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    for index, row in df.iterrows():
        try:
            cur.execute(insert_query, tuple(row))
            print(row)
        except Exception as e:
            print(f"Erreur avec la ligne {row.name}: {e}")
            return

def main():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="piscineds",
            user="tburtin",
            password="toto"
        )
        cur = conn.cursor()

        customer_folder = "../subject/customer"
        for file in os.listdir(customer_folder):
            if file.endswith(".csv"):
                create_table(os.path.splitext(file)[0], cur)
                df = pandas.read_csv(os.path.join(customer_folder, file))
                insert_data_into_table(os.path.splitext(file)[0], df, cur)

        cur.close()
        conn.commit()
        conn.close()

    except Exception as error:
        print(f"{Exception.__name__} : {error}")


if __name__ == "__main__":
    main()