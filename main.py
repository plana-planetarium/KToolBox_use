import os

url = os.getenv("URL") + ','
#url = "https://kemono.su/fanbox/user/16034374, https://kemono.su/fanita/user/16034374," + ','
url = url.replace(' ', '').split(',')
#user_server = []
#user_name = []

for url_down in url:
    if url_down != '':
        os.system("ktoolbox sync-creator " + url_down)
        #user_server += [url_down.split('/user/')[0].replace('https://kemono.su/', '')]
        #dir_file = os.listdir('./')
        #for file in dir_file:
        #    if file not in user_name and file != 'main.py':
        #        user_name += [file]

#i = 0
#user = 'kemono_' + user_server[i] + '-' + user_name[i]
#i += 1
#while i <= len(user_server) - 1:
#    user += '_' + user_server[i] + '-' + user_name[i]
#    i += 1
#
#os.environ["USER"] = user
