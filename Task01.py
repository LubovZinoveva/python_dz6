# Создайте программу для игры в "Крестики-нолики".

from random import randint

def move_cross(list1, row, column):
    if list1[row][column] != '':
        print('Ошибка, место занято. Выберите новое')
        new_row = int(input('Cтрока = '))
        new_column = int(input('Cтолбец = '))
        move_cross(list1, new_row - 1, new_column - 1)
    else:
        list1[row][column] = 'X'
    return list1

def move_zero(list2, row, column):
    if list2[row][column] != '':
        print('Ошибка, место занято. Выберите новое')
        new_row = int(input('Cтрока = '))
        new_column = int(input('Cтолбец = '))
        move_cross(list2, new_row - 1, new_column - 1)
    else:
        list2[row][column] = '0'
    return list2

def print_matrix(mas, n):
    print('  1', end = '')
    for i in range(2, n+1):
        print(f' {i}', end = '')
    print()
    for i in range(n):
        print(i+1, end = '')
        for j in range(n):
            if mas[i][j] == '':
                print('|_', end='')
            else:
                print(f'|{mas[i][j]}', end='') 
        print('|')

def check_array(array):
    count = 1
    result = False
    for j in range(len(array)-1):
            if array[j] == array[j + 1]:
                count += 1
                if count == 3:
                    if array[j] == 'X':
                        print('ПОЗДРАВЛЯЕМ, КРЕСТИКИ ВЫИГРАЛИ!')
                        result = True
                        break
                    elif array[j] == '0':
                        print('ПОЗДРАВЛЯЕМ, НОЛИКИ ВЫИГРАЛИ!')  
                        result = True
                        break
            else:
                count = 1
    return result

def win_check(arr):
    result = False
    # Проверяем по строкам
    for i in range(len(arr)):
       my_list = [j for j in arr[i]]
       if check_array(my_list):
            result = True
            break

    # Проверяем по столбцам        
    for i in range(len(arr)):
        column = [x[i] for x in arr]
        if check_array(column):
            result = True
            break

    # Проверяем по первым диагоналям
    list_check1 = []
    for i in range(len(arr)-2):
        count = 0
        for j in range(i+2, -1, -1):
            list_check1.append(arr[j][count])
            count += 1
        if check_array(list_check1):
            result = True
            break
        else:
            list_check1.clear()

    for i in range(1, len(arr)-2):
        count = i
        for j in range(len(arr)-2, i-2, -1):
            list_check1.append(arr[j][count])
            count += 1
        if check_array(list_check1):
            result = True
            break
        else:
            list_check1.clear()

    # Проверяем по вторым диагоналям
    
    list_check1 = []
    for i in range(len(arr)-2):
        count = 0
        for j in range(len(arr)-i-3, len(arr)):
            list_check1.append(arr[j][count])
            count += 1
        if check_array(list_check1):
            result = True
            break
        else:
            list_check1.clear()

    for i in range(1, len(arr)-2):
        count = i
        for j in range(len(arr)-i):
            list_check1.append(arr[j][count])
            count += 1
        if check_array(list_check1):
            result = True
            break
        else:
            list_check1.clear()
    
    return result

def bot_move(array):
    result = []
    # На номрального бота с "интеллектом" не хватило времени и сил уже, 
    # поэтому он просто будет тыкать в любую свободную клетку
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '':
                result.append(i)
                result.append(j)
                break
    return result    
             
