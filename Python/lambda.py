people = [
    {"name":"harry", "house":"Gryffindor"},
    {"name":"Cho", "house":"Ravenclaw"},
    {"name":"draco", "house":"Slytherin"}
]
people.sort(key=lambda person: person["name"])
print(people)