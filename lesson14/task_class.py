class Group:
    def __init__(self):
        self.students = []

    def g_add(self, other):
        self.students.append(other)

    def g_del(self, other):
        self.students.remove(other)

    def g_print(self):
        for i in self.students:
            print("{:<20} {}".format(i.name, i.grades))


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades


if __name__ == '__main__':
    s1 = Student('Ivanov', 22, 5)
    s2 = Student('Petrov', 22, 4)
    s3 = Student('Sidorov', 22, 4)
    g1 = Group()
    g1.g_add(s1)
    g1.g_add(s2)
    g1.g_add(s3)
    g1.g_print()
    print('---')
    g1.g_del(s2)
    g1.g_print()
