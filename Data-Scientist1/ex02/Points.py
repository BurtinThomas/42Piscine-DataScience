import matplotlib.pyplot as plt
import pandas 

def main():
    df = pandas.read_csv('../Train_knight.csv')
    df2 = pandas.read_csv('../Test_knight.csv')
    jedi_data = df[df['knight'] == 'Jedi']
    sith_data = df[df['knight'] == 'Sith']


    plt.scatter(sith_data['Empowered'], sith_data['Stims'], color='red', alpha=0.6, label='Sith')
    plt.scatter(jedi_data['Empowered'], jedi_data['Stims'], color='blue', alpha=0.6, label='Jedi')
    plt.xlabel("Empowered")
    plt.ylabel("Stims")
    plt.legend()
    plt.show()

    plt.scatter(df2['Empowered'], df2['Stims'], color='green', alpha=0.6, label='Knight')
    plt.xlabel("Empowered")
    plt.ylabel("Stims")
    plt.legend()
    plt.show()

    plt.scatter(sith_data['Pull'], sith_data['Push'], color='red', alpha=0.6, label='Sith')
    plt.scatter(jedi_data['Pull'], jedi_data['Push'], color='blue', alpha=0.6, label='Jedi')
    plt.xlabel("PULL")
    plt.ylabel("PUSH")
    plt.legend()
    plt.show()

    plt.scatter(df2['Pull'], df2['Push'], color='green', alpha=0.6, label='Knight')
    plt.xlabel("PULL")
    plt.ylabel("PUSH")
    plt.legend()
    plt.show()

main()