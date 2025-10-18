import pygame
import math
pygame.init()

WIDTH,HEIGHT = 800,600 
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Gravitational Simulation")


OBJ_MASS = 100
G = 5 
FPS = 60
PLANET_SIZE = 50 #radius of planet
OBJ_SIZE = 5
VEL_SCALE = 100
dt = 0.3

BG = pygame.transform.scale(pygame.image.load("background.jpg"),(WIDTH,HEIGHT))

WHITE =(255,255,255)
RED=(255,0,0)
color1 = (181,0,90)
color2 = (65,105,225)

class Planet :
    def __init__(self,x,y,mass , radius):
        self.x = x
        self.y = y 
        self.mass = mass
        self.radius = radius

    def draw(self,color):
        pygame.draw.circle(win, color, (int(self.x), int(self.y)), self.radius)


class spacecraft:
    def __init__(self,x,y,vel_x,vel_y,mass):
        self.x = x
        self.y =y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass
        self.ax=0
        self.ay=0

    def move_acc(self,planets):
        fx_total,fy_total = 0 ,0
        for p in planets:
            dx = p.x - self.x
            dy = p.y - self.y
            distance = math.sqrt(dx**2 + dy**2)

            if distance < p.radius:
                distance = p.radius
            f = G*self.mass *p.mass/ distance**2
            fx_total += f * (dx/distance)
            fy_total += f * (dy/distance)
        self.ax = fx_total/self.mass
        self.ay = fy_total/self.mass

    def move_velpos(self,dt):
        self.vel_x += self.ax * dt
        self.vel_y += self.ay*dt
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt
        

    def draw(self):
         pygame.draw.circle(win,RED,(int(self.x),int(self.y)),OBJ_SIZE)


def create_ship(location,mouse): 
    t_x,t_y =location 
    m_x,m_y = mouse
    vel_x = (m_x - t_x)/VEL_SCALE
    vel_y = (m_y - t_y)/VEL_SCALE
    return spacecraft(t_x,t_y,vel_x , vel_y,OBJ_MASS)
    


def main():
    running = True
    clock = pygame.time.Clock()

    planet1 = Planet(WIDTH / 4, HEIGHT / 2, 1000, 100)
    planet2 = Planet(3 * WIDTH / 4, HEIGHT / 2, 500, 50)
    planets = [planet1, planet2]
    objects = []
    temp_obj_pos = None


    while running:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos :
                    obj = create_ship(temp_obj_pos,mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None 
                else :
                    temp_obj_pos = mouse_pos

        win.blit(BG,(0,0))

        if temp_obj_pos :
            pygame.draw.line(win,WHITE,temp_obj_pos,mouse_pos,2)
            pygame.draw.circle(win,RED,temp_obj_pos,OBJ_SIZE)

        for obj in objects[:]:
            obj.move_acc(planets)
            obj.move_velpos(dt)
            obj.draw()
            off_screen = obj.x < 0 or obj.x> WIDTH or obj.y < 0 or obj.y > HEIGHT
            collided = any(
                math.sqrt((obj.x - p.x)**2 + (obj.y - p.y)**2) <= p.radius
                for p in planets
            )
            if off_screen or collided:
                objects.remove(obj)


        planet1.draw(color1)
        planet2.draw(color2)
        pygame.display.update()
    pygame.quit()
        

if __name__=="__main__": 
    main()


