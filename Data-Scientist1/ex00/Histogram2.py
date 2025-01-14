import matplotlib.pyplot as plt
import pandas 

def main():
    df = pandas.read_csv('../Train_knight.csv')
    jedi_data = df[df['knight'] == 'Jedi']
    sith_data = df[df['knight'] == 'Sith']
    columns = df.columns

    for i, column in zip(range(1, 31, 1), columns):
        plt.subplot(6, 5, i)
        plt.hist(jedi_data[column], bins=40, color='blue', alpha=0.6, label='Jedi')
        plt.hist(sith_data[column], bins=40, color='red', alpha=0.6, label='Sith')
        plt.title(column)
    plt.tight_layout()
    plt.show()

main()