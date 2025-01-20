import pandas
import numpy
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA 

def main():
    df = pandas.read_csv('Test_Knight.csv')
    variances = df.var()
    variance_pourcentage = (variances / variances.sum()) * 100
    print(variance_pourcentage)

    print("------------------------------")

    standart_df = StandardScaler().fit_transform(df)
    pca = PCA(0.99)
    pc = pca.fit_transform(standart_df)
    cumulative_variance = numpy.cumsum(pca.explained_variance_ratio_)
    cumulative_variance = cumulative_variance * 100
    print(cumulative_variance)

    plt.plot(range(1, len(pca.explained_variance_ratio_) + 1), cumulative_variance)
    plt.xlabel('Number of Components')
    plt.ylabel('Percentage of Variance Explained (%)')
    plt.show()

main()