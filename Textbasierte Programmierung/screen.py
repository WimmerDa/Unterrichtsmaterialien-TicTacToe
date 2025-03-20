import turtle

#Screen class: There can only be one instance of the class screen
class Screen:
    instance = None

    @staticmethod
    def getInstance():
        if Screen.instance is None:
            Screen()
        return Screen.instance

    def __init__(self):
        if Screen.instance is not None:
            raise Exception("Singleton exists already!")
        else:
            Screen.instance = turtle.Screen()