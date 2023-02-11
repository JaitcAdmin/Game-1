import time


class Student:
    def __init__(self, name):
        self.marks = []
        self.time_marks = []
        self.name = name
        self.delete_marks = []

    def print_marks(self):
        for i in self.marks:
            print(i)

    def add_marks(self, mark):
        if 1 <= mark <= 5:
            self.marks.append(mark)

    def delete_mark(self, index):
        self.delete_marks.append(self.marks[index])
        self.marks.pop(index)

    def sr_arefm(self):
        b = 0
        for i in range(0, len(self.marks)):
            b += self.marks[i]
        print(b / len(self.marks))

    def change_mark(self, index, new_mark):
        self.delete_marks.append(self.marks[index - 1])
        self.marks[index - 1] = new_mark

    def delete_marks(self, index):
        for i in self.delete_marks:
            print(i)

    def add_time(self, time):
        self.time_marks.append(time)


students = []

while 1:
    a = input("Возможные комманды: \n"
              "1 добавить ученика \n"
              "2 удалить ученика \n"
              "3 добавить оценку \n"
              "4 изменить оценку \n"
              "5 удалить оценку \n"
              "6 среднее арефметическое \n"
              "7 все оценки \n"
              "8 все удалённые оценки \n"
              "9 все ученики\n"
              "0 выйти\n")

    if a == 'добавить ученика' or a == "1":
        s = Student(input("Введите имя ученика\n"))
        students.append(s)
        print("операция успешно завершена")


    elif a == 'удалить ученика' or a == "2":
        print('Введи номер ученика для удаления:')
        for i in range(0, len(students)):
            print(F"{i + 1} - {students[i].name}")
        index_s = int(input("Номер ученика ")) - 1
        students.pop(index_s)
        print("операция успешно завершена")

    elif a == 'добавить оценку' or a == "3":
        for i in range(0, len(students)):
            print(F"{i + 1} - {students[i].name}")
        c = int(input("Номер ученика "))
        students[c - 1].add_marks(int(input("Оценка ")))
        students[c - 1].add_time(time.time)
        print("операция успешно завершена")

    elif a == 'изменить оценку' or a == "4":
        for i in range(0, len(students)):
            print(F"{i + 1} - {students[i].name}")
        students[int(input("Номер ученика ")) - 1].change_mark(int(input("Номер оценки")) - 1,  )
        print("операция успешно завершена")

    elif a == 'удалить оценку' or a == "5":
        for i in range(0, len(students)):
            print(F"{i + 1} - {students[i].name}")
        c = int(input("Номер ученика "))
        for y in range(0, len(students[c - 1].marks)):
            print(F"{y + 1} - {students[c - 1].marks[y]}     {students[c-1].time_marks[y]}")
        students[c - 1].delete_mark(int(input("Номер")) - 1)

    elif a == 'среднее арефметическое' or a == "6":
        for i in range(0, len(students)):
            print(F"{i + 1} - {students[i].name}")
        students[int(input("Номер ученика ")) - 1].sr_arefm()

    elif a == 'все оценки' or a == "7":
        for i in range(0, len(students)):
            print(F"{i + 1} - {students[i].name}")
        students[int(input("Номер ученика ")) - 1].print_marks()

    elif a == 'все удалённые оценки' or a == "8":
        for i in range(0, len(students)):
            print(F"{i + 1} - {students[i].name}")
        students[int(input("Номер ученика ")) - 1].delete_mark(int(input("Номер оценки")) - 1)

    elif a == 'все ученики' or a == "9":
        for i in students:
            print(i.name)

    elif a == 'выйти' or a == "0":
        print("Чао!")
        break
    else:
        print("Комманда не распознана \n")
