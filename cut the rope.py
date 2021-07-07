# importing all required modules
import pygame
import math
import time


#initialising pygame
pygame.init()
file = '123.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

#colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
#etc

# max height is, say, 2000           (for window)
display_h = 800
display_w = int(display_h*1.2)
# creating the screen window
surface = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption("Cut The Rope")
#creating clock to track time
clock=pygame.time.Clock()

# note : max img size=2000/20
candy_width = int(display_h/20)

#creating objects for the images required
candy = pygame.image.load('CANDY.png')
bowl=pygame.image.load('bowl1.png')
##bwc=pygame.image.load('bowl and candy.png')
stari=pygame.image.load('star2.png')
menu = pygame.image.load('menu.png')
back = pygame.image.load('back6.png')
back1 = pygame.image.load('back1.png')
sound_on = pygame.image.load('sound_on.png')
sound_off = pygame.image.load('sound_off.png')
levelselect = pygame.image.load('level select.png')
score1 = pygame.image.load('s1.png')
score2 = pygame.image.load('s2.png')
score3 = pygame.image.load('s3.png')
score0 = pygame.image.load('s0.png')
go2menu = pygame.image.load('go2menu.png')
playagain = pygame.image.load('playagain.png')
nextlevel = pygame.image.load('nextlevel.png')
hat1 = pygame.image.load('redhat.png')
hat2 = pygame.image.load('bluehat.png')

#transforming images to the sizes required
candy = pygame.transform.scale(candy,(candy_width,candy_width))
bowl = pygame.transform.scale(bowl,((candy_width*4,candy_width*4)))
stari= pygame.transform.scale(stari,(candy_width,candy_width))
menu = pygame.transform.scale(menu,(display_w,display_h))
back = pygame.transform.scale(back,(display_w,display_h))
back1 = pygame.transform.scale(back1,(display_w,display_h))
sound_on = pygame.transform.scale(sound_on,(int(display_w*0.30576923),int(display_h*0.1358975)))
sound_off = pygame.transform.scale(sound_off,(int(display_w*0.30576923),int(display_h*0.1358975)))
levelselect = pygame.transform.scale(levelselect,(int(display_h*0.7),int(display_h*0.8)))
score1 = pygame.transform.scale(score1,(int(candy_width*6),int(candy_width*1.6236)))
score2 = pygame.transform.scale(score2,(int(candy_width*6),int(candy_width*1.6236)))
score3 = pygame.transform.scale(score3,(int(candy_width*6),int(candy_width*1.6236)))
score0 = pygame.transform.scale(score0,(int(candy_width*6),int(candy_width*1.6236)))
go2menu = pygame.transform.scale(go2menu,(int(candy_width*4),int(candy_width*2)))
nextlevel = pygame.transform.scale(nextlevel,(int(candy_width*4),int(candy_width*2)))
playagain = pygame.transform.scale(playagain,(int(candy_width*4),int(candy_width*2)))
hat1 = pygame.transform.scale(hat1,(int(candy_width*2),int(candy_width*2)))
hat2 = pygame.transform.scale(hat2,(int(candy_width*2),int(candy_width*2)))
hat1 = pygame.transform.rotate(hat1,170)


#001
#For background sound options ON or OFF
def Sound():
    if pygame.mixer.music.get_busy():
        surface.blit(menu, (0, 0))
        surface.blit(sound_off,(display_h/2.425373,display_h/1.340206)) 
        pygame.mixer.music.stop()
        pygame.display.update()
    else:
        surface.blit(menu, (0, 0))
        surface.blit(sound_on,(display_h/2.425373,display_h/1.340206))
        pygame.mixer.music.play()
        pygame.display.update()

#002
#For managing the menu window
def Menu():
    surface.blit(menu, (0, 0))
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    surface.blit(sound_on,(int(display_h/2.425373),int(display_h/1.340206)))
    pygame.display.update()
    global sound_state
    c = 0
    while 1:
        for event in pygame.event.get():     
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                (mx,my) = pygame.mouse.get_pos()
                if int(mx) in range(int(display_h/2.32142857),int(display_h/1.3)) and int(my) in range(int(display_h/1.3131313),int(display_h/1.17117117)):
                    Sound() # calling 001
                if int(mx) in range(int(display_h/2.32142857),int(display_h/1.3)) and int(my) in range(int(display_h/1.547619),int(display_h/1.35416667)):
                    c = 1
                    break
        if c:
            break
    LevelSelect()

