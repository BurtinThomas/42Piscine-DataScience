import pandas
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    train_knight = pandas.read_csv('Train_knight.csv')
    #pandas.set_option('future.no_silent_downcasting', True)
    train_knight = train_knight.replace({'knight': 'Jedi'}, 1)
    train_knight = train_knight.replace({'knight': 'Sith'}, 0)
    corr = train_knight.corr()
    print(corr)
    sns.heatmap(corr)
    plt.show()

main()