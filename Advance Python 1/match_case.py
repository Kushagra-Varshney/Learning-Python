def match_example(value):
    match value:
        case 1:
            print("Value is 1")
        case 2:
            print("Value is 2")
        case 3:
            print("Value is 3")
        case _:
            print("Value is not 1, 2, or 3")

match_example(2)