def LevelSelect():
    global level
    surface.blit(levelselect,(int(display_h*0.6-display_h*0.35),display_h*0.1))
    pygame.display.update()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                (mx,my) = pygame.mouse.get_pos()
                if int(mx) in range(int(display_h/2.15),int(display_h/1.36)) and int(my) in range(int(display_h/5),int(display_h/3.6)):
                    l1.time_start = time.time()
                    level = l1
                    l1.Play_Level()
                if int(mx) in range(int(display_h/2.15),int(display_h/1.36)) and int(my) in range(int(display_h/2.5),int(display_h/2.07)):
                    l2.time_start = time.time()
                    level = l2
                    l2.Play_Level()
                if int(mx) in range(int(display_h/2.15),int(display_h/1.36)) and int(my) in range(int(display_h/1.67),int(display_h/1.46)):
                    l3.time_start = time.time()
                    level = l3
                    l3.Play_Level()
                
        
                    
#003
#For swinging movement of the candy
def swing(x,y, cx,cy, r, ay, dt, t):
    global check
    global angle_max
    angle_max *= 0.9995
    angle = angle_max * math.sin((ay/r)**1/2 * (t+2.5))
    yn = r * math.cos(angle) + cy
    xn = r * math.sin(angle) + cx
    vx =(xn - x)/dt
    vy = (yn - y)/dt
    return (xn,yn),angle,[vx,vy]
        
#004
#CHECK THIS
def Result(win):
    time.sleep(1.5)
    global level
    if win:
        time_taken = time.time()-level.time_start
        num_stars = 0
        for i in [s1,s2,s3]:
            if not i.exist:
                num_stars += 1
        score = str(int(10*(200+200 * num_stars )/ time_taken))
        font_size = pygame.font.Font('freesansbold.ttf',int(candy_width/2))
        WIN = font_size.render('YOU WIN! CONGRATS =)', True, black)
        score = font_size.render('Score: '+score,True,black)
        WIN_Rect = WIN.get_rect()
        WIN_Rect.center = (int(display_w/2), int(display_h/2-candy_width*3))
        score_Rect = score.get_rect()
        score_Rect.center = ((display_w/2), (display_h/2-candy_width*2))
        surface.blit(back,(0,0))
        surface.blit(WIN, WIN_Rect)
        surface.blit(score,score_Rect)
        if num_stars == 0:
            surface.blit(score0,(int(display_w/2-candy_width*3), int(display_h/2-candy_width)))
        elif num_stars == 1:
            surface.blit(score1,(int(display_w/2-candy_width*3), int(display_h/2-candy_width)))
        elif num_stars == 2:
            surface.blit(score2,(int(display_w/2-candy_width*3), int(display_h/2-candy_width)))
        elif num_stars == 3:
            surface.blit(score3,(int(display_w/2-candy_width*3), int(display_h/2-candy_width)))
        if level.level == 3:
            surface.blit(playagain,(int(display_w/2-candy_width*2), int(display_h/2+candy_width*3)))
            surface.blit(go2menu,(int(display_w/2-candy_width*2), int(display_h/2+candy_width*5)))
            pygame.display.update()
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        (mx,my) = pygame.mouse.get_pos()
                        if int(mx) in range(int(display_w/2-candy_width*2),int(display_w/2+candy_width*2)):
                            if int(my) in range(int(display_h/2+candy_width*3),int(display_h/2+candy_width*5)):
                                level.time_start = time.time()
                                level.Play_Level()
                        if int(mx) in range(int(display_w/2-candy_width*2),int(display_w/2+candy_width*2)):
                            if int(my) in range(int(display_h/2+candy_width*5),int(display_h/2+candy_width*7)):
                                Menu()
                                
        else:
            surface.blit(playagain,(int(display_w/2-candy_width*4.5), int(display_h/2+candy_width*3)))
            surface.blit(nextlevel,(int(display_w/2+candy_width*0.5), int(display_h/2+candy_width*3)))
            surface.blit(go2menu,(int(display_w/2-candy_width*2), int(display_h/2+candy_width*5)))
            pygame.display.update()
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        (mx,my) = pygame.mouse.get_pos()
                        if int(mx) in range(int(display_w/2-candy_width*4.5),int(display_w/2-candy_width*0.5)):
                            if int(my) in range(int(display_h/2+candy_width*3),int(display_h/2+candy_width*5)):
                                level.time_start = time.time()
                                level.Play_Level()
                        if int(mx) in range(int(display_w/2+candy_width*0.5),int(display_w/2+candy_width*4.5)):
                            if int(my) in range(int(display_h/2+candy_width*3),int(display_h/2+candy_width*5)):
                                if level.level == 1:
                                    level = l2
                                elif level.level == 2:
                                    level = l3
                                level.time_start = time.time()
                                level.Play_Level()
                        if int(mx) in range(int(display_w/2-candy_width*2),int(display_w/2+candy_width*2)):
                            if int(my) in range(int(display_h/2+candy_width*5),int(display_h/2+candy_width*7)):
                                Menu()
        
        
    else:
        surface.blit(back,(0,0))
        font_size = pygame.font.Font('freesansbold.ttf',candy_width/2)
        LOSE = font_size.render('Oops. Try again!', True, black)
        LOSE_Rect = LOSE.get_rect()
        LOSE_Rect.center = ((display_w/2), (display_h/2 - candy_width*2))
        surface.blit(LOSE, LOSE_Rect)
        surface.blit(playagain,(int(display_w/2-candy_width*2), int(display_h/2)))
        surface.blit(go2menu,(int(display_w/2-candy_width*2), int(display_h/2+candy_width*2)))
        pygame.display.update()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    (mx,my) = pygame.mouse.get_pos()
                    if int(mx) in range(int(display_w/2-candy_width*2),int(display_w/2+candy_width*2)):
                        if int(my) in range(int(display_h/2),int(display_h/2+candy_width*2)):
                            level.time_start = time.time()
                            level.Play_Level()
                    if int(mx) in range(int(display_w/2-candy_width*2),int(display_w/2+candy_width*2)):
                        if int(my) in range(int(display_h/2+candy_width*2),int(display_h/2+candy_width*4)):
                            Menu()


