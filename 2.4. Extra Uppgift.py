Mile = float(input('skriv in antalet miles: ')) #här skriver man in antalet miles.
Gallon = float(input('skriv in antalet gallons: '))#här skriver man in antalet gallons.
Km = Mile * 1.609 #här sätter man värdet för Km, antalet miles som skrevs in * 1.609
L = Gallon * 3.785 #här sätter man värdet för liter, antalet gallons som skrevs in * 3.785

print(f'Antalet km:{Km:.3f} \nLiter {L:.3f}') #här får man resultatet av km och liter som har en F string som bara tillåter resultat värdet att visa 3 decimaler max.