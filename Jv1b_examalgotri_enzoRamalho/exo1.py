#1/ Nous allons avoir besoin de permuter deux valeurs d’un tableau à partir de leurs indices.
#Écrire un programme permettant de permuter deux valeurs du tableau myTable.

myTable = [1,2,3,4]

stock = myTable[0]
myTable[0]=myTable[1]
myTable[1]=stock

print (myTable)