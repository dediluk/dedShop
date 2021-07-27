from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging
import requests
import random, yandex_weather_api

TOKEN = '1448157517:AAHEqEeQVbYU7M9FqPHfREzULD0QxrdPWSI'
updater = Updater(token=TOKEN, use_context=True)
updater.bot.setWebhook('https://goodmorningcountrybot.herokuapp.com/' + TOKEN)

dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я бот, поговори со мной, пожалуйста")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def caps(update, context):
    text_caps = ''.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


def weather(update, context):
    re = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q=Minsk&lang=ru&appid=6fdf3de8bbe6794ac7a7cb712babb4b4&units=metric').json()
    text = '🌤Погода: {}\n Температура: {}°C \n Ощущается как: {}°C \n '.format(
        re['weather'][0]['description'].title(), round(re['main']['temp']), round(re['main']['feels_like']))
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)


def rates(update, context):
    re = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.0/public/rates').json()
    text = '💲Курс доллара: \n\t\t Покупка: {} \n\t\t Продажа:{} \n💶Курс евро: \n\t\t Покупка: {} \n\t\t Продажа:{} \n'.format(
        re['rates'][5]['sellRate'], re['rates'][5]['buyRate'], re['rates'][4]['sellRate'], re['rates'][4]['buyRate'])
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


rates_handler = CommandHandler('rates', rates)
dispatcher.add_handler(rates_handler)


# def hi(update, context):
#     re = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.0/public/rates').json()
#     text_rates = '💲Курс доллара: \n\t\t Покупка: {} \n\t\t Продажа:{} \n💶Курс евро: \n\t\t Покупка: {} \n\t\t Продажа:{} \n'.format(
#         re['rates'][5]['sellRate'], re['rates'][5]['buyRate'], re['rates'][4]['sellRate'], re['rates'][4]['buyRate'])
#     re = requests.get(
#         'https://api.openweathermap.org/data/2.5/weather?q=Minsk&lang=ru&appid=6fdf3de8bbe6794ac7a7cb712babb4b4&units=metric').json()
#     text_weather = '🌤Погода: {}\n Температура: {}°C \n Ощущается как: {}°C \n '.format(
#         re['weather'][0]['description'].title(), round(re['main']['temp']), round(re['main']['feels_like']))
#     context.bot.send_message(chat_id=update.effective_chat.id, text=text_rates + text_weather)
#
#
# hi_handler = CommandHandler('hi', hi)
# dispatcher.add_handler(hi_handler)


def hi(update, context):
    re = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.0/public/rates').json()
    text_rates = '💲Курс доллара: \n\t\t Покупка: {} \n\t\t Продажа:{} \n💶Курс евро: \n\t\t Покупка: {} \n\t\t Продажа:{} \n'.format(
        re['rates'][5]['sellRate'], re['rates'][5]['buyRate'], re['rates'][4]['sellRate'], re['rates'][4]['buyRate'])
    re = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q=Minsk&lang=ru&appid=6fdf3de8bbe6794ac7a7cb712babb4b4&units=metric').json()
    text_weather = '🌤Погода: {}\n Температура: {}°C \n Ощущается как: {}°C \n '.format(
        re['weather'][0]['description'].title(), round(re['main']['temp']), round(re['main']['feels_like']))
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_rates + text_weather)


hi_handler = MessageHandler(Filters.text, hi)
dispatcher.add_handler(hi_handler)


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    result = list()
    result.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, result)


inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Извините, я не знаю эту команду')


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()
