# importing panda library 
#import re
#import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
from zenrows import ZenRowsClient

zenrows_api_base = "https://api.zenrows.com/v1/?apikey=418f0f712b9a0764661a3f315fc96659797d0908"

#capitalletters=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
#structuredecks=["Blackwing's Pride","Spiral Spear Strike","Vortex of Magic","Burning Spirits","Dragonmaid-to-Order","Magicians of Pendulum","Immortal Glory","Re-Contract Universe","Cybernetic Successor","Spellbook of Prophecy","Rage of Cipher","Hidden Arts of Shadows"] 
secretpacks=['A Song of Zephyr and Petals', 'Abyssal Underworld', 'Advanced Warriors', 'AI Omniscience', 'Alba Abyss', 'Altered Heraldry', 'Artistic Angel', 'Astral Trinity of Gods', 'Awakening of the Ancients', 'Beastly Claws of Terror', 'Beasts of the Inferno', 'Beetle Troops Roll Out', 'Beloved Dolls', 'Blazing Fortitude', 'Blazing Warriors', 'Blooming in Adversity', "Bujin's Vault of Heaven", 'Captivating Curtain Call', 'Celestial Dragon and Bear', 'Cell "A" Corruption', 'Champions of Hope', 'Champions of Salvation', 'Colossal Mech', 'Combatants of Flame', 'Cosmic Mechanical Entities', 'Counterswing Mages', 'Cross-Dimensional Contracts', 'Crystal Septenary', 'Curse of the Serpent', 'Cyber City Guardians', 'Darkest Magics', 'Deceitful Wings of Darkness', 'Denizens of Sacred Tree Grove', "Destiny's Sorceress", 'Devastation Regenerated', 'Draconic Resplendence', 'Dragon Knight Gorge', 'Dragon Luster', 'Dragon Spirit', 'Dreadnought Advance', 'Echo Chamber Nation', 'Electrilyrical', 'Electron Illusions', 'Elemental Exchanges', 'Emblazoned Armor', 'Emerging Monstrosity Recon!', 'Enchanted Threads of Shade', 'Essence of Flora and Ocean', 'Exquisite Jet-Black Rose', 'Fabled Gods', 'Fiendish Encounter', 'Fiendish Playthings', 'Fires of This World and The Next', 'Forest Friends', 'Forgotten City Dwellers', 'Futuristic Creatures', 'Galaxy War', 'Gargantuan Gears', 'Glacial Seal', 'Glory on Wings', 'Gods of Abyss and Arcadia', "Great Shogun's Rule", 'Guardian of Kings', 'Guardian of the Sacred Summit', 'Guardians of Fire', 'Guardians of the Sacred Sky', 'Guided by Fate', 'Guided by the Noble Blade', 'Hand of Fate', 'Immortal Royalty', 'Immovable Samurai', 'Impending Assassination', 'Indomitable Knights', 'Inevitability of Chaos', 'Insect Metamorphosis', 'Interdimensional Interlopers', 'Invaders from Outer Space', 'Invulnerable Iron Wings', 'Iron Core Synthetics', 'Justice Before Attribute', 'Justice from Light', 'Knowledge of the Mythlords', 'Legends of Old', 'Life Finds a Way', 'Life Force Control System', 'Mastery of the Grimoire', 'Miraculous Advent', 'Mischievous Specters', 'Monster Overdrive', 'Moonlit Avian Dance', "Mother Nature's Snare", 'Natural Selection', 'Nebula Cyclone', 'Neo Space Comrades', 'Number Recall', 'Onomatopair-Up', 'Pearlescent Cyber Dragons', 'Piercing Winds', 'Pledge of Sword', 'Prank Panic!', 'Prehistoric Beast Advance', 'Primordial Rising', 'Pyroxene Relinquished', 'Rapid Aircraft Advancement', 'Rites of the Mirrorworld', 'Roaring Thunder', 'Roid Nexus', 'Roused from Destruction', 'Rulers of Darkness', 'Rulers of the Deep', 'Savage Crimson Dragon', 'Scientific Analysis', 'Scrap Iron Soldiers', 'Secret Fighters', 'Seedling Soul Fey', 'Seekers of Witchcraft', "Shark's Pride", 'Shifting Gears', 'Shot Through Fiction', 'Shrouded Heroes', 'Singular Strike Overthrow', 'Soaring on Darkest Wings', 'Soldiers from the Storm', 'Souls of Sublime Gods', 'Space-Time Transcendents', 'Spiritual Mastery', 'Star-Studded Futures', 'Stardust Ties', 'Supernatural Elements', 'Sword of the Seventh One', 'Synchro Mode Change', 'Terra Firma Transcendants', 'The Azure in the Ivory', 'The Cerise in the Ebony', 'The Cost of Dark Powers', 'The Darkness Amuses', 'The First Heroes', 'The Great Olds', 'The Hidden Arts', 'The Infinite Void', 'The Noble Knights of Crimson Flowers', 'The Opening Act of an Apocalypse', 'The Trap in the Wicked Castle', 'The Ultimate Traditional Art', 'Those who Stand Against Kings', 'Three-Strike Success', 'Ties to Mother Nature', 'Timeworn Legacies', 'Toontastic', 'Tournament Athletes', 'Traditions of Trickery', 'Transfigured Heroes', 'Transforming Tech', 'Valiant Gladiator Beasts', 'Vessels of Freedom', 'Warp-Speed Toys', 'Warriors of Legend', 'Warriors Unite!', 'Wind-Up Soldiers', 'World Cloaked in Magical Power', 'Worthy Adversaries', 'Yearning Evil Body']
links=['https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366046', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366047', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366048', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366049', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/398510', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366050', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366051', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366052', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366053', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/422982', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366054', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/426619', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366055', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366056', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366057', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366058', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366059', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366060', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366061', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366062', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366063', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366064', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366065', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366066', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366067', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366068', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366069', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366070', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366071', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366072', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366081', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366073', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366074', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366075', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366076', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366078', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366080', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366082', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366079', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366086', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366083', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366084', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366090', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366085', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366087', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366088', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366089', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366091', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366097', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366092', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366093', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366094', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366095', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366101', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366096', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366098', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366099', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366100', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366102', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366103', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366104', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366105', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366106', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/419751', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366107', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366108', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/420602', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366109', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366110', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366044', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366111', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366112', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366113', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366114', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366115', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366116', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366117', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366118', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366119', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366120', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366121', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366122', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366123', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366124', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366125', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366127', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366128', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366130', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366130', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366131', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366132', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366133', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366134', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366135', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366136', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366137', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366138', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366140', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366139', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366142', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366142', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366144', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366145', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366146', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366148', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366147', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366150', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366149', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366152', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366151', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366154', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366153', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366154', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366155', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366156', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366157', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366158', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366159', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366160', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366161', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366162', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366163', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366164', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366165', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366166', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366167', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366169', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366171', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366170', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366171', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366174', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366173', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366174', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366175', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366176', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366177', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366178', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366179', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366180', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366181', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/426398', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/429900', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/417809', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/419752', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366182', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366183', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366041', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366042', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366041', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366043', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366040', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366038', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366037', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366035', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366034', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366033', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366032', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366039', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366036', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366031', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366030', 'https://game8.co/games/Yu-Gi-Oh-Master-Duel/archives/366029']
#Urcounter = 0
#num_structuredecks=len(structuredecks)
#num_secretpacks=len(secretpacks)
#num_links=len(links)

