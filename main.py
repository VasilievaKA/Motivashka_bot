import time

from telebot import types
import telebot
from telegram import message
import random
import schedule
import time

TOKEN = '2091780548:AAE8OC8kWSa7U0lE2eVaqErooH1SM08WjOI'
bot = telebot.TeleBot('2091780548:AAE8OC8kWSa7U0lE2eVaqErooH1SM08WjOI')
for_schastie=['Для счастья надо либо уменьшить желания, либо увеличить средства.',
             'Для счастья нужно что-то делать, что-то любить и во что-то верить.',
             'Единственное счастье в жизни — это постоянное стремление вперед.',
             'Самые счастливые те, кто понимает, что хорошее происходит с ними тогда, когда они позволяют этому случиться.',
             'Самый счастливый человек тот, кто дарит счастье наибольшему числу людей.',
             'Счастье — как здоровье: когда его не замечаешь, значит оно есть.',
             'Счастье — не данность, за него надо постоянно бороться. И думаю, когда оно приходит, важно уметь его принять.',
             'Счастье — это когда ваши действия согласуются с вашими словами.']
for_study = ['Если ты сейчас уснешь, то тебе приснится твоя мечта, но если ты сейчас будешь учиться, то воплотишь свою мечту в жизнь.',
             'Если ты работаешь над поставленными целями, то эти цели будут работать на тебя.',
             'Боль учения лишь временна. Боль незнания – невежество – вечна.',
             'Ты должен уже сегодня относиться к себе как к человеку, добившемуся успеха.',
             'Не все могут по-настоящему преуспеть во всем. Но успех приходит только с самосовершенствованием и решительностью.',
             'Если ты не идешь сегодня, завтра тебе придется бежать.',
             'Запомни, как бы плохо все ни было, ты молодец, и ты все сможешь осилить.',
             'Не останавливайся! Ты на верном пути.']
for_life = ['Возьми на себя ответственность за свою жизнь. Знай, что только ты можешь привести себя туда, куда ты хочешь, и никто больше.',
            'Не жалей о том, что сделал, жалей о том, чего ты не сделал.',
            'Живи! Жизнь коротка.',
            'Делай то, что нравится тебе.',
            'Пошли они все! Ты самый классный! Не сомневайся в этом!',
            'В жизни есть два правила: № 1 – Никогда не сдавайтесь, № 2 – Всегда помните правило № 1.',
            'Начать - значит перестать говорить об этом и начать делать!',
            'Не бойся идти туда, где тебе страшно! Поверь, тебе нужно именно туда.',
            'Дорогу осилит идущий.']
for_love = ['Помни, что надо быть самим собой, чтобы уметь любить.',
            'Не бойся разговаривать с любимым!',
            'Жизнь прекрасна если в ней есть любовь и понимание!',
            'Любовь и отношения - сложная работа, на которой обязаны трудиться оба.',
            'Истинная любовь не знает пресыщения. Будучи всецело духовной, она не может охладиться.',
            'Не давай волю сердцу думать быстрее мозга.',
            'Будь с тем, с кем ты можешь расти.',
            'Твой партнер - это зеркало, показывающее то, что тебе нужно узнать о себе.']
for_loveyourself = ['Любить себя - это начало пожизненного романа.',
                    'Человек не может чувствовать себя комфортно без собственного одобрения.',
                    'Желание быть кем-то другим - пустая трата того, кем ты являешься.',
                    'Никогда не поздно быть тем, кем ты мог быть.',
                    'Вся любовь начинается с внутренней любви.',
                    'Посмотри в зеркало и ты увидишь самого уникального человека на Земле.',
                    'Люби себя и будь доволен невероятной жизнью, которую ты создаешь.',
                    'Когда ты любишь себя, ты принимаешь лучшие решения.']
for_foraday = ['Ты со всем справишься! Я в тебя верю.',
               'Нет ничего невозможного, все в твоих руках!',
               'Сегодня будет очень продуктивный день.',
               'Лучше жалеть о том, что сделал.',
               'Верь в свои силы, ведь ты можешь свернуть горы.']


@bot.message_handler(content_types=['text'])
def get_text_messages(massage):
    if massage.text == "/start":
        bot.send_message(massage.from_user.id, "Для начала напиши Привет")

    if massage.text == "Привет":
        keyboard = types.InlineKeyboardMarkup()
        key_schastie = types.InlineKeyboardButton(text='О счастье ✨', callback_data='schastie')
        keyboard.add(key_schastie)
        key_study = types.InlineKeyboardButton(text='Для учебы и работы 📚', callback_data='study')
        keyboard.add(key_study)
        key_life = types.InlineKeyboardButton(text='О жизни 🕛', callback_data='life')
        keyboard.add(key_life)
        key_love = types.InlineKeyboardButton(text='О любви ❤', callback_data='love')
        keyboard.add(key_love)
        key_loveyourself = types.InlineKeyboardButton(text='О любви к себе 🥰', callback_data='loveyourself')
        keyboard.add(key_loveyourself)
        key_foraday = types.InlineKeyboardButton(text='На каждый день 🏙', callback_data='foraday')
        keyboard.add(key_foraday)
        key_new = types.InlineKeyboardButton(text='Хочу добавить что-то свое', callback_data='new')
        keyboard.add(key_new)
        bot.send_message(massage.from_user.id, text='Выбери мотивашку на сегодня', reply_markup=keyboard)

    elif massage.text == "/help":
        bot.send_message(massage.from_user.id, "Напиши Привет")
    else:
        bot.send_message(massage.from_user.id, "Я тебя не понимаю. Напиши /help.")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "schastie":
            msg = random.choice(for_schastie)
        elif call.data == "study":
            msg = random.choice(for_study)
        elif call.data == "life":
            msg = random.choice(for_life)
        elif call.data == "love":
            msg = random.choice(for_love)
        elif call.data == "loveyourself":
            msg = random.choice(for_loveyourself)
        elif call.data == "foraday":
            msg = random.choice(for_foraday)
        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)