import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

def main():
    # Charger les données d'entraînement
    Train_knight = pd.read_csv("Train_knight.csv")
    features = Train_knight.drop("knight", axis=1)
    features = Train_knight[['Hability', 'Agility', 'Reactivity', 'Push', 'Survival', 'Blocking', 'Deflection', 'Mass', 'Sprint', 'Attunement']]
    result = Train_knight["knight"]
    
    #spliter les donner (70% pour l'entrainement et 30% pour le teste)
    X_train, X_test, y_train, y_test = train_test_split(features, result, test_size=0.3, random_state=42)
    
    # Entraîner le modèle
    voting = VotingClassifier(estimators=[
    ('tree', KNeighborsClassifier(n_neighbors=5)),
    ('knn', LogisticRegression(max_iter=1000)),
    ('svm', DecisionTreeClassifier(criterion="gini", max_depth=5, random_state=42))
    ], voting='hard')

    voting.fit(X_train, y_train)
    
    # Faire des prédictions
    y_pred = voting.predict(X_test)

    with open('volting.txt', 'w') as volting:
        for value in y_pred:
            volting.write(f"{value}\n")
    
    f1 = round(f1_score(y_test, y_pred, average="weighted"), 2)
    print(f"F1-score: {f1}")
    print(f"La performance du model est : {f1 * 100} %")


main()