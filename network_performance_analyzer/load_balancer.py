import asyncio
import random

class LoadBalancer:
    def __init__(self):
        self.tcp_weight = 0.5  # 50% traffic to TCP
        self.mptcp_weight = 0.5  # 50% traffic to MPTCP

    async def send_request(self, protocol):
        if protocol == 'TCP':
            await asyncio.sleep(random.uniform(0.1, 0.3))  # Simulate TCP delay
        else:
            await asyncio.sleep(random.uniform(0.05, 0.15))  # Simulate MPTCP

    async def balance_load(self):
        for _ in range(20):  # Simulate 20 requests
            protocol = 'TCP' if random.random() < self.tcp_weight else 'MPTCP'
            print(f"Sending request via {protocol}")
            await self.send_request(protocol)

if __name__ == "__main__":
    balancer = LoadBalancer()
    asyncio.run(balancer.balance_load())
