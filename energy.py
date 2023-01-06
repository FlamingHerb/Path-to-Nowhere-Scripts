#=====================================================================================
# TODO: REWRITE THE FUCKING THING
# TODO: ADD MORE COMMENTS

import sys

# These two mammoth sized 2D arrays the static values of each increment from one level to another. Due to the nature of Python, the 
# following has been zero-indexed for convenience.
discoins = [
    # B-Class
    [0, 0, 100, 250, 450, 650, 950, 1300, 1700, 2200, 2750, 3400, 4150, 5000, 5950, 7000, 8200, 9500, 10950, 12550, 14250, 16150, 18150, 20350, 22700, 25200, 27900, 30750, 33800, 37000, 40400, 44000, 47800, 51800, 56000, 60400, 65000, 69800, 74800, 80000, 85400, 90800, 96250, 101700, 107200, 112700, 118200, 123750, 129350, 134950, 140600, 146300, 152000, 157800, 163600, 169500, 175400, 181400, 187450, 193550, 199750, 206000, 212350, 218750, 225250, 231850, 238550, 245350, 252250, 259250, 266350, 273700, 281550, 290050, 299400, 309800, 321400, 334400, 349000, 365400, 383800, 404350, 427250, 452750, 481000, 512200, 546600, 584350, 625650, 670750, 719850],
    # A-Class
    [0, 0, 150, 350, 600, 850, 1200, 1650, 2150, 2750, 3450, 4250, 5200, 6250, 7450, 8750, 10250, 11900, 13700, 15700, 17850, 20200, 22700, 25450, 28400, 31550, 34900, 38450, 42250, 46250, 50500, 55000, 59750, 64750, 70000, 75500, 81250, 87250, 93500, 100000, 106750, 113500, 120300, 127100, 133950, 140850, 147800, 154750, 161750, 168750, 175800, 182900, 190050, 197300, 204550, 211900, 219300, 226800, 234350, 242000, 249750, 257550, 265500, 273500, 281650, 289900, 298250, 306750, 315350, 324100, 332950, 342150, 351950, 362600, 374300, 387300, 401800, 418050, 436300, 456800, 479800, 505500, 534150, 566000, 601300, 640300, 683300, 730500, 782150, 838550, 899900],
    # S-Class
    [0, 0, 200, 450, 750, 1100, 1550, 2100, 2750, 3500, 4350, 5350, 6500, 7800, 9250, 10850, 12650, 14650, 16850, 19250, 21850, 24700, 27750, 31050, 34600, 38400, 42450, 46750, 51350, 56200, 61350, 66750, 72450, 78450, 84750, 91350, 98250, 105450, 112950, 120800, 128950, 137100, 145300, 153500, 161750, 170000, 178300, 186650, 195050, 203500, 212000, 220550, 229150, 237850, 246600, 255450, 264350, 273350, 282450, 291650, 300950, 310350, 319900, 329550, 339350, 349250, 359300, 369500, 379850, 390350, 401000, 412050, 423850, 436650, 450700, 466300, 483750, 503300, 525250, 549900, 577500, 608350, 642750, 681000, 723400, 770250, 821850, 878500, 940500, 1008200, 1081850]
    ]
mania = [
    # B-Class
    [0, 0, 400, 900, 1500, 2200, 3000, 3950, 5050, 6250, 7650, 9200, 10950, 12900, 15050, 17450, 20050, 22950, 26100, 29500, 33200, 37550, 42100, 46900, 51900, 57150, 62650, 68400, 74400, 80650, 87150, 93900, 100900, 108200, 115800, 123650, 131800, 140250, 149000, 158100, 167500, 177050, 186750, 196650, 206700, 216900, 227300, 237900, 248700, 259700, 270900, 282350, 294050, 305950, 318100, 330500, 343150, 356050, 369250, 382700, 396400, 410400, 424700, 439300, 454200, 469400, 484950, 500850, 517050, 533600, 550500, 568200, 587200, 607950, 630900, 656500, 685300, 717700, 754200, 795200, 841200, 892700, 950150, 1014050, 1084800, 1162900, 1248800, 1343000, 1445950, 1558100, 1679900],
    # A-Class
    [0, 0, 500, 1100, 1850, 2700, 3700, 4900, 6250, 7750, 9500, 11450, 13650, 16100, 18800, 21800, 25050, 28650, 32600, 36850, 41500, 46950, 52650, 58650, 64900, 71450, 78350, 85550, 93050, 100850, 108950, 117400, 126150, 135250, 144750, 154550, 164750, 175300, 186250, 197600, 209350, 221300, 233450, 245800, 258350, 271100, 284100, 297350, 310850, 324600, 338600, 352900, 367500, 382400, 397600, 413100, 428900, 445050, 461550, 478350, 495500, 513000, 530900, 549150, 567800, 586800, 606250, 626100, 646350, 667050, 688150, 710300, 734050, 760000, 788700, 820700, 856700, 897200, 942800, 994050, 1051550, 1115950, 1187750, 1267600, 1356050, 1453650, 1561050, 1678800, 1807500, 1947700, 2099950],
    # S-Class
    [0, 0, 600, 1350, 2250, 3300, 4550, 6000, 7650, 9500, 11600, 13950, 16600, 19550, 22800, 26400, 30350, 34700, 39450, 44600, 50200, 56750, 63600, 70800, 78350, 86250, 94550, 103200, 112200, 121600, 131350, 141500, 152050, 163000, 174400, 186200, 198450, 211150, 224300, 237950, 252050, 266400, 281000, 295850, 310950, 326300, 341950, 357900, 373850, 390400, 407250, 424450, 442000, 459900, 478150, 496750, 515750, 535150, 554950, 575150, 595750, 616800, 638300, 660250, 682650, 705500, 728850, 752700, 777050, 801900, 827250, 853850, 882350, 913500, 947950, 986400, 1029600, 1078200, 1132950, 1194500, 1263550, 1340850, 1427050, 1522900, 1629050, 1746200, 1875100, 2016400, 2170850, 2339100, 2521850]
]

