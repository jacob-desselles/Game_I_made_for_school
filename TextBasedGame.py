#Jacob Desselles
def show_instructions():
    #This function shows how to play
    print("Mercenary vs. Dragon Game")
    print('''
    There are a number of items to collect,
    though not every one will be good for you.
    Choose wisely what you obtain, or suffer the consequences
    of your lust for gold.
    Move commands: north, south, east, west.
    get: asks you what you'd like to get. Input item afterwards.
    look: look around (very useful).
    status: check your current status.''')
def main():
    show_instructions()
    #First, define the rooms
    rooms = {'Dungeon': {'name': 'Dungeon', 'south': 'Armory', 'west': 'Weapons Room',
    'east': 'Church', 'north' : 'True Despair'},
    'Armory':{'name': 'Armory','north':'Dungeon', 'item' : 'plate-set'},
    'Weapons Room' : {'name' : 'Weapons Room','east':'Dungeon', 'item' : 'sword'},
    'Church' : {'name' : 'Church','west' : 'Dungeon', 'item' : 'Holy book'},
    'True Despair' : {'name' : 'True Despair','east' : 'Decision', 'south': 'Dungeon', 'item' : 'Head of Solitude'},
    'Decision' : {'name' : 'Decision','east' : 'Gambit', 'north': 'Escape'},
    'Gambit' : {'name' : 'Gambit', 'west' : 'Decision', 'north' : 'Bad Ending', 'item' : ['key', 'coin']},
    'Escape' : {'name' : 'Escape','south' : 'Decision', 'item' : 'cloak'}
    }
    directions = ['north', 'south', 'east', 'west'] #This will continuously call upon our rooms dictionary.
    current_room = rooms['Dungeon'] #Our starting room.
    inventory = []
    def check_status():
    #Check the current status of your character
        print('You are in the {}'.format(current_room['name']))
        print(f'Inventory: {inventory}')
        print('____________') #Defining check_status within our main function helps with not having to deal with glob functions and helps with when we define our variables.
    #To keep the game continuous, we'll have a while True condition
    while True:
        try:
            user_input = input('What would you like to do?: ')
            if user_input == 'status':
                check_status()
            if user_input in directions:
                if user_input in current_room:
                    current_room = rooms[current_room[user_input]]
                    print("You have moved to the {}\n".format(current_room['name']))
            if user_input == 'get': #Approaching it this way is a lot easier and more consistent than handling it with stripping
                pick_up = input('What would you like to get?: ') #Select specifically what you'd like to pick up
                if pick_up == current_room['item']:
                    inventory.append(pick_up)
                    print(f'You have picked up the {pick_up}')
            if user_input == 'get' and current_room == rooms['Gambit']:
                pick_up1 = input('What would you like to REALLY get?: ') #Since the Gambit has two items, we have to handle this uniquely.
                #However, this also prompts 'What would you like to get?: ' twice.
                if pick_up1 == current_room['item'][0] or pick_up1 == current_room['item'][1]:
                    inventory.append(pick_up1)
            if user_input == 'look':
                if current_room == rooms['Dungeon']: #Since we have a look ability in our game, each room has to be uniquely described.
                    print('''
                    The texture of rust and the smell of decay
                    take hold of what was once a more refined form of
                    imprisonment. The only source of light is the hole that
                    you have fell through to reach this place, and,
                    just as the skeletons of the bodies from long ago,
                    you are trapped. To your south is a wooden door reinforced
                    by two iron bars with a sign that displays the word "Armory",
                    while to the west is a purely steel door containing a sign
                    which reads "Weapons". To the East, in the meanwhile,
                    is not a door, but a bannister covered in a flourescent glow.
                    Finally, to the North is purely darkness; you are unsure
                    if there even is a North, though you do see a slight concave
                    shapening around the walls as you peer more towards it.\n''') #We could go simple, but I'd like the game to be entertaining.
                if current_room == rooms['Armory'] and 'plate-set' not in inventory: #We have to re-explain our rooms in a unique way depending upon if the item is picked up.
                    print('''
                    Iron, stone, wood, steel, bronze, all which are found 
                    within here, yet only the shavings of such. You see a series
                    of lockers to your right, all which are either opened or damaged
                    to the point of not being safe to even pry. To your left,
                    a fireplace with a bellow attached, though both have been collecting
                    dust for some time. To the other side of the room is a table,
                    containing a plate-set and a pierced chestplate. As you analyze
                    the chestplate more, you see that it is damaged beyond usability,
                    with a gigantic slash going from corner to corner and rust forming
                    along the bloodstreaks of it. It is safe to assume that if the previous
                    owner is suffering from buyer's remorse, it is no longer a concern.\n''')
                if current_room == rooms['Armory'] and 'plate-set' in inventory:
                    print('''
                    Iron, stone, wood, steel, bronze, all which are found 
                    within here, yet only the shavings of such. You see a series
                    of lockers to your right, all which are either opened or damaged
                    to the point of not being safe to even pry. To your left,
                    a fireplace with a bellow attached, though both have been collecting
                    dust for some time. To the other side of the room is a table,
                    containing an empty space of once was a plate-set and a pierced chestplate.
                    This room no longer serves a purpose, especially to you.\n
                    ''')
                if current_room == rooms['Weapons Room'] and 'sword' not in inventory:
                    print('''
                    Red. Nothing but the sight of red and the feelings of wrath and heat 
                    envelop the energy of the room. As you look around, you see red walls,
                    decorated with patterns of warriors fighting historic battles. To your
                    right is a furnace, surprisingly still burning bright despite the obvious
                    lack of maintenance and attention. To your left are a series of chairs
                    surrounding a table, along with die and some bottles laying on top.
                    Above you is a chandelier, though it does not seem to be supported properly
                    as the iron plate it is attached to is detaching itself from the ceiling.
        
                    To the other side of the room is a decomposing body, sitting in a chair.
                    He appears to be in uniform, and is sitting in a respectful position.
                    He is holding a sword in his right hand.\n
                    ''')
                if current_room == rooms['Weapons Room'] and 'sword' in inventory:
                    print('''
                    Red. Nothing but the sight of red and the feelings of wrath and heat 
                    envelop the energy of the room. As you look around, you see red walls,
                    decorated with patterns of warriors fighting historic battles. To your
                    right is a furnace, surprisingly still burning bright despite the obvious
                    lack of maintenance and attention. To your left are a series of chairs
                    surrounding a table, along with die and some bottles laying on top.
                    Above you is a chandelier, though it does not seem to be supported properly
                    as the iron plate it is attached to is detaching itself from the ceiling.

                    To the other side of the room is a decomposing body, sitting in a chair.
                    He appears to be in uniform, and is sitting in a respectful position,
                    or at least he was before you stole his sword. You're still a good person though,
                    I'm sure.\n
                    ''')
                if current_room == rooms['Church'] and 'Holy book' not in inventory: #Since I'm a Christian man, I figured having a Holy Book in a dragon game is only appropriate.
                    print('''
                    Truly, you are Blessed.
                    1 Samuel 1:13 "Now Hannah spoke in her heart; only her lips moved,
                    but her voice was not heard. Therefore, Eli thought she was drunk."
                    Who do you believe is unheard?

                    The room glows with such a brightness that you cannot help but kneel
                    in awe, yet there is no plausible source of its light. You feel a shame
                    crawling beneath your skin and underneath the scars you've been carrying
                    throughout majority of your life. To your left is a bookshelf,
                    containing several translations of both the Old and New Testament.
                    To your right are statues of saints kneeling before Jesus
                    and a fountain with a donation box for tithes. Directly adjacent
                    to you is an altar. Above the altar is a cross, not made of gold
                    but of clay. Above that are murals, encapsulating the entirety
                    of the ceiling.

                    As you peer closer to the altar, you notice there is a Holy book.\n
                    ''')
                if current_room == rooms['Church'] and 'Holy book' in inventory:
                    print('''
                    Truly, you are Blessed.
                    1 Samuel 1:13 "Now Hannah spoke in her heart; only her lips moved,
                    but her voice was not heard. Therefore, Eli thought she was drunk."
                    Who do you believe is unheard?

                    The room glows slightly dimmer. To your left is a bookshelf,
                    containing several translations of both the Old and New Testament.
                    To your right are statues of saints kneeling before Jesus
                    and a fountain with a donation box for tithes. Directly adjacent
                    to you is an altar. Above the altar is a cross, not made of gold
                    but of clay. Above that are murals, encapsulating the entirety
                    of the ceiling.\n
                    ''')
                if current_room == rooms['True Despair'] and 'Head of Solitude' not in inventory: #Since our character is a mercenary, he'll need the head as proof he killed the beast.
                    print('''Beyond the light of your Holy book is a veil of darkness.
                    Surrounding you are columns and marble, all containing markings from
                    the claws of Solitude. In front of you lies the body of once was the
                    bane of society itself; his scales covered in his blood, and
                    his stomach opened from the inside. Yet, he looks peaceful. To your east
                    lies an empty room, yet it contains one of the most important decisions
                    you've ever had to make in your life.

                    His face appears to have accepted his face. Let's change that,say "get Head of Solitude".\n
                    ''') #Also I want the game to be funny.
                if current_room == rooms['True Despair'] and 'Head of Solitude' in inventory:
                    print('''Beyond the light of your Holy book is a veil of darkness.
                    Surrounding you are columns and marble, all containing markings from
                    the claws of Solitude. In front of you lies the body of once was the
                    bane of society itself; his scales covered in his blood, and
                    his stomach opened from the inside. To your east
                    lies an empty room, yet it contains one of the most important decisions
                    you've ever had to make in your life.\n''')
                if current_room == rooms['Decision']:
                    print('''This room is empty. This room is really empty.
                    Stone walls and wooden doors is all it contains. To your north
                    is a locked door and to your east is an unlocked door.
                    How will you solve this kerfuffle?\n
                    ''')
                if current_room == rooms['Escape'] and 'key' in inventory:
                    print('''A breath of fresh air fills your nostrils.
                    In front of you is a wall that has collapsed downward
                    in such a way that you could scale down it, but only
                    if you feel ready. Once you'd like to call the adventure
                    to an end, say "get cloak".\n
                    ''')
                if current_room == rooms['Gambit'] and ('key' not in inventory and 'coin' not in inventory): #Yes, I'm getting lazy with my writing
                    print('''Flashing lights fill this room, spearheaded by machines
                    with levers near them. To your north is a door, though instead of a keyhole,
                    it appears to be a coinslot.

                    Adjacent to you is a stool containing both a key and a coin.\n
                    ''')
                if current_room == rooms['Gambit'] and ('key' in inventory and 'coin' not in inventory):
                    print('''Flashing lights fill this room, spearheaded by machines
                    with levers near them. To your north is a door, though instead of a keyhole,
                    it appears to be a coinslot.

                    Adjacent to you is a stool containing a coin.\n
                    ''')
            if current_room == rooms['True Despair'] and ('Holy book' not in inventory and 'sword' not in inventory and 'plate-set' not in inventory): #Writing each situation for True Despair was absolutely painful.
                print('''You truly have not prepared. Immediately, you were
                gored. You did not see it, you had no idea there was an enemy
                nearby, and you had no way to fight it. Be grateful that it was
                quick and mostly painless, yet be humble enough to realize
                that the blindness of bravery was your undoing.\n''')
                break
            if current_room == rooms['True Despair'] and ('Holy book' in inventory and 'sword' in inventory and 'plate-set' in inventory and 'look' not in user_input and 'get' not in user_input):
                print('''The light from your Holy book illuminates your surroundings,
                showing pillars of marble and stone circulating a pedestal within the room.
                On top of that pedestal appears to be Solitude, the dragon who strikes
                fear into existence.
                Though, he seems to be of normal height compared to you. He also does not
                seem as much of a dragon as he is a man covered in scales. He appears
                to solely want to be by himself and to live by his name, Solitude.
                You go up to speak to him.
                "What are you doing here?"\n
                "I'm simpl-"\n
                "WHOA, WHOA, CHILL OUT!"\n
                You slash his stomach open. It's too late right now to really give alternate choices here.\n
                ''')
            if current_room == rooms['True Despair'] and ('Holy book' in inventory and 'sword' not in inventory and 'plate-set' not in inventory): #Again, getting lazy
                print('''The light from your Holy book illuminates your surroundings,
                showing pillars of marble and stone circulating a pedestal within the room.
                On top of that pedestal appears to be Solitude, the dragon who strikes
                fear into existence.
                Though, he seems to be of normal height compared to you. He also does not
                seem as much of a dragon as he is a man covered in scales. He appears
                to solely want to be by himself and to live by his name, Solitude.
                You go up to speak to him.
                "What are you doing here?"\n
                "I'm simpl-"\n
                "WHOA, WHOA, CHILL OUT!"\n
                He slashed your stomach open. You're dead lol.\n
                ''')
                break
            if current_room == rooms['True Despair'] and ('Holy book' not in inventory and 'sword' in inventory and 'plate-set' in inventory):
                print('''You can not see well around you. The darkness envelops the environment.
                Before you could even react, you felt a tinge into your chest. Then, you felt nothing.
                This is where your adventure ends.\n
                ''')
                break
            if current_room == rooms['True Despair'] and ('Holy book' in inventory and 'sword' not in inventory and 'plate-set' in inventory):
                print('''The light from your Holy book illuminates your surroundings,
                showing pillars of marble and stone circulating a pedestal within the room.
                On top of that pedestal appears to be Solitude, the dragon who strikes
                fear into existence.
                Though, he seems to be of normal height compared to you. He also does not
                seem as much of a dragon as he is a man covered in scales. He appears
                to solely want to be by himself and to live by his name, Solitude.
                You go up to speak to him.
                "Excuse me sir, would you like to accept Je-"\n
                Apparently not. He pierced your chest open pretty quick, even with that plate-set you were wearing.\n
                ''')
                break
            if current_room == rooms['True Despair'] and ('Holy book' in inventory and 'sword' in inventory and 'plate-set' not in inventory):
                print('''The light from your Holy book illuminates your surroundings,
                showing pillars of marble and stone circulating a pedestal within the room.
                On top of that pedestal appears to be Solitude, the dragon who strikes
                fear into existence.
                Though, he seems to be of normal height compared to you. He also does not
                seem as much of a dragon as he is a man covered in scales. He appears
                to solely want to be by himself and to live by his name, Solitude.
                You go up to speak to him.
                "What are you-"\n
                Before you could react, he immediately turned around and slashed your stomach open.
                "Oh jeez, bro. I'm sorry, you just snuck up right behind me. If only
                you were wearing some sort of plate-set, I could hear you right away."
                You died to a goof.\n
                ''')
                break
            if current_room == rooms['True Despair'] and ('Holy book' not in inventory and 'sword' in inventory and 'plate-set' not in inventory):
                print('''You ran into the darkness, swinging wildly into the air. Then,
                you smash your sword against some stone. It shatters almost immediately,
                and then after that shattering, nothing. You have not felt your last breath,
                nor did you feel the claw piercing your skull.\n
                You have died, adventurer, a foolish death.\n
                ''')
                break
            if current_room == rooms['True Despair'] and ('Holy book' not in inventory and 'sword' not in inventory and 'plate-set' in inventory):
                print('''You are truly a fool. You walk into the darkness, covered in its shroud.
                Within it, you hear a tinge from your plate-set. And then, you felt your heart stop.
                Afterwards, nothing. Despite your armor, you are defenseless against the absence of light,
                and you will have nothing to show for your efforts.\n
                ''')
                break
            if current_room == rooms['Gambit'] and 'coin' in inventory: #In order to keep it simple and able to fulfill the project within the time limit,
                #I made sure that the moment you pick up the coin, the bad ending triggers. I felt like I could get away with it too since it implies he
                #IMMEDIATELY wants to go gambling and was overwhelmed by temptation.
                print('''You could not resist the temptation of the jingles
                from the machines. You grabbed the coin and inserted it into
                the door, hoping to witness what would be the immediate change
                of circumstance in your personal life. Inside was what made you
                believe this was the case. Coins upon coins. You used one on the machines
                inside of the Gambit room. You won! You used another, you won again!
                For hours, you've played. Hours then turned into days. Then weeks.
                Eventually, you lost track of time. You'd live off the flesh of rats
                that would crawl in. For water, you'd collect whenever it would rain into the dungeon.
                Eventually, you would become who everyone believed you'd have to be born as: Solitude.\n
                ''')
                break
            if current_room == rooms['Escape'] and 'cloak' in inventory and 'Head of Solitude' in inventory:
                print('''You grab your cloak and scale down the wall. In three hours walk,
                you've made it back to your town. As you carry the Head of Solitude by your side,
                people stare in both shock and surprise. "Is it finally over?" you hear one passerby
                remark. You cash in on your bounty and buy a room to sleep in, getting the much
                needed rest a mercenary like you deserves. Today, it's a room in the local
                inn. Tomorrow, it's going to be inside of an actual home. The day after that,
                maybe some chickens and some animals. You have finally achieved a goal which will
                render the need to shed blood for money redundant, and now you can finally move on
                to a brighter future. This is the true end of your journey.\n
                ''')
                break
            if current_room == rooms['Escape'] and 'cloak' in inventory and 'Head of Solitude' not in inventory:
                #I wanted to make sure to add as much variety as possible when it comes to the endings you can get.
                print('''You grab your cloak and scale down the wall. In three hours walk,
                you've made it back to your town. You walk into the burgher and tell them,
                "I killed Solitude."\n
                "Where's your proof?"\n
                "What do you mean?"\n
                "Do you have his head?"\n
                In this moment, you realize that you forgot to grab his head. You will never
                truly escape the life of being a mercenary, and you will always have to place your loyalty
                upon the highest bidder as a sellsword.\n
                ''')
                break
            if current_room == rooms['Escape'] and 'key' not in inventory:
                    print('Sadly, the door is locked.\n')
                    current_room = rooms['Decision']
            if user_input == 'exit':
                break
        except:
            print('INVALID INPUT')
if __name__ == "__main__":
    main()