f = open('tempdatabase2.csv', 'w',newline="",encoding='utf-8')
writer = csv.writer(f)


"""
with open('c:/Users/SAHIL YADAV/Desktop/New folder/listofsecretpackswithlinkstobescraped.txt','r',encoding='utf-8') as f:
    for lines in f:
        temp=lines.replace("href=", ">")
        temp1=temp.split(">")
        temp2=(temp.replace("<", ">")).split(">")
        for i in temp1:
            if i.startswith("https"):
                links.append(i)
        for j in temp2:
            if j.startswith(capitalletters):
                secretpacks.append(j)
"""



"""
with open('temp.csv',mode='r') as file:
    csvtemp = csv.reader(file)
    
    for lines in csvtemp:
        
        if lines[0].startswith(('ãƒ','<a class=')) and lines[0].endswith('</a>'):
            temp=lines[0].replace("<", ">")
            temp1=temp.split(">")
            for i in temp1:
                if i.startswith(capitalletters):
                    Urcounter=Urcounter+1
"""                    


"""
url = links[0]
r = requests.get(url)
soup = BeautifulSoup(r.content,features="html.parser")
URs=[]
SRs=[]
for tr in soup.find_all(name= "tr"):
    th = tr.find("th")
    if th == None:
        continue
    else:
        a = str(th)
    Urarity = a.find("UR")
    Srarity = a.find("SR")

    if th and Urarity!= -1 :
        td = tr.find("td")

        if td:
            URs.append(((td.text).replace("\n","")).replace("・",","))

    if th and Srarity!= -1 :
        td = tr.find("td")

        if td:
            SRs.append(((td.text).replace("\n","")).replace("・",","))

URs.pop(0)
URs[0] = URs[0].replace(URs[0][0], "", 1)
SRs.pop(0)
SRs[0] = SRs[0].replace(SRs[0][0], "", 1)
URs = URs[0].split(",")
SRs = SRs[0].split(",")

data=[secretpacks[0],URs,SRs]
print(data)
"""


