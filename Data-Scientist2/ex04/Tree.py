import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

def main():
    # Charger les données d'entraînement
    Train_knight = pd.read_csv("Train_knight.csv")
    features = Train_knight.drop("knight", axis=1)
    result = Train_knight["knight"]
    
    #spliter les donner (70% pour l'entrainement et 30% pour le teste)
    X_train, X_test, y_train, y_test = train_test_split(features, result, test_size=0.3, random_state=42)
    
    # Entraîner le modèle
    model = DecisionTreeClassifier(criterion="gini", max_depth=5, random_state=42)
    model.fit(X_train, y_train) 
    
    # Faire des prédictions
    y_pred = model.predict(X_test)

    with open('Tree.txt', 'w') as tree_file:
        for value in y_pred:
            tree_file.write(f"{value}\n")
    
    f1 = round(f1_score(y_test, y_pred, average="weighted"), 2)
    print(f"F1-score: {f1}")
    print(f"La performance du model est : {f1 * 100} %")

    plot_tree(model, filled=True, feature_names=X_train.columns, class_names=['Jedi', 'Sith'])
    plt.show()

main()
