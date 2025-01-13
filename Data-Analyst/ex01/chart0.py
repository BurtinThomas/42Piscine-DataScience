import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt

def main():
    try:
        with open("chart0.sql", "r") as file:
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

        purchase_counts = {}
        for event_time, event_type in results:
            if event_type == 'purchase':
                date = datetime(event_time.year, event_time.month, event_time.day)
                date_str = date.strftime('%Y-%m-%d')
                if date_str not in purchase_counts:
                    purchase_counts[date_str] = 0
                purchase_counts[date_str] += 1
        
        dates = list(purchase_counts.keys())
        counts = list(purchase_counts.values())

        plt.plot(dates, counts)
        plt.ylabel("Number of customers")
        ticks = [0, len(dates) // 5, 2 * len(dates) // 5, 3 * len(dates) // 5, 4 * len(dates) // 5]
        labels = ["Oct", "Nov", "Dec", "Jan", "Feb"]
        plt.xticks(ticks, labels)
        plt.xlim(dates[0], dates[-1])
        plt.show()

        cur.close()
        conn.commit()
        conn.close()
    except Exception as error:
        print(f"{Exception.__name__} : {error}")

if __name__ == "__main__":
    main()