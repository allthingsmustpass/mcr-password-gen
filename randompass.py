import random

songs = ["Interlude",
    "Thank You For the Venom", "Hang 'Em High",
    "It's Not a Fashion Statement It's a Deathwish", "Cemetery Drive",
    "I Never Told You What I Do For a Living",
    "Bury Me In Black",
    "Desert Song",
    "Blood",
    "The End.",
    "Dead!",
    "This Is How I Disappear",
    "The Sharpest Lives",
    "Welcome to the Black Parade",
    "I Don't Love You",
    "House of Wolves",
    "Cancer",
    "Mama",
    "Sleep",
    "Teenagers",
    "Disenchanted",
    "Famous Last Words",
    "Look Alive, Sunshine",
    "Na Na Na (Na Na Na Na Na Na Na Na Na)",
    "Bulletproof Heart",
    "SING",
    "Planetary (GO!)",
    "The Only Hope For Me Is You",
    "Jet-Star And The Kobra Kid / Traffic Report",
    "Party Poison",
    "Save Yourself, I'll Hold Them Back",
    "S/C/A/R/E/C/R/O/W",
    "Summertime",
    "DESTROYA",
    "The Kids from Yesterday",
    "Goodnite, Dr. Death",
    "Vampire Money",
    "The Five of Us Are Dying",
    "Kill All Your Friends",
    "Party at the End of the World",
    "My Way Home Is Through You",
    "Not That Kind of Girl",
    "Emily",
    "All the Angels",
    "Boy Division",
    "Tomorrow's Money",
    "AMBULANCE",
    "Gun.",
    "The World Is Ugly",
    "The Light Behind Your Eyes",
    "Number Four",
    "Kiss the Ring",
    "Make Room!!!!",
    "Surrender the Night",
    "Burn Bright"
    ]

"""
this procedure uses random.choice to select a random song from the list.
@param: songs. a list of strings wich contains all the titles of the songs.
"""
def selectPassword(songs):
    password = random.choice(songs)
    return password

"""
this procedure remove the spaces from the string.
@param: password. a string selected from selectPassword()
"""
def removeSpacesAndStuff(password):
    password.replace(" ","")
    password.replace("'","")
    password.replace(".","")
    return password.replace(" ","")

"""
now we replace all the vowels with some number.
@param: password. a string with the spaces removed from removeSpaces()
        x. a copy of 'password'.
"""
def replaceVowelsWithNumbers(password):
    vowels = {
        'a':'4',
        'A':'4',
        'e':'3',
        'E':'3',
        'i':'1',
        'I':'1',
        'o':'0',
        'O':'0',
    }
    x = password
    for i in password:
        if i in vowels:
             x = x.replace(i, vowels[i])
    return x

def addRandomStuff(x):
    print(f"random!")


def generatePassword(songs):
    password = selectPassword(songs)
    password = removeSpacesAndStuff(password)
    password = replaceVowelsWithNumbers(password)
    print(password)

def main():
    generatePassword(songs)
        
if __name__ == "__main__":
    main()