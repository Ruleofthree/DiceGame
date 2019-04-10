import cmd
import charCreation
import charInfo
import charFeats

class Character(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        print("Welcome to Character Creation. To begin, type 'start'. To exit, type 'quit'. For a list of commands and"
              " their descriptions, type 'help'")

    def do_start(self, args):
        """Use this command to create a new character. Note you can only have one character per account. Feats are selected using the 'feats' option"""
        charStats = charCreation.basics()
        charMods = charCreation.abilities(charStats)
        charCreation.save(charStats, charMods)

    def do_listfeatsstrength(self, args):
        charFeats.featlist()

    def do_viewchar(self, args):
        """Use this command to get a list of your character statics"""
        charInfo.charSheet()

    def do_quit(self, args):
        """Leaves character Creation"""
        print("Closing Character Creation.")
        return True

if __name__ == "__main__":
    character = Character()
    character.cmdloop()