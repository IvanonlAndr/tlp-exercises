arr_start = ["fox","goose","corn"]
arr_end = []
arr_boat = []
MAX_LENGTH = 1

# arr_start.pop(0)
# arr_boat.append("farmer")
# print(arr_start)
# print(arr_boat)

# arr_start.pop(0)
# arr_boat.append("fox")
# print(arr_start)
# print(arr_boat)

# arr_boat.pop(1)
# arr_end.append("fox")
# print(arr_boat)
# print(arr_end)

# if "fox" in arr_start and "goose" in arr_start:
#     print("lost")
# elif "goose" in arr_start and "corn" in arr_start:
#     print("lost")


def check_shore():
    if len(arr_start) == 2 and "fox" in arr_start and "goose" in arr_start:
        return False
    elif len(arr_start) == 2 and "goose" in arr_start and "corn" in arr_start:
        return False
    if len(arr_end) == 2 and "fox" in arr_end and "goose" in arr_end:
        return False
    elif len(arr_end) == 2 and "goose" in arr_end and "corn" in arr_end:
        return False
    else:
        print("nothing")
        return True

def add_to_boat(item: str):
    check_shore()
    if item in arr_start:
        arr_start.remove(item)
        arr_boat.append(item)
        print(f"boat '{arr_boat}' ")
            
    else:
        print("no such item on the shore")
        return

def add_to_end(item: str):
    if check_shore():
            arr_boat.remove(item)
            arr_end.append(item)
            print(f"end '{arr_end}' ")
    else:
        print("lost")
        return

def bring_back(item: str):
    if item in arr_end:
        arr_end.remove(item)
        arr_boat.append(item)
        print(f"boat '{arr_boat}' ")
    else:
        print("no such item on the shore")
        return
    if check_shore():
        arr_boat.remove(item)
        arr_start.append(item)
        print(f"start '{arr_start}' ")
    else:
      print("lost")
      return

#win
print("win")
add_to_boat("goose")
add_to_end("goose")
add_to_boat("fox")
add_to_end("fox")
bring_back("goose")
add_to_boat("corn")
add_to_end("corn")
add_to_boat("goose")
add_to_end("goose")

#lose
# print("lose")
# add_to_boat("goose")
# add_to_end("goose")
# add_to_boat("fox")
# add_to_end("fox")
# add_to_boat("corn")
# add_to_end("corn")
# add_to_boat("goose")
# add_to_end("goose")

if len(arr_end) == 3:
    print("success")