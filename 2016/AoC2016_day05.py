import hashlib

door_id = "abbhdwsy"

password = "________"
result = ""
ind = 0

while "_" in password:
    result = hashlib.md5((door_id + str(ind)).encode("utf-8")).hexdigest()
    if result.startswith("00000") and result[5].isnumeric():
        print(result)
        pos = int(result[5])
        if pos in range(8) and password[pos] == "_":
            password = password[:pos] + result[6] + password[pos+1:]
            print(password)
    ind += 1


