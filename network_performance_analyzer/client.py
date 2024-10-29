# import asyncio
# import time
# import socket
# import matplotlib.pyplot as plt

# async def send_data(protocol, server_ip='localhost', port=8888):
#     if protocol == 'TCP':
#         reader, writer = await asyncio.open_connection(server_ip, port)
#     else:
#         # Simulating MPTCP with multiple connections
#         reader, writer = await asyncio.open_connection(server_ip, port)

#     data = b'x' * 1024  # 1 KB of data
#     start_time = time.time()
#     for _ in range(100):  # Send 100 KB
#         writer.write(data)
#         await writer.drain()
#     end_time = time.time()

#     writer.close()
#     await writer.wait_closed()
#     return end_time - start_time

# async def test_latency(protocol, server_ip='localhost', port=8888):
#     latencies = []
#     for _ in range(10):  # 10 ping tests
#         start_time = time.time()
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((server_ip, port))
#         sock.send(b'ping')
#         sock.recv(1024)
#         latencies.append(time.time() - start_time)
#         sock.close()
#     return latencies

# async def main():
#     protocol = 'TCP'  # Change to 'MPTCP' if supported
#     print(f"Testing {protocol}...")

#     total_time = await send_data(protocol)
#     print(f"{protocol} Total Time: {total_time:.2f} seconds")

#     latencies = await test_latency(protocol)
#     print(f"{protocol} Latencies: {latencies}")

#     # Plot latency results
#     plt.plot(latencies)
#     plt.title(f'{protocol} Latency')
#     plt.xlabel('Ping Number')
#     plt.ylabel('Latency (s)')
#     plt.show()

# if __name__ == "__main__":
#     asyncio.run(main())


# import asyncio
# import time

# async def send_data(protocol, server_ip='localhost', port=8888):
#     if protocol == 'TCP':
#         reader, writer = await asyncio.open_connection(server_ip, port)

#     data = b'x' * 1024  # 1 KB of data
#     start_time = time.time()
    
#     # Send 100 KB of data in chunks
#     for _ in range(100):
#         writer.write(data)
#         await writer.drain()  # Ensure the data is flushed to the server

#     end_time = time.time()

#     print(f"Sent 100 KB of data")
#     writer.close()
#     await writer.wait_closed()  # Properly close the connection

#     return end_time - start_time

# async def main():
#     protocol = 'TCP'
#     print(f"Testing {protocol}...")

#     total_time = await send_data(protocol)
#     print(f"{protocol} Total Time: {total_time:.2f} seconds")

# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import time

async def send_data(protocol, total_size_kb=100, server_ip='localhost', port=8888):
    """Send data of specified size to the server."""
    if protocol == 'TCP':
        reader, writer = await asyncio.open_connection(server_ip, port)

    chunk_size = 1024  # 1 KB per chunk
    data = b'x' * chunk_size  # Create 1 KB data

    total_chunks = total_size_kb  # Number of chunks to send
    start_time = time.time()

    # Send data in chunks
    for _ in range(total_chunks):
        writer.write(data)
        await writer.drain()  # Flush data to the server

    end_time = time.time()

    print(f"Sent {total_size_kb} KB of data")
    writer.close()
    await writer.wait_closed()  # Properly close the connection

    return end_time - start_time

async def main():
    protocol = 'TCP'
    data_size_kb = int(input("Enter the amount of data to send (KB): "))  # User input for data size

    print(f"Testing {protocol}...")

    total_time = await send_data(protocol, total_size_kb=data_size_kb)
    print(f"{protocol} Total Time: {total_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
