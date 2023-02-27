
import telebot

token = 'TOKEN'

bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    if message.text == "/start":

        bot.reply_to(message, "Привет дружок пирожок, я Исторический бот. Я помогу тебе проверить твои знания по истории. Начинаем!")

    if message.text == "/bye":

        bot.reply_to(message,  "Пока, приходи снова! :)")    

    if message.text == "/first":

        bot.reply_to(message,  "В каком году началась вторая мировая война?")

        bot.register_next_step_handler(message, first)

    if message.text == "/second":

        bot.reply_to(message,  "В каком году началась русско-французская война?")

        bot.register_next_step_handler(message, second)

    if message.text == "/third":

        bot.reply_to(message,  "В каком году распался Советский Союз?")

        bot.register_next_step_handler(message, third)

    if message.text == "/fourth":

        bot.reply_to(message,  "В каком году отменили крепостное право на Руси?")

        bot.register_next_step_handler(message, fourth)

    if message.text == "/fifth":

        bot.reply_to(message,  "В каком году был основан Советский Союз?")

        bot.register_next_step_handler(message, fifth)

@bot.message_handler(content_types=['text'])

def first(message):

    if message.text == "1939":

        bot.reply_to(message, "Молодец, ты совершенно прав!")

    else:

        bot.reply_to(message, "К сожалению нет, ведь вторая мировая война началась в 1939 году. Я верю, что ты запомнишь! :)")

@bot.message_handler(content_types=['text'])

def second(message):

    if message.text == "1812":

        bot.reply_to(message, "Действительно: русско-французская война произошла в 1812 году.")

    else:

        bot.reply_to(message, "К сожалению нет, ведь русско-французская война началась в 1812 году. Я верю, что ты запомнишь! :)")

@bot.message_handler(content_types=['text'])

def third(message):

    if message.text == "1991":

        bot.reply_to(message, "Молодец, ты совершенно прав!")

    else:

        bot.reply_to(message, "Ответ неверен, ведь Советский Союз распался в 1991 году. Я верю, что ты запомнишь! :)")

@bot.message_handler(content_types=['text'])

def fourth(message):

    if message.text == "1861":

        bot.reply_to(message, "Молодец, ты совершенно прав! Крепостное право действительно отменили в 1861 году.")

    else:

        bot.reply_to(message, "Неверно: крепостное право отменили в 1861 году. Я верю, что ты запомнишь! :)")

@bot.message_handler(content_types=['text'])

def fifth(message):

    if message.text == "1922":

        bot.reply_to(message, "Молодец, ты совершенно прав! Советский Союз и вправду был основан в 1922 году.")

    else:

        bot.reply_to(message, "К сожалению нет, ведь Советский Союз был основан в 1922 году. Я верю, что ты запомнишь! :)")

bot.polling(none_stop=True, interval=0)
