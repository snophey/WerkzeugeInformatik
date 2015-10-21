 
size(400, 250) # Breite des Zeichenfensters setzen
    
# Farben der olympischen Ringe in der richtigen Reihenfolge definieren
     
blau = color(0, 133, 199)
gelb = color(244, 195, 0)
schwarz = color(0, 0, 0)
gruen = color(0, 159, 61)
rot = color(223, 0, 36)
    
noFill() # Die Ringe sollen nicht ausgefüllt werden
strokeWeight(4) # Breite der Ringe auf 4 Stellen

radius = 100  

stroke(blau)
ellipse(100,100,radius,radius)
stroke(gelb)
ellipse(150,150,radius,radius)
stroke(schwarz)
ellipse(200,100,radius,radius)
stroke(gruen)
ellipse(250,150,radius,radius)
stroke(rot)
ellipse(300,100,radius,radius)
