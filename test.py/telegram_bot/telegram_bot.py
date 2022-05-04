import telebot
bot = telebot.TeleBot('5128203456:AAF0bktGNHjSUZCyUjFUUBhnZ0R4STX5Njw')

@bot.message_handler(commands=['start'])
def start (message):
    mess = f'привет , <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b> , я телеграм бот  , и меня создал мой создатель Аблай \nУ меня есть такие команды как : \nПривет \nКак твои дела?\nКакая сегодня погода ? \nСделай мне комплимент))) '
    bot.send_message(message.chat.id , mess ,  parse_mode='html')

while True:
    @bot.message_handler()
    def get_user_text(message):

        if message.text == 'Привет':
            bot.send_message(message.chat.id , f'и тебе привет мой бро ')

        elif message.text == 'Как твои дела?':
            bot.send_message(message.chat.id , f'Отлично , спасибо что спросили ))) ' )

        elif message.text == 'Какая сегодня погода ?':
            bot.send_message(message.chat.id , f'Сегодня погода временами пасмурная , в горных районах ожидаются дожди ')

        elif message.text == 'Сделай мне комплимент)))':
            bot.send_message (message.chat.id , f'Ты выглядиь безупречно ' )

        elif message.text == 'Спасибо':
            bot.send_message (message.chat.id , f'На здоровье)' )

        else:
            bot.send_message (message.chat.id , f'Извиите такой команды у меня пока нет ( ')




    bot.polling(non_stop=True)

