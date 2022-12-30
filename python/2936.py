mealsSize = {
    "curupira" : 300,
    "boitata" : 1500,
    "boto" : 600,
    "mapinguari" : 1000,
    "iara" : 150
}

cx = int(input())
boix = int(input())
botox = int(input())
mx = int(input())
ix = int(input())

sum = (cx * mealsSize["curupira"]) + (boix * mealsSize["boitata"]) + (botox * mealsSize["boto"]) + (mx * mealsSize["mapinguari"]) + (ix * mealsSize["iara"]) + 225

print(sum)