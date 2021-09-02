import requests, random

def check(pin):
    req = requests.get(f'https://kahoot.it/reserve/session/{pin}')
    try:
        return req.json()
    except:
        return False

def main():
    t = input('Check a pin(1) or gen pins(2): ')
    if t == '1' :
        pin = input('Pin: ')
        if check(pin):
            print(f'{pin}: success')
        else:
            print(f'{pin}: fail')
    elif '2' in t:
        while True:
            pin = random.randint(1000000, 9999999)
            if check(pin):
                print(f'{pin}: success')
    main()

if __name__ == '__main__':
    main()