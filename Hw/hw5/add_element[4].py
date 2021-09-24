the_dict = {
    'one': [1, 2, 3],
    'two': [4, 5, 6],
    'three': [7, 8, 9]
}
list_name = input('enter the list name : ')
element = input('enter the element :')


def add_to_list_in_dict(the_dict, list_name, element):
    try:
        if the_dict[list_name]:
            l = the_dict[list_name]
            print("%s already has %d elements." % (list_name, len(l)))
        the_dict[list_name].append(element)
        print("Added %s to %s." % (element, list_name))

    except Exception as kr:
        print(f"{kr.__class__.__name__} the list name doesn't exist in dict, ")

    finally:
        the_dict[list_name] = []
        print("Created %s." % list_name)


add_to_list_in_dict(the_dict, list_name, element)
