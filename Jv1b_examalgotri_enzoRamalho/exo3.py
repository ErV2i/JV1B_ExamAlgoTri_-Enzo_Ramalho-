#3/ Écrire un programme implémentant le tri à bulles complet, permettant de trier totalement
#un tableau grâce à l’algorithme du tri à bulles. On pourra se servir de la permutation, ainsi
#que de la réponse à la question précédente.

tableau = [1,8,5,6,9,4]
trie = False
cherche = tableau[0]
while ( trie == True ) :
    for i in range (len(tableau)):
        if (cherche < tableau [i]): 
        cherche = tableau [i]
        tableau.insert(cherche, len(tableau))
        tableau.pop(0)
    else:
        trie = True


print (tableau)

#ou

tableau.sort()

print (tableau)
