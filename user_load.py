import json
filename = 'username.json'
with open(filename) as f:
    username=json.load(f)
    print(f"Welcome back, {username}!")

    #combine user_dump and user_load into one file the code in user_dump_load

