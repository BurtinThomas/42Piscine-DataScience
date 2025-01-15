import psycopg2
from datetime import datetime
from collections import Counter
import matplotlib.pyplot as plt
import numpy

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
        data = load_data("average_basket_price.sql")
        average_basket_price = [row[1] for row in data]
        
        plt.boxplot(average_basket_price, vert=False, widths=0.5, notch=True, patch_artist=True, boxprops=dict(facecolor="lightblue"))
        plt.xlabel("price")
        plt.show()

    except Exception as error:
        print(f"{Exception.__name__} : {error}")

if __name__ == "__main__":
    main()