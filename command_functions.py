# Command function module
class Command:
    def __init__(self, primary_call, desc="", func=None):
        self.primary_keyword = primary_call
        self.command_desc = desc
        self.operation = func

    def __contains__(self, keyword):
        if keyword.lower() in self.keywords or keyword.lower() == self.primary_keyword:
            return True
        else:
            return False

    def __eq__(self, cmd):
        if cmd == self.primary_keyword:
            return True
        else:
            return False

    def __str__(self):
        statement = "\nPrimary keyword : " + self.primary_keyword
        statement += "\nDescription : " + self.command_desc + "\n"
        return statement

    def addOperation(self, func):
        self.operation = func

    def run(self, *args):
        if self.operation is not None:
            try:
                self.operation(*args)
                pass
            except TypeError as e:
                print(e)
                print('ERROR: Arguments are not matched in the function!\n')

        else:
            raise ValueError('ERROR 501: No operation defined for this function!')
