def start_training(сharacter):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    commands = {'attack':attack,
                    'defence':defence,
                    'special':special
               }
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

    cmd : str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        for command in commands:
            if cmd in command:
                comman = commands[cmd](char_name, char_class) 
                print(comman)
            else:
                return 'Тренировка окончена.'


