import pandas as pd

def collect_data():
    """Simule la collecte de données historiques."""
    data = {
        'feature1': [0.5, 1.0, 1.5, 2.0, 2.5],
        'feature2': [100, 200, 300, 400, 500],
        'feature3': [5, 10, 15, 20, 25],
        'target': [1.1, 1.3, 1.2, 1.4, 1.5]  # Multiplicateur de gain simulé
    }
    df = pd.DataFrame(data)
    return df

def prepare_data(df):
    """Prépare les données pour l'entraînement du modèle."""
    X = df[['feature1', 'feature2', 'feature3']]
    y = df['target']
    return X, y
