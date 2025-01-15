import psycopg2
from datetime import datetime
from collections import Counter
import matplotlib.pyplot as plt

def load_data(path):
    with open(path, "r") as file:
        query = file.read()

        conn = psycopg2.connect(
            host="localhost",
            database="piscineds",
            user="tburtin",
            password="toto"
        )
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return data

        cur.close()
        conn.commit()
        conn.close()


def main():
    try:
        data_frequency = load_data("Building.sql")
        data_value = load_data("Building2.sql")
    
        frequency = [row[1] for row in data_frequency if row[1] < 40]
        value = [row[1] for row in data_value if row[1]]

        plt.hist(frequency)
        plt.xlim(0, 40)
        plt.ylim(0, 65000)
        plt.xlabel("frequency")
        plt.ylabel("customers")
        plt.xticks(range(0, 39, 10))
        plt.show()

        plt.hist(value)
        plt.xlim(0, 250)
        plt.ylim(0, 45000)
        plt.xlabel("monetary value in A")
        plt.ylabel("customers")
        plt.xticks(range(0, 249, 50))
        plt.show()
    except Exception as error:
        print(f"{Exception.__name__} : {error}")

if __name__ == "__main__":
    main()