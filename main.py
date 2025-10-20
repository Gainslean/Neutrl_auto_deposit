import asyncio
import random
from datetime import datetime
from client import Client
from config import Chain_id, chain_name, rpc_url, explorer_url,USDN



class DEPOSIT:
    def __init__(self, client: Client):
        self.client = client
        self.usdn = self.client.get_contract(
            contract_address="0x866C6c6627303Be103814150fC0e886BE5D9ea83",
            abi=USDN
        )


    async def approve(self): # Делает апрув

        amount = random.randint(70000 * 10**6 , 999999999999 * 10**6)

        await self.client.make_approve("0xdAC17F958D2ee523a2206206994597C13D831ec7","0x866C6c6627303Be103814150fC0e886BE5D9ea83", amount)

        print(f"Успешно сделал апрув {amount/10**6}")


    async def supply(self): # Основная функция депозита

        await self.approve()


        amount = await self.client.get_balance_erc("0xdAC17F958D2ee523a2206206994597C13D831ec7")

        print(f"Баланс {self.client.address} равен = {amount / 10**6} USDT")

        if amount == 0:
            print(f"Депать нечего")
            return False


        for attempt in range(1, 100):  # 100 попытки
            try:
                print(f"Попытка {attempt}/3: депозит {amount / 10 ** 6} USDC...")

                # Формируем транзакцию
                txn = await self.usdn.functions.deposit(amount, self.client.address).build_transaction(
                    await self.client.prepare_tx()
                )

                # Отправляем транзакцию
                tx_hash = await self.client.send_transaction(txn, need_hash=True)
                print(f"Транзакция успешно отправлена: {tx_hash}")

                # Ожидаем подтверждения
                success = await self.client.wait_tx(tx_hash)
                if success:
                    print(f"✅ Успешно сделал вклад {amount / 10 ** 6} USDT")
                    return True  # Выходим из функции, если успех

            except Exception as e:
                print(f"❌ Ошибка при отправке транзакции (попытка {attempt}): {e}")

            # Если неудачно и не последняя попытка — ждем 1 секунду
            if attempt < 99:
                await asyncio.sleep(3)

        print("⚠️ Все 3 попытки депозита не удались.")
        return False



chain_name = "Ethereum" # Arbitrum Optimism Base Ethereum Mantle

proxy = '' # ПО ФАКТУ НЕ НУЖНЫ ТУТ
rpc_url = rpc_url[chain_name]
chain_id = Chain_id[chain_name]
explorer_url = explorer_url[chain_name]

async def start():

    with open("wallets.txt", "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f.readlines()]

    private_keys = [ln for ln in lines]

    tasks = []
    for pk in private_keys:

        w3_client = Client(private_key=pk, proxy=proxy, chain_name=chain_name, chain_id=chain_id,
                           explorer_url=explorer_url, rpc_url=rpc_url)
        swap_client = DEPOSIT(client=w3_client)

        task = asyncio.create_task(swap_client.supply())
        tasks.append(task)

    await asyncio.gather(*tasks, return_exceptions=True)


asyncio.run(start())
