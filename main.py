import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import numpy as np

# Étape 1 : Collecte de données simulée
def collect_data():
    data = {
        'feature1': np.random.rand(100),
        'feature2': np.random.rand(100),
        'feature3': np.random.rand(100),
        'target': np.random.uniform(1, 3, 100)
    }
    df = pd.DataFrame(data)
    return df

# Préparation des données
df = collect_data()
X = df[['feature1', 'feature2', 'feature3']]
y = df['target']

# Séparation des données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Fonction de prédiction
def predict(features):
    prediction = model.predict([features])
    return prediction[0]

# Token d'API du bot Telegram
TOKEN = '7297828366:AAFvfMfNGsZ_Xm6pEpVCR482RlxsUqiG0-4'

def start(update, context):
    update.message.reply_text(
        "Bienvenue sur le bot de prédiction des cotes de Lucky Jet! "
        "Envoyez-moi les caractéristiques sous la forme : feature1,feature2,feature3 "
        "ou utilisez les commandes /strategy1, /strategy2, ou /strategy3 pour des conseils."
    )

def handle_message(update, context):
    message = update.message.text
    try:
        features = list(map(float, message.split(',')))
        if len(features) != 3:
            raise ValueError("Nombre incorrect de caractéristiques.")
        prediction = predict(features)
        update.message.reply_text(f'La prédiction des cotes est : {prediction:.2f}')
    except Exception as e:
        update.message.reply_text(f'Erreur : {str(e)}')

def strategy1(update, context):
    update.message.reply_text(
        "Stratégie du calme : Parier et retirer à des multiplicateurs faibles mais réguliers, comme 1.09, pour éviter les pertes majeures."
    )

def strategy2(update, context):
    update.message.reply_text(
        "Miser x100+ : Placer des paris en fonction des historiques des multiplicateurs élevés et viser des gains substantiels en retirant à des multiplicateurs élevés."
    )

def strategy3(update, context):
    update.message.reply_text(
        "Double Up : Doubler la mise après chaque perte jusqu'à un gain, puis revenir à la mise initiale."
    )

def predict_next_scores(update, context):
    # Simuler les futures caractéristiques pour les prédictions
    future_features = np.random.rand(3)
    prediction = predict(future_features)
    update.message.reply_text(
        f'La prédiction des cotes pour les prochaines caractéristiques {future_features} est : {prediction:.2f}'
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("strategy1", strategy1))
    dp.add_handler(CommandHandler("strategy2", strategy2))
    dp.add_handler(CommandHandler("strategy3", strategy3))
    dp.add_handler(CommandHandler("predict_next", predict_next_scores))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
