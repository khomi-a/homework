import os
from shutil import rmtree


def user_connection(username):
    import random
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"


def establish_connection(auth=True):
    import random
    id = f"{random.randint(0,100000000):010}"
    if auth:
        yield f"auth {id}"
    yield from user_connection(id)
    if auth:
        yield f"disconnect {id}"


def connection():
    import random
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]


def connect_user(id):
    with open(f'user_connection/{id}.txt', 'a') as af:
        yield from write_to_file(af)


def write_to_file(f):
    while True:
        message = yield
        if message == 'disconnect':
            yield
        f.write(message + '\n')


def task_planner():
    print('Connection established')
    users = {}
    for s in connection():
        s = s.split()
        if s[0] == 'auth':
            connect_s = connect_user(s[1])
            connect_s.send(None)
            users[s[1]] = connect_s
        elif s[0] in users.keys():
            users[s[0]].send(s[1])
        elif s[0] == 'disconnect':
            users[s[1]].send(s[0])
    print('Finished')


if 'user_connection' in os.listdir():
    rmtree('user_connection')
    os.mkdir('user_connection')
else:
    os.mkdir('user_connection')

task_planner()

