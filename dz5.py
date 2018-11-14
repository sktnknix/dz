# -*- coding: utf-8 -*-

class Animals:
    def __init__(self, name, weight, voice, color, _class):
        self.name = name
        self.weight = weight
        self.voice = voice
        self.color = color
        self._class = _class
    def give_food(self):
        print('Спасибо за еду')
    def give_drink(self):
        print('Спасибо за воду')

class Beeves:
    def take_milk(self):
        print('дала молоко')
    def _cut(self):
        print('побрит налысо')

class Home_Birds:
    def take_eggs(self):
        print('яйца собраны')
    def need_cut_wings(self):
        print('крылья подрезаны')

class Gooses(Animals, Home_Birds):
    character = 'Спокойный'
    sentiment = 'Улыбчивый'
    speed = 'Медленный'

class Cows(Animals, Beeves):
    exp = 'Даю молоко'

class Sheeps(Animals, Beeves):
    pass

class Chickens(Animals, Home_Birds):
    pass

class Goats(Animals, Beeves):
    pass

class Ducks(Animals, Home_Birds):
    pass

goose_Grey = Gooses('Серый', 5, 'Га-га', 'Серый', 'Гусь')
goose_White = Gooses('Белый', 4.2, 'Га-га', 'Белый', 'Гусь')
cow_Mashka = Cows('Манька', 100, 'Му-му', 'Бурый', 'Корова')
sheep_Barashek = Sheeps('Барашек', 100, 'Бе-бе', 'Серо-бурый', 'Овца')
sheep_Kudryashka = Sheeps('Кудрявый', 57, 'Бе-бе', 'Малиновый', 'Овца')
chicken_Koko = Chickens('Ко-ко', 3.2, 'Ко-ко', 'Пестрый', 'Курица')
chicken_Kukareku = Chickens('Кукареку', 3.4, 'Ко-ко', 'Сизый', 'Курица')
goat_Roga = Goats('Рога', 42, 'Ме-ме', 'Черный', 'Коза')
goat_Kopyta = Goats('Копыта', 43, 'Ме-ме', 'Непонятный', 'Коза')
duck_Kryakva = Ducks('Кряква', 4.2, 'Кря-кря', 'Фиолетовый', 'Утка')

animals_list = [goose_Grey, goose_White, cow_Mashka, sheep_Barashek, sheep_Kudryashka, chicken_Koko, chicken_Kukareku, \
                goat_Roga, goat_Kopyta, duck_Kryakva]
_beeves = [cow_Mashka, sheep_Barashek, sheep_Kudryashka, goat_Roga, goat_Kopyta]
_home_birds = [goose_Grey, goose_White, chicken_Koko, chicken_Kukareku, duck_Kryakva]

def _weight():
    weights = {goose_White.name: goose_White.weight, goose_Grey.name: goose_Grey.weight, \
               cow_Mashka.name: cow_Mashka.weight, sheep_Barashek.name: sheep_Barashek.weight, \
               sheep_Kudryashka.name: sheep_Kudryashka.weight, chicken_Koko.name: chicken_Koko.weight, \
               chicken_Kukareku.name: chicken_Kukareku.weight, goat_Roga.name: goat_Roga.weight, \
               goat_Kopyta.name: goat_Kopyta.weight, duck_Kryakva.name: duck_Kryakva.weight}
    sum_weight = round(sum(weights.values()), 1)
    print('Суммарный вес всех животных ' + str(sum_weight) + ' кг.')
    _max = 0
    for name, value in weights.items():
        if value > _max:
            _max = value
    for name, value in weights.items():
        if value == _max:
            print('Наибольший вес ' + str(_max) + ' кг. имеет ' + name)

def _choose_animal():
    for index in range(1, len(animals_list) + 1):
        print(str(index) + ' ' + animals_list[index - 1]._class + ', зовут ' + animals_list[index - 1].name)
    while 1:
        ent = input('Выбери зверушку из списка (номер): ')
        if not ent.isnumeric() or not 1 <= int(ent) <= len(animals_list):
            print('Необходимо ввести порядковый номер из списка')
        else:
            current_index = int(ent)
            break
    print('Ты подошел к зверушке ' + animals_list[current_index - 1]._class + ' ' + animals_list[
        current_index - 1].name)
    return current_index

while 1:
    _key = input('Для просмотра команд, нажмите [h], для выхода - [q]\n')
    if _key == 'q':
        print('Bye ...\n------------------')
        break
    elif _key == 'h':
        print('''a: всех посмотреть
wt: вывести суммарный вес животных и самого тяжелого
f: накормить
w: напоить
ct: побрить
m: подоить
e: собрать яйца
cw: обрезать крылья''')
    elif _key == 'a':
        for animal in animals_list:
            print('Вид ' + animal._class + '. Зовут: ' + animal.name + ', весит: ' + str(animal.weight) + 'кг' + ', язык: ' \
      + animal.voice + ', национальность: ' + animal.color)
    elif _key == 'wt':
        _weight()
    elif _key == 'f':
        print('Кого нужно накормить ?')
        index = _choose_animal()
        print(animals_list[index - 1].name + ':')
        animals_list[index - 1].give_food()
    elif _key == 'w':
        print('Кого нужно напоить ?')
        index = _choose_animal()
        print(animals_list[index - 1].name + ':')
        animals_list[index - 1].give_drink()
    elif _key == 'ct':
        print('Кого нужно обрить ?')
        index = _choose_animal()
        if not animals_list[index - 1] in _beeves:
            print('Птичку брить наголо нельзя, можно только обрезать крылья ☺')
        else:
            print('Зверек ' + animals_list[index - 1].name, end=' ')
            animals_list[index - 1]._cut()
    elif _key == 'cw':
        print('Кому нужно обрезать крылья ?')
        index = _choose_animal()
        if not animals_list[index - 1] in _home_birds:
            print('У парнокопытных нет крыльев, идите к птичкам ☺')
        else:
            print('У птички ' + animals_list[index - 1].name, end=' ')
            animals_list[index - 1].need_cut_wings()
    elif _key == 'm':
        print('Кого подоить ?')
        index = _choose_animal()
        if not animals_list[index - 1] in _beeves:
            print('Птицы молоко не дают')
        else:
            print('Зверек ' + animals_list[index - 1].name, end=' ')
            animals_list[index - 1].take_milk()
    elif _key == 'e':
        print('У кого собрать яйца ?')
        index = _choose_animal()
        if not animals_list[index - 1] in _home_birds:
            print('Парнокопытные не несут яиц')
        else:
            print('У птицы ' + animals_list[index - 1].name, end=' ')
            animals_list[index - 1].take_eggs()
    else:
        print('Такой команды не найдено, нажмите [h] для вывода списка команд')
