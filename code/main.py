from example_class import ExampleClass

def hello_from_example_class():
    '''
    this function says hello from the example class

    Note
    ----
    The absolute import pattern, this ensures any process can call 
    this function from any location on the computer and the path to
    our import is still accurate. Avoid relative imports.

    '''
    ec = ExampleClass(1,2,3)
    print(ec.print_hello_world("Tayo"))

#hello_from_example_class()