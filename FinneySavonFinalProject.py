import random
import time

# ---------- PLAYER ----------
def create_player(name):
    return {
        "name": name,
        "sanity": 100,
        "stamina": 100,
        "fear": 0,
        "level": 1,
        "alive": True,
        "encounter_chance": 10,
        "day": 0,          # hidden day schedule
        "debuffs": []      # active debuffs
    }

def change_stat(player, stat, amount):
    player[stat] = max(0, min(100, player[stat] + amount))

# ---------- TEXT DISTORTION ----------
def distort_text(text, sanity):
    if sanity > 60:
        return text
    elif sanity > 35:
        return text.replace("e", "3").replace("a", "@")
    elif sanity > 15:
        return text.replace("e", "3").replace("a", "@").replace("o", "0")
    else:
        return "".join(
            c if random.random() > 0.2 else random.choice("#$%@!?")
            for c in text
        )

def narrate(player, text):
    print(distort_text(text, player["sanity"]))
    time.sleep(0.6)

# ---------- GAME OVER ----------
def check_sanity(player):
    if player["sanity"] <= 0:
        narrate(player, f"\n{player['name']}, your thoughts collapse into static. The Backrooms keep what is left of you.")
        player["alive"] = False

def game_over(player):
    narrate(player, f"\n{player['name']}, something finds you before you can beg, run, or understand.")
    print("GAME OVER")
    player["alive"] = False

def game_over_animations(player):
    narrate(player, f"\n{player['name']}, Laugther starts invade your mind and you can't help but to start laughing, Soon you hear a sword swung down your head, The madness has another soul")
    print("Game Over")
    player["alive"] = False

# ---------- DEBUFF SYSTEM ----------
DEBUFF_POOL = [
    {
        "name": "Shaking Hands",
        "duration": (2, 4),
        "fear_per_day": 4,
        "sanity_per_day": -2,
        "stamina_per_day": -8,
        "message": "Your hands will not stay still."
    },
    {
        "name": "Splintered Focus",
        "duration": (2, 5),
        "fear_per_day": 2,
        "sanity_per_day": -6,
        "stamina_per_day": -3,
        "message": "Your thoughts keep breaking apart mid-sentence."
    },
    {
        "name": "Trembling Legs",
        "duration": (1, 3),
        "fear_per_day": 3,
        "sanity_per_day": -1,
        "stamina_per_day": -12,
        "message": "Every step feels like it costs too much."
    },
    {
        "name": "Cold Sweat",
        "duration": (2, 4),
        "fear_per_day": 5,
        "sanity_per_day": -3,
        "stamina_per_day": -6,
        "message": "Your skin feels wet and wrong."
    },
    {
        "name": "Whisper-Sick",
        "duration": (2, 6),
        "fear_per_day": 6,
        "sanity_per_day": -5,
        "stamina_per_day": -2,
        "message": "You hear your name in the walls."
    },
    {
        "name": "The Madness",
        "duration": (2, 6),
        "fear_per_day": +1,
        "sanity_per_day": -3,
        "stamina_per_day": +2,
        "message": "There is always laughter, why wouldn't there be?"
    }
]

def apply_random_debuff(player):
    debuff = random.choice(DEBUFF_POOL)
    duration = random.randint(*debuff["duration"])
    player["debuffs"].append({
        "name": debuff["name"],
        "days_left": duration,
        "fear_per_day": debuff["fear_per_day"],
        "sanity_per_day": debuff["sanity_per_day"],
        "stamina_per_day": debuff["stamina_per_day"],
        "message": debuff["message"]
    })
    narrate(player, f"\nA new curse settles into you: {debuff['name']}. {debuff['message']}")

def process_debuffs(player):
    if not player["debuffs"]:
        return

    narrate(player, "\nThe day drags on. Whatever touched you is still inside you.")
    for debuff in player["debuffs"][:]:
        change_stat(player, "fear", debuff["fear_per_day"])
        change_stat(player, "sanity", debuff["sanity_per_day"])
        change_stat(player, "stamina", debuff["stamina_per_day"])
        debuff["days_left"] -= 1

        if debuff["days_left"] <= 0:
            narrate(player, f"The pressure in your chest eases. {debuff['name']} finally loosens its grip.")
            player["debuffs"].remove(debuff)

