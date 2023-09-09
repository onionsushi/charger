import asyncio
from bleak import BleakScanner, BleakClient

# Replace with your service UUID and characteristic UUID
service_uuid = "a5d3a518-3d69-11ee-be56-0242ac120002"
characteristic_uuid = "d49293cc-85ee-4404-b141-100f3563085e"

# Value to write to the characteristic (example: [1, 2, 3, 4, 5])
value = "Hello, World!"

async def discover_and_write(service_uuid, characteristic_uuid, value):
    # Scan for nearby devices
    devices = await BleakScanner.discover()
    # Check each device for the specified service UUID
    for device in devices:
        # Connect to the device 
        if len(device.metadata.get("uuids", ["0"])) != 0 and device.metadata.get("uuids", ["0"])[0] == service_uuid:
            try:
                async with BleakClient(device.address) as client:
                    # await client.connect()
                    #chat gpt says connect() must be done.
                    print(f"Found device with address {device.address} that provides the service {service_uuid}.")
                    # Write a value to the characteristic
                    msg = await client.read_gatt_char(characteristic_uuid)
                    print(msg)
                    res = await client.write_gatt_char(characteristic_uuid, value, response = True)
                    print(f"Written value '{value}' to characteristic {characteristic_uuid}.")

                    msg = await client.read_gatt_char(characteristic_uuid)
                    print(msg)
                    print("disconnecting...")
                    print("disconnected")
                    # await client.disconnect()
                    # Disconnect from the device
                    return
            except Exception as e:
                print("failed to get device info: " + str(e))

    print(f"No devices found that provide the service.")

# Run the discover_and_write function
if __name__ == "__main__":
    asyncio.run(discover_and_write(service_uuid, characteristic_uuid, b'\x04'))