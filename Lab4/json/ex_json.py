import json
idx = 33

print()
print("Interface Status \n" + "=" * 85)
print("DN" + " " * 50 + "Description" + " " * 10 + "Speed" + "   " + "MTU" + "\n" + "-" * 50 + "  " + "-" * 20 + " " + "-" * 6 + " " + "-" * 6 )

with open('sample-data.json', 'r') as file:
    data = json.load(file)
    for x in data["imdata"]:
        if x["l1PhysIf"]["attributes"]["id"] == "eth1/" + str(idx) and idx <= 35:
            dn = x["l1PhysIf"]["attributes"]["dn"]
            speed = x["l1PhysIf"]["attributes"]["speed"]
            mtu =  x["l1PhysIf"]["attributes"]["mtu"]
            print(dn + " " * 30 + speed + "  " + mtu)
        idx += 1