#2/ Lors d’une seule itération, l'algorithme du tri à bulles parcourt le tableau, et compare les
#éléments consécutifs. Lorsque deux éléments consécutifs ne sont pas dans l'ordre, ils sont
#échangés. Par conséquent, à l’issue d’une itération (et donc, d’un parcours entier du
#tableau), le plus grand élément est systématiquement déplacé en fin de tableau ; comme s’il
#s’agissait d’une bulle qui remonte à la surface.

tableau = [7,6,5,4,3,2,1]
cherche = tableau[0]
for i in range(len(tableau)):
    if (cherche < tableau [i]): 
        cherche = tableau [i]
      
tableau.insert(cherche, len(tableau))
tableau.pop(0)

print (tableau)