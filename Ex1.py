name = "toto"
prénom = "titi"
math = 12.5
info =  12.5
anglais = 12.5
promotion = 2023
moy = (math + info + anglais)/3
print(f"Type de 'name': {type(name)}")
print(f"Type de 'prénom': {type(prénom)}")
print(f"Type de 'anglais': {type(anglais)}")
print(f"Type de 'info': {type(info)}")
print(f"Type de 'promotion': {type(promotion)}")
print(f"Type de 'moy': {type(moy)}")
print (f" L'étudiant {name} {prénom} de la promotion {promotion} a une moyenne de {moy:.1f}")
