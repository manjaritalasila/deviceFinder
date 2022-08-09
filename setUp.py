from iCloudInfo import getDevice
import time

# asks user to input iCloud username and password and stores
# data in a text file
username = input("What is your iCloud username?: ")
password = input("What is your iCloud password?: ")

with open('info.txt', 'w') as f:
    f.write("%s\n" % username)
    f.write("%s\n" % password)
        
numRooms = int(input("How many rooms are in your house/apartment?: "))
dev = getDevice(username, password)
roomNames = []
roomLat = []
roomLong = []

# maps out room locations
# user brings chosen device to each room and follows given direction
for i in range(1,(numRooms + 1)):
    avgLat = 0
    avgLong = 0
    if i != 1:
        print ("Go to the next room.")
    rdy = input("Type Y when you are in the room:")
    if rdy == "Y":
        print ("Please wait in the room for five minutes")
        time.sleep(300)
        roomName = input("Enter room name:")

        for i in range (0,100):
            loc = dev.location()
            avgLat += loc['latitude']
            avgLong += loc['longitude']
        print("Move around the room")
        time.sleep(5)
    
        for i in range (0,100):
            loc = dev.location()
            avgLat += loc['latitude']
            avgLong += loc['longitude']
        time.sleep(5)

        for i in range (0,100):
            loc = dev.location()
            avgLat += loc['latitude']
            avgLong += loc['longitude']
        time.sleep(5)

        for i in range (0,100):
            loc = dev.location()
            avgLat += loc['latitude']
            avgLong += loc['longitude']
        time.sleep(5)
    
        for i in range (0,100):
            loc = dev.location()
            avgLat += loc['latitude']
            avgLong += loc['longitude']

        avgLat = (avgLat/500)
        avgLong = (avgLong/500)

        roomLat.append(avgLat)
        roomLong.append(avgLong)
        roomNames.append(roomName)

    else:
        print ("Invalid Input")
        
# stores room location data in text files
with open('roomNames.txt', 'w') as f:
    for item in roomNames:
        f.write("%s\n" % item)
with open('roomLat.txt', 'w') as f:
    for item in roomLat:
        f.write("%s\n" % item)
with open('roomLong.txt', 'w') as f:
    for item in roomLong:
        f.write("%s\n" % item)
print("Set up is complete!")

