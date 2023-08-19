import asyncio
from bleak import BleakScanner, BleakClient

# Replace with your service UUID and characteristic UUID
service_uuid = "19B10010-E8F2-537E-4F6C-D104768A1214"
characteristic_uuid = "19B10011-E8F2-537E-4F6C-D104768A1214"

# Value to write to the characteristic (example: [1, 2, 3, 4, 5])
value = [1, 2, 3, 4, 5]

async def discover_and_write(service_uuid, characteristic_uuid, value):
    # Scan for nearby devices
    devices = await BleakScanner.discover()

    # Check each device for the specified service UUID
    for device in devices:
        # Connect to the device
        async with BleakClient(device.address) as client:
            services = await client.get_services()
            if any(s.uuid == service_uuid for s in services):
                print(f"Found device with address {device.address} that provides the service {service_uuid}.")

                # Write a value to the characteristic
                await client.write_gatt_char(characteristic_uuid, bytearray(value))
                print(f"Written value '{value}' to characteristic {characteristic_uuid}.")

                # Disconnect from the device
                return

    print(f"No devices found that provide the service {service_uuid}.")

# Run the discover_and_write function
asyncio.run(discover_and_write(service_uuid, characteristic_uuid, value))