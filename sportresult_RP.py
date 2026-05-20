#################################   3 Sportresultat   ##################################################
"""
Tottenham spelar mot Liverpool i Champions League. Skriv ett program som frågar användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.
Exempel på output:

Matchen är över, nu ska vi räkna ut resultatet!
Hur många mål gjorde Tottenham? 2
Hur många mål gjorde Liverpool? 1
Tottenham vann!

Version 2: programmet ska tala om ifall det blev oavgjort.

Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
Tottenham vann med 1 mål!

Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) behöver du minst tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.
"""

liverpool = int(input("Hur många mål gjorde Liverpool: "))
tottenham = int(input("Hur många mål gjorde Tottenham: "))

if liverpool < tottenham:
    print("Tottenham vann!")
elif liverpool > tottenham:
    print("Liverpool vann!")
else:
    print("Matchen blev oavgjort.")
