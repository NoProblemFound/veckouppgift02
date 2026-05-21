#################################   2 Balder   ##################################################
"""
För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!

Fråga användaren hur lång man är (i cm)
Skriv ut antingen "Du får åka!" eller "Du får inte åka"

Skriv in följande värden för att testa att ditt program gjort rätt:
121 cm (får inte åka)
130 cm (får åka)
155 cm (får åka)

Diskutera:
Varför just tre värden? För att testa 3 olika vilkor, < > =
Varför dessa värden? 121 för att testa <, 130 för att testa =, 135 för att testa >
Skulle det vara bra att lägga till testvärdet 129 cm? Nej, fyller inget syfte

"""

length = float(input("Hur lång är du? Ange din längd i CM: "))


if length < 130.0:
    print("Du får inte åka.")
else:
    print("Du får åka.")

