import pandas
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def main():
    df = pandas.read_csv('../Train_knight.csv')
    columns_to_standardize = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler() 
    df_standardized = df.copy()
    df_standardized[columns_to_standardize] = scaler.fit_transform(df[columns_to_standardize])
    print(df['Friendship'])
    print("---------------")
    print(df_standardized['Friendship'])

    jedi_data = df_standardized[df['knight'] == 'Jedi']
    sith_data = df_standardized[df['knight'] == 'Sith']
    
    df2 = pandas.read_csv('../Test_knight.csv')
    columns_to_standardize2 = df2.select_dtypes(include=['float64', 'int64']).columns
    scaler2 = StandardScaler() 
    df_standardized2 = df2.copy()
    df_standardized2[columns_to_standardize2] = scaler2.fit_transform(df2[columns_to_standardize2])


    plt.scatter(sith_data['Empowered'], sith_data['Stims'], color='red', alpha=0.6, label='Sith')
    plt.scatter(jedi_data['Empowered'], jedi_data['Stims'], color='blue', alpha=0.6, label='Jedi')
    plt.xlabel("Empowered")
    plt.ylabel("Stims")
    plt.legend()
    plt.show()

    plt.scatter(df_standardized2['Empowered'], df_standardized2['Stims'], color='green', alpha=0.6, label='Knight')
    plt.xlabel("Empowered")
    plt.ylabel("Stims")
    plt.legend()
    plt.show()

main()