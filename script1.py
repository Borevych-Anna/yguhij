lst1 = [4,6,5,8,12,3,10]
lst2 = [6,2,1,2,5,7,8]
lst3 = [8,9,11,12,10,10,8]
lst4 = [2,3,4,2,1,2,3,5]
users = {
    'Лябук Тарас Анатолійович': {'password': '634748', 'grades': lst1},
    'Огравш ауацшао': {'password': '123456', 'grades': lst2},
    'Балєріна Капучіна': {'password': '783629', 'grades': lst3},
    'Mogger': {'password': '676767', 'grades': lst4},
}
while True:
     username = input("Будь ласка, введіть свій логін: ")
     password = input("Будь ласка, введіть свій пароль: ")
     if username in users and users[username]['password'] == password:
         print('Доступ дозволено')
         grades = users[username]['grades']
         print('Ваші оцінки:', grades)
         print('Задовільні оцінки:')
         for a in grades:
             if 5 <= a <= 12:
                print(a)
         print('Незадовільні оцінки:')
         for b in grades:
             if 1 <= b <= 4:
                print(b)
         break
     else:
         continue