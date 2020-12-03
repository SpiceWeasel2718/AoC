import hashlib

count = 0
result = ""

while not result.startswith("000000"):
    count += 1
    result = hashlib.md5(("bgvyzdsv"+str(count)).encode("utf-8")).hexdigest()

print(count)
