import pandas

def main():
    df = pandas.read_csv('../Train_knight.csv')
    df['knight_encoded'] = df['knight'].map({'Jedi': 1, 'Sith': 0})
    df = df.drop('knight', axis=1)
    cor = df.corr()
    cor_sorted = cor['knight_encoded'].sort_values(ascending=False)
    print(cor_sorted)

main()