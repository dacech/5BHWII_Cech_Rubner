import numpy as np                  #import

a1 = np.array([1,2,3,4,5])           #definiertes erstellen
print(a1)                            #inhalt ausgeben
print(a1.shape)                      #anz. d. werte
print(len(a1.shape))                 #anz. d. dim.
print(a1.dtype)                      #dt d. arrays

#_______________________________________________________________________________________________________________

b1 = np.arange(10)                  #0 -> XX
b2 = np.arange(10,20,2)             #start/stop/step
b3 = np.linspace(10,20,2)          #start/stop/anz. d werte (gleicher abstand)
b4 = np.zeros(10)                   #anz. d. 0
b5 = np.ones(10)                    #anz. d. 1
b6 = np.random.rand(10)             #anz. zz. zw. 0 & 1
b7 = np.random.randint(10,20,5)     #start/stop/anz. d. zz.

#_______________________________________________________________________________________________________________

c1 = np.random.rand(3,2,4)          #mehrdim. array (mit zz) -> !!!

#_______________________________________________________________________________________________________________

d1 = np.array([1,2,3], dtype=int)                           #dt bei erstellen festlegen
d1 = d1.astype(str, copy=False, casting='safe')             #dt nachträglich ändern (copy!, casting!)
d2 = np.array(['1995-10-28 23:55', '2020-01-18 23:01'])
d2 = d2.astype('M')                                         #so bei nicht built-in dt (...)

#_______________________________________________________________________________________________________________

e1 = np.zeros(10)
e1 = e1.reshape(2,5)        #ändern d. dim (!)

#_______________________________________________________________________________________________________________

f1 = np.arange(10)*10      #rechenoperationen

#_______________________________________________________________________________________________________________

g1 = np.arange(15)      #0-14
print(g1[0])            #ausgabe index 0 (0)
print(g1[:5])           #ausgabe index 0-4
print(g1[6:])           #ausgabe index 6-14
print(g1[1:4])          #ausgabe index 1-3
print(g1[-1])           #ausgabe erster wert von hinten (14)

#_______________________________________________________________________________________________________________

h1 = np.array([[1,2,3],[4,5,6],[7,8,9]])        #[]!
print(h1)                                       #ausgabe gesamte matrix
print(h1[:,1])                                  #ausgabe spalte 2
print(h1[1,:])                                  #ausgabe zeile 2
print(h1[1,1])                                  #ausgabe spalte 2 & zeile 2
print(h1[[1,2],[0,1]])                          #positionen (1,0), (2,1) also 4 und 8

#_______________________________________________________________________________________________________________

i1 = np.arange(10)
print(i1[i1> 5])            #werte > 5
print(i1[~(i1<6)])          #werte NICHT < 6 (~ = not)

#_______________________________________________________________________________________________________________

j1 = np.array([1,2,np.nan,4,5,np.nan,7,8,np.nan])       # nan = fehlender wert
print(j1[~np.isnan(j1)])                                # nan filtern

#_______________________________________________________________________________________________________________

k1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
i = np.where(k1<=5)                         #gibt indexe von werten <= 5
print(k1[i])                                #ausgabe der ges. indexe
k1[i] = 20                                  #überschreiben der ges. indexe
print(k1)                                   #alle werte <=5 -> 20

#_______________________________________________________________________________________________________________

l1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(l1)

new_line = [[10,11,12]]                         #neue zeile
l1 = np.append(l1,new_line, axis=0)             #neue zeile einfügen (0)
print(l1)

new_column = np.array([[11], [22], [33], [44]])     #neue spalte
l1 = np.append(l1, new_column, axis=1)              #neue spalte einfügen (1)
print(l1)

#_______________________________________________________________________________________________________________

m1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

m2 = np.split(m1,2,1)                               #teilt spaltenweise (1) in 2 neue arrays
print(m2)

m3 = np.split(m1,3,0)                               #teilt zeilenweise (0) in 3 neue arrays
print(m3)

m4 = np.delete(m1,2,0)                              #löscht 3te zeile (0)
print(m4)

m5 = np.delete(m1,3,1)                              #löscht 4te spalte (1)
print(m5)

m6 = np.array([[1,4,4],[2,4,4],[3,4,4]])            #matrix mit widerholten werten (ww)
m7 = np.unique(m6)                                  #entf. ww -> 1-dim. array (1x w bleibt!!)
print(m7)

m8 = np.ravel(m6)                                   #macht zu 1-dim. array
print(m8)

#_______________________________________________________________________________________________________________

#Lagemaße

n1 = np.random.normal(170,10, 1000)     #(1000 werte, mittelwert 170, sw 10)
n1.mean                                 #Mittelwert (Summe/Anz.)
np.median(n1)                           #Median (Mitte d. sort. L.)
np.quantile(n1,0.1)                     #Quantil (links von diesem Wert sind die unteren 10%)

from scipy import stats                 #für Modus (häüfigster Wert)
n2 = np.random.randint(10,20,500)       #500 zw. 10 & 20
modus = stats.mode(n2)
print("Modus",modus.mode, modus.count)  #ausgabe (wert + anz.)


#Streuungsmaße
np.std(n1)                              #standartabweichung (???)
n1.min() - n1.max()                     #spannweite

# --> Umgang mit fehlenden Werten           (-> Folien!!)
# --> Daten aus Datei in NumPy importieren  (-> Folien!!)
