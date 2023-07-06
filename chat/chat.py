from user import room, user, db_path
import sys
from functools import partial

db = partial(open, db_path+room)

def logs():
    try:
        print('\n'.join(f"{user}: {msg}" for user, msg in map(eval, db('r'))))
    except FileNotFoundError:
        print()

match sys.argv[1:]:
    case ["user", user]:     print(f"{user=}")
    case ["join", room]:     print(f"{room=}")
    case ["write", *args]:   db('a').write(f"'{user}', '{' '.join(args)}'\n")
    case _:                  logs()

open('user.py','w').write(f"{room=}\n{user=}\n{db_path=}")