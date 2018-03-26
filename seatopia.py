
import textwrap

import random
from random import randint

global sack
def addToSack(item):
    sack.append(item)
sack =[]


def currentStatus():
    print('You are in ' + zones[currentzone]['name'])
    #print('You have: {} dubloons in your sack'.format(sack))
    if 'item' in zones[currentzone]:
        print('In this zone, there is a ' + zones[currentzone]['item'])
    print()

def commands():
    print('---------------------------------------------------------------------')
    print('Directions are south, north, east, west')
    print('---------------------------------------------------------------------')
    print('To move from zone to zone type: go [direction]')
    print('---------------------------------------------------------------------')
    print('To open an item, type: open [item-name]')
    print('---------------------------------------------------------------------')
    print('To find the cost of an item, type: cost [item-name]')
    print('---------------------------------------------------------------------')
    print('To purchase an item, type: purchase [item-name]')
    print('---------------------------------------------------------------------')
    print('To leave to the ball and go to the shop type: leave')
    print('---------------------------------------------------------------------')


print('******************************Seatopia*********************************')

opening = 'You are a sea creature of seatopia, a paradise \
under the sea. Here all of the underwater denizens live \
together in peace and harmony, eels and urchins, belugas \
and hermit crabs, stingrays and snappers. However, the \
residents of seatopia are a competitively stylish bunch.\
There is a great dance coming up, the Mermaid\'s ball. \
Your wardrobe is looking a bit empty, and you need to get \
yourself some new threads in order to arrive at the ball \
in style. In order to do this, you will need to come up \
with some gold dubloons to go shopping.'




for line in textwrap.wrap(opening, 80):
    print(line)

commands()

class Character:
    def __init__(self,name,species,speed,luck,):
        self.name = name
        self.species = species
        self.speed = speed
        self.luck = luck

class Octopus(Character):
    def __init__(self):
        super().__init__(name=name, species='Octopus', speed=3, luck=2)

class Lobster(Character):
    def __init__(self):
        super().__init__(name=name, species='Lobster', speed=1, luck=4)

class Seamonkey(Character):
    def __init__(self):
        super().__init__(name=name, species='Sea Monkey', speed=4, luck=1)

print('***********************************************************************')
print('You will now choose what character you would like to play.')
print()
print('Speed impacts how many zones your character can visit, \
luck impacts how many dubloons your character is likely to find.')
print()
print('Lobster\'s have speed = 1, luck = 4')
print('Sea Monkey\'s have speed = 4, luck = 1')
print('Octopus\'s have speed = 3, luck = 2')
print()
print('Would you like to be a lobster, a sea monkey, or an octopus? Each \
has different attributes.')

player = input()
player = player.lower()
player = player.replace(' ','')

zones = {
            1: { 'name' : 'Trench 1' ,
                 'north': 5,
                 'south': 6,
                 'east' : 2 } ,

            2: { 'name' : 'Trench 2' ,
                 'north': 7,
                 'south': 8,
                 'east' : 3,
                 'west' : 1, } ,

            3: { 'name' : 'Trench 3' ,
                 'north': 9,
                 'south': 10,
                 'east' : 4,
                 'west' : 2 } ,

            4: { 'name' : 'Trench 4' ,
                 'north': 11,
                 'south': 12,
                 'east' : 13,
                 'west' : 3 } ,

            5: { 'name' : 'Spooky Cave' ,
                 'south': 1,
                 'item' : 'hollow-stalagmite' } ,

            6: { 'name' : 'Stingray Breeding Ground' ,
                 'north': 1,
                 'item' : 'giant-egg' } ,

            7: { 'name' : 'Loon Lagoon' ,
                 'south': 2,
                 'item' : 'broken-motorboat'} ,

            8: { 'name' : 'Cozy Cave' ,
                 'north': 2,
                 'item' : 'lava-lamp'} ,

            9: { 'name' : 'Coral Reef' ,
                 'south': 3,
                 'item' :'brain-coral'} ,

            10: { 'name' : 'Pirate Ship' ,
                  'north': 3,
                  'item' :'treasure-chest' } ,

            11: { 'name' : 'Sunken Boot' ,
                  'south': 4,
                  'item' : 'mini-boot' } ,

            12: { 'name' : 'Fishing Traps' ,
                  'north': 4,
                  'item' : 'tackle-box'} ,

            13: { 'name' : 'The Eel\'s Heel: Fine Apparel' ,
                  'west': 4 } ,

        }



currentzone = 1
#def currentStatus():
    #print('You are now in ' + zones[currentzone]['name'])
print()
print('You start your search for dubloons, there are a\
 variety of pathways that stretch in all directions.')
