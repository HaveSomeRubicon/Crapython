class Interpret():
    def __init__(self, path) -> None:
        self.path = path

    def interpret(self):
        with open(self.path) as crpy_file:
            print(crpy_file.readlines())


coompiler = Interpret('main.crpy')
coompiler.interpret()
