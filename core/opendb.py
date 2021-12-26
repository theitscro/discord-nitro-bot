import os

async def write(name, obj):
    try:
        os.remove(name)
        open(name, "x").close()
        open(name).write(obj)
    except:
        open(name, "w").write(obj)