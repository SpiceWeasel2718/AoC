import json

f = open("input_files/AoC2015_day12_input.txt")
input_json = json.loads(f.read())
input_text = f.read()
f.close()


def add_up(obj):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return 0
    elif isinstance(obj, list):
        return sum([add_up(item) for item in obj])
    elif isinstance(obj, dict):
        if "red" in obj.keys() or "red" in obj.values():
            return 0
        else:
            return sum([add_up(item) for item in obj.values()])
    else:
        return 0


print(add_up(input_json))
