n = int(input())
godofor = {
    "name": '',
    "power": 0,
    "godsKilled": 0,
    "timesDied": 0
}

for _ in range(n):
    entry = input().split()
    candidate = {
        "name": entry[0],
        "power": int(entry[1]),
        "godsKilled": int(entry[2]),
        "timesDied": int(entry[3])
    }
    if candidate["power"] > godofor["power"] or (candidate["power"] == godofor["power"] and candidate["godsKilled"] > godofor["godsKilled"]) or (candidate["power"] == godofor["power"] and candidate["godsKilled"] == godofor["godsKilled"] and candidate["timesDied"] < godofor["timesDied"]) or (candidate["power"] == godofor["power"] and candidate["godsKilled"] == godofor["godsKilled"] and candidate["timesDied"] == godofor["timesDied"] and sorted([godofor["name"], candidate["name"]])[0] == candidate["name"]):
        godofor = candidate

print(godofor["name"])