# ---------- TIME SYSTEM ----------
def advance_day(player):
    player["day"] += 1

    # hidden schedule increases pressure over time
    sanity_drain = 2 + (player["day"] // 4)
    change_stat(player, "sanity", -sanity_drain)

    # debuffs tick every day
    process_debuffs(player)

# ---------- LEVEL WRITING ----------
def generate_level_descriptions():
    return {
        1: [
            "The yellow wallpaper stretches in every direction, its pattern repeating with a tiny imperfection that becomes harder to ignore the longer you stare. The fluorescent lights above you hum with a sick, insect-like patience.",
            "You stand in a corridor that seems to have no intention of ending. The carpet is damp beneath your shoes, and the air tastes stale, dusty, and old enough to have forgotten what sunlight is.",
            "The Backrooms open around you like a wound that never closes. Every wall is the same tired yellow, every shadow too deep, every silence too complete."
        ],
        2: [
            "The geometry here feels bruised. Hallways bow inward when you look away, then straighten again with a subtle cruelty that makes you doubt your own eyes.",
            "The lights flicker like something is breathing inside them. Each pulse leaves the room a little more uncertain, as if the place is slowly losing its grip on reality.",
            "The walls here do not simply exist. They watch. They listen. They make you feel as though your footsteps are being counted somewhere just out of sight."
        ],
        3: [
            "The rooms twist with a quiet, deliberate malice. A hallway you swear was straight a moment ago now bends to the left, then the right, as though the building itself is choosing a path for you.",
            "You begin to hear faint echoes that do not match your movements. Something is following your rhythm, but always half a beat behind, always wrong in a way your body notices before your mind can.",
            "The silence presses against your ears until it feels almost physical, thick and wet and waiting."
        ],
        4: [
            "Reality feels threadbare here, as if one wrong breath might tear it open. The air is cold enough to sting, and the walls pulse faintly with a slow, repulsive rhythm.",
            "You feel watched from every angle at once. Not in the ordinary way of being observed, but in the far worse way of being anticipated.",
            "The Backrooms are no longer a place. They are a mood, a pressure, a patient thing that is learning your shape."
        ],
        5: [
            "A door stands alone in the distance, impossible and wrong, as though someone ripped it out of a different world and dropped it here by mistake. The air around it feels thinner. Quieter. Waiting.",
            "You reach a chamber that should not exist. At its center is a door so still it seems carved from the absence of all the rooms behind you.",
            "There is a door ahead. It does not belong here. It looks almost kind."
        ]
    }

def describe_level(player, descriptions):
    line = random.choice(descriptions[player["level"]])
    narrate(player, "\n" + line)

# ---------- ENTITIES ----------
def get_level_entity(level):
    return {
        1: "Watcher",
        1: "The Animations",
        2: "Smiler",
        3: "Hound",
        4: "Skin Stealer",
        5: "The End"
    }[level]

def encounter_cost(player):
    # fear increases encounter pressure
    player["encounter_chance"] = min(90, 10 + (player["fear"] // 3) + (player["level"] * 5))

# ---------- ENCOUNTERS ----------
def encounter(player):
    entity = get_level_entity(player["level"])
    narrate(player, "\nYou feel the room change before you see anything at all.")
    apply_random_debuff(player)

    if entity == "Watcher":
        narrate(player, "Something stands at the edge of the corridor, too far away to measure and too still to be alive. It tilts its head only after you notice it.")
        choice = input("Do you LOOK AWAY, HOLD STILL, or WALK BACK? ").lower()

        if choice == "look away":
            if player["sanity"] > 45:
                narrate(player, "You force your eyes forward and keep moving. Behind you, the silence shifts with disappointment.")
                change_stat(player, "fear", 6)
                change_stat(player, "sanity", -4)
            else:
                game_over(player)

        elif choice == "hold still":
            if player["fear"] < 35:
                narrate(player, "You do not move. After a long moment, the shape stops being a shape and becomes distance again.")
                change_stat(player, "sanity", -3)
            else:
                game_over(player)

        elif choice == "walk back":
            if player["stamina"] > 40:
                narrate(player, "You back away slowly, one step at a time. The corridor behind you feels longer than it should.")
                change_stat(player, "stamina", -18)
                change_stat(player, "fear", 8)
            else:
                game_over(player)
        else:
            game_over(player)

    elif entity == "Smiler":
        narrate(player, "A grin appears in the dark. It does not belong to a face you can fully understand, only to something that knows how fear works.")
        narrate(player, "The smile widens every time your breathing quickens.")
        choice = input("Do you LOOK AWAY, RUN, or SHUT YOUR EYES? ").lower()

        if choice == "look away":
            if player["sanity"] > 55:
                narrate(player, "You refuse to feed it with your attention. The grin lingers, then fades into the walls.")
                change_stat(player, "sanity", -5)
                change_stat(player, "fear", 7)
            else:
                game_over(player)

        elif choice == "run":
            if player["stamina"] > 55:
                narrate(player, "You run until your lungs burn. The laughter behind you sounds very close, then far away, then close again.")
                change_stat(player, "stamina", -30)
                change_stat(player, "fear", 10)
            else:
                game_over(player)

        elif choice == "shut your eyes":
            if player["sanity"] > 35:
                narrate(player, "You close your eyes and pray the thing in the darkness loses interest. When you open them again, nothing is where it was.")
                change_stat(player, "sanity", -8)
                change_stat(player, "fear", 12)
            else:
                game_over(player)
        else:
            game_over(player)

    elif entity == "Hound":
        narrate(player, "Heavy footsteps slam against the floor behind you. Something is running, and it has already decided where you are going.")
        narrate(player, "Its breathing is wet, close, and far too fast for anything that should still be called alive.")
        choice = input("Do you HIDE, RUN, or FIND COVER? ").lower()

        if choice == "hide":
            if player["fear"] < 55 and player["stamina"] > 25:
                narrate(player, "You flatten yourself against the wall and stop breathing. The thing charges past, dragging the smell of rot and wet fur with it.")
                change_stat(player, "stamina", -12)
                change_stat(player, "sanity", -4)
            else:
                game_over(player)

        elif choice == "run":
            if player["stamina"] > 65:
                narrate(player, "You sprint until the hallway blurs into a smear of yellow and shadow. Something behind you crashes into the wall, then resumes the chase.")
                change_stat(player, "stamina", -35)
                change_stat(player, "fear", 12)
            else:
                game_over(player)

        elif choice == "find cover":
            if player["sanity"] > 30:
                narrate(player, "You dive behind a broken cabinet and hold your breath. Claws scrape the floor just inches away, lingering far too long.")
                change_stat(player, "stamina", -20)
                change_stat(player, "fear", 9)
            else:
                game_over(player)
        else:
            game_over(player)

    elif entity == "Skin Stealer":
        narrate(player, "A person stands in the corridor ahead of you. They look relieved to see you. That is the first mistake.")
        narrate(player, "Their smile is too practiced, their posture too careful, like something wearing the memory of a human being.")
        choice = input("Do you ASK A QUESTION, BACK AWAY, or SPRINT PAST? ").lower()

        if choice == "ask a question":
            if player["sanity"] > 50:
                narrate(player, "Its answer arrives a second too late, and the voice slips in tone halfway through the sentence. Whatever it is, it is trying very hard to sound normal.")
                change_stat(player, "sanity", -7)
                change_stat(player, "fear", 8)
            else:
                game_over(player)

        elif choice == "back away":
            if player["stamina"] > 30:
                narrate(player, "You back up slowly. The thing mirrors your movement with an almost human patience.")
                change_stat(player, "stamina", -10)
                change_stat(player, "fear", 7)
            else:
                game_over(player)

        elif choice == "sprint past":
            if player["stamina"] > 70:
                narrate(player, "You break into a run. The thing reaches out, just once, and misses by a matter of inches.")
                change_stat(player, "stamina", -40)
                change_stat(player, "fear", 15)
            else:
                game_over(player)
        else:
            game_over(player)

    elif entity == "The End":
        narrate(player, "The door is still there, but the room around it has changed. The air is too quiet. Even your breathing seems afraid.")
        narrate(player, "Something on the other side knows your name.")
        choice = input("Do you OPEN THE DOOR, WAIT, or TURN AWAY? ").lower()

        if choice == "open the door":
            if player["sanity"] > 35 and player["level"] >= 5:
                narrate(player, "The door opens without resistance. Light spills through, thin and merciful. For the first time, the Backrooms let go.")
                player["alive"] = False
                player["won"] = True
            else:
                game_over(player)

        elif choice == "wait":
            narrate(player, "You wait. The thing on the other side learns your hesitation.")
            game_over(player)

        elif choice == "turn away":
            narrate(player, "You make the mistake of looking back into the hallway. The door is gone.")
            game_over(player)
        else:
            game_over(player)
    elif  entity == "The Animations":
        narrate(player, "As you procced to walk further into the backrooms, You hear laughter coming from all directions. Paralysis soon enter your body as fear of what is coming run rampant in your mind.")
        narrate(player, "The laughter has soon converged into one direction, BEHIND")
        narrate(player, "You turn around and see the source of the laughing. Creatures that look they came off a 1980s cartoon and welding axes and swords that send a shiver down your spine.")
        choice = input("The animations are lunging at you while laughing manically, Do you RUN, HIDE, or LAUGH? ").lower()

        if choice == "RUN":
            if player["stamina"] >= 35:
                narrate(player, "You can ran as fast as your leg can manage. but the laugther follows behind ")
                change_stat(player, "stamina", -20)
                change_stat(player, "sanity", -7)
            else:
                game_over_animations(player)

        elif choice == "Hide":
            if player["sanity"] >= 50:
                narrate(player,"You hide from the laughter, You really want to laugh at the situation you are in, but your mind refuses to give in to the madness.")
                narrate(player, "You hear the laughter passed by, you then proceed to your own journey.")
                change_stat(player, "sanity", -10)
                change_stat(player, "Fear", -15)
            else:
                game_over_animations(player)
        elif choice == "Laugh":
            if player["sanity"] >= 80:
                narrate(player, "You can't help but laugh at the absurdly of the situation you are in, the creatures join in the madness.")
                narrate(player, "After a few minutes, the creatures proceed to go away and laughing all the same. You feel like you lost a part of yourself.")
                change_stat(player, "sanity", -50)
                change_stat(player, "Fear", +20)
                change_stat(player, "stamina", +40)
                
            else:
                game_over_animations(player)

# ---------- EXPLORATION ----------
def explore(player, descriptions):
    describe_level(player, descriptions)

    narrate(player, "\nThe corridor splits ahead of you, and each direction feels like a decision the place already expects you to regret.")
    choices = ["forward", "left", "right"]

    if player["level"] >= 2:
        choices.append("back")
    if player["level"] >= 3:
        choices.append("enter room")
    if player["level"] >= 4:
        choices.append("go down")

    if player["sanity"] < 50:
        choices.append("follow the whisper")
    if player["sanity"] < 30:
        choices.append("???")
        choices.append("listen to the walls")

    random.shuffle(choices)
    print("\nOptions:", ", ".join(choices))
    choice = input("What do you do? ").lower()

    # Exploration costs a lot of stamina
    stamina_loss = random.randint(18, 32) + (player["level"] * 2)
    sanity_loss = random.randint(6, 12) + (player["day"] // 4)
    fear_gain = random.randint(4, 8)

    change_stat(player, "stamina", -stamina_loss)
    change_stat(player, "sanity", -sanity_loss)
    change_stat(player, "fear", fear_gain)

    if choice not in choices:
        narrate(player, "You hesitate. The hesitation feels loud. The hallway seems to shift while you stand there trying to decide what to become.")
        change_stat(player, "sanity", -10)
        change_stat(player, "fear", 8)
        return

    # movement narration
    if choice == "enter room":
        narrate(player, "You push into the room. It is too empty to be safe, and too arranged to be accidental.")
    elif choice == "go down":
        narrate(player, "You descend a narrow stairwell that should not exist in a place like this. The steps feel damp and recently used.")
    elif choice == "follow the whisper":
        narrate(player, "You follow the whisper because it sounds almost like your name, and because fear has started making your decisions for you.")
    else:
        narrate(player, f"You move {choice}, deeper into the yellow maze.")

    # chance to progress deeper
    progress_chance = 35 + (player["level"] * 8) - (player["fear"] // 10)
    progress_chance = max(10, min(85, progress_chance))

    if random.randint(1, 100) <= progress_chance and player["level"] < 5:
        player["level"] += 1
        narrate(player, f"\nThe Backrooms tighten around you. You have reached Level {player['level']}.")

# ---------- REST ----------
def rest(player):
    narrate(player, "\nYou stop moving. The silence grows heavy enough to press against your skin.")

    # small recovery only
    change_stat(player, "sanity", +8)
    change_stat(player, "stamina", +12)
    change_stat(player, "fear", -4)

    player["encounter_chance"] = min(90, player["encounter_chance"] + 18)

    # resting may still trigger something
    narrate(player, "The stillness feels wrong. The longer you stay, the more the room seems to notice that you have stopped.")
    if random.randint(1, 100) < 55:
        encounter(player)

# ---------- MAIN ----------
def main():
    name = input("Enter your name: ").strip()
    if not name:
        name = "Unknown"

    player = create_player(name)
    descriptions = generate_level_descriptions()

    print(f"\n{name}, you wake to the sound of fluorescent lights buzzing overhead.")
    time.sleep(1)
    print("There is no sky. No window. No exit. Only a corridor that smells faintly of mold and old rain.")
    time.sleep(1)
    print("When you turn around, the place you came from is already gone.")
    time.sleep(1)
    print("The Backrooms have decided you belong here now.\n")
    time.sleep(1)

    while player["alive"]:
        if player["level"] >= 5:
            narrate(player, "\nA door waits ahead. It looks real in a way nothing else here has.")
            if player["sanity"] <= 25:
                narrate(player, "Your mind screams at you not to trust it.")
            # final encounter chance is high
            if random.randint(1, 100) <= 35:
                encounter(player)
            else:
                narrate(player, "You reach for the handle.")
                narrate(player, "The door opens.")
                narrate(player, "For a moment, the air beyond it smells like the world you lost.")
                print("\nYOU WIN")
                break

        encounter_cost(player)

        print(distort_text(
            f"\n{name} | Level {player['level']} | Sanity: {player['sanity']} | Stamina: {player['stamina']} | Fear: {player['fear']}",
            player["sanity"]
        ))
        if player["debuffs"]:
            print("Current debuffs:", ", ".join([f"{d['name']} ({d['days_left']} days)" for d in player["debuffs"]]))

        action = input("\nDo you EXPLORE or REST? ").lower()

        if action == "explore":
            explore(player, descriptions)
        elif action == "rest":
            rest(player)
        else:
            narrate(player, "You freeze in place, uncertain whether movement is safer than stillness.")
            change_stat(player, "sanity", -6)
            change_stat(player, "fear", 5)

        advance_day(player)

        if random.randint(1, 100) <= player["encounter_chance"]:
            encounter(player)

        check_sanity(player)

        if player["stamina"] <= 0:
            narrate(player, "\nYour legs fail beneath you. You cannot keep running forever.")
            game_over(player)

    print("\nEnd.")

# ---------- START ----------
if __name__ == "__main__":
    main()