#005
def fall(x,y,angle, v, a, dt, t,x_bowl,y_bowl, xc, yc, xc2=0, yc2=0, r2=0):
    global s1,s2,s3,r,h1,h2,hi1,hi2
    cont = True
    t_h = 0
    while cont:
        c=0
        #For normal freefall, not within bubble - r (r for ring)
        if r.occupied==False:
            x += v[0]*dt
            y += v[1]*dt
            v[1] += a*dt
            for event in pygame.event.get():     
                if event.type == pygame.QUIT:
                     pygame.quit()
                     quit()
        #For bubble floating up
        else:
            v0=200 #some const speed in bubble
            y -= 200*dt
            r.y=y+5
            v[0] = 0
            v[1] = 0
            #checking if bubble is getting popped
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if int(pos[0]) in range(int(r.x-candy_width/2-5),int(r.x+candy_width/2+5)):
                        if int(pos[1]) in range(int(r.y-candy_width/2-5),int(r.y+candy_width/2+5)):
                            r.occupied = False
                            r.exist = False
                    
        blit(back,x,y,x_bowl,y_bowl,xc,yc,False,xc2,yc2,v)
        pygame.display.update()
        clock.tick(100)

        #falling out of screen
        if y > display_h+candy_width or x > display_w+candy_width or x < -candy_width or y < -candy_width:
            cont = False
            Result(False)
            
        t+=dt
        
        #checking for stars
        check_star(x,y)
        
        ######new swing-may have second swinging centre which you fall into######

        #check for hat
        for h in (h1,h2,hi1,hi2):
            if h.exist:
                if int(x) in range(h.pos1[0]-candy_width,h.pos1[0]+candy_width*2):
                    if int(y) in range(h.pos1[1]-candy_width,h.pos1[1]+candy_width*2):
                        if h.d1 == 'u' and v[1]>0:
                            surface.blit(h.img1,h.pos1)
                            pygame.display.update()
                            if t>t_h+0.5 and int(x) in range(int(h.pos1[0]-candy_width*0.2),int(h.pos1[0]+candy_width*1.2)):
                                if int(y) in range(h.pos1[1],h.pos1[1]+candy_width):
                                    t_h = t
                                    (x,y) = h.pos2
                                    if h.d2 == 'u':
                                        v[0],v[1] = 0,-v[1]
                                    if h.d2 == 'l':
                                        v[0],v[1] = -v[1],0
                                    if h.d2 == 'r':
                                        v[0],v[1] = v[1],0
                                    else:
                                        v[0],v[1] = 0,v[1]
                        if h.d1 == 'l' and v[0]>0:
                            surface.blit(h.img1,h.pos1)
                            pygame.display.update()
                            if t>t_h+0.5 and int(x) in range(h.pos1[0],h.pos1[0]+candy_width):
                                if int(y) in range(int(h.pos1[1]-candy_width*0.2),int(h.pos1[1]+candy_width*1.2)):
                                    t_h = t
                                    (x,y) = h.pos2
                                    if h.d2 == 'u':
                                        v[0],v[1] = 0,-v[0]
                                    if h.d2 == 'l':
                                        v[0],v[1] = -v[0],0
                                    if h.d2 == 'd':
                                        v[0],v[1] = 0,v[0]
                                    else:
                                        v[0],v[1] = v[0],0
                        if h.d1 == 'r' and v[0]<0:
                            surface.blit(h.img1,h.pos1)
                            pygame.display.update()
                            if t>t_h+0.5 and int(x) in range(h.pos1[0],h.pos1[0]+candy_width):
                                if int(y) in range(int(h.pos1[1]-candy_width*0.2),int(h.pos1[1]+candy_width*1.2)):
                                    t_h = t
                                    (x,y) = h.pos2
                                    if h.d2 == 'u':
                                        v[0],v[1] = 0,v[0]
                                    if h.d2 == 'd':
                                        v[0],v[1] = 0,-v[0]
                                    if h.d2 == 'r':
                                        v[0],v[1] = -v[0],0
                                    else:
                                        v[0],v[1] = v[0],0
                        if h.d1 == 'd' and v[1]<0:
                            surface.blit(h.img1,h.pos1)
                            pygame.display.update()
                            if t>t_h+0.5 and int(x) in range(int(h.pos1[0]-candy_width*0.2),int(h.pos1[0]+candy_width*1.2)):
                                if int(y) in range(h.pos1[1],h.pos1[1]+candy_width):
                                    t_h = t
                                    (x,y) = h.pos2
                                    if h.d2 == 'd':
                                        v[0],v[1] = 0,-v[1]
                                    if h.d2 == 'l':
                                        v[0],v[1] = v[1],0
                                    if h.d2 == 'r':
                                        v[0],v[1] = -v[1],0
                                    else:
                                        v[0],v[1] = 0,v[1]

                
        #check for bubble if not already inside
        if r.occupied == False and r.exist == True:
            for i in range(int(r.x-candy_width*1.8), int(r.x+candy_width*0.8)):
                if i==int(x):
                    for j in range(int(r.y-candy_width*0.8), int(r.y+candy_width*0.8)):
                        if j==int(y):
                            r.occupied = True
                            x,y=r.x-candy_width/2,r.y-candy_width/2

        #check for bowl
        for i in range(int(x_bowl-candy_width/2),int(x_bowl+candy_width*2.8)):
            if i==int(x):
                for i in range(int(y_bowl+candy_width*0.2),y_bowl+candy_width):
                    if i==int(y):
                        c=1
        if c==1:
            cont=False
            Result(True)

