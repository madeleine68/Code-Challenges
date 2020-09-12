    
import stddraw
import random

# Draw a bouncing ball to standard draw.
balls=[]
for _ in range (5):
      RADIUS = .05
      DT =  15.0
      balls.append(RADIUS)
      
stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)
 
for RADIUS in balls:  
    rx = random.random()
    ry = random.random()
    vx = .035
    vy = .035
print(balls)     

while True:
    # Update ball position and draw it there.
    if abs(rx + vx) + RADIUS > 1.0:
        vx = -vx
    if abs(ry + vy) + RADIUS > 1.0:
        vy = -vy
    
    # new location
    rx += vx
    ry += vy
    
    
    stddraw.clear(stddraw.YELLOW)
    stddraw.filledCircle(rx, ry, RADIUS)
    stddraw.show(DT)    
        
    
