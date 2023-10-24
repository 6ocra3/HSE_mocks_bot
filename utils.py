import random
import json
class Number:
    def __init__(self, field, min, max):
        self.field = field
        self.min = min
        self.max = max

    def generate(self):
        return random.randint(self.min, self.max)

class Name:
    def __init__(self, field):
        self.field = field
        self.data = ['Александр', 'Алексей', 'Андрей', 'Анна', 'Артём', 'Дарья', 'Дмитрий', 'Евгения', 'Екатерина', 'Иван', 'Ксения', 'Мария', 'Максим', 'Наталья', 'Никита', 'Ольга', 'Павел', 'Светлана', 'Сергей', 'Татьяна', 'Юлия', 'Яна', 'Алина', 'Анатолий', 'Валерия', 'Виктор', 'Галина', 'Георгий', 'Елена', 'Илья', 'Кирилл', 'Лариса', 'Любовь', 'Михаил', 'Надежда', 'Олег', 'Полина', 'Роман', 'София', 'Станислав', 'Тимофей', 'Ульяна', 'Федор', 'Христина', 'Эдуард', 'Юрий', 'Ярослав']
    def generate(self):
        return random.choice(self.data)


mask = [Number("age", 5, 20), Name("name")]
itog = []
for i in range(5):
    a = {}
    for j in mask:
        a[j.field] = j.generate()
    itog.append(a)

print(json.dumps(itog, ensure_ascii=False))

#Name, Number, City, Date, Uuid, Email, PhoneNumber, Login, Password.