#function to check if candy hits star
def check_star(x,y):
    global s1,s2,s3
    for s in [s1,s2,s3]:
        for i in range(int(s.x-candy_width*0.8), int(s.x+candy_width*0.8)):
            if i==int(x):
                for j in range(int(s.y-candy_width*0.8), int(s.y+candy_width*0.8)):
                    if j==int(y):
                        s.exist = False

######WILL NEED TO CHANGE to suit newest level 3 when made######
def blit(back,x,y,xb,yb,xc,yc,sw=False,xc2=0,yc2=0,v=[0,0]):
    global s1,s2,s3,r,h1,h2
    surface.blit(back,(0,0))
    surface.blit(bowl,(xb,yb))
    if s1.exist==True:
        surface.blit(s1.img,(s1.x,s1.y))
    if s2.exist==True:
        surface.blit(s2.img,(s2.x,s2.y))
    if s3.exist==True:
        surface.blit(s3.img,(s3.x,s3.y))
    if r.exist==True:
        pygame.draw.circle(surface,blue,(int(r.x),int(r.y)),int(candy_width*0.5+30),10)
    if sw==True:
        pygame.draw.lines(surface, black, False,[(x+candy_width/2, y+candy_width/2),(xc+candy_width/2, yc+candy_width/2)], 2)
    pygame.draw.circle(surface,black,[xc+20,yc+20],5,5)
    if xc2 and yc2:
        pygame.draw.circle(surface,black,[xc2+20,yc2+20],5,5)
    if h1.exist:
        surface.blit(h1.img1,h1.pos1)
        surface.blit(h1.img2,h1.pos2)
    if h2.exist:
        surface.blit(h2.img1,h2.pos1)
        surface.blit(h2.img2,h2.pos2)
    surface.blit(candy,(x,y))
    
        
            
        

