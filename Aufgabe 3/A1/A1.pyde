def setup():
    size(580,200)
    frameRate(10)
    global x
    global white
    x = 10
    colorMode(RGB)
    white = color(255,255,255)
    
def draw():
    global x
    global white
    
    noStroke()
    
    fill(white, 255*(1.0/4.0)) 
    rect(0.0, 0.0, 580.0, 200.0)
    stroke(0,0,0,255)
    
    drawSurfer(x, 100)
    
    if x > 580:
        x = 10
    else:
        x += 40

# Diese Methode soll von Ihnen nicht verändert werden
def drawSurfer(x,y):
    line(x,y - 10, x, y + 20)
    ellipse(x, y - 15, 15, 15)
    line(x, y, x + 10, y - 3)
    line(x, y, x - 10, y - 3)
    line(x, y + 20, x + 6, y + 28)
    line(x, y + 20, x - 6, y + 28)
    
