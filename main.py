import time
class Interpret():
    def __init__(self, path) -> None:
        self.path = path

    def interpret(self):
        with open(self.path) as file:
            file_lines = [line.replace('\n', '') for line in file.readlines()]
        file_lines = [line.split(' ') for line in file_lines]

        
                    

coompiler = Interpret('main.crpy')
coompiler.interpret()
