class Cat:
    def __init__(self, height=35):
        self.height = height
        print("hi im a cat")
    def grow(self, height=1):
        self.height += height
    def feed(self):
        print("Чим покормити кота?")
        print("1. Риба (росте на 5)")
        print("2. Молоко (росте на 2)")
        print("3. Корм (росте на 10)")
        choice = input("Зробіть вибір (1/2/3 або назву): ").strip().lower()

        if choice in ["1", "риба", "рыба"]:
            self.grow(5)
            print("Мур! Кіт з'їв рибу і підріс.")
        elif choice in ["2", "молоко"]:
            self.grow(2)
            print("Ням! Кіт попив молока і трохи підріс.")
        elif choice in ["3", "корм"]:
            self.grow(10)
            print("Ого! Супер-корм! Кіт став набагато більшим.")
        else:
            print("Кіт таке не їсть...")

        print(f"Поточний зріст кота: {self.height}")
my_cat = Cat()
my_cat.feed()
