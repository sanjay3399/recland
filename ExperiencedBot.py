from chatterbot import ChatBot
import logging

# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    'Example Bot',
    trainer='chatterbot.trainers.UbuntuCorpusTrainer',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter'
)

# Start by training our bot with the Ubuntu corpus data
chatbot.train()

while True:
    try:
        input_statement = raw_input("USER: ")#chatbot.input.process_input_statement()
        # Now let's get a response to a greeting
        response = chatbot.get_response(input_statement)
        print("BOT: " + response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break