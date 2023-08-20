class MacroCommand:
    """
    A command that executes a list of commands
    A closure can be used to hold the internal state of a function between calls.
    """

    def __init__(self, commands):
        # Building a list from the commands arguments ensures that it is iterable and keeps a local copy of the command references in each MacroCommand instance.
        self.commands = list(commands)

    def __call__(self):
        # When an instance of MacroCommand is invoked, each command in self.commands is called in sequence
        for command in self.commands:
            command()
