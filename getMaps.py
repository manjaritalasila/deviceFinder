
# returns room names and coordinates
def getMaps():
    
    # empty lists
    roomNames = []
    roomLong = []
    roomLat = []

    # opens files and reads the contents
    with open('roomNames.txt', 'r') as f:
        for line in f:
            x = line[:-1]
            roomNames.append(x)


    with open('roomLat.txt', 'r') as f:
        for line in f:
            x = float(line[:-1])
            roomLat.append(x)

    with open('roomLong.txt', 'r') as f:
        for line in f:
            x = float(line[:-1])
            roomLong.append(x)

    return roomNames, roomLat, roomLong



