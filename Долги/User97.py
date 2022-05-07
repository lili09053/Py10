class User:

    def __init__(self):
        self.profile = ""
        pass

    def set_profile(self):  # установление профиля

        self.profile = input("Введите уровень доступа(Администратор/Гость): ")

        if self.profile == "Администратор":
            pass
        if self.profile == "Гость":
            pass
        while self.profile != "Администратор" and self.profile != "Гость":
            print("Повторите ввод")
            self.profile = input("Введите уровень доступа(Администратор/Гость): ")

    def set_application(self):  # установление приложения
        st = input("Введите первое слово названия приложения:\n")
        return st
