import matplotlib.pyplot as plt
import pandas 

def main():
    df = pandas.read_csv('../Test_knight.csv')
    columns = df.columns

    for i, column in zip(range(1, 31, 1), columns):
        plt.subplot(6, 5, i)
        plt.hist(df[column], bins=40, color='green', label='knight')
        plt.title(column)
    plt.tight_layout()
    plt.show()

main()