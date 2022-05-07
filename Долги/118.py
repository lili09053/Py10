class Profile:

    def __init__(self, prof):
        self.prof = prof

    def info(self):
        return " "

    def describe(self):
        print(self.prof, self.info())


class Vacancy(Profile):

    def __init__(self, prof, the_salary):
        super(Vacancy, self).__init__(prof)
        self.the_salary = the_salary

    def info(self):
        return f"Предлагаемая зарплата: {self.the_salary}"


class Resume(Profile):
    def __init__(self, prof, experience):
        super(Resume, self).__init__(prof)
        self.experience = experience

    def info(self):
        return f"Стаж работы:{self.experience}"
