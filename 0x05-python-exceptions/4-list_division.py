#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists"""

    i = 0
    new_list = []
    output = 0
    for i in range(0, list_length):
        try:
            result = (my_list_1[i] / my_list_2[i])
            except TypeError:
                output = 0
                print("wrong type")
                except ZeroDivisionError:
                    output = 0
                    print("division by 0")
                    except IndexError:
                        output = 0
                        print("out of range")
                    finally:
                        new_list.append(result)
                        return new_list
