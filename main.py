import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import requests
from vk_api import VkUpload

KEY = "24f2ea2a1a5c7430f8aea6ade9e197474b391b6d15a9e1aaa2fb0f52fcb1d61b2e815c65df362af0e21f2"


def main():
    vk_session = vk_api.VkApi(token=KEY)
    lp = VkBotLongPoll(vk_session, "200855805")
    session = requests.Session()
    for ev in lp.listen():
        if ev.type == VkBotEventType.MESSAGE_NEW:
            print(ev.obj)
            if ev.obj['text'] in ("мой гендер", "гендер", "Кто я", "Кто я?", "Гендер", "Мой гендер", "кто я", "кто я?"):
                text = random.choice(
                    ['Agender', 'Androgynous', 'Bigender', 'Cis', 'Female', 'Cis', 'Male', 'Cis', 'Man', 'Cis', 'Woman',
                     'Cisgender', 'Cisgender', 'Female', 'Cisgender', 'Male', 'Cisgender', 'Man', 'Cisgender', 'Woman',
                     'Female', 'to', 'Male', 'Gender', 'Fluid', 'Gender', 'Nonconforming', 'Gender', 'Questioning',
                     'Gender', 'Variant', 'Genderqueer', 'Intersex', 'Male', 'to', 'Female', 'Neither', 'Neutrois',
                     'Non-binary', 'Pangender', 'Trans', 'Trans', 'Female', 'Trans', 'Male', 'Trans', 'Man', 'Trans',
                     'Person', 'Trans', 'Woman', 'Trans(asterisk)', 'Trans(asterisk)Female', 'Trans(asterisk)Male',
                     'Trans(asterisk)Man', 'Trans(asterisk)Person', 'Trans(asterisk)Woman', 'Transexual', 'Transexual',
                     'Female', 'Transexual', 'Male', 'Transexual', 'Man', 'Transexual', 'Person', 'Transexual', 'Woman',
                     'Transgender', 'Female', 'Transgender', 'Male', 'Transgender', 'Man', 'Transgender', 'Person',
                     'Transgender', 'Woman', 'Transmasculine', 'Two-spirit']
                )
                user = ev.obj['from_id']
                us = vk_session.get_api()
                us.messages.send(user_id=user,
                                 message=f"Согласно анализу последних данных с вашей страницы вы {text}",
                                 random_id=random.randint(0, 2 ** 64))
            elif ev.obj['text'] in 'Начатьначать':
                user = ev.obj['from_id']
                us = vk_session.get_api()
                us.messages.send(user_id=user,
                                 message="Кончать",
                                 random_id=random.randint(0, 2 ** 64))
            elif ev.obj['text'] in 'стартСтартStartstart':
                user = ev.obj['from_id']
                us = vk_session.get_api()
                us.messages.send(user_id=user,
                                 message='чтобы провести гендерный анализ вашей страницы, напишите "мой гендерэ", "гендер" или "кто я?"',
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
