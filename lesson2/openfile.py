'''
вcегда нужно использовать with - позволяет не беспокоиться о том, закрыт файл или нет. он закроется автоматом после завершения программы
для работы с кириллицей всегда используем utf-8
w - запись (содержимое перезапишется полностью), r - чтение,
a - новое содержимое пишется в конец файла (\n - перенос строки, t - табуляция)
'''

#var1
number_of_words = 0

with open ("../referat.txt","r", encoding = "utf-8") as ref:
    for line in ref:
#   line = line.upper()
        print(line)
        number_of_words += len(line.split())

    print(number_of_words, "слов")

'''
#var 2
with open ("../referat.txt","r", encoding = "utf-8") as ref:

    content = ref.read()
    print(content)
    print(len(content.split()), "слов")
'''