# Range values for the low, mid and high ends of the raids. The middle is more important due to the bell curve imposed by game. The rest are
# treated as control values.
raidrange = [9000, 11000, 13000]

# Compared to whatever mammalian nightmare discoins and mania are, the DCC phases are actually static and multiplied given the rank of the 
# Sinner.
dcc_phases = [24000, 80000, 350000]

# If DisCoins
distemp = 0
maniatemp = 0

#===========================
# INITIALIZATION ENDS HERE
#===========================

# TODO: Rewrite argument catcher
# COMMAND:
# energy(initlevel, estlevel, class, refreshes, phasecost) phasecost = [y,n]
if len(sys.argv) != 6:
    print("Please give the following arguments!")
    quit()
if sys.argv[5].lower() not in ["y", "n"]:
    print("Please say if you want to include phase costs when reaching certain levels (20,40,70)")
    quit()
if not (-1 < int(sys.argv[4]) < 11):
    print(f"Refreshes must be up to 0 - 10. Input = {sys.argv[4]}") 
    quit()
if sys.argv[3].lower() not in ["s", "a", "b"]:
    print("Please specify Sinner Class: S-Rank(s), A-Rank(a) or B-Rank (b)")
    quit()
if isinstance(sys.argv[1], int) or isinstance(sys.argv[2], int):
    print("Please input a non-negative integer!")
    quit()
if sys.argv[1] >= sys.argv[2]:
    print("Initial level greater than expected level!")
    quit()


epd = 360 + int(sys.argv[4]) * 100      # Energy per day
initlevel = int(sys.argv[1])            # Initial Level
estlevel = int(sys.argv[2])             # Estimated Level
rank = sys.argv[3].lower()              # Sinner Class


print(f"Sinner rank:            {sys.argv[3].upper()}")
print(f"Initial Level:          {sys.argv[1]}")
print(f"Estimated Level:        {sys.argv[2]}")
if sys.argv[5].upper() == "Y":
    print(f"Phase Cost Inclusive?   YES (Adds cost to breach to next phase)")
else:
    print(f"Phase Cost Inclusive?   NO (Only adds cost after breaching phase)")
print(f"Refreshes per Day:      {sys.argv[4]}")
print(f"Energy Per Day:         {epd}")
print("=========================")


# Initial conditions
# If Sinner Rank is B
if sys.argv[3].lower() == "b":
    distemp = discoins[0][estlevel] - discoins[0][initlevel] 
    maniatemp = mania[0][estlevel] - mania[0][initlevel] 
if sys.argv[3].lower() == "a":
    distemp = discoins[1][estlevel] - discoins[1][initlevel] 
    maniatemp = mania[1][estlevel] - mania[1][initlevel] 
if sys.argv[3].lower() == "s":
    distemp = discoins[2][estlevel] - discoins[2][initlevel] 
    maniatemp = mania[2][estlevel] - mania[2][initlevel] 

# Phase additions (and readability)
# if phasecost = y, then will add phase cost if specified estimated level is exactly the phase up level.
if sys.argv[5].lower() == "y":
    if estlevel >= 20 and initlevel < 20:
        distemp += dcc_phases[0] if rank == "b" else dcc_phases[0] + 6000 if rank == "a" else dcc_phases[0] + 12000

    if estlevel >= 40 and initlevel < 40:
        distemp += dcc_phases[1] if rank == "b" else dcc_phases[1] + 20000 if rank == "a" else dcc_phases[1] + 40000

    if estlevel >= 70 and initlevel < 70:
        distemp += dcc_phases[2] if rank == "b" else dcc_phases[2] + 130000 if rank == "a" else dcc_phases[2] + 260000

# if phasecost = n, then will only add phase cost AFTER breaching the phase level
else:
    if estlevel > 20 and initlevel < 20:
        distemp += dcc_phases[0] if rank == "b" else dcc_phases[0] + 6000 if rank == "a" else dcc_phases[0] + 12000

    if estlevel > 40 and initlevel < 40:
        distemp += dcc_phases[1] if rank == "b" else dcc_phases[1] + 20000 if rank == "a" else dcc_phases[1] + 40000

    if estlevel > 70 and initlevel < 70:
        distemp += dcc_phases[2] if rank == "b" else dcc_phases[2] + 130000 if rank == "a" else dcc_phases[2] + 260000



# energy = [discoin, mania]
energy = []
for i in raidrange:
    energy.append([(distemp / i) * 30, (maniatemp / i) * 30])



print(f"RESULTS")
print(f"DISCOINS:   {distemp}")
print(f"    Low Mode:    {round(energy[0][0], 2)} Energy | {round(energy[0][0] / epd, 2)} Days")
print(f"    Average:     {round(energy[1][0], 2)} Energy | {round(energy[1][0] / epd, 2)} Days")
print(f"    High Mode:   {round(energy[2][0], 2)} Energy | {round(energy[2][0] / epd, 2)} Days")
print(f"MANIA:      {maniatemp}")
print(f"    Low Mode:    {round(energy[0][1], 2)} Energy | {round(energy[0][1] / epd, 2)} Days")
print(f"    Average:     {round(energy[1][1], 2)} Energy | {round(energy[1][1] / epd, 2)} Days")
print(f"    High Mode:   {round(energy[2][1], 2)} Energy | {round(energy[2][1] / epd, 2)} Days")