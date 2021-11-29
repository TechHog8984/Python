import os, requests, time, string, random

url = 'https://bonk2.io/scripts/register_legacy.php'

def unpack(s):
    result = ''
    for a in s:
        result += a
    return result
def getpassword():
    return unpack(random.choices(string.ascii_letters + '!@#$%^&*(){}:".,<>', k = 10))

def getproxy():
    r = random.randint(0, len(proxies) - 1)
    return f'http://{proxies[r]}'

def send(name):
    print(f'attempting to create {name}')
    try:
        p = getpassword()
        req = requests.post(url = url, data = {'username' : name, 'password' : p, 'remember' : False})
        try:
            success = req.json().get('r')
            if success == 'success':
                file = open('bonk results.txt', 'a')
                file.write(f'{name} : {p}\n')
                file.close()
                return f'{success}\n{name} : {p}'
            else:
                return req.json()
        except:
            pass
    except:
        pass
    return f'failed to create {name}'

if __name__ == '__main__':
    clear = lambda: os.system('clear')
    clear()
    input('you are going to get rate limited after a while, beware ')
    basename = 'tZ1choSgF'
    name = f'{basename}1'
    n = 1
    while True:
        print(send(name))
        n += 1
        name = f'{basename}{n}'
        time.sleep(2)
