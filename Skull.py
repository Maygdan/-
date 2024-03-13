
print(''' Здраствуйте игроки!
         для начала игры определитесь, чем будете ходить: "x","o"(x - икс),(o - англ. о)''')
print("Для остановки игры введите слово 'end' на этапе выбора x или o")
matrix = [[0,  1,   2,  3 ], 
          [1, '-', '-','-'], 
          [2, '-', '-','-'],
          [3, '-', '-','-']]

matrix_length = len(matrix) 
 
for i in range(matrix_length): 
    print(*matrix[i]) 

def win():
    win_cord =(((1,1),(1,2),(1,3)),((2,1),(2,2),(2,3)),((3,1),(3,2),(3,3)),
    ((1,1),(2,2),(3,3)),((1,3),(2,2),(3,1)),((1,1),(2,1),(3,1)),
    ((1,2),(2,2),(3,2)),((1,3),(2,3),(3,3)))
    for cord in win_cord:
        u=[]
        for c in cord:
            u.append(matrix[c[0]][c[1]])
        if u == ["x","x","x"]:
            print("Победа x !!!")
            return True
        if u==["o","o","o"]:
            print("победа о !!!")
            return True
    return False

def x_o(dictionary,a,b,l:str):
       
        global matrix_length
        print('--------')
        if (a, b) in dictionary.values() :
            print("Помоему вы немного ошиблись в данных")
        elif (a,b) not in dictionary.values():
            dictionary[len(dictionary)+1] = (a, b)  
            matrix[a][b] = l
            for i in range(matrix_length):
                 print(*matrix[i])
                
        else: 
            return('вы вышли за пределы игры')
def hello():
    hello.counter += 1
    return (hello.counter) 
    
    
hello.counter = 0            
my_dict = {}

while 1 == True: 
    a = input('''Уважаемые игроки выберете кто будете ходить: ''')
    if a == "x":
        print('--------')
        print('Ход за x ')
        d = int(input('''Первый игрок 
    введите строку хода
    (введите строку, начиная с 1-й по 3-у): '''))
        p = int(input('''Первый игрок 
    введите место хода 
    (введите место, начиная с 1-ого по 3-ие): '''))
        h = print(x_o(my_dict,d,p, l='x'))
        print(h)
        w = hello()
        if w >8:
            print('Ничья, не забудь-те поблагодарить другого игрока за игру')
            break
        if win():
            break
    elif a == "o":
        print('--------')
        print('Ход за o ')
        d = int(input('''Второй игрок 
    введите строку хода
    (введите строку, начиная с 1-й по 3-у): '''))
        p = int(input('''Второй игрок 
    введитевте место хода 
    (введите место, начиная с 1-ого по 3-ие): '''))
        h = print(x_o(my_dict,d,p, l='o'))
        print(h)
        w = hello()
        if w > 8:
            print('Ничья, не забудь-те поблагодарить другого игрока за игру')
            break 
        if win():
            break
    elif a == 'end':
        print('Спасибо за игру')
        break
    elif a != 'x' or 'o':
        print("вы ввели не совсем те данные")


