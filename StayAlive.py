import time

import pygame

pygame.mixer.init()
pygame.mixer.music.load('soundtrack4.wav')
pygame.mixer.music.play(-1)

game_over = False
game_win = False
was_key_lvl3_found = False
was_key_lvl5_found = False
was_scrap_found = False
was_friend_found = False
chapter_2 = False
restart = True
while restart:
    location = 'начало'
    restart = False
    print('\n' * 1000)

    print('''                        ________________________________ПРАВИЛА И ЗАМЕТКИ_______________________________
                        1) Для этого, осматривать помещения, в поле ввода, напишите: "осмотреть",
                            "посмотреть" и т. д. Для успешного прохождения данной мини-инры вы не должны
                            забывать делать это.
                        2) Если в конце высказывания, присутствует символ "&", то для продолжения,
                           необходимо нажать клавишу "ENTER"
                        3) Если вы заблудитесь, то в любой момент можно взглянуть на карту!
                           Для этого, напишите в поле ввода "карта", появится окно с необходимой информацией.
                           Чтобы продолжить играть, просто закройте окно.
                        4) В этой игре 3 концовки, чтобы посмотреть их все, нужно играть!
                        5) Поддержать разработчиков ---> Qiwi +7-903-667-16-41''')
    print()
    print()
    input('Press Enter to continue')
    print('\n' * 1000)

    pygame.mixer.music.load('soundtrack3.mp3')
    pygame.mixer.music.play(-1)

    print('Вы очнулись в комнте, не понимая, как сюда попали.')
    print('Вдруг, из кромкоговорителя раздался напуганный мужской голос:')
    print('Громкоговоритель: - Привет! Я Гешка! Мы тут находимся вдвоём...')
    print('Если ты все забыл после взрыва, я тебе напомню.')
    input('Нажмите enter для продолжения')
    print('Мы с тобой - коллеги, изучаем образцы животных, которые черезвычайно опасны для общества.')
    print('Их сожержат в специальных клетках, но что-то пошло не так...')
    input('Короче, мы с тобой остались одни в лаборатории, полной диких мутантов. &')
    print('Обьект хорошо охраняется, сюда уже едет группа зачистки, но для нас это очень плохо.')
    print('Вместе с этими монстрами, они обязаны уничтожить весь выживший персонал комплекса.')
    input('Думаю, ты понял, что нам нужно выбираться от сюда. &')
    print('Оглянувшись, вы не нашли ничего, кроме колб с разноцветными веществами и ')
    print('многочисленных стопок бумаг, разбросанных по помещению. Подняв одну из них,')
    print(' вы узнали свой почерк. Похоже, это ваш кабинет.')

    location = 'начало'

    while not game_over and not game_win:
        if location == 'начало':
            print('*Вы находитесь в своем рабочем кабинете*')
            print('Можете пойти: в кабинет охранника - 1, к воротам - 2 или в камеру содержания - 3.')
            while True:
                direction = input()
                if 'карт' in direction.lower():
                    sc = pygame.display.set_mode((700, 700))
                    sc.fill((100, 150, 200))

                    youhere = pygame.image.load('map_начало.bmp')
                    dog_rect = youhere.get_rect(bottomright=(700, 700))
                    sc.blit(youhere, dog_rect)

                    pygame.display.update()

                elif 'смотр' in direction.lower():
                    print('Вы ничего не нашли, здесь пусто!')
                elif direction == '1':
                    location = 'кабинет охранника'
                    break
                elif direction == '2':
                    location = 'ворота'
                    break
                elif direction == '3':
                    location = 'камера содержания'
                    break

        elif location == 'кабинет охранника':
            print('Вы пришли в кабинет охранника.Вы попали в кабинет охранника, он , кстати, имеет'
                  ' доступ к некоторым помещениям.Тут находится много бумаг, электроники и многого'
                  ' другого. ')
            print('Можете пойти: в свой рабочий кабинет - 1 или к воротам - 2')

            while True:
                direction = input()
                if '1' in direction or '2' in direction or 'смотр' in direction.lower():
                    break
            if 'смотр' in direction.lower():
                if not was_key_lvl3_found:
                    pygame.mixer.music.load('pickup.mp3')
                    pygame.mixer.music.play(0)
                    time.sleep(1)
                    pygame.mixer.music.load('soundtrack3.mp3')
                    pygame.mixer.music.play(-1)
                    print('Вы обнаружили ключ-карту уровня 3!')
                    was_key_lvl3_found = True
                    print('Можете пойти: в свой рабочий кабинет - 1 или к воротам - 2')
                    direction = input()
                else:
                    print('Вы уже здесь всё перерыли. Карта уровня 3 давно лежит у вас.')
                    print('Можете пойти: в свой рабочий кабинет - 1 или к воротам - 2')
                    direction = input()
            if direction == '1':
                location = 'начало'
            elif direction == '2':
                location = 'ворота'

        elif location == 'ворота':
            print('Вы подошли к большим железным вототам, которые разделяют корпус "A"'
                  ' от корпуса "B"')
            print('На табло рядом с вратами было написано: Необходима карта, уровня 2 или больше')
            if was_key_lvl3_found:
                print('Голос из громкоговорителя: -Как хорошо, что вы ее нашли в кабинете охранника! '
                      'Отпирайте ворота!')
                print('Можете пойти: в свой рабочий кабинет - 1, в кабинет охранника - 2 или узнать,'
                      ' что находится за воротами - 3')
                while True:
                    direction = input()
                    if '1' in direction or '2' in direction or '3' in direction \
                            or 'смотр' in direction.lower():
                        break
                if 'смотр' in direction.lower():
                    print('Здесь ничего нет!')
                elif direction == '1':
                    location = 'начало'
                elif direction == '2':
                    location = 'кабинет охранника'
                elif direction == '3':
                    location = 'рабочие помещения'
            else:
                print('Голос из громкоговорителя: -Нужно искать карту!')
                print('Можете пойти: в свой рабочий кабинет - 1 или в кабинет охранника - 2')
                while True:
                    direction = input()
                    if '1' in direction or '2' in direction or 'смотр' in direction.lower():
                        break
                if 'смотр' in direction.lower():
                    print('Здесь ничего нет!')
                elif direction == '1':
                    location = 'начало'
                elif direction == '2':
                    location = 'кабинет охранника'

        elif location == 'камера содержания':
            print('Вы вошли в камеру содержания, повсюду валяются осколки разбитого стекла')
            print('Может, здесь удасться найти что-то нужное.')
            print('Вы можете: Вернуться в свой кабинет - 1')
            while True:
                direction = input()
                if '1' in direction or 'смотр' in direction.lower():
                    break
            if 'смотр' in direction.lower():
                pygame.mixer.music.load('soundtrack1.mp3')
                pygame.mixer.music.play(-1)
                print('Когда вы приступили к обыску комнаты, кто-то вдребизги разбил')
                print('единственный источник света в помещении - лампу...')
                print()
                time.sleep(5)
                game_over = True
            if direction == '1':
                location = 'начало'

        elif location == 'рабочие помещения':
            if not chapter_2:
                pygame.mixer.music.load('cardridder.mp3')
                pygame.mixer.music.play(0)
                time.sleep(2)
                print('Как только вы вошли, ворота закрылись. "Кардридер" на'
                      ' второй стороне ворот сломан, попасть обратно уже не выйдет.')
                print('Можете пойти: в кабинет директора лаборатории - 1, к пустой комнате - 2'
                      ' или в кладовку - 3')
                pygame.mixer.music.load('soundtrack6.mp3')
                pygame.mixer.music.play(-1)
                chapter_2 = True
            else:
                print('Вы попали в рабочие помещения')
                print('Можете пойти: в кабинет директора лаборатории - 1, к пустой комнате - 2'
                      ' или в кладовку - 3')
            while True:
                direction = input()
                if '1' in direction or '2' in direction or '3' in direction \
                        or 'смотр' in direction.lower():
                    break
            if 'смотр' in direction.lower():
                print('Вы ничего не нашли, здесь ничего нет!')
            elif direction == '1':
                location = 'кабинет директора'
            elif direction == '2':
                location = 'комната с другом'
            elif direction == '3':
                location = 'кладовка'

        elif location == 'кладовка':
            print('Вы зашли в кладовку.')
            print('Среди этих палок и тряпок могло бы лежать что-то интерессное.')
            print('Вы можете: вернуться в рабочие помещения - 1')
            while True:
                direction = input()
                if '1' in direction or 'смотр' in direction.lower():
                    break
            if not was_scrap_found:
                if 'смотр' in direction.lower():
                    pygame.mixer.music.load('pickup.mp3')
                    pygame.mixer.music.play(0)
                    time.sleep(1)
                    pygame.mixer.music.load('soundtrack6.mp3')
                    pygame.mixer.music.play(-1)
                    print('Отодвинув палки, вы обнаружили лом! Он точно пригодится!')
                    was_scrap_found = True
                    print('Вы можете: вернуться в рабочие помещения - 1')
                    direction = input()
            else:
                print('Вы уже нашли здесь лом')
                print('Вы можете: вернуться в рабочие помещения - 1')
                direction = input()
            if direction == '1':
                location = 'рабочие помещения'

        elif location == 'кабинет директора':
            print('Вы пришли в кабинет директора лаборатории.'
                  ' Он имеет доступ ко всем помещениям,'
                  ' в его кабинете точно есть что-то полезное.')
            print('Можете пойти: в рабочие помещения - 1 или к пустой комнате - 2')

            while True:
                direction = input()
                if '1' in direction or '2' in direction or 'смотр' in direction.lower():
                    break
            if 'смотр' in direction.lower():
                if not was_key_lvl5_found:
                    pygame.mixer.music.load('pickup.mp3')
                    pygame.mixer.music.play(0)
                    time.sleep(1)
                    pygame.mixer.music.load('soundtrack5.mp3')
                    pygame.mixer.music.play(-1)
                    print('Вы обнаружили ключ-карту уровня 5!')
                    was_key_lvl5_found = True
                    print('Можете пойти: в рабочие помещения - 1 или к пустой комнате - 2')
                    direction = input()
                else:
                    print('Вы уже здесь всё обыскали. Карта уровня 5 у вас.')
                    print('Можете пойти: в рабочие помещения - 1 или к пустой комнате - 2')
                    direction = input()
            if direction == '1':
                location = 'рабочие помещения'
            elif direction == '2':
                location = 'комната с другом'

        elif location == 'комната с другом':
            print('Вы оказались в пустой бетонной комнате, с винтеляционной решёткой.')
            if not was_friend_found:
                if was_scrap_found:
                    print('Голос из решётки: -Э-ЭЙ! Ты здесь?'
                          'Найди, что-нибудь, чем можешь меня освободить!')
                    print('Можете: пойти в кабинет директора - 1, пойти к рабочим помещениям - 2,'
                          ' освободить товарища - 3 или пойти к выходу - 4')
                    while True:
                        direction = input()
                        if '1' in direction or '2' in direction or '3' in direction \
                                or '3' in direction or 'смотр' in direction.lower():
                            break
                    if 'смотр' in direction.lower():
                        print('Здесь ничего нет!')
                    elif direction == '1':
                        location = 'начало'
                    elif direction == '2':
                        location = 'кабинет охранника'
                    elif direction == '3':
                        pygame.mixer.music.load('friend.mp3')
                        pygame.mixer.music.play(0)
                        time.sleep(1)
                        pygame.mixer.music.load('soundtrack5.mp3')
                        pygame.mixer.music.play(-1)
                        print('С грохотом, решётка упала... Следом за ней, перед вами рухнул'
                              ' ваш друг, Гешка.')
                        print('Он протянул вам руку, и сказал: -Нужно выбираться!')
                        was_friend_found = True
                    elif direction == '4':
                        location = 'выход'
                else:
                    print('Голос из решётки: -Э-ЭЙ! Ты здесь?'
                          'Найди, что-нибудь, чем можешь меня освободить!')
                    print('Вы можете: пойти в кабинет директора - 1, пойти'
                          ' к рабочим помещениям - 2 или направиться к выходу - 3')
                    while True:
                        direction = input()
                        if '1' in direction or '2' in direction or '3' in direction or 'смотр' in direction.lower():
                            break
                    if 'смотр' in direction.lower():
                        print('Здесь ничего нет!')
                    elif direction == '1':
                        location = 'кабинет директора'
                    elif direction == '2':
                        location = 'рабочие помещения'
                    elif direction == '3':
                        location = 'выход'
            else:
                print(
                    'Вы можете: пойти в кабинет директора - 1, пойти к'
                    ' рабочим помещениям - 2 или направиться к выходу - 3')
                while True:
                    direction = input()
                    if '1' in direction or '2' in direction or '3' in direction or 'смотр' in direction.lower():
                        break
                if 'смотр' in direction.lower():
                    print('Здесь ничего нет!')
                elif direction == '1':
                    location = 'кабинет директора'
                elif direction == '2':
                    location = 'рабочие помещения'
                elif direction == '3':
                    location = 'выход'

        elif location == 'выход':
            print('Вы подошли к выходу, на табло была надпись: Необходима карта'
                  ' максимального уровня!')
            if was_key_lvl5_found:
                pygame.mixer.music.load('siren.mp3')
                pygame.mixer.music.play(1)
                print('\n')
                time.sleep(5)
                print('Для вас не составило труда пройти через дверь,'
                      ' вы оказались на улице, были сумерки...')
                print('Вы скорее ушли от этого места. Когда вы убежали достаточно'
                      ' далеко, раздался громкий взрыв!')
                print('Вы успешно добрались домой.')
                game_win = True
            else:
                print('Ключ-карты подходящего уровня у нас нет! стоит поискать еще.')
                print('Вы направились к пустой комнате.')
                location = 'комната с другом'
    if game_over:
        print('\n' * 100)
        time.sleep(2)
        pygame.mixer.music.load('sound1.mp3')
        pygame.mixer.music.play(0)
        time.sleep(2)
        print('Вас убил местный мутант! Конец игры! (Плохая концовка)')
        pygame.mixer.music.load('soundtrack4.wav')
        pygame.mixer.music.play(-1)
    if game_win:
        if was_friend_found:
            pygame.mixer.music.load('end2.mp3')
            pygame.mixer.music.play(1)
            print('''Вы с гешкой заварили чаю, и выпили. Через несколько месяцев вы уже отошли
             от происходящего, устроились на новою работу и начали жизнь с Гешкой с нуля!''')
            print('Поздравляю с успешным прохождением игры! (Хорошая концовка)')
        else:
            pygame.mixer.music.load('end1.mp3')
            pygame.mixer.music.play(1)
            print('Вы успешно добрались домой, но чувствовали'
                  ' себя очень плохо... Вы так и не спасли Гешку...')
    print()
    input('Press ENTER to continue')
    print('\n' * 100)
    print('Хотите поиграть заново?')
    say = input()
    if 'не' in say.lower():
        print('Хорошо, до скорых встреч!')
        time.sleep(2)
    else:
        location = 'начало'
        game_over = False
        game_win = False
        restart = True
