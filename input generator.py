import random

for _ in range(5):
    x = random.randint(3, 4)
    print('5 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 4), random.randint(0, 4), random.randint(1, 2)))

for _ in range(5):
    x = random.randint(3, 4)
    print('6 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 5), random.randint(0, 5), random.randint(1, 2)))

for _ in range(5):
    x = random.randint(4, 7)
    print('7 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 6), random.randint(0, 6), random.randint(1, 2)))

for _ in range(4):
    x = random.randint(5, 10)
    print('8 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 7), random.randint(0, 7), random.randint(1, 3)))

for _ in range(3):
    x = random.randint(7, 13)
    print('9 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 8), random.randint(0, 8), random.randint(1, 3)))

for _ in range(3):
    x = random.randint(10, 15)
    print('10 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 9), random.randint(0, 9), random.randint(1, 3)))

for _ in range(3):
    x = random.randint(13, 18)
    print('11 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 10), random.randint(0, 10), random.randint(1, 3)))

for _ in range(3):
    x = random.randint(15, 20)
    print('12 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 11), random.randint(0, 11), random.randint(1, 4)))

for _ in range(3):
    x = random.randint(17, 25)
    print('13 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 12), random.randint(0, 12), random.randint(2, 4)))

for _ in range(3):
    x = random.randint(20, 30)
    print('14 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 13), random.randint(0, 13), random.randint(2, 4)))

for _ in range(3):
    x = random.randint(20, 35)
    print('15 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 14), random.randint(0, 14), random.randint(2, 5)))

for _ in range(2):
    x = random.randint(30, 40)
    print('16 %d' % (x))
    for _ in range(x):
         print('%d %d %d' % (random.randint(0, 15), random.randint(0, 15), random.randint(2, 5)))

for _ in range(2):
    x = random.randint(30, 40)
    print('17 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 16), random.randint(0, 16), random.randint(2, 5)))

for _ in range(2):
    x = random.randint(30, 45)
    print('18 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 17), random.randint(0, 17), random.randint(3, 6)))
    
for _ in range(2):
    x = random.randint(30, 50)
    print('19 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 18), random.randint(0, 18), random.randint(3, 6)))

for _ in range(2):
    x = random.randint(35, 50)
    print('20 %d' % (x))
    for _ in range(x):
        print('%d %d %d' % (random.randint(0, 19), random.randint(0, 19), random.randint(3, 6)))
