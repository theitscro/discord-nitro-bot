try:
    from nextcord.ext.commands import Bot, Context
    from nextcord.ext.tasks import loop
    import nextcord
except:
    import os
    os.system("pip install nextcord")
    raise SystemExit("Выходим...")
from core import generator, opendb

bot = Bot("?") # Префикс ?

@bot.command()
async def set_channel(ctx : Context, channel : nextcord.TextChannel= None):
    """
    Установить канал для публикации успешных кодов
    """
    if channel == None:
        await ctx.send(
            "Укажите канал\n?set_channel ID канала"
        )
    else:
        try:
            await ctx.guild.fetch_channel(int(channel.id))
        except:
            await ctx.send(
                "Укажите действительный канал"
            )
            return
        await opendb.write("kanal.txt",str(channel.id))
        await ctx.send("Всо")

@loop(minutes=1)
async def gen():
    r = generator.get_codes(50) # Не нужно больше , а то дискорд пошлет тебя :D
    result = await generator.checker(r)
    if result[0] != "Кодов нету":
        channel = await bot.fetch_channel(int(open("kanal.txt").readlines()[0]))
        await channel.send(
            f"{result}"
        )
    else:
        channel = await bot.fetch_channel(int(open("kanal.txt").readlines()[0]))
        await channel.send(
            "Кодов нету :(, коды которые были \n "
        )
        await channel.send(
            f"{result[1]} {result[2]}"
        )

@bot.command()
async def run(ctx : Context):
    """
    Запустить генератор!
    """
    if gen.is_running():
        return await ctx.send(
            "Генератор уже запущен!"
        )
    try:
        open("kanal.txt").close()
        gen.start()
        await ctx.send(
            "Генератор запущен!"
        )
    except:
        await ctx.send(
            "Вы не установили канал пуликации учпешных кодов"
        )

bot.run("ваш токен")
