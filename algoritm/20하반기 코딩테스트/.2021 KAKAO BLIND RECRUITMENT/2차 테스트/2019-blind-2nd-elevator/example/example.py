import requests


url = 'http://localhost:8000'


def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token}).json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()

def Enter(floor, call, status, passenger_cnt):
    if passenger_cnt == 8:
        return False
    for passenger in call:
        if passenger['start'] == floor:
            passenger_Status = 1
            if passenger['start'] > passenger['end']:
                passenger_Status = -1
            if status == 0 or status == passenger_Status:
                return True
    return False


def Exit(floor, passengers):
    for passenger in passengers:
        if passenger['end'] == floor:
            return True
    return False


def command(idx,elevator,calls, enter_list):
    DicStatus = {'STOPPED':'STOP', 'OPENED':'OPEN', 'UPWARD':'UP', 'DOWNWARD':'DOWN'}

    Floor = elevator['floor']
    Status = elevator['status']
    Passengers = elevator['passengers']
    Passengers_cnt = len(Passengers)

    Elevator_Status = 0  # -1:down, 0:empty, 1:up
    if Passengers:
        if Passengers[-1]['start'] < Passengers[-1]['end']:
            Elevator_Status = 1
        elif Passengers[-1]['start'] > Passengers[-1]['end']:
            Elevator_Status = -1

    cmd = {"elevator_id": idx, "command": DicStatus[Status]}

    if Status == 'STOPPED':         # STOP, OPEN, UP, DOWN
        if Enter(Floor, calls, Elevator_Status, Passengers_cnt) or Exit(Floor, Passengers):
            cmd['command'] = 'OPEN'
        elif Passengers:
            if Elevator_Status == 1:
                cmd['command'] = 'UP'
            elif Elevator_Status == -1:
                cmd['command'] = 'DOWN'
        elif not Passengers and calls:
            Passenger = calls[0]['start']
            if Passenger > Floor:
                cmd['command'] = 'UP'
            elif Passenger < Floor:
                cmd['command'] = 'DOWN'
            else:
                cmd['command'] = 'OPEN'
    elif Status == 'OPENED':        # OPEN, ENTER, EXIT, CLOSE
        PassegersCnt = len(Passengers)
        Possible = 8 - PassegersCnt
        if Exit(Floor, Passengers):
            ids = []
            for passenger in Passengers:
                if passenger['end'] == Floor:
                    ids.append(passenger['id'])
            cmd['command'] = 'EXIT'
            cmd['call_ids'] = ids
        elif Enter(Floor, calls, Elevator_Status, Passengers_cnt) and Possible > 0:
            ids = []
            tmp = 0
            for passenger in calls:
                passenger_status = 1
                if passenger['start'] > passenger['end']:
                    passenger_status = -1
                if passenger['start'] == Floor:
                    if (Elevator_Status == 0 or (Elevator_Status == passenger_status)) and passenger['id'] not in enter_list:
                        ids.append(passenger['id'])
                        enter_list.append(passenger['id'])
                        tmp += 1
                        if tmp ==Possible:
                            break
            cmd['command'] = 'ENTER'
            cmd['call_ids'] = ids[:Possible]
        else:
            cmd['command'] = 'CLOSE'
    elif Status == 'UPWARD':        # STOP, UP
        if Floor == 25 or Enter(Floor, calls, Elevator_Status, Passengers_cnt) or Exit(Floor, Passengers):
            cmd['command'] = 'STOP'
    elif Status == 'DOWNWARD':      # STOP DOWN
        if Floor == 1 or Enter(Floor, calls, Elevator_Status, Passengers_cnt) or Exit(Floor, Passengers):
            cmd['command'] = 'STOP'

    return cmd, enter_list


def p0_simulator():
    user = 'tester'
    problem = 2
    count = 1

    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))

    while True:
        call_ret = oncalls(token)
        cmd = []
        Enter_list = []
        for idx in range(count):
            Cmd, enter = command(idx, call_ret['elevators'][idx], call_ret['calls'], Enter_list)
            cmd.append(Cmd)
            Enter_list += enter
        if call_ret['is_end']:
            break
        action(token, cmd)


if __name__ == '__main__':
    p0_simulator()


