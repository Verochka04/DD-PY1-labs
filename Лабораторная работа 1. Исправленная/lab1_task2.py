# TODO Найдите количество книг, которое можно разместить на дискете

Volume_in_megabytes = 1.44
Number_of_pages = 100
Number_of_lines = 50
Number_of_symbols = 25
Place_for_the_symbol_in_bytes = 4
Megabytes = 1024
Kilobytes = 1024

Volume_in_bytes = Volume_in_megabytes * Megabytes * Kilobytes
Volume_of_the_book = Number_of_pages * Number_of_lines * Number_of_symbols * Place_for_the_symbol_in_bytes
Number_of_books = Volume_in_bytes / Volume_of_the_book
Number_of_books = int(Number_of_books)
print("Количество книг, помещающихся на дискету:", Number_of_books)
