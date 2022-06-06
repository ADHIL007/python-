c = ""
started = False
stopped = False
while c.lower() != 'quit':
    c = input('>')
    if c == 'help':
        print('''
                    start - to start car
                    stop - to stop car
                    quit - to quit game
        
        ''')
    elif c == 'start':
        if started:
            print('car already started')
            started = False
        else:
            started = True
            print('car started')

    elif c == 'stop':
        if stopped:
            stopped = False
            print('car already stopped')
        else:
            stopped = True
            print('car stopped')
    elif c == 'quit':
        break
    else:
        print('sorry id ont understand')