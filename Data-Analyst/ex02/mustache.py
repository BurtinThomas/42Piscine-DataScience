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
        data = load_data("mustache.sql")

        prices = [i[1] for i in data if i[0] == "purchase"]
        
        count = len(prices)
        mean = numpy.mean(prices)
        std = numpy.std(prices)
        min = numpy.min(prices)
        max = numpy.max(prices)
        quartiles = numpy.percentile(prices, [25, 50, 75])

        print(f"count: {count:.6f}")
        print(f"mean: {mean:.6f}")
        print(f"std: {std:.6f}")
        print(f"min: {min:.6f}")
        print(f"25%: {quartiles[0]:.6f}")
        print(f"50%: {quartiles[1]:.6f}")
        print(f"75%: {quartiles[2]:.6f}")
        print(f"max: {max:.6f}")

        plt.boxplot(prices, vert=False, widths=0.5, notch=True)
        plt.xlabel("price")
        plt.show()
        
        plt.boxplot(prices, vert=False, widths=0.5, notch=True, showfliers=False, patch_artist=True, boxprops=dict(facecolor="lightgreen"))
        plt.xlabel("price")
        plt.show()

    except Exception as error:
        print(f"{Exception.__name__} : {error}")

if __name__ == "__main__":
    main()