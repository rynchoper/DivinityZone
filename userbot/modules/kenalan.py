from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.r(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Hai Perkenalkan Namaku Ryanwica`")
    sleep(3)
    await typew.edit(" umur gatau`")
    sleep(1)
    await typew.edit("`Tinggal Di Jogja, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Gua Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Gausa sok asik`")
    sleep(1)
    await typew.edit("`MINIMAL MANDI BANH`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Masalah Mu Sekarang`")
    sleep(3)
    await typew.edit("`Tetaplah Menjadi orang baik`")
    sleep(1)
    await typew.edit("`Dan Tetaplah Semangat❤️`")
# Create by myself @localheart
