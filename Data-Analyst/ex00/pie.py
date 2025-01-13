import psycopg2
import matplotlib.pyplot as plt

def main():
    try:
        with open("pie.sql", "r") as file:
            query = file.read()

        conn = psycopg2.connect(
            host="localhost",
            database="piscineds",
            user="tburtin",
            password="toto"
        )
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()

        labels = [row[0] for row in results]
        sizes = [row[1] for row in results]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.show()

        cur.close()
        conn.commit()
        conn.close()
    except Exception as error:
        print(f"{Exception.__name__} : {error}")

if __name__ == "__main__":
    main()