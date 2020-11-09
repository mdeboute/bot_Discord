import discord, random


# Some generic utility commands.

def format_seconds(time_seconds):
    """Formats some number of seconds into a string of format d days, x hours, y minutes, z seconds"""

    seconds = time_seconds
    hours = 0
    minutes = 0
    days = 0
    while seconds >= 60:
        if seconds >= 60 * 60 * 24:
            seconds -= 60 * 60 * 24
            days += 1
        elif seconds >= 60 * 60:
            seconds -= 60 * 60
            hours += 1
        elif seconds >= 60:
            seconds -= 60
            minutes += 1

    return f"{days}d {hours}h {minutes}m {seconds}s"

def randomColor():
    hexa="0123456789abcdef"
    random_hexa="0x"
    for i in range(6):
        random_hexa+=random.choice(hexa)
    return discord.Colour(int(random_hexa, 16))

def randomURL(): #https://github.com/captbaritone/urlmeme
    letter="abcdefghijklmnopqrstuvwxyz"
    random_url="https://urlme.me/"
    for i in range(1):
        random_url+=random.choice(letter)
    for i in range(1):
        random_url+=random.choice(letter)
    return str(random_url+".jpeg")

def randomDescription():
    citations=["Je ne crois pas qu'il y ait de bonne ou de mauvaise situation 🙄","Ou tu sors ou je te sors...","J'aime les panoramas 🌅!","- Il s'appelle Juste Leblanc. - Ah bon, il a pas de prénom ?", "Vous avez de la pâte ? Vous avez du sucre ? Alors avec la pâte vous faites une crêpe et puis vous mettez du sucre dessus !", "Alors, on n'attend pas Patrick 😏?","Casséééé 🤙!!!","Tu vois Bernard, toi et moi, on a un peu le même problème. On peut pas tout miser sur notre physique, enfin surtout toi. Alors si j'ai un bon conseil à te donner, oublie que t'as aucune chance, vas-y, fonce. On sait jamais, sur un malentendu, ça peut marcher.", "Vous voulez un whisky ?- Juste un doigt.- Vous voulez pas un whisky d'abord 🥃 ?","Si je ne suis pas de retour dans 5 minutes, attendez encore ⏳.","Jour, nuit, jour, nuit 🌝🌚."]
    for i in range(1):
        description=random.choice(citations)
    return str(description)

def createEmbed(title, description, color, img):
    embed=discord.Embed()
    embed.title=title
    embed.colour=color
    embed.set_image(url=img)
    embed.description=description
    return embed
