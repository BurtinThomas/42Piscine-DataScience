class Chevalier:
    def __init__(self, name, tableau_truth, tableau_prediction):
        self.tableau_truth = tableau_truth
        self.tableau_prediction = tableau_prediction
        self.name = name

    def precision(self):
        VP = 0
        FP = 0
        for truth, prediction in zip(self.tableau_truth, self.tableau_prediction):
            if(prediction == self.name and prediction == truth):
                VP += 1
            elif(prediction == self.name and prediction != truth):
                FP +=1
        precision = VP / (VP + FP)
        return round(precision, 2)

    def recall(self):
        VP = 0
        FN = 0
        for truth, prediction in zip(self.tableau_truth, self.tableau_prediction):
            if(truth == self.name and prediction == truth):
                VP += 1
            elif(truth == self.name and prediction != truth):
                FN +=1
        precision = VP / (VP + FN)
        return round(precision, 2)

    def total(self):
        len = 0
        for i in self.tableau_truth:
            if i == self.name:
                len += 1
        return len

    def f1_score(self):
        f1_score = (2 * self.precision() * self.recall()) / (self.precision() + self.recall())
        return round(f1_score, 2)