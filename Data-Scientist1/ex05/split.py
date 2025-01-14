import pandas
from sklearn.model_selection import train_test_split


def split_csv(file_path, split_ratio):
    df = pandas.read_csv(file_path)
    
    train_data, val_data = train_test_split(df, train_size=split_ratio, random_state=42)
    
    train_data.to_csv('Training_knight.csv', index=False)
    val_data.to_csv('Validation_knight.csv', index=False)
    
    print(f"Les données ont été divisées :")
    print(f" - {len(train_data)} lignes dans Training_knight.csv ({split_ratio * 100}% des données)")
    print(f" - {len(val_data)} lignes dans Validation_knight.csv ({(1 - split_ratio) * 100}% des données)")


def main():
    split_csv('../Train_knight.csv', 0.8)

main()
