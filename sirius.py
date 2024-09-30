from random import randint
from threading import Thread, Lock
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(150):
            b = randint(50, 500)
            if self.lock.locked() and self.balance+b >= 500:
                self.balance = self.balance + b
                self.lock.release()
                print('блок снят')
                print(f"Пополнение: {b}. Баланс: {self.balance}" + '\n', end='')
            else:
                self.balance = self.balance + b
                print(f"Пополнение: {b}. Баланс: {self.balance}" + '\n', end='')

    def take(self):
        for i in range(150):
            c = randint(50, 500)
            if not self.lock.locked():
                if c > self.balance:
                    print(f'Запрос на {c}' + '\n', end='')
                    self.lock.acquire()
                    print("Запрос отклонён, недостаточно средств" + '\n', end='')
                else:
                    print(f'Запрос на {c}' + '\n', end='')
                    self.balance -= c
                    print(f'Снятие: {c}. Баланс: {self.balance}' + '\n', end='')


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
