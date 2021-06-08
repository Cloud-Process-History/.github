
from lambda_code.someclass import SomeClass


def lambda_handler(event, context):

    some_class = SomeClass()
    hello = some_class.say_hello()
    return hello