#006
def cut(x_candy,y_candy,xc,yc):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEMOTION:
            pygame.mouse.set_visible(True)     
            ctr=0
            (x,y)=event.pos
            if x_candy>xc:
                for i in range(xc,int(x_candy)):
                    if i==x:
                        ctr=1
            elif x_candy<xc:
                for i in range(int(x_candy),xc):
                    if i==x:
                        ctr=1
            if ctr==1:
                for i in range(yc,int(y_candy)):
                    if i==y:
                        ctr=2
            if ctr==2:
                return True
            else:
                return False
        else:
            return False


#007
def Game_Loop(l, x_center, y_center, r_candy, x_bowl, y_bowl, x_center2, y_center2, r_candy2):
    global angle_max
    global s1,s2,s3
    angle_max = (math.pi/2)
    x_candy = x_center + r_candy
    y_candy = y_center
    dt = 0.01
    t = 0
    angle = 0
    vel=[0,0]
    if l == 1:
        acc = 800
    elif l == 2:
        acc = 1000
    elif l == 3:
        acc = 1100
    else:
        print("ERROR: unidentifyable level")
        time.sleep(5)
    while 1:
        check_star(x_candy,y_candy)
        if cut(x_candy,y_candy,x_center,y_center):
            break
        else:
            ((x_candy, y_candy), angle, vel) = swing(x_candy,y_candy,x_center, y_center, r_candy, acc, dt, t)
        blit(back,x_candy,y_candy,x_bowl,y_bowl,x_center,y_center,True,x_center2,y_center2)
        pygame.display.update()
        clock.tick(100)
        t += dt
    fall(x_candy, y_candy,angle, vel, acc, dt, t, x_bowl,y_bowl,x_center,y_center, x_center2, y_center2, r_candy2)
    
    
        












class TextRectException:
    def __init__(self, message = None):
        self.message = message
    def __str__(self):
        return self.message

def render_textrect(string, font, rect, text_color, background_color, justification=0):
    """Returns a surface containing the passed text string, reformatted
    to fit within the given rect, word-wrapping as necessary. The text
    will be anti-aliased.

    Takes the following arguments:

    string - the text you wish to render. \n begins a new line.
    font - a Font object
    rect - a rectstyle giving the size of the surface requested.
    text_color - a three-byte tuple of the rgb value of the
                 text color. ex (0, 0, 0) = BLACK
    background_color - a three-byte tuple of the rgb value of the surface.
    justification - 0 (default) left-justified
                    1 horizontally centered
                    2 right-justified

    Returns the following values:

    Success - a surface object with the text rendered onto it.
    Failure - raises a TextRectException if the text won't fit onto the surface.
    """

    import pygame
    
    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException("The word " + word + " is too long to fit in the rect passed.")
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.    
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line 
                else: 
                    final_lines.append(accumulated_line) 
                    accumulated_line = word + " " 
            final_lines.append(accumulated_line)
        else: 
            final_lines.append(requested_line) 

    # Let's try to write the text out on the surface.

    surface = pygame.Surface(rect.size) 
    surface.fill(background_color) 

    accumulated_height = 0 
    for line in final_lines: 
        if accumulated_height + font.size(line)[1] >= rect.height:
            raise TextRectException("Once word-wrapped, the text string was too tall to fit in the rect.")
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise TextRectException("Invalid justification argument: " + str(justification))
        accumulated_height += font.size(line)[1]

    return surface




















