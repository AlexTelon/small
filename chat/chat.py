room = 'derp'
user = 'alex'
from db import rooms
import sys

def history():
    state()
    print('======')
    print('\n'.join(f"{user}: {msg}" for user, msg in rooms[room]))

def state():
    print(f"{room=}, {user=}")


match sys.argv[1:]:
    case ["user", user]:     state()
    case ["join", room]:     state()
    case ["write", *args]:   rooms[room].append((user, ' '.join(args)))
    case _:                  history()


content = open(__file__).read().splitlines()[2:]
open(__file__, 'w').write(f"room = '{room}'\nuser = '{user}'\n" + '\n'.join(content))

content = open('db.py').read().splitlines()[:-1]
open('db.py', 'w').write('\n'.join(content) + f"\nrooms |= {dict(rooms)}\n")
# open('db.py'', 'a').write(f"rooms |= {{'{room}': {rooms[room]}}}\n")