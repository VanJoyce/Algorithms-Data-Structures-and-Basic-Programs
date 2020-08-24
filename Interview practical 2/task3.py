import task2

def read_text_file(name):
    """
    Reads a text file and converts it into a list of strings.

    :param name: Name of the text file
    :pre-condition: file must be a text file and must be in the same folder as this module. Filename must include the
                    file extension
    :post-condition: each line is an element in the list
    :return: list of strings associated to the file
    :complexity: best case and worst case are both O(n) where n is the number of lines in the file
    """
    list_strings = task2.ListADT()
    with open(name) as file:
        for line in file:
            list_strings.append(line)
    if not file.closed:
        file.close()
    for string in list_strings:
        string.strip()
    return list_strings