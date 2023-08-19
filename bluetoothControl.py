import asyncio
from bleak import BleakScanner, BleakClient

# Replace with your service UUID and characteristic UUID
service_uuid = "a5d3a518-3d69-11ee-be56-0242ac120002"
characteristic_uuid = "bd613920-3d64-11ee-be56-0242ac120002"

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
                    print(f"Found device with address {device.address} that provides the service {service_uuid}.")

                    # Write a value to the characteristic
                    if type(value) != str:
                        await client.write_gatt_char(characteristic_uuid, bytearray(value))
                    else:
                        await client.write_gatt_char(characteristic_uuid, bytearray(value.encode('utf-8')))
                    print(f"Written value '{value}' to characteristic {characteristic_uuid}.")

                    # Disconnect from the device
                    return
            except:
                print("failed to get device info")

    print(f"No devices found that provide the service {service_uuid}.")

# Run the discover_and_write function
asyncio.run(discover_and_write(service_uuid, characteristic_uuid, "OHOH"))