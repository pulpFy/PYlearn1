from pprint import pprint

oddelovac = "=" * 62

sluzby = ('1', "dostupne filmy", "detaily filmu", 'reziseri', "doporuc film")

uzivatele = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}

## Spojíme všechny slovníky filmů do jednoho slovníku jménem `filmy` ########
filmy = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3,
    film_4["JMENO"]: film_4
}
#pprint(filmy) # @@@ UKÁZKA 1 ===> řazení dle abecedy@@@ 
#print(filmy.items()[-1]) # @@@ UKÁZKA 2: a) pohled není sekvence: TypeError: 'dict_items' object is not subscriptable
print("Testovací výtisk poslední položky velkého slovníku  filmy: (viz závorky) \n")
print(tuple(filmy.items())[-1]) # UKÁZKA 2: b) pohled dict.items() slouží jako zdroj hodnot do n-tice ..
print("\n")

## Uvítání a výpis nabídky #########
uzivatel = input("Zadej jmeno: ")

if not uzivatel in uzivatele:
    print("neregistrovany uzivatel!")
    quit() # @@@ UKÁZKA 3 ===> ukončení programu! @@@ 
else:
    #print("V poradku", oddelovac, sep="\n")
    print("Vitejte v nasem filmovem slovniku!".upper().center(62),
          oddelovac, sep="\n")
    print(f"| {' | '.join(sluzby)} |".center(62), oddelovac, sep="\n")

## 1. výběr služby ##############################################################
#vyber = input("Vyber sluzbu: ") ## ORIGINÁLNÍ VSTUP - před napasováním na funkci..
#
vol1 = input("Vyber sluzbu: ") ## už NAPASOVANÝ 1.VSTUP

def proved_sluzbu(a, vyber):
    """orig.kód do funkce, pro 1.volbu služby parametr vyber,
další volby služby zkratkou přes parametr a, který případně přepisuje lokalní vyber"""
    if a == '1': vyber = 'dostupne filmy'
    if a == '2': vyber = 'detaily filmu'
    if a == '3': vyber = 'reziseri'
    if a == '4': vyber = 'doporuc film'
    print("Změněný výběr:", vyber) # (hodnota "a" ale nic nemění)
    ## Výpis všech dostupných filmů ##############################
    if vyber in sluzby and (vyber == "dostupne filmy" or vyber ==  "1"):
        print("DOSTUPNE FILMY:", ', '.join(filmy.keys()), oddelovac, sep="\n")
#..UKÁZKA 2: c) pohled slouží jako zdroj hodnot pro metodu .join ..
        
    ## Vyber film a zobraz detaily o něm ########################
    elif vyber in sluzby and vyber == "detaily filmu":
        print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())), sep="\n")
        #..UKÁZKA 2: d) pohled slouží zase jako zdroj hodnot pro konstrukci n-tice @@@
        film = input("Vyber film:")
        print(oddelovac, f"FILM: {film}", filmy.get(film), oddelovac, sep="\n")

    ## Vyber všechny režiséry ###################################
    elif vyber in sluzby and vyber == 'reziseri':
        reziseri = {
            filmy["Shawshank Redemption"]["REZISER"],
            filmy["The Godfather"]["REZISER"],
            filmy["The Dark Knight"]["REZISER"],
            filmy["The Prestige"]["REZISER"]
        }
        print(f" {', ' .join(reziseri)}", oddelovac, sep="\n")

    ## Doporuč film podle ostatních uživatelů ##################
    elif vyber in sluzby and vyber == "doporuc film":
        ## kopie puvodniho slovniku hodnoceni (budeme upravovat pouze kopii!)
        kopie_hodnoceni = uzivatele.copy()

        ## selekce aktivniho uzivatele (vytahnu si uzivatele a jeho oblibene filmy)
        aktivni_uzivatel = kopie_hodnoceni.pop(uzivatel)
        # print(f'{aktivni_uzivatel=}')

        ## zbytek uzivatelu
        zbytek_hodnoceni = kopie_hodnoceni
        # print(f'{zbytek_hodnoceni=}')

        ## ulozim si zbyle uzivatele do oddelenych promennych
        detaily_prvni_uzivatel = zbytek_hodnoceni.popitem()
        detaily_druhy_uzivatel = zbytek_hodnoceni.popitem()
        print(f'{detaily_prvni_uzivatel=}')
        # print(f'{detaily_druhy_uzivatel=}')

        ## tyto detaily jeste rozdelim do samostatnych promennych
        jmeno_prvni_uz = detaily_prvni_uzivatel[0]
        jmeno_druhy_uz = detaily_druhy_uzivatel[0]
        hodnoceni_prvni_uz = detaily_prvni_uzivatel[1]
        hodnoceni_druhy_uz = detaily_druhy_uzivatel[1]
        # print(f'{jmeno_prvni_uz=}')
        # print(f'{jmeno_druhy_uz=}')
        # print(f'{hodnoceni_prvni_uz=}')
        # print(f'{hodnoceni_druhy_uz=}')

        ## porovnani spolecnych filmu pro aktivniho uzivatele a zbytek uzivatelu
        ## udelam prunik obou uzivatelu s aktivnim uzivatelem abych videl, jake filmy maji spolecne
        spolecni_prvni_uziv = aktivni_uzivatel.intersection(hodnoceni_prvni_uz)
        spolecni_druhy_uziv = aktivni_uzivatel.intersection(hodnoceni_druhy_uz)
        # print(f'{spolecni_prvni_uziv=}')
        # print(f'{spolecni_druhy_uziv=}')

        ## porovnavam, jestli prvni uzivatel ma vetsi pocet spolecnych filmu nez druhy (vuci aktivnimu uzivateli)
        if len(spolecni_prvni_uziv) > len(spolecni_druhy_uziv):
            nejvice_spolecnych = uzivatele[jmeno_prvni_uz]

        elif len(spolecni_prvni_uziv) < len(spolecni_druhy_uziv):
            nejvice_spolecnych = uzivatele[jmeno_druhy_uz]

        elif len(spolecni_prvni_uziv) == len(spolecni_druhy_uziv):
             nejvice_spolecnych = uzivatele[jmeno_druhy_uz].union(uzivatele[jmeno_prvni_uz])
        # print(f'{nejvice_spolecnych=}')

        ## doporuc film podle rozdilu shlednutych od akt. uzivatele a nejvice shodnych filmu
        print(f"Oblibene filmy akt. uzivatel: {aktivni_uzivatel}\n")
        print(f"Nejvice spol. oblibenych filmu: {nejvice_spolecnych}")

        navrhy = set(nejvice_spolecnych).difference(aktivni_uzivatel)
        print(f"Navrhuji filmy: {navrhy}" if navrhy else "Nemam pro tebe zadny film")
        print(oddelovac)
    else:
        print("SLUZBA NENI DOSTUPNA!")
    
# pro opětovné zavolání služeb
dal = 'a'; volby = [*'a1234']
while dal in volby:
    proved_sluzbu(dal, vol1)
    dal = input("další službu? 1 až 4: ")
        
input('end (input na posledním řádku kódu): ')
