

def hello_world():
    """
    Just print a message

    :return: none
    """

    print("hello world")


class HelloWorld(object):
    """
    This class only prints a simple message

    """

    def __init__(self):

        # Just printing a message

        print("Hello world")

    def this_is_a_method(self, argument):
        """
        It just returns the argument

        :param argument: the object you want returned
        :return: the argument object
        """

        return argument

