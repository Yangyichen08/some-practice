import random
random_num = random.randint(1,100)
for frequency in range(1,11):
    number = input('才一个数字：')
    if random_num == int(number):
        print(f'恭喜你用了{frequency}次就猜对了')
        break
    elif random_num > int(number):
        print('很可惜，你猜小了',end = ',')
        n = 10 - frequency
        if n > 0:
            print(f'你还有{n}次机会')
        else:
            print('没机会了，下次加油！')
    elif random_num < int(number):
                    print('很可惜，你猜大了',end = ',')
                    n = 10 - frequency
                    if n > 0:
                        print(f'你还有{n}次机会')
                    else:
                        print('没机会了，下次加油！')