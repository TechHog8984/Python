import requests, random
from threading import Thread

def check(pin):
    try:
        req = requests.get(f'https://kahoot.it/reserve/session/{pin}')
        try:
            return req.json()
        except:
            return False
    except:
        return False
def gen():
            while True:
                pin = random.randint(1000000, 9999999)
                if check(pin):
                    print(f'{pin}: success')

def main():
    t = input('Check a pin(1) or gen pins(2): ')
    if t == '1' :
        pin = input('Pin: ')
        if check(pin):
            print(f'{pin}: success')
        else:
            print(f'{pin}: fail')
    elif '2' in t:
        dothreading = input('Use threading?(y/n): ') == 'y'
        if dothreading:
            threads = []
            try:
                threadamount = int(input('Thread amount: '))
            except:
                threadamount = 5
            for i in range(threadamount + 1):
                thread = Thread(target=gen)
                threads.append(thread)
            for i in threads:
                i.start()
            for i in threads:
                i.join()
        else:
            gen()
    main()

if __name__ == '__main__':
    main()
