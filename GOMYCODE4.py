#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Écrivez une fonction Python pour trouver le maximum de trois nombres.

#par exemple, le maximum de ces trois nombres 20, 35, 19 est 35

def comparaison():

    a = int(input("Entrer le premier nombre "))
    b = int(input("Entrer le deuxieme nombre "))
    c = int(input("Entrer le troisieme nombre "))

    if (a>b)and(b>c):
        print('le maximum de ces trois nombres:',a)
    elif (b>a)and(a>c):
        print('le maximum de ces trois nombres:',b)
    else:
        print('le maximum de ces trois nombres:',c)


# In[139]:


comparaison()


# In[13]:


#Écrivez une fonction calcul() telle qu'elle puisse accepter deux variables et en calculer l'addition et la soustraction. Et aussi, il doit renvoyer à la fois l'addition et la soustraction dans un seul appel de retour

#Par example:

#calcul(40, 10) devrait produire 50, 30

def calcul(a,b):
   print(a+b,a-b)


# In[14]:


calcul(50,60)


# In[109]:


# Ecrire une fonction qui additionne les éléments d'une liste d'entiers.
# Ecrire une fonction qui multiplie les éléments d'une liste d'entiers.
# Utilisez les deux fonctions pour additionner les éléments dont la position est un nombre pair (0,2,4…) et multiplier le reste.

list_1=[6,7,2,4,5,8,9,1]
list_2=[12,7,4,5,2,7,2,5]
def addition(a):
   
    return sum(a)
    
def multi(a):
    n=1
    for i in a :
        
        n=n*i
    return(n)
def somme(a) :
    x=[]
    z=[]
    for i in range (0,len(a),2) :
        
            x.append(a[i])
            z.append(a[i+1])  
    
    return addition(x), multi(z)
            
        
    
        
        


# In[110]:



multi(list_1)
multi(list_2)


# In[111]:


addition(list_1)


# In[112]:


addition(list_2)


# In[113]:


somme(list_1)


# In[114]:


somme(list_2)


# In[137]:


# un programme Python qui accepte une séquence de mots séparés par des tirets en entrée et imprime les mots dans une séquence
#séparée par des tirets après les avoir triés par ordre alphabétique.
#Exemples d'items : vert-rouge-jaune-noir-blanc
#Résultat attendu : noir-vert-rouge-blanc-jaune
    
D1=input('tapez une list:')
x=D1.split("-")
x.sort()


# In[138]:


print(x)


# In[140]:


'''Question 5 

Écrivez une fonction qui calcule et imprime la valeur selon la formule donnée :
Q = Racine carrée de [(2 * C * D)/H] Voici les valeurs fixes de C et H : C est 50. H est 30. D est la variable dont les valeurs doivent
être entrées dans votre programme dans une séquence séparée par des virgules. 
Exemple Supposons que la séquence d'entrée suivante séparée par des virgules 
soit donnée à la fonction : 100,150,180 La sortie du programme devrait être : 18,22,24 
'''
import numpy as np 

D1,D2,D3=list(map(int,input('tapez 3 nombres:').split(",")))

res1=(2*50*int(D1))/30
RES1=np.sqrt(res1)

res2=(2*50*int(D2))/30
RES2=np.sqrt(res2)

res3=(2*50*int(D3))/30
RES3=np.sqrt(res3)

print(round(RES1),round(RES2),round(RES3))


# In[ ]:




