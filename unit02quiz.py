light = 'red'
state = 'solid'
if light == 'green':
    print('Drive through.')
elif state == 'solid' and light == 'yellow':
    print ('Prepare to stop.')
elif state == 'flashing' and light == 'yellow':
    print ('Proceed through with caution.')
elif state == 'solid' and light == 'red':
    print ('Stop!')
else:
    print('Treat as 4-way Stop sign.')
