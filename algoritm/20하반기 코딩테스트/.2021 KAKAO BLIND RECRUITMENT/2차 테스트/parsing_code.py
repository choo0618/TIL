# parsing code

import requests

url = 'http://.....'


def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token}).json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()


def p0_simulator():
    user = 'test'
    problem = 1
    cnt = 4

    ret = start(user, problem, cnt)
    token = ret['token']

    while True:
        call_ret = oncalls(token)
        cmd = []

        for idx in range(cnt):
            # cmd 만들기
            pass

        if call_ret['is_end']:
            break

        action(token, cmd)


if __name__ == '__main__':
    p0_simulator()