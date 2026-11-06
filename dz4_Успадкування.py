class Phone:
    def call(self):
        print("Виконується голосовий дзвінок)")
class Camera:
    def take_photo(self):
        print("йоу фотографія збережена в галерею смартфона")
class Smartphone(Phone, Camera):
    def show_all_features(self):
        print("Запуск функцій смартфона")
        self.call()
        self.take_photo()
my_smartphone = Smartphone()
my_smartphone.show_all_features()