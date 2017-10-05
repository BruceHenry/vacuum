import vacuum

if __name__ == "__main__":
    print("Please input environment, 1 for dirty, 0 for clean")
    print("For example: 1101 means there are 4 squares with statuses: dirt, dirt, no dirt, dirt")
    env = [int(i) for i in list(input())]
    while True:
        print("Please input valid location of vacuum (no less than 0 and less than length of environment):")
        location = int(input())
        if 0 <= location < len(env):
            break
    step = vacuum.vacuum(env, location)
    print('\nIt takes agent ' + str(step) + ' steps to clean the room')
