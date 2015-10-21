def setup():
  global img
  size(381, 250)
  img = loadImage("toolbox.jpg")
  image(img,0,0)
  img.loadPixels()
  loadPixels()

def draw():
  global img
  maxDist = 50
  
  for y in range(0, 250):
      for x in range(0, 381):
        index = y*381+x
        r = red(img.pixels[index])
        g = green(img.pixels[index])
        b = blue(img.pixels[index])
        
        if dist(x, y, mouseX, mouseY) <= maxDist:
            h = (hue(img.pixels[index]) + 180) % 360
            s = saturation(img.pixels[index])
            b = brightness(img.pixels[index])
            colorMode(HSB, 360)
            pixels[index] = color(h,s,b)
            colorMode(RGB)
        else:
            pixels[index] = color(r,g,b)

  updatePixels()

