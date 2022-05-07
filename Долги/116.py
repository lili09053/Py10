class User(object):

    def __init__(self):
        pass

    def solve(self, n):
        pass


class Student(User):
    pass


class Teacher(User):

    def chek_solution(self, user, n):
        #user = User() - ?   - user - объект класса User
        pass


class Admin(User):

    def edit(self, n):
        pass


class SuperAdmin(Admin):
    def grant(self, user):

        pass