def play_with_friend(N, player1, player2):
    if first_move == 1:
        print(f'{player1} ходит первым, играет крестиками')
        print(f'{player2} играет ноликами')
        first = player1
        second = player2
    else:
        print(f'{player2} ходит первым, играет крестиками')
        print(f'{player1} играет ноликами')
        first = player2
        second = player1
    my_playing_field = []
    for i in range(N):
        my_playing_field.append(["" for _ in range(N)])
    round = (N*N)//2 + 1
    if N*N % 2 != 0:
        round += 1
    for step in range(1, round): 
        print()
        print(f'ХОД {step}')
        print_matrix(my_playing_field, N)
        print(f'{first} ходит. Выберите позицию на поле')
        my_row = int(input('Введите номер строки: '))
        my_column = int(input('Введите номер столбца: '))
        my_playing_field = move_cross(my_playing_field, my_row - 1, my_column - 1)
        if step > 2:
            if win_check(my_playing_field):
                print_matrix(my_playing_field, N)
                break
        if N*N % 2 != 0 and step == round - 1:    
                print('Ничья! Конец игры :)')
                break
        print_matrix(my_playing_field, N)
        print(f'{second} ходит. Выберите позицию на поле')
        my_row = int(input('Введите номер строки: '))
        my_column = int(input('Введите номер столбца: '))
        my_playing_field = move_zero(my_playing_field, my_row - 1, my_column - 1)
        if step > 2:
            if win_check(my_playing_field):
                print_matrix(my_playing_field, N)
                break
        if step == round - 1:    
                print('Ничья! Конец игры :)')

def play_with_bot(N, player):
    my_playing_field = []
    for i in range(N):
        my_playing_field.append(["" for _ in range(N)])
    round = (N*N)//2 + 1
    if N % 2 != 0:
        round += 1
    if first_move == 1:
        print(f'{player} ходит первым, играет крестиками')
        print('Бот играет ноликами')
        for step in range(1, round): 
            print()
            print(f'ХОД {step}')
            print_matrix(my_playing_field, N)
            print(f'{player} ходит. Выберите позицию на поле')
            my_row = int(input('Введите номер строки: '))
            my_column = int(input('Введите номер столбца: '))
            my_playing_field = move_cross(my_playing_field, my_row - 1, my_column - 1)
            if step > 2:
                if win_check(my_playing_field):
                    print_matrix(my_playing_field, N)
                    break
            if step == round - 1:    
                    print('Ничья! Конец игры :)')
                    break
            print_matrix(my_playing_field, N)
            print('Бот ходит. Выбирает позицию..')
            b_move = bot_move(my_playing_field)
            print(f'Строка = {b_move[0]}')
            print(f'Столбец = {b_move[1]}')
            my_row = b_move[0]
            my_column = b_move[1]
            my_playing_field = move_zero(my_playing_field, my_row, my_column)
            if step > 2:
                if win_check(my_playing_field):
                    print_matrix(my_playing_field, N)
                    break
    else:
        print('Бот ходит первым, играет крестиками')
        print(f'{player} играет ноликами')
        for step in range(1, round): 
            print()
            print(f'ХОД {step}')
            print_matrix(my_playing_field, N)
            print('Бот ходит. Делает выбор..')
            b_move = bot_move(my_playing_field)
            print(f'Строка = {b_move[0]}')
            print(f'Столбец = {b_move[1]}')
            my_row = b_move[0]
            my_column = b_move[1]
            my_playing_field = move_cross(my_playing_field, my_row, my_column)
            if step > 2:
                if win_check(my_playing_field):
                    print_matrix(my_playing_field, N)
                    break
            if step == round - 1:    
                    print('Ничья! Конец игры :)')
                    break
            print_matrix(my_playing_field, N)
            print(f'{player} ходит. Выберите позицию на поле')
            my_row = int(input('Введите номер строки: '))
            my_column = int(input('Введите номер столбца: '))
            my_playing_field = move_zero(my_playing_field, my_row - 1, my_column - 1)
            if step > 2:
                if win_check(my_playing_field):
                    print_matrix(my_playing_field, N)
                    break

try:
    first_move = randint(1, 2)
    num = int(input('Введите размерность поля: '))
    print('2 режима игры: 1. С другом 2. С ботом')
    variant = int(input('Выберите режим игры: '))
    if variant == 1:
        name1 = input("Введите имя первого игрока: ")
        name2 = input("Введите имя второго игрок: ")
        play_with_friend(num, name1, name2)
    elif variant == 2:
        name = input("Введите имя игрока: ")
        play_with_bot(num, name)
except:
    print('Упс, что-то пошло не так')
