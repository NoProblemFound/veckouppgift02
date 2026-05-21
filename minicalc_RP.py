#################################   5 Miniräknare   ############################################
"""
1 Gör ett program som frågar användaren efter 3 tal. Sedan ska det räkna ut vad summan blir, och skriva ut på konsolen. (summa: tal1 + tal2 + tal3)

2 Programmet ska tala om vilket som är det största talet, utan att använda Python-funktionen max. Använd i stället if/elif/else. Fundera på om man kan lösa uppgiften på olika sätt.

3 Programmet ska tala om ifall två av talen är lika, eller alla tre är lika.

4 Programmet ska tala om vilket som är det mellersta talet. Observera att det bara finns ett mellersta tal om alla tre är olika, eller alla tre är lika. (Om talen skulle vara till exempel 2, 2, 5 så räknas inget av dem som mellerst i den här uppgiften.)

För att testa systematiskt kan du göra en tabell. Kör sedan programmet. Kontrollera att programmet skriver ut samma saker som du har skrivit in i tabellen. Vi kallar talen t1, t2 och t3.
Förslag på värden att testa med:  1 2 3, 1 3 2, 3 2 1, -1 -3 -1, 9 9 9, 32 32 16

"""
#1

tal1 = float (input ("Ange tal1: "))
tal2 = float (input ("Ange tal2: "))
tal3 = float (input ("Ange tal3: "))
sum = tal1 + tal2 + tal3

print (f"Summan: {tal1} + {tal2} + {tal3} = {sum}")

#2
if tal1 >= tal2 and tal1 >= tal3:
    print ("Maxvärdet är: ", tal1)
elif tal2 >= tal1 and tal2 >= tal3:
    print ("Maxvärdet är: ", tal2)
else:
    print ("Maxvärdet är: ", tal3)

#3
if tal1 == tal2 == tal3:
    print ("Alla tal är lika.")
elif tal1 == tal2:
    print ("Tal1 är lika med Tal2")
elif tal1 == tal3:
    print("Tal1 är lika med Tal3")
elif tal2 == tal3:
    print("Tal2 är lika med Tal3")

#4

if (tal1 < tal2 < tal3) or (tal3 < tal2 < tal1):
    print("Mellersta talet är: ", tal2)
elif (tal3 < tal1 < tal2) or (tal2 < tal1 < tal3):
    print("Mellersta talet är: ", tal1)
elif (tal1 < tal3 < tal2) or (tal2 < tal3 < tal1):
    print ("Mellersta talet är: ", tal3)
elif tal3 == tal2 == tal1:
    print("Mellersta talet är: ", tal3)

