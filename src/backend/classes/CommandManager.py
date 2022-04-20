class CommandManager:
    discord_commands = {}
    
    # kwargs is implictly defined as a dictionary
    # (a='a', b='b', ... z='z')
    def __init__(self, dictionaryOfDatabaseItems):
        self.discord_commands = dictionaryOfDatabaseItems
            
    @property
    def discord_commands(self):
        return self._discord_commands

    @discord_commands.setter    
    def discord_commands(self, dictionary_of_discord_commands):
        if not isinstance(dictionary_of_discord_commands, dict):
            raise TypeError('Invalid argument for dictionary of discord commands. Must be a dictionary.')
        self._discord_commands = dictionary_of_discord_commands