from db import rooms
from user import room, user
import sys

match sys.argv[1:]:
    case ["user", user]:     print(f"{user=}")
    case ["join", room]:     print(f"{room=}")
    case ["write", *args]:   open('db.py','a').write(f"rooms['{room}'].append({(user, ' '.join(args))})\n")
    case _:                  print('\n'.join(f"{user}: {msg}" for user, msg in rooms[room]))

open('user.py','w').write('\n'.join([f"{room=}", f"{user=}"]))