# Exercise 43. Basic Object-Oriented Analysis and Design
# 攻略：
# 1. take a joke
# 2. 必须输对密码...
# 3. slowly place the bomb
# 4. 选对逃生舱

from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):
    # different types of death
    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smater.",
        "Such a loser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(0)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
             The Gothons of Planet Percal #25 have invaded your ship around
             destroyed your entire crew.You are the last surviving member
             and your last mission is to get the neutron destruct bomb from the
             Weapons Armory,put it in the bridge,and blow the ship up after
             getting into an escape pod.

             You're running the CentralCorridor to the Weapons Armory when a
             Gothons jumps out,red scaly skin,dark grimy teeth,and evil clown
             costume flowing around his hate filled body.He's blocking the
             door to the Armory and about to pull a weapon to blast you.
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quik on the draw you yank out your blaster and fire it at the
                Gothon. His clown costume is flowing and moving around his body
                ,which throws off you aim.Your laser hits his costume but misses
                him entirely.This completely ruins his brand new costume his
                mother bought him,which makes him fly into an insane rage and
                blast you repeatedly in the face until you are dead.Then he eats
                you.
            """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer,you dodge,weave,slip and
                slide righe as the Gothon's blaster cranks a laser
                past your head. In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out.You wake up shortly after only to
                die as the Gothon stomps on your head and eats you.
            """))
            return 'death'

        elif action == 'take a joke':
            print(dedent("""
                Lucky for you they made you learn Gothon insults in
                the academy. You tell the one Gothon jokes you know:
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr, The Gothon stops,tries
                not to laugh , then busts out laughing and can't move
                While he's laughing you run up and shoot him square in
                Weapon Armory door.
            """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do a dibe roll into the Weapon Aemory,crouch and scan
            the room for more Gothons that might be hiding.It's dead
            quiet, too quiet. you stand ip and run to the far side of
            the room and find the neutron bomb in  its cintainer.
            There's a keypad lock on the box and you need the code to
            get the bob out. If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb.The
            code is 3 digits.
        """))

        #生成一个3位随机的密码，要求用户输入
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print("The Code is ", code)
        guess = input("[keypad]> ")
        guesses = 1

        # 输入密码，如果错了，重新输入，最多输入10次，都不对也用最后一次的guess
        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        # 如果输入对了，到the_bridge；如果错了，你挂了
        if guess == code:
            print(dedent("""
                The container cliks open and the seal breaks, letting
                gas out. You grab the neutron bomb and run as fast as
                you can to the bridge where you must place ti in the
                right spot.
            """))
            return 'the_bridge'

        else:
            print(dedent("""
                the lock buzzes one last time and then you hear a
                sickening melting sound as the mechanism is fused
                together. You decide to sit there, and finally the
                Gothons blow up the ship from their shop and you died.
            """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You burst onto the Bridge with thw netron destruct bomb
            under your arm and surprise 5Gothons who are trying to
            take control of the ship.Each of them has an even uglier
            clown costume than the last. They haven't pulled their
            weapons out yet,as they see the active bomb under your
            arm and don't want to set it off.
        """))

        action = input("> ")

        # 丢炸弹是死，安放炸弹才能进到escape_pod
        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw thw bomb at the group of Gothons
                and make a leap for the door.Right as you drop it a
                Gothons and make a leap for the door. Right as you drop it
                a Gothon shoots you right in the back killing you.as
                you die you see another Gothon frantically try to
                disarm the bomb . You knowing they will probably
                blow ip when it goes off.
            """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                You point your blaster at the bomb under your arm and
                the Gothons put their hands up and start to sweat.
                You inch bankward to the door,open it , and then
                carefully place the bomb on the floor,pointing your
                blaster at it.You then jump back through the door,
                punch the close button and blast the lock so the
                Gothons can't get out. Now that the bomb is placed
                you run to the escape pod to get off this tin can.
            """))
            
            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"
        
class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes.It seems
            like hardly any Gothons are on the ship explodes. It seems
            like hardly any Gothons are on the shop,so your run is clear
            of interference. You get to the chamber with the escape
            pods, and now need to pick one to take.Some of them could be
            damaged but you don't have time to look.
            There's 5 pods,which one do you take?
        """))

        # 随机生成一个可以好的逃生舱，选一个
        good_pod = randint(1,5)
        print("Good Pod is ", good_pod)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                You jump into pod {guess} and hit the eject button.
                The pod escapes out into the void of space, then
                implodes as the full ruptures,crushing your body into
                jam jelly.
            """))
            return 'death'

        else:
            print(dedent("""
                      You jump into pod {guess} and hit the eject button.
                      The pod easily slide out into space heading to the
                      planet below.As it flies to the plane,you look back
                      and see your ship implode then explode like a bright
                      star, taking out the Gothon ship at the time.  You won!
            """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# 初始化地图
a_map = Map('central_corridor')
# 运行游戏
a_game = Engine(a_map)
a_game.play()