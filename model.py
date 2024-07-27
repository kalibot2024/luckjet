from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

class Predictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
    
    def predict(self, features):
        return self.model.predict([features])[0]
