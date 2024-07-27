import logging
from datetime import datetime, timedelta
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TOKEN
from data_handler import collect_data, prepare_data
from model import Predictor

# Configurer le logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialiser les composants du modèle
df = collect_data()
X, y = prepare_data(df)
predictor = Predictor()
predictor.train(X, y)

# Liste des utilisateurs autorisés (ID Telegram)
AUTHORIZED_USERS = [5136550250]  # Remplacez par les IDs Telegram des utilisateurs autorisés

def restricted(func):
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in AUTHORIZED_USERS:
            logging.warning(f"Unauthorized access denied for {user_id}.")
            update.message.reply_text("Vous n'êtes pas autorisé à utiliser cette commande.")
            return
        return func(update, context, *args, **kwargs)
    return wrapped

def start(update, context):
    welcome_message = (
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n"
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n"
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n"
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n"
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n"
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n"
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n"
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n"
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n"
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n"
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n"
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n"
        "🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫🛫\n\n"
        "Bienvenue sur le bot de prédiction des cotes de Lucky Jet! "
        "Envoyez-moi les caractéristiques sous la forme : feature1,feature2,feature3 "
        "ou utilisez les commandes /strategy1, /strategy2, /strategy3 pour des conseils "
        "ou /predict pour des exemples de prédictions.\n\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬\n"
        "🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬"
    )
    update.message.reply_text(welcome_message)

@restricted
def handle_message(update, context):
    message = update.message.text
    try:
        features = list(map(float, message.split(',')))
        if len(features) != 3:
            raise ValueError("Nombre incorrect de caractéristiques.")
        prediction = predictor.predict(features)
        update.message.reply_text(f'La prédiction des cotes est : {prediction:.2f}')
    except ValueError as ve:
        logging.error(f"Erreur de valeur : {repr(ve)}")
        update.message.reply_text(f'Erreur : {str(ve)}')
    except Exception as e:
        logging.error(f"Erreur lors de la prédiction : {repr(e)}")
        update.message.reply_text(f'Erreur : {str(e)}')

@restricted
def strategy1(update, context):
    update.message.reply_text(
        "Stratégie du calme : Parier et retirer à des multiplicateurs faibles mais réguliers, comme 1.09, pour éviter les pertes majeures."
    )

@restricted
def strategy2(update, context):
    update.message.reply_text(
        "Miser x100+ : Placer des paris en fonction des historiques des multiplicateurs élevés et viser des gains substantiels en retirant à des multiplicateurs élevés."
    )

@restricted
def strategy3(update, context):
    update.message.reply_text(
        "Double Up : Doubler la mise après chaque perte jusqu'à un gain, puis revenir à la mise initiale."
    )

@restricted
def predict(update, context):
    example_data = [
        [0.5, 100, 5],
        [1.0, 200, 10],
        [1.5, 300, 15]
    ]
    now = datetime.now()
    predictions = []
    for i, features in enumerate(example_data):
        prediction = predictor.predict(features)
        prediction_time = (now + timedelta(minutes=i)).strftime("%H:%M:%S")
        predictions.append(f"{prediction_time} : x{prediction:.2f}")
    
    response = "\n".join(predictions)
    update.message.reply_text(response)

def generate_prediction(context):
    job = context.job
    bot = context.bot
    chat_id = job.context

    now = datetime.now()
    signals = []
    for i in range(13):  # Générer 13 prédictions
        current_time = (now + timedelta(minutes=i)).strftime("%H:%M:%S")
        prediction = predictor.predict([1.0, 200, 10])  # Utiliser des caractéristiques fictives pour les prédictions
        signal = f"{current_time} : x{prediction:.2f}"
        signals.append(signal)

    message = f"lucky jet predictor\n\nsignaux du : {now.strftime('%d/%m/%y')}\n\n👇👇👇👇\n\n" + "\n\n".join(signals)
    bot.send_message(chat_id=chat_id, text=message)

@restricted
def start_predictions(update, context):
    chat_id = update.message.chat_id
    context.job_queue.run_repeating(generate_prediction, interval=5*60, first=0, context=chat_id, name=str(chat_id))  # interval set to 5 minutes
    update.message.reply_text('Prédictions automatiques démarrées toutes les 5 minutes.')

@restricted
def stop_predictions(update, context):
    chat_id = update.message.chat_id
    current_jobs = context.job_queue.get_jobs_by_name(str(chat_id))
    for job in current_jobs:
        job.schedule_removal()
    update.message.reply_text('Prédictions automatiques arrêtées.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dp.add_handler(CommandHandler("strategy1", strategy1))
    dp.add_handler(CommandHandler("strategy2", strategy2))
    dp.add_handler(CommandHandler("strategy3", strategy3))
    dp.add_handler(CommandHandler("predict", predict))
    dp.add_handler(CommandHandler("start_predictions", start_predictions))
    dp.add_handler(CommandHandler("stop_predictions", stop_predictions))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
