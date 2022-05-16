from modules import art
sectorcount = 11
totalsectors = 121

if sectorcount == int(totalsectors*0.1):
    art.cd(22, '', "10% completed...", "reset", True)
elif sectorcount == int(totalsectors*0.2):
    art.cd(23, '', "20% completed...", "reset", True)
elif sectorcount == int(totalsectors*0.3):
    art.cd(24, '', "30% completed...", "reset", True)
elif sectorcount == int(totalsectors*0.4):
    art.cd(25, '', "40% completed...", "reset", True)
elif sectorcount == int(totalsectors*0.5):
    art.cd(26, '', "50% completed...", "reset", True)
elif sectorcount == int(totalsectors*0.6):
    art.cd(27, '', "60% completed...", "reset", True)
elif sectorcount == int(totalsectors*0.7):
    art.cd(28, '', "70% completed...", "reset", True)
elif sectorcount == int(totalsectors*0.8):
    art.cd(29, '', "80% completed...", "reset", True)
elif sectorcount == int(totalsectors*0.9):
    art.cd(30, '', "90% completed...", "reset", True)
elif sectorcount == int(totalsectors):
    art.cd(31, '', "100% completed...", "reset", True)
