def setup():
    size(300,300)
    
def draw():
    RADIUS = 120
    BREITE = 40
    OFFSET = 150
    
    for x in range(1,300):
        for y in range(1,300):
            if pow(x-OFFSET,2) + pow(y-OFFSET,2) <= RADIUS*RADIUS and pow(x-OFFSET,2) + pow(y-OFFSET,2) > pow(RADIUS-BREITE,2):
                c = color(random(255), random(255), random(255))
                stroke(c)
                point(x,y)
                
