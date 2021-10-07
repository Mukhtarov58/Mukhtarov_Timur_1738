import sys
import json

with open('users.csv', 'r', encoding='utf-8') as f:
    users = [user for user in f.read().split('\n')]

with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobbys = [hobby for hobby in f.read().split('\n')]

if len(users) < len(hobbys):
    sys.exit('1')

result_file = {user: hobbys[i] if len(hobbys) > i else None for i, user in enumerate(users)}

with open('hobby_man.json', 'w', encoding='utf-8') as f:
    json.dump(result_file, f)

with open('hobby_man.json', 'r', encoding='utf-8') as f:
    print(json.load(f))
