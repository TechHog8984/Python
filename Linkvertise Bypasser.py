#this is a linkvertise bypasser using 3 apis.
import requests, time

def main():
    link = input('Enter link here: ')
    start = time.time()
    if not 'https://' in link and not 'http://' in link:
        link = f'https://{link}'
    get1 = f'https://bypass.bot.nu/bypass2?url={link}'
    get2 = f'https://vacant-curtly-composure.herokuapp.com/bypass2?url={link}'
    post1 = ' https://api.bypass.vip/'
    
    try:
        req1 = requests.get(url = get1)
        result1 = req1.json()
        print(f"Method 1: {result1.get('destination') or result1.get('msg')}")
    except:
        print('Failed to get method 1.')

    try:
        req2 = requests.get(url = get2)
        result2 = req2.json()
        print(f"Method 2: {result2.get('destination') or result2.get('msg')}")
    except:
        print('Failed to get method 2. ')
    
    try:
        req3 = requests.post(url = post1, data = {'url' : link})
        result3 = req3.json()
        print(f"Method 3: {result3.get('destination') or result3.get('response')}")
    except:
        print('Failed to get method 3')

    print(f'Time taken: {round(time.time() - start, 2)}')
    main()

if __name__ == '__main__':
    main()
