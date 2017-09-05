list = [5,1,2,2.33,0] # не доделала
def get_answer2():
    while True:
        try:
            answer = str.lower(input("На какое число из списка [5,1,2,2.33,0] мы будем делить 23? ")) #ZeroDivisionError
            summ = 23/int(answer) #TypeError
            print("Результат деления 23 на {}: ".format(answer),summ)
        except ZeroDivisionError:
            print("На ноль делить нельзя, попробуйте еще раз")
        except (TypeError, ValueError):
            print("Возьмите целое число")
        except KeyboardInterrupt:
            return
get_answer2()