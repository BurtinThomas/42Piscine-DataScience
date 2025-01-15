import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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
        data = load_data("elbow.sql")
        wcss = []

        for k in range(1, 11):
            kmeans = KMeans(n_clusters=k, n_init=10, random_state=0)
            kmeans.fit(data) 
            wcss.append(kmeans.inertia_)

        plt.plot(range(1, 11), wcss)
        plt.xlabel("Number of clusters")
        plt.title("The Elbow Method")
        plt.show()
    
        
    except Exception as error:
        print(f"{Exception.__name__} : {error}")

if __name__ == "__main__":
    main()