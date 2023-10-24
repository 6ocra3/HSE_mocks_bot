# -*- coding: utf-8 -*-
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

class Password:
    def __init__(self,field):
        self.field = field
        self.data = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '!', '?', '_', '#', '$', '%', '&', '*', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    def generate(self):
        pas = ''
        for i in range(random.randint(8,16)):
            pas += random.choice(self.data)
        return pas

class Email:
    def __init__(self,field):
        self.field = field
        self.em = ['@yandex.ru','@mail.ru','@gmail.com']
        self.data = ["car", "house", "book", "tree", "dog", "cat", "table", "chair", "phone", "computer", "hat", "sun", "moon", "star", "bed", "door", "window", "cup", "plate", "fork", "knife", "spoon", "guitar", "piano", "violin", "airplane", "train", "ship", "bicycle", "ball", "game", "music", "painting", "camera", "street", "river", "mountain", "ocean", "beach", "child", "parent", "friend", "teacher", "student", "doctor", "nurse", "engineer", "scientist", "artist", "writer", "singer", "dancer", "actor", "actress", "athlete", "chef", "police", "firefighter", "soldier", "king", "queen", "prince", "princess", "baby", "tiger", "lion", "elephant", "monkey", "snake", "bird", "fish", "butterfly", "flower", "grass", "forest", "cloud", "rain", "snow", "wind", "fire", "earth", "sky", "space", "time", "money", "love", "hope", "dream", "fear", "happiness", "sorrow", "truth", "beauty", "wisdom", "knowledge", "freedom", "justice", "peace", "war", "history", "science", "art", "music", "literature", "sport", "food", "drink", "coffee", "tea", "juice", "water", "pizza", "burger", "pasta", "salad", "cake", "ice cream", "chocolate", "hamburger", "sandwich", "cheese", "butter", "milk", "yogurt", "egg", "meat", "vegetable", "fruit", "bread", "rice", "potato", "onion", "garlic", "tomato", "carrot", "apple", "banana", "orange", "lemon", "pear", "peach", "grape", "strawberry", "blueberry", "cherry", "pineapple", "coconut", "kiwi", "watermelon", "melon", "pepper", "salt", "sugar", "spice", "flower", "tree", "grass", "leaf", "branch", "root", "sunflower", "rose", "tulip", "daisy", "lily", "oak", "pine", "maple", "ocean", "beach", "wave", "sand", "rock", "shell", "starfish", "seagull", "boat", "ship", "sail", "anchor", "desert", "mountain", "valley", "cave", "volcano", "river", "lake", "island", "forest", "rainforest", "jungle", "sunrise", "sunset", "cloud", "rain", "snow", "thunder", "lightning", "wind", "storm", "fire", "earthquake", "tornado", "time", "clock", "watch", "hour", "minute", "second", "day", "week", "month", "year", "past", "present", "future", "history", "science", "mathematics", "physics", "chemistry", "biology", "astronomy", "geography", "literature", "poetry", "novel", "story", "book", "author", "music", "song", "melody", "rhythm", "instrument", "guitar", "piano", "violin", "drum", "voice", "singer", "band", "orchestra", "dance", "dancer", "choreography", "actor", "actress", "theater", "movie", "film", "director", "screenplay", "camera", "painting", "sculpture", "photography", "canvas", "brush", "colors", "artist", "exhibition", "gallery", "writer", "poet", "fiction", "nonfiction", "essay", "novelist", "journalist", "newspaper", "magazine", "editor", "reader", "library", "teacher", "student", "school", "university", "classroom", "lecture", "homework", "exam", "study", "knowledge", "math", "science", "history", "language", "art", "music", "sport", "football", "basketball", "tennis", "swimming", "running", "athlete", "team", "competition", "medal", "stadium", "training", "game", "soccer", "baseball", "volleyball", "golf", "hockey", "skiing", "snowboarding", "surfing", "cycling", "boxing", "martial arts", "yoga", "gymnastics", "fitness", "exercise", "food", "drink", "restaurant", "cafeteria", "cafe", "menu", "chef", "cook", "cuisine", "recipe", "breakfast", "lunch", "dinner", "appetizer", "main course", "dessert", "beverage", "coffee", "tea", "juice", "water", "milk", "ice cream", "cake", "chocolate", "bread", "cheese", "fruit", "vegetable", "meat", "fish", "seafood", "spice", "salt", "pepper", "sugar", "oil", "sauce", "ketchup", "mayonnaise", "mustard", "honey", "seasoning", "snack", "chips", "popcorn", "crackers", "candy", "sweets", "cookies", "biscuit", "chocolate", "gum", "nut", "peanut", "cashew", "almond", "walnut", "pistachio", "coconut", "cereal", "rice", "pasta", "noodle", "soup", "salad", "sandwich", "burger", "pizza", "fries", "kebab", "sushi", "taco", "burrito", "pita", "pancake", "waffle", "omelette", "eggs", "bacon", "sausage", "ham", "yogurt", "milkshake", "smoothie", "cocktail", "coffee", "tea", "juice", "water", "soda", "energy drink", "beer", "wine", "whiskey", "vodka", "rum", "gin", "brandy", "cocktail", "alcohol", "glass", "bottle", "can", "straw", "ice", "lemon", "lime", "mint", "sugar", "salt", "pepper", "spice", "sauce", "ketchup", "mayonnaise", "mustard", "honey", "garlic", "onion", "chili", "bacon", "cheese", "butter", "cream", "jelly", "marmalade", "jam", "chocolate", "vanilla", "strawberry", "banana", "pineapple", "coconut", "watermelon", "melon", "grape", "orange", "apple", "lemon", "peach", "pear", "plum", "kiwi", "raspberry", "blueberry", "cherry", "blackberry", "apricot", "pomegranate", "fig", "date", "raisin", "nut", "peanut", "cashew", "almond", "walnut", "pistachio", "hazelnut", "pine nut", "coconut", "cereal", "oatmeal", "cornflakes", "rice", "wheat", "pasta", "noodle", "bread", "bagel", "croissant", "toast", "pancake", "waffle", "muffin", "donut", "cookie", "biscuit", "cake", "pie", "pastry", "tart", "pudding", "ice cream", "sundae", "gelato", "sorbet"]
    def generate(self):
        email = ''
        email += random.choice(self.data)
        email += random.choice(self.data)
        for i in range(3):
            email += str(random.randint(0,9))
        email += random.choice(self.em)
        return email

