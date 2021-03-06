# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Creating a new instance of a ChatBot
bot = ChatBot(
    'Feedback Learning Bot',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter'
)

DEFAULT_SESSION_ID = bot.default_session.id

def get_feedback():
    from chatterbot.utils import input_function

    text = input_function()

    if 'Yes' in text:
        return True
    elif 'No' in text:
        return False
    else:
        print('BOT: Please type either "Yes" or "No"')
        return get_feedback()

print('BOT: Please, say something')

# The following loop will execute each time the user enters input
while True:
    try:
        input_statement = bot.input.process_input_statement()
        statement, response = bot.generate_response(input_statement, DEFAULT_SESSION_ID)

        # print('BOT: {}'.format(response, input_statement))
        print('BOT: Is "{}" this a coherent response to "{}"?'.format(response, input_statement))

        if get_feedback():
            bot.learn_response(response, input_statement)

        # bot.output.process_response("BOT: " + str(response))
        print("BOT: "+str(response.text))

        # Update the conversation history for the bot
        # It is important that this happens last, after the learning step
        bot.conversation_sessions.update(
            bot.default_session.id_string,
            (statement, response, )
        )

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break