"""
#use csv to commit to database
def extract_content(soup): 
    URs=[]
    SRs=[]
    for tr in soup.find_all(name= "tr"):
        th = tr.find("th")
        if th == None:
            continue
        else:
            a = str(th)
        Urarity = a.find("UR")
        Srarity = a.find("SR")

        if th and Urarity!= -1 :
            td = tr.find("td")

            if td:
                URs.append(((td.text).replace("\n","")).replace("・",","))

        if th and Srarity!= -1 :
            td = tr.find("td")

            if td:
                SRs.append(((td.text).replace("\n","")).replace("・",","))

    URs.pop(0)
    URs[0] = URs[0].replace(URs[0][0], "", 1)
    SRs.pop(0)
    SRs[0] = SRs[0].replace(SRs[0][0], "", 1)
    URs = URs[0].split(",")
    SRs = SRs[0].split(",")
"""
 
counter = 0
for url in links:
    response = requests.get(zenrows_api_base, params={"url": url})
    soup = BeautifulSoup(response.text, "html.parser")
    URs=[]
    SRs=[]
    for tr in soup.find_all(name= "tr"):
        th = tr.find("th")
        if th == None:
            continue
        else:
            a = str(th)
        Urarity = a.find("UR")
        Srarity = a.find("SR")

        if th and Urarity!= -1 :
            td = tr.find("td")

            if td:
                URs.append(((td.text).replace("\n","")).replace("・",","))

        if th and Srarity!= -1 :
            td = tr.find("td")

            if td:
                SRs.append(((td.text).replace("\n","")).replace("・",","))

    URs.pop(0)
    URs[0] = URs[0].replace(URs[0][0], "", 1)
    SRs.pop(0)
    SRs[0] = SRs[0].replace(SRs[0][0], "", 1)
    URs = URs[0].split(",")
    SRs = SRs[0].split(",")
    templist=[secretpacks[counter],URs,SRs]
    print(templist)
    writer.writerow(templist)
    counter=counter+1





#print(Urcounter)
#print(num_structuredecks)
#print(Urcards)
#print(num_secretpacks)
#print(num_links)
#print(secretpacks)
#print(Urcards)