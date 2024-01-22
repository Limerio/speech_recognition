from utils.client import close, send

done = False

while not done:
    try:
        msg = input("Enter the message : ")
        if msg == 'disconnect':
            send('disconnect')
            done = True
            break

        print(send(msg))
    except KeyboardInterrupt:
        send('disconnect')
        done = True
    except ConnectionAbortedError:
        done = True

print('Disconnected')
close()