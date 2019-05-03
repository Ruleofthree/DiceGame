import cmd
import charCreation
import charFeats
import charWrite
import gameCombat

"""
The intended scope of this game is to eventually be placed within a chatroom. I intend to start with discord, as making
bots for discord is HEAVILY documented, and therefore should be easy to get started in listening to a chatroom for
commands, implementing those commands in this program, and spitting out desired results to chatroom.

I believed the cmd library to be of best use for this, but am not uncertain as to how it will work once I manage to get
this live in a discord chatroom. For testing purposes, and trying to run this 'single player' however, this seems to be
working fine.
"""

class Hub(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Hub > "
        print("Welcome to the Hub. From here, you can create your first character and view the character sheet with the"
              " 'char' command, or review and select feats with the 'feats' command. For more information on both,"
              " please type help <command>.")

    def do_fight(self, args):
        """
        This command will initiate combat between two opponents.
        """
        combat = gameCombat.Combat()
        combat.initiative()

    def  do_char(self, args):
        """
        this command will give you access to the 'create' command, to create your character for this account. It
        will also give you access to the 'viewchar' command, which will provide you with a basic character sheet
        containing all needed information
        """
        character = Character()
        character.cmdloop()

    def do_feats(self, args):
        """
        this command will give you access to the commands to look at all feats in the game and their descriptions
        and any required qualifications that are needed before taking the feat. Feats are divided into three categories:
        Strength, Dexterity, and Constitution.
        """
        feats = Feats()
        feats.cmdloop()

    def do_quit(self, args):
        """Exits the bot"""
        print("Closing closing the bot.")
        return True

class Character(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Character > "
        print("Welcome to Character Creation. To begin, type 'create'. To exit, type 'quit'. For a list of commands and"
              " their descriptions, type 'help'")

    def do_create(self, args):
        """
        Use this command to create a new character. Note you can only have one character per account. Feats are
        selected using the 'feats' option
        """
        charBasics = charCreation.Character()
        basics = charBasics.basics()
        abilities = charBasics.abilities(basics)
        charBasics.save(basics, abilities)

    # When you run this, it immediately asks for you to type in the character sheet you want to view. I REALLY want to
    # find a way to do this all in one execution, such as 'viewchar irixis'. I believe using an 'args' value is the
    # key to the answer, but am unsure from how to do the rest.
    def do_viewchar(self, args):
        """
        Use this command to get a list of your character statics
        """
        module = charWrite.SaveModule()
        module.charSheet()

    def do_quit(self, args):
        """
        Leaves character Creation
        """
        print("Closing Character Creation.")
        return True

class Feats(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Feats > "
        print("Welcome to Feat Selection. Here you can view the lists of feats for any given category: Strength"
              " Dexterity, Constitution, and. Simply type 'getfeat' to start the process.")

    def do_getfeat(self,args,):
        """Select your feats with this option"""
        module = charWrite.SaveModule()
        info = module.save()
        getFeats = charFeats.Feats()
        getFeats.playerFeats(info)

    def do_quit(self, args):
        """Leaves Feat Selection"""
        print("Closing Feat Selection.")
        return True

if __name__ == "__main__":
    hub = Hub()
    hub.cmdloop()