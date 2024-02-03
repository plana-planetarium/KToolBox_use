import os

url = os.getenv("URL").replace(' ', '').split(',')
user_server = []
user_name = []

for line in url:
    if url != '':
        os.system("ktoolbox sync-creator " + line)
        user_server += [url.replace('https://kemono.su/', '').split('/user/')[0]]
        dir_file = os.listdir('./images').remove('main.py')
        for i in dir_file:
            if i not in user_name:
                user_name += [i]

i = 0
user = 'kemono_' + user_server[i] + '-' + user_name[i]
i += 1
while i <= len(user_server) + 1:
    user += '_' + user_server[i] + '-' + user_name[i]
    i += 1
    
os.environ["USER"] = user
