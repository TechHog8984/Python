import requests

avatar_url = 'https://bonk2.io/scripts/avatar_update.php'
login_url = 'https://bonk2.io/scripts/login_legacy.php'

avatar = '' #go to bonk.io, login, open up developer toos(control + shift + i), set your avatar, go to developer tools and the network tab, go into filter and type "avatar" (no quotes), click on the request, go to request and find the request data, copy the "newavatar" field, put it here
base_avatar_data = {'token' : '', 'task' : 'updateavatar', 'newavatarslot' : '1', 'newavatar' : avatar}
base_login_data = {'username' : '', 'password' : '', 'remember' : 'false'}

def userpass_set(user, password):
    try:
        new_login_data = base_login_data
        new_login_data['username'] = user
        new_login_data['password'] = password
        login_req = requests.post(url = login_url, data = new_login_data)
        login_data = login_req.json()
        if login_data.get('r'):
            login_success = login_data.get('r')
            if login_success == 'success' and login_data.get('token'):
                token = login_data.get('token')
                new_avatar_data = base_avatar_data
                new_avatar_data['token'] = token
                avatar_req = requests.post(url = avatar_url, data = new_avatar_data)
                avatar_data = avatar_req.json()
                if avatar_data.get('r'):
                    avatar_success = avatar_data.get('r')
                    if avatar_success == 'success':
                        return 'success'
                    elif avatar_data.get('e'):
                        return f"error: {avatar_data.get('e')}"
            elif login_data.get('e'):
                return f"error: {login_data.get('e')}"
    except: pass
    return 'fail'
def token_set(token):
    try:
        new_avatar_data = base_avatar_data
        new_avatar_data['token'] = token
        avatar_req = requests.post(url = avatar_url, data = new_avatar_data)
        avatar_data = avatar_req.json()
        if avatar_data.get('r'):
            avatar_success = avatar_data.get('r')
            if avatar_success == 'success':
                return 'success'
            elif avatar_data.get('e'):
                return f"error: {avatar_data.get('e')}"
    except: pass
    return 'fail'
if __name__ == '__main__':
    while True:
        try:
            douserpass = 'u' in input('Username and pass(u) or token(t)? ')
        except:
            douserpass = False
        if douserpass:
            user = input('User: ')
            password = input('Password: ')
            try:
                print(userpass_set(user, password))
            except:
                print('fail')
        else:
            token = input('Token: ')
            try:
                print(token_set(token))
            except:
                print('fail')