class Login:
    def __init__(self,field):
        self.field = field
        self.sbls = ['!', '?', '_', '#', '$', '%', '&', '*', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.data = ["car", "house", "book", "tree", "dog", "cat", "table", "chair", "phone", "computer", "hat", "sun", "moon", "star", "bed", "door", "window", "cup", "plate", "fork", "knife", "spoon", "guitar", "piano", "violin", "airplane", "train", "ship", "bicycle", "ball", "game", "music", "painting", "camera", "street", "river", "mountain", "ocean", "beach", "child", "parent", "friend", "teacher", "student", "doctor", "nurse", "engineer", "scientist", "artist", "writer", "singer", "dancer", "actor", "actress", "athlete", "chef", "police", "firefighter", "soldier", "king", "queen", "prince", "princess", "baby", "tiger", "lion", "elephant", "monkey", "snake", "bird", "fish", "butterfly", "flower", "grass", "forest", "cloud", "rain", "snow", "wind", "fire", "earth", "sky", "space", "time", "money", "love", "hope", "dream", "fear", "happiness", "sorrow", "truth", "beauty", "wisdom", "knowledge", "freedom", "justice", "peace", "war", "history", "science", "art", "music", "literature", "sport", "food", "drink", "coffee", "tea", "juice", "water", "pizza", "burger", "pasta", "salad", "cake", "ice cream", "chocolate", "hamburger", "sandwich", "cheese", "butter", "milk", "yogurt", "egg", "meat", "vegetable", "fruit", "bread", "rice", "potato", "onion", "garlic", "tomato", "carrot", "apple", "banana", "orange", "lemon", "pear", "peach", "grape", "strawberry", "blueberry", "cherry", "pineapple", "coconut", "kiwi", "watermelon", "melon", "pepper", "salt", "sugar", "spice", "flower", "tree", "grass", "leaf", "branch", "root", "sunflower", "rose", "tulip", "daisy", "lily", "oak", "pine", "maple", "ocean", "beach", "wave", "sand", "rock", "shell", "starfish", "seagull", "boat", "ship", "sail", "anchor", "desert", "mountain", "valley", "cave", "volcano", "river", "lake", "island", "forest", "rainforest", "jungle", "sunrise", "sunset", "cloud", "rain", "snow", "thunder", "lightning", "wind", "storm", "fire", "earthquake", "tornado", "time", "clock", "watch", "hour", "minute", "second", "day", "week", "month", "year", "past", "present", "future", "history", "science", "mathematics", "physics", "chemistry", "biology", "astronomy", "geography", "literature", "poetry", "novel", "story", "book", "author", "music", "song", "melody", "rhythm", "instrument", "guitar", "piano", "violin", "drum", "voice", "singer", "band", "orchestra", "dance", "dancer", "choreography", "actor", "actress", "theater", "movie", "film", "director", "screenplay", "camera", "painting", "sculpture", "photography", "canvas", "brush", "colors", "artist", "exhibition", "gallery", "writer", "poet", "fiction", "nonfiction", "essay", "novelist", "journalist", "newspaper", "magazine", "editor", "reader", "library", "teacher", "student", "school", "university", "classroom", "lecture", "homework", "exam", "study", "knowledge", "math", "science", "history", "language", "art", "music", "sport", "football", "basketball", "tennis", "swimming", "running", "athlete", "team", "competition", "medal", "stadium", "training", "game", "soccer", "baseball", "volleyball", "golf", "hockey", "skiing", "snowboarding", "surfing", "cycling", "boxing", "martial arts", "yoga", "gymnastics", "fitness", "exercise", "food", "drink", "restaurant", "cafeteria", "cafe", "menu", "chef", "cook", "cuisine", "recipe", "breakfast", "lunch", "dinner", "appetizer", "main course", "dessert", "beverage", "coffee", "tea", "juice", "water", "milk", "alcohol", "wine", "beer", "cocktail", "whiskey", "vodka", "rum", "gin", "brandy", "tequila", "champagne", "ice cream", "cake", "chocolate", "bread", "cheese", "fruit", "vegetable", "meat", "fish", "seafood", "spice", "salt", "pepper", "sugar", "oil", "sauce", "ketchup", "mayonnaise", "mustard", "honey", "seasoning", "snack", "chips", "popcorn", "crackers", "candy", "sweets", "cookies", "biscuit", "chocolate", "gum", "nut", "peanut", "cashew", "almond", "walnut", "pistachio", "coconut", "cereal", "rice", "pasta", "noodle", "soup", "salad", "sandwich", "burger", "pizza", "fries", "kebab", "sushi", "taco", "burrito", "pita", "pancake", "waffle", "omelette", "eggs", "bacon", "sausage", "ham", "yogurt", "milkshake", "smoothie", "cocktail", "coffee", "tea", "juice", "water", "soda", "energy drink", "beer", "wine", "whiskey", "vodka", "rum", "gin", "brandy", "cocktail", "alcohol", "glass", "bottle", "can", "straw", "ice", "lemon", "lime", "mint", "sugar", "salt", "pepper", "spice", "sauce", "ketchup", "mayonnaise", "mustard", "honey", "garlic", "onion", "chili", "bacon", "cheese", "butter", "cream", "jelly", "marmalade", "jam", "chocolate", "vanilla", "strawberry", "banana", "pineapple", "coconut", "watermelon", "melon", "grape", "orange", "apple", "lemon", "peach", "pear", "plum", "kiwi", "raspberry", "blueberry", "cherry", "blackberry", "apricot", "pomegranate", "fig", "date", "raisin", "nut", "peanut", "cashew", "almond", "walnut", "pistachio", "hazelnut", "pine nut", "coconut", "cereal", "oatmeal", "cornflakes", "rice", "wheat", "pasta", "noodle", "bread", "bagel", "croissant", "toast", "pancake", "waffle", "muffin", "donut", "cookie", "biscuit", "cake", "pie", "pastry", "tart", "pudding", "ice cream", "sundae", "gelato", "sorbet"]
    def generate(self):
        login = ''
        fl = 1
        login += random.choice(self.data)
        for i in range(random.randint(3,5)):
            login += str(random.randint(0,9))
        fl = random.randint(0,1)
        if fl:
            login = random.choice(self.sbls) + login
        return login


class PhoneNumber:
    def __init__(self,field):
        self.field = field
        self.data = ['1','2','3','4','5','6','7','8','9','0']
    def generate(self):
        pn = '+79'
        for i in range(8):
            pn += random.choice(self.data)
        return pn




mask = [Number("age", 5, 20), Name("name"), Email('email'), PhoneNumber('phone_number'), Login('login'), Password('password')]
itog = []
for i in range(5):
    a = {}
    for j in mask:
        a[j.field] = j.generate()
    itog.append(a)

print(json.dumps(itog, ensure_ascii=False))

#Name, Number, City, Date, Uuid, Email, PhoneNumber, Login, Password.