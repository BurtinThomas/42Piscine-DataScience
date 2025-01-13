import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt

def main():
    try:
        with open("chart2.sql", "r") as file:
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
        
        daily_sales = {}
        unique_customers = {}
        
        for user_id, event_time, event_type, price in results:
            if event_type == 'purchase':
                date_str = event_time.strftime('%Y-%m-%d')
                
                if date_str not in daily_sales:
                    daily_sales[date_str] = 0
                daily_sales[date_str] += price

                if date_str not in unique_customers:
                    unique_customers[date_str] = set()
                unique_customers[date_str].add(user_id)

        dates = list(daily_sales.keys())
        average_per_customers = [daily_sales[date] * 0.8 / len(unique_customers[date]) for date in dates]

        plt.plot(dates, average_per_customers)
        plt.fill_between(dates, average_per_customers, color='blue', alpha=0.3)
        plt.ylabel("average spend\customers in Altairian Dollars")
        ticks = [0, len(dates) // 5, 2 * len(dates) // 5, 3 * len(dates) // 5, 4 * len(dates) // 5]
        labels = ["Oct", "Nov", "Dec", "Jan", "Feb"]
        plt.xticks(ticks, labels)
        y_ticks = list(range(0, int(max(average_per_customers)) + 1, 5))
        plt.yticks(y_ticks)
        plt.xlim(dates[0], dates[-1])
        plt.show()

        cur.close()
        conn.commit()
        conn.close()
    except Exception as error:
        print(f"{Exception.__name__} : {error}")

if __name__ == "__main__":
    main()
