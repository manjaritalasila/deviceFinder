from iCloudInfo import getDevice
import time

# asks for user to input iCloud username and password and stores
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
    rdy = input("Type Y when you are you ready to begin:")
    if rdy == "Y":
        roomName = input("Stand in room corner one. Enter room name:")

        #corner one
        for i in range (0,3):
            loc = dev.location()
            avgLat += loc['latitude']
            avgLong += loc['longitude']
        print("Move to corner two")
        time.sleep(10)
    
        #corner two
        for i in range (0,3):
            loc = dev.location()
            avgLat += loc['latitude']
            avgLong += loc['longitude']
        print("Move to corner three")
        time.sleep(10)

        #corner three
        for i in range (0,3):
            loc = dev.location()
            avgLat += loc['latitude']
            avgLong += loc['longitude']
        print("Move to corner four")
        time.sleep(10)

        #corner four
        for i in range (0,3):
            loc = dev.location()
            avgLat += loc['latitude']
            avgLong += loc['longitude']
        print("Move to room center")
        time.sleep(10)
    
        #center
        for i in range (0,3):
            loc = dev.location()
            avgLat += loc['latitude']
            avgLong += loc['longitude']
        time.sleep(5)

        avgLat = (avgLat/15)
        avgLong = (avgLong/15)

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
