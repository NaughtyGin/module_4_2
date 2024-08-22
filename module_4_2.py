def test_function(x):
    # x = 5
    print(globals(), 'Globals: Вызов из функции test_function')
    print(locals(), 'Locals: Вызов из функции test_function')

    def inner_function(a):
        # nonlocal x
        # x = 7
        for x in range(4, 7):
            if x <= 5:
                print('Я в области видимости функции test_function')
                print(globals(), 'Вызов из функции inner_function')
                print(locals(), 'Вызов из функции inner_function')
            else:
                print('Я всё ещё в области видимости функции test_function')
                print(globals(), 'Вызов из функции inner_function')
                print(locals(), 'Вызов из функции inner_function')
    inner_function(4)


x = 8
a = 2
print(f'{globals()} x = {x}, a = {a}, Globals: первый вызов вне функцмй')
print(f'{locals()} x = {x}, a = {a}, Locals: первый вызов вне функцмй')
print(test_function(3))
print(f'{globals()} x = {x}, a = {a}, Globals: последний вызов вне функцмй')
print(f'{locals()} x = {x}, a = {a}, Locals: последний вызов вне функцмй')
