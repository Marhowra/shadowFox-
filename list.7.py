justice_league= ["superman","batman","wonderwomen","flash","aquaman","greenlantern"]
print(justice_league)

  # number of justice_league member

print("Total number of member;",len(justice_league))

#  add batgirl and knightwing in justice league

justice_league.extend(["batgirl","nightwing"])
print(justice_league)

#  move move superman to wonderwomen

justice_league[0],justice_league[2]=justice_league[2],justice_league[0]
print(justice_league)

#move superman between aquaman and flash
justice_league.remove("superman")
justice_league.insert(3,"superman")
print(justice_league)

# replace with new item
list2=["cyborg","shazam","hawkgirl","martian manuthar","green arrow"]
justice_league[:] = list2
print(justice_league)

#sort member according to alphabet and choose leader of 0 index
justice_league.sort()
print(justice_league)
leader=justice_league[0]
print(leader)