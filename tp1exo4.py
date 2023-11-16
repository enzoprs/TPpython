minutes_ecoulees = int(input("Entrez les miniutes écoulees depuis le debut du mois : "))

jour = 1 + minutes_ecoulees // (24 * 60)
reste_minutes = minutes_ecoulees % (24 * 60)
heure = reste_minutes // 60
minute = reste_minutes % 60

print(f"La date associée à {minutes_ecoulees} minutes écoulées est le {jour} jour, à {heure} heures et {minute} minutes.")
 
