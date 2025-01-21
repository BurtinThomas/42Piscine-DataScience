from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score
import matplotlib.pyplot as plt


def main():
    # Charger les données d'entraînement
    Train_knight = pd.read_csv("Train_knight.csv")
    features = Train_knight.drop("knight", axis=1)
    features = Train_knight[['Hability', 'Agility', 'Reactivity', 'Push', 'Survival', 'Blocking', 'Deflection', 'Mass', 'Sprint', 'Attunement']]
    result = Train_knight["knight"]
    
    #spliter les donner (70% pour l'entrainement et 30% pour le teste)
    X_train, X_test, y_train, y_test = train_test_split(features, result, test_size=0.3, random_state=42)
    
    # Entraîner le modèle
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)
    
    # Faire des prédictions
    y_pred = model.predict(X_test)

    with open('KNN.txt', 'w') as KNN_file:
        for value in y_pred:
            KNN_file.write(f"{value}\n")
    
    f1 = round(f1_score(y_test, y_pred, average="weighted"), 2)
    print(f"F1-score: {f1}")
    print(f"La performance du model est : {f1 * 100} %")

    #teste du meilleur K
    accuracy = []
    X_train, X_test, y_train, y_test = train_test_split(features, result, test_size=0.3, random_state=42)
    for k in range(1, 50):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy.append(accuracy_score(y_test, y_pred))
    print(accuracy)

    plt.plot(range(1, 50), accuracy)
    plt.xlabel('K')
    plt.ylabel('Accuracy')
    plt.show()

main()