print()
roomvisit = 0
while True:

    currentStatus()

    move = input('>').lower().split()
    if move[0] == 'go':
        if move[1] in zones[currentzone]:
            currentzone = zones[currentzone][move[1]]
        else:
            print('Turn back little critter, can\'t go this way')

    if move[0] == 'open':
        if 'item' in zones[currentzone] and move[1] in zones[currentzone]['item']:
            if player == 'octopus':
                dubloonAmt = random.randint(3,5)
                sack.append(dubloonAmt)
                sacksum = sum(sack)
                print('You found {} dubloons in the {}.'.format(dubloonAmt,zones[currentzone]['item']))
                print('You now have: {} dubloons in your sack'.format(sacksum))
                del zones[currentzone]['item']
                roomvisit +=1
                print('You have visited {} rooms, you may visit {} more'.format(roomvisit,(6-roomvisit)))
                if roomvisit == 6:
                    print('You have explored as many zones for dubloons as you were able to, the ball is starting soon, now it\'s time to shop')
                    currentzone = 13
                    break

            elif player == 'seamonkey':
                dubloonAmt = random.randint(2,4)
                sack.append(dubloonAmt)
                sacksum = sum(sack)
                print('You found {} dubloons in the {}.'.format(dubloonAmt,zones[currentzone]['item']))
                print('You now have: {} dubloons in your sack'.format(sacksum))
                del zones[currentzone]['item']
                roomvisit +=1
                print('You have visited {} rooms, you may visit {} more'.format(roomvisit,(7-roomvisit)))
                if roomvisit == 7:
                    print('You have explored as many zones for dubloons as you were able to, the ball is starting soon, now it\'s time to shop')
                    currentzone = 13
                    break

            elif player == 'lobster':
                dubloonAmt = random.randint(5,7)
                sack.append(dubloonAmt)
                sacksum = sum(sack)
                print('You found {} dubloons in the {}.'.format(dubloonAmt,zones[currentzone]['item']))
                print('You now have: {} dubloons in your sack'.format(sacksum))
                del zones[currentzone]['item']
                roomvisit +=1
                print('You have visited {} rooms, you may visit {} more'.format(roomvisit,(4-roomvisit)))
                if roomvisit == 4:
                    print()
                    print('You have explored as many zones for dubloons as you were able to, the ball is starting soon, now it\'s time to shop')
                    currentzone = 13
                    break


            else:
                print('Sorry, that item is not in this room')


print('************************************************************************************************')
print('************************************************************************************************')
eel = 'Making your way out of the long, dark trench, you come up to a shop \
with a sign in the window proclaiming: The Eel\'s Heel: Fine Apparel'
for line in textwrap.wrap(eel, 80):
    print(line)

clothes = {'sea-green-herringbone-tailcoat' : 8, 'black-herringbone-tailcoat' : 8,
'rainbow-tophat': 4, 'black-tophat' : 4, 'orange-jellyfish-hide-cloak': 9,
'clear-jellyfish-hide-cloak': 9, 'violet-ball-gown': 10, 'black-ball-gown': 10,
'yellow-silk-trousers': 6, 'black-silk-trousers': 6, 'dark-green-fancy-shoes': 4,
'black-fancy-shoes': 4, 'hot-pink-shark-fin-stilettos': 4, 'black-shark-fin-stilettos': 4,
'purple-starched-shirt': 5, 'black-starched-shirt': 5, 'white-opera-gloves': 4, 'black-opera-gloves': 4,
'narwhal-tusk-cane': 8, 'beach-glass-monocle': 7, 'black-pearl-necklace': 8, 'coral-bracelet': 4,
'walrus-ivory-cufflinks': 3 }
print('****************************************************************************************************************')

shop = 'Inside the shop, a variety of indulgences await you. You \
can purchase any of these items: type cost before the name of the \
item to find price, and type purchase before name of item to buy'

for line in textwrap.wrap(shop, 80):
    print(line)

print()
for item in clothes:
    print(item)

global shoppingclam

def addToshoppingclam(threads):
    shoppingclam.append(threads)
shoppingclam = []

while sacksum > 2:

    move = input('>').lower().split()
    if move [0] == 'cost':
        if move[1] in clothes:
            print('{} costs {} dubloons'.format(move[1], clothes[move[1]]))

    if move[0] == 'purchase':

        if move[1] in clothes:
            print()
            print('You purchased {}'.format(move[1]))
            shoppingclam.append(move[1])
            sacksum -= clothes[move[1]]
            del clothes[move[1]]
            print('These items remain in the shop:')
            print()
            for item in clothes:
                print(item)
            print()
            print('You now have {} in your shopping clam'.format(shoppingclam))
            print('You have {} dubloons left to spend'.format(sacksum))


        else:
            print('Sorry, we don\'t carry that in the shop')
    if move[0] == 'leave':
        break

#shoppingclam.insert(len(shoppingclam), 'and')

print('You have successfully hunted for dubloons, gone shopping, and \
gotten prepared for the ball, congratulations!')

closing = 'You arrive at the ball, in an underwater castle inside of a \
magnificent kelp forest. A pair of of burly seahorse guards stand over \
the door. As you make your way inside, you look resplendent, in your \
{}. You see a couple of crabs waltzing, with some mischievous young \
clown fish flitting in between them. Puffer Fish are cavorting with squids, \
eels are doing the twist with sea slugs, and an old grizzled looking shark dozes \
off in the corner. Confident in your new threads, you dance the night away, \
remaining at the ball until the early hours of the morning'.format(shoppingclam)

for line in textwrap.wrap(closing, 80):
    print(line)

print('*******************************************The End****************************************')
