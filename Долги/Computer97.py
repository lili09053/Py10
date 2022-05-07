from User97 import User


class Computer:

    def __init__(self, status):
        self.status = status  # состояние вкл\выкл

    def is_on(self):  # проверка на состояние вкл\выкл
        return self.status  # Возвращаем True - включен, False - выключен

    def calculator(self):
        first_number = float(input("Введите первое число: "))
        sign = input("Введите знак опреции (* , **, +, -, /): ")
        second_number = float(input("Введите второе число: "))

        if sign == "*":
            print(first_number * second_number)
        if sign == "**":
            print(first_number ** second_number)
        if sign == "+":
            print(first_number + second_number)
        if sign == "-":
            print(first_number - second_number)
        if sign == "/":
            print(first_number / second_number)

    def transfer(self):
        num = int(input("Введите число для перeвода\n"))
        print(bin(num)[2:])

    def built(self):

        import matplotlib.pyplot as plt

        k = float(input("Введите угловой коэффициент: "))
        b = float(input("Введите значение свободного члена: "))
        diapazon_x1 = int(input("Введите  начало диапазона: "))
        diapazon_x2 = int(input("Введите  конец диапазона: "))
        value_y = []
        value_x = []
        for i in range(diapazon_x1, diapazon_x2):
            y = k * i + b
            value_y.append(y)
            value_x.append(i)
        plt.plot(value_x, value_y, color='aqua')
        plt.show()

    def application_func(self, user):  # предлагает пользователю ввести имя приложения
        print("Выберите приложение из списка:")
        print("> Калькулятор")
        print("> Перевод целого числа из 10-ой системы в 2-ую")
        print("> Построение графика линейной функции (только для Администратора)")
        print("> Выключить компьютер")
        self.app = user.set_application()  # input("Введите первое слово названия приложения:\n")
        if self.app == "Калькулятор":   # действие с двумя числами
            self.calculator()
        elif self.app == "Перевод":
            self.transfer()
        elif self.app == "Построение" and user.profile == "Администратор":  # y = kx + b
            self.built()
        elif self.app == "Построение" and user.profile != "Администратор":
            print("Вам требуются права Администратора")
        elif self.app == "Выключить":
            self.status = False
        else:
            print("Неверно введено приложение!")


a = Computer(True)
b = User()
b.set_profile()

while a.is_on():
    a.application_func(b)
