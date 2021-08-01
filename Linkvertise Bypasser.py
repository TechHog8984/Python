#this is a linkvertise bypasser using 3 apis.
import requests, json, time

def main():
    link = input('Enter link here: ')
    start = time.time()
    get1 = 'https://bypass.bot.nu/bypass2?url=' + link
    get2 = 'https://vacant-curtly-composure.herokuapp.com/bypass2?url=' + link
    post1 = ' https://api.bypass.vip/'
    
    try:
        req1 = str(requests.get(url = get1).content)
        result1 = json.loads(req1[2:len(req1)-1])
        print(f"Method 1: {result1.get('destination') or result1.get('msg')}")
    except:
        print('Failed to get method 1.')

    try:
        req2 = str(requests.get(url = get2).content)
        result2 = json.loads(req2[2:len(req2)-1])
        print(f"Method 2: {result2.get('destination') or result2.get('msg')}")
    except:
        print('Failed to get method 2. ')
    
    try:
        req3 = str(requests.post(url = post1, data = {'url' : link}).content)
        result3 = json.loads(req3[2:len(req3)-1])
        print(f"Method 3: {result3.get('destination') or result3.get('response')}")
    except:
        print('Failed to get method 3')

    print(f'Time taken: {round(time.time() - start, 2)}')
    main()

if __name__ == '__main__':
    main()
