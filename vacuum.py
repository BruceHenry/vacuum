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
    if status == 0:
        return False
    else:
        return True


def suck(location):
    print("suck at", location)
