import csv
from telegram import Bot

# Replace the API token and chat ID with your own values
api_token = '6828057178:AAHqPwGLJMPdM1_B1FQarf9a6_4O3j0XU88'
chat_id = '@ER_BX'

bot = Bot(api_token)

members = bot.get_chat_members_count(chat_id)
offset = 0
limit = 200
all_members = []

while offset <= members:
    chat_members = bot.get_chat_members(chat_id, limit=limit, offset=offset)
    all_members.extend(chat_members)
    offset += limit

with open('group_members.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'first_name', 'last_name', 'username']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for member in all_members:
        writer.writerow({'id': member.user.id, 'first_name': member.user.first_name, 'last_name': member.user.last_name, 'username': member.user.username})
