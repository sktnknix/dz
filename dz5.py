# -*- coding: utf-8 -*-

class Animal:
    def __init__(self, name, weight, voice, color, kind):
        self.name = name
        self.weight = weight
        self.voice = voice
        self.color = color
        self.kind = kind
    def give_food(self):
        print('Спасибо за еду')
    def give_drink(self):
        print('Спасибо за воду')

class Beeve:
    def take_milk(self):
        print('дала молоко')
    def cut(self):
        print('побрит налысо')

class Home_birds:
    def take_eggs(self):
        print('яйца собраны')
    def need_cut_wings(self):
        print('крылья подрезаны')

class Goose(Animal, Home_birds):
    character = 'Спокойный'
    sentiment = 'Улыбчивый'
    speed = 'Медленный'

class Cow(Animal, Beeve):
    exp = 'Даю молоко'

class Sheep(Animal, Beeve):
    pass

class Chicken(Animal, Home_birds):
    pass

class Goat(Animal, Beeve):
    pass

class Duck(Animal, Home_birds):
    pass

goose_grey = Goose('Серый', 5, 'Га-га', 'Серый', 'Гусь')
goose_white = Goose('Белый', 4.2, 'Га-га', 'Белый', 'Гусь')
cow_mashka = Cow('Манька', 100, 'Му-му', 'Бурый', 'Корова')
sheep_barashek = Sheep('Барашек', 100, 'Бе-бе', 'Серо-бурый', 'Овца')
sheep_kudryashka = Sheep('Кудрявый', 57, 'Бе-бе', 'Малиновый', 'Овца')
chicken_koko = Chicken('Ко-ко', 3.2, 'Ко-ко', 'Пестрый', 'Курица')
chicken_kukareku = Chicken('Кукареку', 3.4, 'Ко-ко', 'Сизый', 'Курица')
goat_roga = Goat('Рога', 42, 'Ме-ме', 'Черный', 'Коза')
goat_kopyta = Goat('Копыта', 43, 'Ме-ме', 'Непонятный', 'Коза')
duck_kryakva = Duck('Кряква', 4.2, 'Кря-кря', 'Фиолетовый', 'Утка')

animals_list = [goose_grey, goose_white, cow_mashka, sheep_barashek, sheep_kudryashka, chicken_koko, chicken_kukareku, \
                goat_roga, goat_kopyta, duck_kryakva]
beeve_list = [cow_mashka, sheep_barashek, sheep_kudryashka, goat_roga, goat_kopyta]
home_birds_list = [goose_grey, goose_white, chicken_koko, chicken_kukareku, duck_kryakva]

def weight():
    weights = {goose_white.name: goose_white.weight, goose_grey.name: goose_grey.weight, \
               cow_mashka.name: cow_mashka.weight, sheep_barashek.name: sheep_barashek.weight, \
               sheep_kudryashka.name: sheep_kudryashka.weight, chicken_koko.name: chicken_koko.weight, \
               chicken_kukareku.name: chicken_kukareku.weight, goat_roga.name: goat_roga.weight, \
               goat_kopyta.name: goat_kopyta.weight, duck_kryakva.name: duck_kryakva.weight}
    sum_weight = round(sum(weights.values()), 1)
    print('Суммарный вес всех животных ' + str(sum_weight) + ' кг.')
    max_value = 0
    for name, value in weights.items():
        if value > max_value:
            max_value = value
    for name, value in weights.items():
        if value == max_value:
            print('Наибольший вес ' + str(max_value) + ' кг. имеет ' + name)

def choose_animal():
    for index in range(1, len(animals_list) + 1):
        print(str(index) + ' ' + animals_list[index - 1].kind + ', зовут ' + animals_list[index - 1].name)
    while 1:
        ent = input('Выбери зверушку из списка (номер): ')
        if not ent.isnumeric() or not 1 <= int(ent) <= len(animals_list):
            print('Необходимо ввести порядковый номер из списка')
        else:
            current_index = int(ent)
            break
    print('Ты подошел к зверушке ' + animals_list[current_index - 1].kind + ' ' + animals_list[
        current_index - 1].name)
    return current_index

while 1:
    key = input('Для просмотра команд, нажмите [h], для выхода - [q]\n')
    if key == 'q':
        print('Bye ...\n------------------')
        break
    elif key == 'h':
        print('''a: всех посмотреть
wt: вывести суммарный вес животных и самого тяжелого
f: накормить
w: напоить
ct: побрить
m: подоить
e: собрать яйца
cw: обрезать крылья''')
    elif key == 'a':
        for animal in animals_list:
            print('Вид ' + animal.kind + '. Зовут: ' + animal.name + ', весит: ' + str(animal.weight) + 'кг' + ', язык: ' \
      + animal.voice + ', национальность: ' + animal.color)
    elif key == 'wt':
        weight()
    elif key == 'f':
        print('Кого нужно накормить ?')
        index = choose_animal()
        print(animals_list[index - 1].name + ':')
        animals_list[index - 1].give_food()
    elif key == 'w':
        print('Кого нужно напоить ?')
        index = choose_animal()
        print(animals_list[index - 1].name + ':')
        animals_list[index - 1].give_drink()
    elif key == 'ct':
        print('Кого нужно обрить ?')
        index = choose_animal()
        if not animals_list[index - 1] in beeve_list:
            print('Птичку брить наголо нельзя, можно только обрезать крылья ☺')
        else:
            print('Зверек ' + animals_list[index - 1].name, end=' ')
            animals_list[index - 1].cut()
    elif key == 'cw':
        print('Кому нужно обрезать крылья ?')
        index = choose_animal()
        if not animals_list[index - 1] in home_birds_list:
            print('У парнокопытных нет крыльев, идите к птичкам ☺')
        else:
            print('У птички ' + animals_list[index - 1].name, end=' ')
            animals_list[index - 1].need_cut_wings()
    elif key == 'm':
        print('Кого подоить ?')
        index = choose_animal()
        if not animals_list[index - 1] in beeve_list:
            print('Птицы молоко не дают')
        else:
            print('Зверек ' + animals_list[index - 1].name, end=' ')
            animals_list[index - 1].take_milk()
    elif key == 'e':
        print('У кого собрать яйца ?')
        index = choose_animal()
        if not animals_list[index - 1] in home_birds_list:
            print('Парнокопытные не несут яиц')
        else:
            print('У птицы ' + animals_list[index - 1].name, end=' ')
            animals_list[index - 1].take_eggs()
    else:
        print('Такой команды не найдено, нажмите [h] для вывода списка команд')
