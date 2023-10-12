from bluepy.btle import Peripheral, UUID, AssignedNumbers


def discover_and_write():
    # Define the UUIDs for the service and characteristic you want to write to
    SERVICE_UUID = UUID('a5d3a518-3d69-11ee-be56-0242ac120002')
    CHARACTERISTIC_UUID = UUID('d49293cc-85ee-4404-b141-100f3563085e')

    # Define the UUID of the device you want to connect to
    DEVICE_UUID = 'C0:49:EF:92:5E:66'

    # Define the value you want to write to the characteristic
    value = b'\x04'

    # Connect to the device
    peripheral = Peripheral(DEVICE_UUID)

    # Find the service and characteristic you want to write to
    service = peripheral.getServiceByUUID(SERVICE_UUID)
    characteristic = service.getCharacteristics(CHARACTERISTIC_UUID)[0]

    # Write the value to the characteristic
    characteristic.write(value)

    # Disconnect from the device
    peripheral.disconnect()
    
if __name__ == "__main__":
    discover_and_write()