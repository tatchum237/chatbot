from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean

CORPUS_FILE = "chat.txt"
chatbot = ChatBot("Chatpot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3')

trainer = ListTrainer(chatbot)
cleaned_corpus = clean(CORPUS_FILE)
trainer.train(cleaned_corpus)

exit_conditions = (":q", "quit", "exit")

name = input("Enter Your Name: ")
print("Bot 🪴: Welcome to the Bot Service "+ name +"! Let me know how can I help you?")

while True:
    query = input(name+': ')
    response = chatbot.get_response(query)
    if query in exit_conditions:
        break
    else:
        if query.upper() == 'BYE':
            print('Bot 🪴: Bye')
            break
        else:
            if query.upper() == 'OKAY':
                print('Bot 🪴: Of course')
                break
            else:
                if response.confidence > 0.0:
                    print(f"Bot 🪴: {response.text}")
                else:
                    print('I am sorry, but I do not understand. I am still learning.')