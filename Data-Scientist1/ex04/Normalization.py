import pandas
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def main():
    df = pandas.read_csv('../Train_knight.csv')
    columns_to_normalize  = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = MinMaxScaler() 
    df_normalize = df.copy()
    df_normalize[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])
    print(df['Sensitivity'])
    print("---------------")
    print(df_normalize['Sensitivity'])

    jedi_data = df_normalize[df['knight'] == 'Jedi']
    sith_data = df_normalize[df['knight'] == 'Sith']
    
    df2 = pandas.read_csv('../Test_knight.csv')
    columns_to_normalize2 = df2.select_dtypes(include=['float64', 'int64']).columns
    scaler2 = MinMaxScaler()  
    df_normalize2 = df2.copy()
    df_normalize2[columns_to_normalize2] = scaler2.fit_transform(df2[columns_to_normalize2])


    plt.scatter(sith_data['Pull'], sith_data['Push'], color='red', alpha=0.6, label='Sith')
    plt.scatter(jedi_data['Pull'], jedi_data['Push'], color='blue', alpha=0.6, label='Jedi')
    plt.xlabel("Pull")
    plt.ylabel("Push")
    plt.legend()
    plt.show()

    plt.scatter(df_normalize2['Pull'], df_normalize2['Push'], color='green', alpha=0.6, label='Knight')
    plt.xlabel("Pull")
    plt.ylabel("Push")
    plt.legend()
    plt.show()

main()