import hashlib

salt = "ihaygndm"
ind = 0

keys = []
testing = []

while len(keys) < 64:
    candidate = hashlib.md5((salt + str(ind)).encode("utf-8")).hexdigest()

    # Part 2
    for i in range(2016):
        candidate = hashlib.md5(candidate.encode("utf-8")).hexdigest()

    to_remove = []

    for test in testing:
        if 5*test[1] in candidate:
            keys.append(test)
            to_remove.append(test)

    for test in to_remove:
        testing.remove(test)

    for i in range(len(candidate) - 2):
        if candidate[i] == candidate[i+1] and candidate[i] == candidate[i+2]:
            testing.append([candidate, candidate[i], ind])
            break

    ind += 1

    if testing and ind - testing[0][2] > 1000:
        testing.pop(0)

keys.sort(key=lambda x: x[2])
print(keys[63])
