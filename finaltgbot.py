import telebot,os,random

bot=telebot.TeleBot("TOKEN")
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
        bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")



@bot.message_handler(commands=['help'])
def send_help(message):
       bot.reply_to(message,"Все команды:/start /bye /help /hello /coinflip")

@bot.message_handler(commands=['mem'])
def send_mem(message):
       img_name=random.choice(os.listdir("mems"))
       with open(f'mems/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  
@bot.message_handler(commands=['warming'])
def send_help(message):
       bot.reply_to(message,"Глобальное потепление — это долгосрочное увеличение средней температуры Земли, которое в основном вызвано человеческой деятельностью. Основные факторы, способствующие глобальному потеплению, включают.Выбери причину,/w1,/w2,/w3")
@bot.message_handler(commands=['w1'])
def send_help(message):
       bot.reply_to(message,"Промышленная деятельность:Переход на чистые источники энергии,снижение выбросов парниковых газов,устойчивое управление отходами")
@bot.message_handler(commands=['w2'])
def send_help(message):
       bot.reply_to(message,"Устойчивое землепользование:– Внедрение практик, которые минимизируют воздействие на окружающую среду, таких как агролесоводство или органическое земледелие.")
@bot.message_handler(commands=['w3'])
def send_help(message):
       bot.reply_to(message,"Использование ископаемого топлива: Энергетический сектор, основанный на ископаемом топливе, является основным источником парниковых газов. Переход на возобновляемые источники энергии может помочь снизить эти выбросы.Использование ископаемого топлива: Энергетический сектор, основанный на ископаемом топливе, является основным источником парниковых газов. Переход на возобновляемые источники энергии может помочь снизить эти выбросы.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)


bot.polling()
