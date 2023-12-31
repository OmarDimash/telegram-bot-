import telebot
import openai

bot = telebot.TeleBot("5612999006:AAEVBF-t0yo3Or7Mg2BkLl_ZPoZgBNMxQxQ")
openai.api_key = "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"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    text = 'Привет! Я бот, который может сгенерировать текст на любую тему. Для рекламы пишите мне в direct: [My instagram](https://instagram.com/_.omarrov.d.s._?igshid=NTc4MTIwNjQ2YQ==).'
    bot.send_message(chat_id, text, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def generate_text(message):
    # Получаем текст сообщения
    text = message.text

    # Генерируем ответ с помощью OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Отправляем ответ пользователю
    bot.reply_to(message, response.choices[0].text)


bot.polling()