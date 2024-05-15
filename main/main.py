def is_film_exist(move, films):
    for i_move in films:
        if i_move == move:
            return True
    return False

films = [
         'Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня',
         'Проклятый остров', 'Начало', 'Матрица'
]

my_list = []
while True:
    print("\nВаш текущий топ фильмов:", my_list)
    move = input("Введите название фильма: ")
    if is_film_exist(move, films):
        decision = input("Команды: добавить, вставить, удалить: ")
        if decision == "добавить":
            if is_film_exist(move, my_list):
                print("Этот фильм уже есть в вашем списке")
            else:
                my_list.append(move)
        elif decision == "вставить":
            if is_film_exist(move, my_list):
                print("Этот фильм уже есть в вашем списке")
            else:
                index = int(input("На какое место: "))
                my_list.insert(index - 1, move)
        elif decision == "удалить":
            if is_film_exist(move, my_list):
                my_list.remove(move)
            else:
                print("Этого фильма нет в вашем списке")
        else:
            print("Неверная команда")
    else:
        print("Данного фильма нет в списке")