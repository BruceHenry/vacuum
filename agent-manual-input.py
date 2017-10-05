def vacuum(env, location):
    step_count = 0
    # Decide which direction to go. 1 means right, and -1 means left.
    if location < len(env) / 2:
        direction = -1
    else:
        direction = 1
    # First round to one end
    while True:
        if sense_dirt(env[location]):
            suck(location)
            step_count += 1
            env[location] = 0
        location += direction
        if location == -1 or location == len(env):
            break
        move(direction, location)
        step_count += 1
    # Turn around
    direction = - direction
    location += direction
    while True:
        if sense_dirt(env[location]):
            suck(location)
            step_count += 1
            env[location] = 0
        location += direction
        if location == -1 or location == len(env):
            break
        move(direction, location)
        step_count += 1
    return step_count


def move(direction, location):
    if direction == 1:
        print("move right to", location)
    elif direction == -1:
        print("move left to", location)
    else:
        raise "Wrong Direction!"


def sense_dirt(status):
    if int(status) == 0:
        return False
    else:
        return True


def suck(location):
    print("suck at", location)


if __name__ == "__main__":
    print("Please input environment, 1 for dirty, 0 for clean")
    print("For example: 1101 means there are 4 squares with statuses: dirt, dirt, no dirt, dirt")
    env = [int(i) for i in list(input())]
    while True:
        print("Please input valid location of vacuum (no less than 0 and less than length of environment):")
        location = int(input())
        if 0 <= location < len(env):
            break
    step = vacuum(env, location)
    print('\nIt takes agent ' + str(step) + ' steps to clean the room')