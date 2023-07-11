from config import room, db_path
import sys
from functools import partial
from getpass import getuser

db = partial(open, db_path+room)

match sys.argv[1:]:
    case ["join", room]:     print(f"{room=}")
    case ["write", *args]:   db('a').write(f"user='{getuser()}'; msg='{' '.join(args)}'\n")
    case _:
        try:
            for line in db():
                exec(line+'print(f"{user}: {msg}")')
        except FileNotFoundError:
            print()

open('config.py','w').write(f"{room=}\n{db_path=}")