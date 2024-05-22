from telebot import TeleBot
from data import ProfitData

profit_data = ProfitData()
received_profits = False

def handle_start(bot: TeleBot, message):
    global received_profits
    received_profits = False
    bot.reply_to(message, "Привет! Перешлите мне сообщения с профитами, и я посчитаю КПД. Отправьте /done, когда закончите.")

def handle_message(bot: TeleBot, message):
    global received_profits
    try:
        lines = message.text.split('\n')
        amount_line = next((line for line in lines if "Сумма:" in line), None)
        
        if amount_line is None:
            return 

        amount_str = amount_line.split('Сумма:')[1].strip().split(' ')[0].replace('.', '').replace(',', '.')
        amount = float(amount_str)

        is_tp = 'ТП' in message.text

        profit_data.add_profit(amount, is_tp)
        received_profits = True
    except ValueError:
        bot.reply_to(message, "Не удалось распознать сумму профита.")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")

def handle_check(bot: TeleBot, message):
    global received_profits
    if received_profits:
        bot.reply_to(message, "Профит добавлен. Отправьте /stats для просмотра статистики.")
        received_profits = False
    else:
        bot.reply_to(message, "Не было добавлено ни одного профита. Перешлите сообщения с профитами и затем отправьте /done.")

def handle_stats(bot: TeleBot, message):
    stats = profit_data.get_statistics()
    stats_message = (
        f"КПД - {stats['efficiency']:.2f}\n"
        f"Средний ОБЩИЙ профит - {stats['average_total_profit']:,.0f}₽\n"
        f"Средний ТП профит - {stats['average_tp_profit']:,.0f}₽\n\n"
        f"Общее количество профитов: {stats['total_count']}\n"
        f"Количество по ТП: {stats['tp_count']}\n\n"
        f"Общий профит: {stats['total_profit']:,.0f}₽\n"
        f"Общий профит по ТП: {stats['tp_profit']:,.0f}₽"
    ).replace(',', '.')
    bot.reply_to(message, stats_message)
