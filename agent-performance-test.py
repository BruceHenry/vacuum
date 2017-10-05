import itertools


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
            # suck(location)
            step_count += 1
            env[location] = 0
        location += direction
        if location == -1 or location == len(env):
            break
        # move(direction, location)
        step_count += 1
    # Turn around
    direction = - direction
    location += direction
    while True:
        if sense_dirt(env[location]):
            # suck(location)
            step_count += 1
            env[location] = 0
        location += direction
        if location == -1 or location == len(env):
            break
        # move(direction, location)
        step_count += 1
    return step_count


def sense_dirt(status):
    if int(status) == 0:
        return False
    else:
        return True


# Test environments in input length for all possible initial dirt configurations and agent locations
def performance_test(length):
    result = []
    for env in itertools.product('10', repeat=length):
        for location in range(0, len(env)):
            result.append(vacuum(list(env), location))
    print('Result set: ' + str(result))
    print('To clean a room with ' + str(length) + ' length, it takes the agent ' + str(sum(result) / len(
        result)) + ' steps on average')


performance_test(10)
