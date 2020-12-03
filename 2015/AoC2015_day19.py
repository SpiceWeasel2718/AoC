data = [
    {
        "filename": "input_files/AoC2015_day19_input.txt",
        "string": "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
     },
    {
        "filename": "input_files/AoC2015_day19_input_alt1.txt",
        "string": "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"
     },
    {
        "filename": "input_files/AoC2015_day19_input_alt2.txt",
        "string": "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"
     },
    {
        "filename": "input_files/AoC2015_day19_input_alt3.txt",
        "string": "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"
     },
    {
        "filename": "input_files/AoC2015_day19_input_alt4.txt",
        "string": "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"
     },
    {
        "filename": "input_files/AoC2015_day19_input_alt5.txt",
        "string": "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
     }
]

ind = 0

f = open(data[0]["filename"])
input_text = f.read().split("\n")
f.close()

string = data[ind]["string"]

rep_rules = {}
rev_rules = {}

for line in input_text:
    rep = line.split(" => ")

    rev_rules.update({rep[1]: rep[0]})

    if rep[0] not in rep_rules.keys():
        rep_rules.update({rep[0]: []})
    rep_rules[rep[0]].append(rep[1])

"""
Part 1

replacements = []
start = ""

while len(string) > 0:
    match = False
    for atom in rep_rules.keys():
        if string.startswith(atom):
            match = True
            string = string[len(atom):]
            for rep in rep_rules[atom]:
                replacements.append(start + rep + string)
            start += atom
            break

    if not match:
        start += string[0]
        string = string[1:]

replacements = list(dict.fromkeys(replacements))

print(len(replacements))
"""

products = list(rev_rules.keys())


def separate(string):
    result = []

    while len(string) > 1:
        if string[1].islower():
            result.append(string[0:2])
            string = string[2:]
        else:
            result.append(string[0:1])
            string = string[1:]

    if len(string) > 0:
        result.append(string)

    return result


starters = []
enders = []

for mol in rev_rules.keys():
    temp = separate(mol)
    if temp[0] not in starters:
        starters.append(temp[0])
    if temp[-1] not in enders:
        enders.append(temp[-1])

joints = []

for ender in enders:
    for starter in starters:
        joints.append(ender + starter)

for mol in rev_rules.keys():
    for j in joints:
        if j in mol:
            joints.remove(j)


def chunks(string):
    sep_string = separate(string)
    result = [""]
    ind = 0

    for i in range(len(sep_string) - 1):
        result[ind] += sep_string[i]
        if sep_string[i] + sep_string[i + 1] in joints:
            ind += 1
            result.append("")
    result[ind] += sep_string[-1]

    return result


def reduce(in_dict):
    result = [in_dict]
    finished = False

    while not finished:
        finished = True
        for i in range(len(result)):
            comp = result.pop(0)
            comp_str = comp["string"]
            match = False
            for product in products:
                ind = comp_str.find(product)
                while ind > -1:
                    rep = {"string": comp_str[0:ind] + rev_rules[product] + comp_str[ind + len(product):],
                           "count": comp["count"] + 1}
                    if rep not in result:
                        result.append(rep)
                    match = True
                    finished = False
                    ind = comp_str.find(product, ind+1)
            if not match:
                result.append(comp)

    return result


def split_and_reduce(in_dict):
    results = [{"string": "", "count": in_dict["count"]}]

    for chunk in chunks(in_dict["string"]):
        reductions = reduce({"string": chunk, "count": 0})
        for i in range(len(results)):
            result = results.pop(0)
            for reduction in reductions:
                results.append({"string": result["string"] + reduction["string"],
                                "count": result["count"] + reduction["count"]})

    return results


stuff = [{"string": string, "count": 0}]
done = False

print(stuff[0])

while not done:
    print(" ")
    for i in range(len(stuff)):
        for r in split_and_reduce(stuff.pop(0)):
            if r not in stuff:
                stuff.append(r)

    for elem in stuff:
        print(elem)
        if elem["string"] == "e":
            done = True







