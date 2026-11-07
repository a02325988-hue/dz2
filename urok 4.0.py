def textfunc (a,b):
    return a+b

print(textfunc(1,2))
a = textfunc (1,3)
print(a)
#

my_list = [1,2,3]

iterator = iter(my_list)
print(iterator)

#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))

for item in iterator:
    print(item)

class Counter:
    def __init__(self , max_number ):
        self.max_number = max_number
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i >= self.max_number:
            raise StopIteration
        return self.i

counter = Counter(5)
for item in counter:
    print(item)

def raise_to_the_degrees(number, max_degree ):
    i = 0
    for _ in range(number):
        yield number**i
        i += 1

res = raise_to_the_degrees(1332424582, 6769)
print(res)
for _ in res:
    print(_)

