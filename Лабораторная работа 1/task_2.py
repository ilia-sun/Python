# TODO Найдите количество книг, которое можно разместить на дискете
disketa = 1.44
pages = 100
lines = 50
symbols = 25
all_symbols = symbols * lines * pages
memory = (4 * all_symbols)/(1024*1024)
numbers = disketa // memory
print("Количество книг, помещающихся на дискету:", int(numbers))
