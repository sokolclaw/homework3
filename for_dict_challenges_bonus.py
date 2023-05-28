"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            'id': uuid.uuid4(),
            'sent_at': sent_at,
            'sent_by': random.choice(users_ids),
            'reply_for': random.choice(
                [
                    None,
                    (
                        random.choice([m['id'] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            'seen_by': random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            'text': lorem.sentence(),
        })
    return messages


def max_count_messages(all_messages):
    all_users_messeges = {}
    before_ides = [i['sent_by'] for i in all_messages]
    ides = list(set(before_ides))
    for id in ides:
        a = before_ides.count(id)
        all_users_messeges[str(id)] = a
    max_message = max(all_users_messeges.values())
    print(ides)
    print(all_users_messeges)
    for value, key in zip(all_users_messeges.values(), all_users_messeges.keys()):
        if max_message == value:
            return key   
    return None
        
def max_answers_on_messages(all_messages):
    all_replies = {}
    before_replies = [i['reply_for'] for i in all_messages if i != None]
    replies = list(set(before_replies))
    for reply in replies:
        if reply != None:
            a = before_replies.count(reply)
            all_replies[str(reply)] = a
    max_replies = max(all_replies.values())
    number_of_message = ''
    for key, value in all_replies.items():
        if max_replies == value and key != None:
                number_of_message = key
    for message in all_messages:
        id, data, user, repost, watchers, text = message.values()
        if number_of_message == str(id):
            return user
    return None

def max_saw_messages(all_messages):
    users = [message['sent_by'] for message in all_messages]
    watchers_list = [len(message['seen_by']) for message in all_messages]
    max_watchers = max(watchers_list)
    for user, watchers in zip(users, watchers_list):
        if max_watchers == watchers:
            return user

def data_messages_count(all_messages):
    message_time = [str(message['sent_at']).split() for message in all_messages]
    hour_time = [time[1].split(':') for time in message_time]
    morning_messages = 0
    afternoon_messages = 0
    evening_messages = 0
    for hour in hour_time:
        if 4 <= int(hour[0]) < 12:
            morning_messages += 1
        if 12 <= int(hour[0]) < 18:
            afternoon_messages += 1
        if 18 <= int(hour[0]) < 24:
            evening_messages += 1
    when_more = 'утром'
    if afternoon_messages > morning_messages and afternoon_messages > evening_messages:
        when_more = 'днем'
    if evening_messages > morning_messages and evening_messages > afternoon_messages:
        when_more = 'вечером'
    return f'Сообщений больше: {when_more}'

# def find_longest_tread(all_messages):
#     ids = [i['id'] for i in all_messages]
#     replies = [i['reply_for'] for i in all_messages]
#     first_id = ''
#     max_replies = 0
#     count = 0
#     for id, reply in zip(ids, replies):
#         while reply != None:
#             count += 1
#             id = reply

#         if count > max_replies:
#             max_replies = count
#             first_id = str(id)
#     return first_id
    

if __name__ == '__main__':
    # print(generate_chat_history())
    # print(max_count_messages(generate_chat_history()))
    # print(max_answers_on_messages(generate_chat_history()))
    # print(max_saw_messages(generate_chat_history()))
    # print(data_messages_count(generate_chat_history()))
    print(find_longest_tread(generate_chat_history()))