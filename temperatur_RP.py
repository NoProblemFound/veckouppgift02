#################################   4 Temperaturomvandling   ##################################################
"""
Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
Version 1, exempel på output:

Skriv in en temperatur i grader Celsius: 22
Det blir 71.6 grader Fahrenheit.

Version 2: fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit.
Sedan räknar programmet om till den andra temperaturen.

Formel för konvertering mellan temperaturenheter:
C = (F - 32) / 1.8
F = 1.8 * C + 32

Version 3: om temperaturen som omvandlas är under 10°C ska programmet dessutom säga till användaren att ta
på sig vinterkläder. Och om temperaturen är minst 20°C ska det föreslå att man packar badkläder.

"""
#Version1
temp_c = float(input("Skriv in en temperatur i grader Celsius: "))
temp_f = temp_c * 1.8 + 32
print(f"Det blir {temp_f} grader Fahrenheit.")

#Version2
c_or_f = int(input("Vill du ange temperaturen i Celsius eller Fahrenheit? Skriv 1 för Celsius eller 2 för Fahrenheit "))
if c_or_f == 1:
    unit = "Celsius"
else:
    unit = "Fahrenheit"
temp = float(input(f"Skriv in en temperatur i {unit}: "))
if c_or_f == 1:
    temp_f = temp * 1.8 + 32
    temp_c = temp
    print(f"Det blir {temp_f} grader Fahrenheit.")

else:
    temp_c = (temp - 32) / 1.8
    temp_f = temp
    print(f"Det blir {temp_c} grader Celsius.")

if temp_f < 50.0 or temp_c < 10.0:
    print("Ta på dig vinterkläder!")
elif temp_f >= 68.0 or temp_c >= 20.0:
    print ("Packa badkläder!")