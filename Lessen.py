from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio, logging
from config import my_token

logging.basicConfig(level=logging.INFO)

bot = Bot(token = my_token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("""Приветствую, дорогой пользователь! 👋
    
Я ваш верный помощник, созданный для того, чтобы помогать вам находить нужную информацию на любые темы! 📚✨
Будь то быстрый ответ на вопрос, полезные советы или глубокий разбор интересующей вас темы — я всегда готов помочь.""")
    
    await message.answer('''Я могу:  
- Показать последние новости 📰 /news
- Предоставить курсы валют 💰  /currency
- Информация о боте /about
- Помоч /help
- Меню /menu''')
                
   

@dp.message(Command("help"))
async def help(message:types.Message):
    await message.answer('''бул help(жардам) дегенди билдирет

Вот список моих возможностей:  

- /start — Начать работу с ботом. Узнайте, как я могу помочь вам!  
- /help — Полный список команд и описания их функций.  
- /menu — Показывает главное меню с выбором доступных опций.  
- /about — Узнайте, кто я и зачем я здесь!  

Дополнительно, вы можете использовать следующие команды для быстрого доступа:  
- /news — Получить актуальные новости дня.  
- /currency — Узнать текущие курсы валют.  
- /FAQ — Ответы на популярные вопросы.  
- /contacts — Контактная информация для связи.

Если у вас есть вопросы или предложения, смело обращайтесь!''')
    

@dp.message(Command("menu"))
async def menu(message:types.Message):
    await message.answer('''Главное меню:  
Выберите интересующий вас раздел.


Я могу:  
- Показать последние новости 📰 /news
- Предоставить курсы валют 💰  /currency
- Информация о боте /about
- Помоч /help''')
    

@dp.message(Command("about"))
async def about(message:types.Message):
    await message.answer('''

О боте:  

Этот бот создан для того, чтобы упростить вашу жизнь, предоставляя быстрый доступ к нужной информации! 🌐  
Я могу помочь вам:  
- Следить за новостями 📰  
- Узнавать актуальные курсы валют 💵  
- Отвечать на ваши вопросы ❓  

Моя миссия — быть вашим надёжным информационным спутником. Если у вас есть идеи или предложения, как меня улучшить, пожалуйста, напишите!''')


@dp.message(Command("news"))
async def news(message:types.Message):
    await message.answer('''

Сегодняшние главные новости:  

1️⃣ Курс доллара вырос на 2%, экономика адаптируется к изменениям.  
2️⃣ Технологические гиганты обсуждают развитие искусственного интеллекта.  
3️⃣ В мире спорта: сборная одержала победу в финале.  

Хотите узнать больше? Напишите запрос или уточните тему!''')
    

@dp.message(Command("currency"))
async def currency(message:types.Message):
    await message.answer('''Актуальные курсы валют на сегодня:  

- 💵 Доллар США: 85₽  
- 💶 Евро: 90₽  
- 🪙 Биткоин: 3,500,000₽  

Данные обновляются ежедневно. Напишите, если хотите узнать курсы другой валюты!''')

async def main():
        
        await dp.start_polling(bot)
if __name__=='__main__':
    try:
         asyncio.run(main())
    except KeyboardInterrupt:
        print('Завершение работы бота.')
