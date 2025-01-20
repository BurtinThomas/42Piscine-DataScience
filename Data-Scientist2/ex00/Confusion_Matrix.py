from Chevalier import Chevalier
import seaborn as sns
import matplotlib.pyplot as plt

def read_file(path):
    with open(path, 'r') as fichier:
        tableau = [ligne.strip() for ligne in fichier]
        return tableau

def calcul_accuracy(tableau_truth, tableau_prediction):
    i = 0
    for truth, prediction in zip(tableau_truth, tableau_prediction):
        if prediction == truth:
            i += 1
    accuracy = i / len(tableau_truth)
    return accuracy

def calculer_matrice_confusion(tableau_truth, tableau_prediction):
    TN = FP = FN = VP = 0
    for truth, prediction in zip(tableau_truth, tableau_prediction):
        if truth == 'Sith' and prediction == 'Sith':
            TN +=1
        elif truth == 'Sith' and prediction == 'Jedi':
            FP +=1
        elif truth == 'Jedi' and prediction == 'Jedi':
            VP +=1
        elif truth == 'Jedi' and prediction == 'Sith':
            FN += 1
    return [[VP, FN], [FP, TN]]


def main():
    tableau_truth = read_file('truth.txt')
    tableau_prediction = read_file('predictions.txt')
    Jedi = Chevalier('Jedi', tableau_truth, tableau_prediction)
    Sith = Chevalier('Sith', tableau_truth, tableau_prediction)
    accuracy = calcul_accuracy(tableau_truth, tableau_prediction)
    matrix = calculer_matrice_confusion(tableau_truth, tableau_prediction)

    print("precision recall f1-score total")
    print(f"{Jedi.name} {Jedi.precision()} {Jedi.recall()} {Jedi.f1_score()} {Jedi.total()}")
    print(f"{Sith.name} {Sith.precision()} {Sith.recall()} {Sith.f1_score()} {Sith.total()}")
    print(f"accuracy {accuracy} {len(tableau_truth)}")
    print(matrix)
    
    sns.heatmap(matrix, annot=True, fmt='d', xticklabels=['Jedi', 'Sith'], yticklabels=['Jedi', 'Sith'])
    plt.xlabel('Prédictions')
    plt.ylabel('Vérités Réelles')
    plt.title('Matrice de Confusion')
    plt.show()
    

main()
