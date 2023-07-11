from user import room, user, db_path
import sys
from functools import partial

db = partial(open, db_path+room)

match sys.argv[1:]:
    case ["user", user]:     print(f"{user=}")
    case ["join", room]:     print(f"{room=}")
    case ["write", *args]:   db('a').write(f"{user=}; msg='{' '.join(args)}'\n")
    case _:
        try:
            for line in db():
                exec(line+'print(f"{user}: {msg}")')
        except FileNotFoundError:
            print()

open('user.py','w').write(f"{room=}\n{user=}\n{db_path=}")