import pygame
import pymunk
import pymunk.pygame_util
import math

(screen_width, screen_height) = (1080, 720)

def get_distance_between_two_bodies(pos_body_1, pos_body_2):
    return math.dist(pos_body_1, pos_body_2)

class Car:
    def __init__(self, space, pos):
        self.position = pos
        self.is_alive = True
        self.car_length = 30
        self.car_width = 15
        self.four_points = []
        self.speed = 130
        self.body = pymunk.Body()
        self.body.position = self.position
        self.shape = pymunk.Poly(self.body, [(self.car_length, self.car_width), (self.car_length, -self.car_width), (-self.car_length, -self.car_width), (-self.car_length, self.car_width)])
        self.shape.mass = 500
        self.shape.elasticity = 0.4
        space.add(self.body, self.shape)

    def stand_still(self):
        self.body.velocity = 0, 0

    def move_forward(self):
        x = math.cos(self.body.angle) * self.speed
        y = math.sin(self.body.angle) * self.speed
        self.body.velocity =  x, y
    
    def move_backward(self):
        x = math.cos(self.body.angle) * self.speed
        y = math.sin(self.body.angle) * self.speed
        self.body.velocity =  -x, -y

    def turn_left(self):
        self.body.angle -= 0.05

    def turn_right(self):
        self.body.angle += 0.05


class Ball:
    def __init__(self, space, pos, collision_type):
        self.radius = 8
        self.body = pymunk.Body()
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.mass = 5
        self.shape.elasticity = 0.8
        self.shape.collision_type = collision_type
        space.add(self.body, self.shape)


class Playfield:
    # Singleton Design Pattern
    __instance = None
    def __new__(cls):
        if(cls.__instance is None):
            cls.__instance = super(Playfield, cls).__new__(cls)
        return cls.__instance

    def set_borders(self, space):
            
        self.map_borders = [
            # field borders
            [(-20, -20), (screen_width*2+40, 40)],              # top
            [(-20, 0), (40, screen_height*2)],                  # left
            [(-20, screen_height+19), (screen_width*2+40, 40)], # bottom
            [(screen_width+19, 0), (40, screen_height*2)],      # right

            # goal pools
            [(0, screen_height/2-75), (screen_width/15, 3)],
            [(0, screen_height/2+75), (screen_width/15, 3)],
            [(screen_width-15, screen_height/2-75), (screen_height/15, 3)],
            [(screen_width-15, screen_height/2+75), (screen_height/15, 3)],
        ]
        for pos, size in self.map_borders:
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            shape = pymunk.Poly.create_box(body, size)
            body.position = pos
            shape.elasticity = 0.4
            space.add(body, shape)


class ScoreZone:
    def __init__(self, space, pos, collision_type):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Poly.create_box(self.body, pos[1])
        self.body.position = pos[0]
        self.shape.color = (255, 0, 0, 255)
        self.shape.collision_type = collision_type
        space.add(self.body, self.shape)


class PyGame2D:
    def __init__(self):
        # goal score zones
        score_zones = [
            [(15, (screen_height/2)), (18, 135)],
            [(screen_width-15, screen_height/2), (18, 135)]
        ]
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.reward = 0
        self.done = False

        self.space = pymunk.Space()
        self.ball = Ball(self.space, (screen_width/2, screen_height/2), collision_type=1)
        self.car_1 = Car(self.space, (screen_width*0.56, screen_height*0.5))

        self.Playfield = Playfield() 
        self.Playfield.set_borders(self.space)
        self.score_zone_team_1 = ScoreZone(self.space, score_zones[0], collision_type=2)
        self.score_zone_team_2 = ScoreZone(self.space, score_zones[1], collision_type=3)

        self.score_goal_team_1 = self.space.add_collision_handler(self.ball.shape.collision_type, self.score_zone_team_1.shape.collision_type)
        self.distance_ball_goal = get_distance_between_two_bodies(self.ball.body.position, self.score_zone_team_1.body.position)
        self.distance_car_1_ball = get_distance_between_two_bodies(self.car_1.body.position, self.ball.body.position)
        self.draw_init = True

    def action(self, action):
        # action space
        if action == 0: # stand still
            self.car_1.stand_still()

        elif action == 1: # go forward
            self.car_1.move_forward()

        elif action == 2: # go backward
            self.car_1.move_backward()

        elif action == 3: # rotate left
            self.car_1.turn_left()

        elif action == 4: # rotate right
            self.car_1.turn_right()

        elif action == 5: # shoot
            pass

        self.ball.body.velocity = self.ball.body.velocity * 0.999

        self.clock.tick(self.fps)
        self.space.step(1 / self.fps)

    def colission_ball_score_zone(self, arbiter, space, data):
        self.reward += 100000
        self.done = True
        return True


        
    def evaluate(self):
        # check if the ball contacted the score zone
        self.score_goal_team_1.begin = self.colission_ball_score_zone
        distance_ball_goal = get_distance_between_two_bodies(self.ball.body.position, self.score_zone_team_1.body.position)
        distance_car_1_ball = get_distance_between_two_bodies(self.car_1.body.position, self.ball.body.position)
        if distance_ball_goal < self.distance_ball_goal:
            self.reward += 100
        else:
            self.reward -= 1

        if distance_car_1_ball < self.distance_car_1_ball:
            self.reward = 300 - distance_car_1_ball
        else:
            self.reward -= 1
        # check distance between the ball and the goal
        self.distance_ball_goal = distance_ball_goal
        return self.reward


    def is_done(self):
        if self.done:
            return True
        return False

    def observe(self):
        ball_pos = self.ball.body.position
        car_1_pos = self.car_1.body.position
        car_1_angle = math.degrees(self.car_1.body.angle) % 360
        return [ball_pos[0], ball_pos[1], car_1_pos[0], car_1_pos[1], car_1_angle]

    def view(self):
        # initialize the screen window for drawing
        if self.draw_init:
            self.screen = pygame.display.set_mode((screen_width, screen_height))
            pygame.display.set_caption('RoboSoccer')
            self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
            self.draw_init = False
        
        # render each step
        self.screen.fill((0,0,0))
        self.space.debug_draw(self.draw_options)
        pygame.display.update()

    

# temp instance of game to test if everything works

game = PyGame2D()
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        game.action(1)
    elif keys[pygame.K_DOWN]:
        game.action(2)
    elif keys[pygame.K_LEFT]:
        game.action(3)
    elif keys[pygame.K_RIGHT]:
        game.action(4)
    else:
        game.action(0)
    game.observe()
    game.evaluate()
    game.view()

pygame.quit()
