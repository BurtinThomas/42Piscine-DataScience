import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt

def main():
    try:
        with open("chart1.sql", "r") as file:
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

        monthly_sales = {}
        for event_time, event_type, price in results:
            if event_type == 'purchase':
                date = datetime(event_time.year, event_time.month, 1)
                date_str = date.strftime('%Y-%m')
                if date_str not in monthly_sales:
                    monthly_sales[date_str] = 0
                monthly_sales[date_str] += price
        
        months = ['Oct', 'Nov', 'Dec', 'Jan', 'fev']
        sales = [monthly_sales[month] * 0.8 for month in monthly_sales]
        plt.bar(months, sales)
        plt.ylabel("Total sales in million of Altairian Dollars")
        plt.xlabel("month")
        plt.show()
        

        cur.close()
        conn.commit()
        conn.close()
    except Exception as error:
        print(f"{Exception.__name__} : {error}")

if __name__ == "__main__":
    main()