import os

for f in os.listdir("input"):
  os.rename("input/" + f, "input/" + f + ".txt")
for f in os.listdir("output"):
  os.rename("output/" + f, "output/" + f + ".txt")
