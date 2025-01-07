import psycopg2
import pandas

def create_table(table_name, cur):
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            product_id BIGINT,
            category_id BIGINT,
            brand VARCHAR(255)
        );
    """)

def insert_data_into_table(table_name, df, cur):
    insert_query = f"""
        INSERT INTO {table_name} (product_id, category_id, brand)
        VALUES (%s, %s, %s)
    """
    for index, row in df.iterrows():
        try:
            cur.execute(insert_query, tuple(row))
            print("Insertion réussie")
        except Exception as e:
            print(f"Erreur avec la ligne {index}: {e}")
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

        path = "../subject/item/item.csv"
        table_name = "item"
        create_table(table_name, cur)
        
        df = pandas.read_csv(path)
        df = df.drop(df.columns[2], axis=1)
        df = df.dropna()
        insert_data_into_table(table_name, df, cur)

        cur.close()
        conn.commit()
        conn.close()

    except Exception as error:
        print(f"{Exception.__name__} : {error}")

if __name__ == "__main__":
    main()
