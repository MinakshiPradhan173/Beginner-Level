# Initial List
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

# 1. Calculate the number of members
members = len(justice_league)
print("Number of members in the Justice League:", members)

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Justice League after adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Justice League after making Wonder Woman the leader:", justice_league)

# 4. Move Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
aqua = justice_league.index("Aquaman")
justice_league.insert(aqua + 1, "Green Lantern")
print("Justice League after moving Green Lantern between Aquaman and Flash:", justice_league)

# 5. Replace the list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League:", justice_league)

# 6. Sort alphabetically and determine the new leader
justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New leader of the Justice League:", justice_league[0])