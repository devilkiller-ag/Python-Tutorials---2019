#ditionary is nothing but key value pairs
d1  = {}
print(type(d1))
d2 = {"Ashmit":"Egg", "Prashant":"Chhicken", "Nancy":"Roti", "Ritz":"Fish", "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d2["Damru"] = "Junk Food"
d2["Akanksha"] = "Saag"
d2[420] = "fish"
print(d2)
print(d2["Ashmit"])
print(d2["Shubham"]["B"])
#Some functions of dict
del d2[420]
print(d2)
d3 = d2.copy()
print(d2.get("Ashmit"))
d2.update({"Nannu":"Dimaag"})
print(d2)
print(d2.keys())
print(d2.items())