#Class for levels-b(bowl),s(star),r(ring/bubble),c(centre of rotation 1),c2(centre of rotation 2),r(radius of swing)
class levels(object):
    def __init__(self,l,xb,yb,xs1,ys1,xs2,ys2,xs3,ys3,xr,yr,xh11,yh11,xh12,yh12,d11,d12,xh21,yh21,xh22,yh22,d21,d22,xc,yc,r,xc2=0,yc2=0,r2=0):
        self.level = l
        self.xb = xb
        self.yb = yb
        self.xs1 = xs1
        self.ys1 = ys1
        self.xs2 = xs2
        self.ys2 = ys2
        self.xs3 = xs3
        self.ys3 = ys3
        self.r = r
        self.xc = xc
        self.yc = yc
        self.r2 = r2
        self.xc2 = xc2
        self.yc2 = yc2
        self.xr = xr
        self.yr = yr
        self.xh11 = xh11
        self.yh11 = yh11
        self.xh12 = xh12
        self.yh12 = yh12
        self.d11 = d11
        self.d12 = d12
        self.xh21 = xh21
        self.yh21 = yh21
        self.xh22 = xh22
        self.yh22 = yh22
        self.d21 = d21
        self.d22 = d22
    #function to invoke game play for respective level
    def Play_Level(self):
        global s1,s2,s3,r,h1,h2,hi1,hi2
        s1 = star(self.xs1,self.ys1)
        s2 = star(self.xs2,self.ys2)
        s3 = star(self.xs3,self.ys3)
        r = ring(self.xr,self.yr)
        h1 = hat(self.xh11,self.yh11,self.xh12,self.yh12,self.d11,self.d12,hat1)
        hi1 = hat(self.xh12,self.yh12,self.xh11,self.yh11,self.d12,self.d11,hat1)
        h2 = hat(self.xh21,self.yh21,self.xh22,self.yh22,self.d21,self.d22,hat2)
        hi2 = hat(self.xh22,self.yh22,self.xh21,self.yh21,self.d22,self.d21,hat2)
        if r.x==0 and r.y==0:
            r.exist = False
        Game_Loop(self.level, self.xc, self.yc, self.r, self.xb, self.yb, self.xc2, self.yc2, self.r2)
        
#star as an object
class star:
    def __init__(self,x,y):
        self.img = stari
        self.x = x
        self.y = y
        self.exist = True

#ring as an object
class ring:
    def __init__(self,x,y):
        self.occupied = False
        self.x = x
        self.y = y
        self.exist = True

class hat:
    def __init__(self,x1,y1,x2,y2,dir1,dir2,hat):
        self.pos1 = (x1,y1)
        self.pos2 = (x2,y2)
        self.d1 = dir1 #angle wrt upwards facing,anti-clockwise
        self.d2 = dir2
        if x1 or y1 or x2 or y2:
            self.exist = True
            if self.d1 == 'r':
                self.img1 = pygame.transform.rotate(hat,-90)
            elif self.d1 == 'l':
                self.img1 = pygame.transform.rotate(hat,90)
            elif self.d1 == 'u':
                self.img1 = hat
            elif self.d1 == 'd':
                self.img1 = pygame.transform.rotate(hat,180)
            else:
                print('Not correct direction for hat!')
            if self.d2 == 'r':
                self.img2 = pygame.transform.rotate(hat,-90)
            elif self.d2 == 'l':
                self.img2 = pygame.transform.rotate(hat,90)
            elif self.d2 == 'u':
                self.img2 = hat
            elif self.d2 == 'd':
                self.img2 = pygame.transform.rotate(hat,180)
            else:
                print('Not correct direction for hat!')
        else:
            self.exist = False

##initialising
l1=levels(1,550,500,280,330,350,350,400,400,0,0,0,0,0,0,'','',0,0,0,0,'','',200,200,150,0,0,0)
l1=levels(1,500,500,330,270,400,250,460,300,0,0,0,0,0,0,'','',0,0,0,0,'','',200,200,150,0,0,0)
l2=levels(2,677-candy_width*2,600,450,250,650,135,345,252,677,406,0,0,0,0,'','',0,0,0,0,'','',200,50,200,0,0,0)
l3=levels(3,450,500,330,270,200,100,460,300,250,500,200,350,600,400,'d','l',200,600,500,300,'u','d',200,200,150,0,0,0)
angle_max  = (math.pi/2)
check=0
level = None


#starting game
fo = open('Instructions.txt')
r = '\n\n'+fo.read()
fo.close()
font_size = pygame.font.Font('freesansbold.ttf',30)
instr = font_size.render(r, True, black)
##Rect = instr.get_rect()
##Rect.center = (int(display_w/2), int(display_h/2-candy_width*3))
surface.blit(back1,(0,0))
Rect = pygame.Rect((25, 25, display_w-50, display_h-50))
rendered_text = render_textrect(r, font_size, Rect, (216, 216, 216), (48, 48, 48), 1)
if rendered_text:
    surface.blit(rendered_text, Rect.topleft)
    pygame.display.update()
    
c=1
while c:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYUP:
            c=0
Menu()


        
    
        
