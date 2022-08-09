from pyicloud import PyiCloudService
from getMaps import getMaps
import time

# returns device of interest
def getDevice (username,password):
    api = PyiCloudService(username, password)
    if api.requires_2fa:
        print("Two-factor authentication required.")
        code = input("Enter the code you received of one of your approved devices: ")
        result = api.validate_2fa_code(code)
        print("Code validation result: %s" % result)

        if not result:
            print("Failed to verify security code")
            sys.exit(1)

        if not api.is_trusted_session:
            print("Session is not trusted. Requesting trust...")
            result = api.trust_session()
            print("Session trust result %s" % result)

            if not result:
                print("Failed to request trust. You will likely be prompted for the code again in the coming weeks")
    elif api.requires_2sa:
        import click
        print("Two-step authentication required. Your trusted devices are:")

        devices = api.trusted_devices
        for i, device in enumerate(devices):
            print(
                "  %s: %s" % (i, device.get('deviceName',
                "SMS to %s" % device.get('phoneNumber')))
            )

        device = click.prompt('Which device would you like to use?', default=0)
        device = devices[device]
        if not api.send_verification_code(device):
            print("Failed to send verification code")
            sys.exit(1)

        code = click.prompt('Please enter validation code')
        if not api.validate_verification_code(device, code):
            print("Failed to verify verification code")
            sys.exit(1)
            
    # provides user with list of devices associated with iCloud account
    for i in range (1,len(api.devices.keys())+ 1):
        dev = api.devices[i-1]
        if dev.location() != None:
            print (str(i) + " - " + str(api.devices[i-1]))

    dev = api.devices[(int(input("Which device are you looking for? Input the number assigned to that particular device: ")) - 1)]
    return dev

# finds room location of device
def findLoc():
    iCloudInfo = []
    # reads text file with iCloud account info
    with open('info.txt', 'r') as f:
        for line in f:
            x = line[:-1]
            iCloudInfo.append(x)
    [username, password] = iCloudInfo
    dev = getDevice(username, password)
    [roomNames, roomLat, roomLong] = getMaps()
    loc = dev.location()

    # finds battery and coordinates of device
    bat = dev.status()
    bat = "This device has " + str(bat['batteryLevel'] * 100) + "% battery" + " left"
    lat = loc['latitude']
    long = loc['longitude']
    user_location = [lat,long]


    # determines which room device is in
    vals = []
    for i in range (0, len(roomNames)):
        vals.append((abs(user_location[0] - roomLat[i])) +  (abs(user_location[1] - roomLong[i])))
       
    X = vals.index(min(vals))
    print(bat)
    if (min(vals)) > 0.1:
        print ("It is not on the premises")
    else:
        print("It is located in: " + roomNames[X])


