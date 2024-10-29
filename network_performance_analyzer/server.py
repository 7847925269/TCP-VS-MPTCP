# import asyncio
# import time

# class TCPServer:
#     def __init__(self):
#         self.total_data = 0
#         self.start_time = None

#     async def handle_client(self, reader, writer):
#         client_addr = writer.get_extra_info('peername')
#         print(f"New connection from {client_addr}")

#         if self.start_time is None:
#             self.start_time = time.time()  # Start the timer only once, when the first client connects
        
#         try:
#             while True:
#                 data = await reader.read(1024)  # Read in 1KB chunks
#                 if not data:
#                     print(f"Connection closed by {client_addr}")
#                     break
#                 self.total_data += len(data)  # Accumulate data size
#         except asyncio.IncompleteReadError:
#             print(f"Connection lost with {client_addr}")
#         except Exception as e:
#             print(f"Error with {client_addr}: {e}")
#         finally:
#             writer.close()
#             await writer.wait_closed()  # Ensure writer is properly closed
#             print(f"Connection cleaned up for {client_addr}")

#     async def start_server(self):
#         server = await asyncio.start_server(self.handle_client, 'localhost', 8888)
#         print("Server started at localhost:8888")
#         async with server:
#             await server.serve_forever()

#     def report_performance(self):
#         if self.start_time is None:
#             print("No data received. Server shutting down.")
#             return

#         elapsed_time = time.time() - self.start_time
#         throughput = self.total_data / elapsed_time if elapsed_time > 0 else 0
#         print(f"\nPerformance Report:")
#         print(f"Total Data: {self.total_data} bytes")
#         print(f"Time Taken: {elapsed_time:.2f} seconds")
#         print(f"Throughput: {throughput:.2f} bytes/second")

# if __name__ == "__main__":
#     server = TCPServer()
#     try:
#         asyncio.run(server.start_server())
#     except KeyboardInterrupt:
#         print("\nShutting down server...")
#         server.report_performance()
import asyncio
import time

class TCPServer:
    def __init__(self):
        self.total_data = 0
        self.start_time = None

    async def handle_client(self, reader, writer):
        client_addr = writer.get_extra_info('peername')
        print(f"----------------------------------")
        print(f"New connection from {client_addr}")

        if self.start_time is None:
            self.start_time = time.time()  # Start the timer only once, when the first client connects

        try:
            while True:
                data = await reader.read(1024)  # Read in 1KB chunks
                if not data:
                    print(f"Connection closed by {client_addr}")
                    break
                self.total_data += len(data)  # Accumulate data size
        except asyncio.IncompleteReadError:
            print(f"Connection lost with {client_addr}")
        except Exception as e:
            print(f"Error with {client_addr}: {e}")
        finally:
            writer.close()
            await writer.wait_closed()  # Ensure writer is properly closed
            print(f"Connection cleaned up for {client_addr}")

    async def start_server(self):
        server = await asyncio.start_server(self.handle_client, 'localhost', 8888)
        print("Server started at localhost:8888")
        async with server:
            await server.serve_forever()

    def report_performance(self):
        if self.start_time is None:
            print("No data received. Server shutting down.")
            return

        elapsed_time = time.time() - self.start_time
        throughput = self.total_data / elapsed_time if elapsed_time > 0 else 0
        print(f"\nPerformance Report:")
        print(f"Total Data: {self.total_data} bytes")
        print(f"Time Taken: {elapsed_time:.2f} seconds")
        print(f"Throughput: {throughput:.2f} bytes/second")

async def main():
    server = TCPServer()
    server_task = asyncio.create_task(server.start_server())

    try:
        await server_task
    except asyncio.CancelledError:
        print("\nShutting down server...")
        server.report_performance()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("KeyboardInterrupt detected, exiting...")
