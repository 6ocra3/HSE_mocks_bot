import random
import json
import datetime
import uuid
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

class City:
    def __init__(self,field):
        self.field = field
        self.data = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань', 'Челябинск', 'Омск', 'Самара', 'Ростов-на-Дону']
    def generate(self):
        return random.choice(self.data)

class Date_of_birth:
    def __init__(self, field):
        self.field = field
    def generate(self):
        end_date = datetime.now() - timedelta(days=365 * 100)
        start_date = end_date - timedelta(days=365)
        random_date = start_date + (end_date - start_date) * random.random()
        return random_date.strftime("%d.%m.%Y")

class Uuid:
    def __init__(self):
        self.field = field
    def generate(self):
        generated_uuid = uuid.uuid4()
        shortened_uuid = str(generated_uuid)[:16]
        return shortened_uuid

mask = [Name("name"), Number("age", 5, 20), City("city"), Date_of_birth("date_of_birth"), Uuid("uuid")]
itog = []
for i in range(5):
    a = {}
    for j in mask:
        a[j.field] = j.generate()
    itog.append(a)

print(json.dumps(itog, ensure_ascii=False))

#Name, Number, City, Date, Uuid, Email, PhoneNumber, Login, Password.