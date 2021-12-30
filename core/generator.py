import asyncio
import random, string
import aiohttp

def checks_elements(codes):
    amout = 0
    for code in codes:
        amout = 0 + 1
    else:
        return amout


def get_codes(nums : int):
    codes = []
    for n in range(0, nums):
       y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
       url = f'https://discordapp.com/api/v9/entitlements/gift-codes/{y}'
       codes.append(url)
    else:
        return codes

async def checker(codes):
    valid_codes = []
    for code in codes:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(code) as RESPONSE:
                await asyncio.sleep(0.2)
                if RESPONSE.status != 10038:
                    valid_codes.append(str(code))
                else:
                    pass

                json = await RESPONSE.json()

                if json["message"] == 'You are being rate limited.':
                    print("Достиг лимит на запросы к Discord Nitro Api.Пожалуйста отключите бота!")
    else:
        if checks_elements(valid_codes) > 1:
            return valid_codes
        else:
            return "Кодов нету"
