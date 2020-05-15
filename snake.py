import time
import pygame
import sys
import random
from snakebrain import brain
Uselessobject=0

HEIGHT = 800
WIDTH = 600

Traectory ='RIGHT'
pygame.init()
clock = pygame.time.Clock()
score=0
class Game:
    def __init__(self):
        self.white = pygame.Color(255, 255, 255)
        self.green = pygame.Color(0, 255, 0)
        self.red = pygame.Color(255, 0, 0)
        self.black = pygame.Color(0, 0, 0)
        self.brown = pygame.Color(165, 42, 42)

    def create_window(self):
        self.window = pygame.display.set_mode((HEIGHT,WIDTH))
        pygame.display.set_caption('Py Snake')
        self.window.fill(self.white)

    def otherthings(self):
        pygame.time.Clock().tick(120)
        pygame.draw.line(self.window, (0, 0, 0), [0, 39], [HEIGHT, 39], 1)
        pygame.display.flip()

    def k_press(self):
        global Traectory
        keys=pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and Traectory!='RIGHT':
            Traectory='LEFT'
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and Traectory!='LEFT':
            Traectory='RIGHT'
        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and Traectory!='DOWN':
            Traectory='UP'
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and Traectory!='UP':
            Traectory='DOWN'
        #if press esc- close the game
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    def show_score(self,score):
        #show a score
        s_font=  pygame.font.SysFont('Arial',16)#Font score
        s_surf= s_font.render('Score: {0}'.format(score), True, self.black)#create score tab
        s_rect = s_surf.get_rect()
        s_rect.midtop= (40,10)
        self.window.blit(s_surf, s_rect)
    def game_over(self):
        time.sleep(3)
        print('Score: ', score)
        pygame.quit()
        sys.exit()

class Snake:
    def __init__(self):
        #SNAKE'S POSITION
        self.head_pos=[120,40]

        self.body_pos=[[120,40],[100,40],[80,40]]

        self.speed = 20

        self.snake_height = 20

        self.snake_width = 20


    def snake_change_position(self):
        if Traectory =='RIGHT':
            self.head_pos[0]+=self.speed
        elif Traectory =='LEFT':
            self.head_pos[0]-=self.speed
        elif Traectory =='UP':
            self.head_pos[1]-=self.speed
        elif Traectory =='DOWN':
            self.head_pos[1]+=self.speed

    def check_position(self,game_over):
        if any((self.head_pos[0]>HEIGHT - self.snake_width or self.head_pos[0]<0,self.head_pos[1]<40, self.head_pos[1]>WIDTH - self.snake_height)):
            game_over()
        for pos in self.body_pos[1::]:
            if pos == self.head_pos:
                game_over()


    def snake_mekanism(self,food_pos):
        global score
        self.body_pos.insert(0, list(self.head_pos))
        if self.head_pos[0] == food_pos[0] and self.head_pos[1] == food_pos[1]:
            while food_pos in self.body_pos:
                food_pos=[random.randrange(0, HEIGHT,20),random.randrange(40, WIDTH,20)]
            score+=1
        else:
            self.body_pos.pop()
        return food_pos, score

    def draw_snake(self,window,color):
        for pos in self.body_pos:     
            pygame.draw.rect(window, color,(pos[0],pos[1],self.snake_height,self.snake_width ))
        
class Food():
    def __init__(self):
        self.food_size = 20
        self.food_pos =[random.randrange(0, HEIGHT,20),random.randrange(40, WIDTH,20)]


    def draw_food(self,window,color):        
        pygame.draw.rect(window, color,pygame.Rect(self.food_pos[0],self.food_pos[1],self.food_size,self.food_size))


def main():
    global score
    global Traectory
    snake = Snake()
    game = Game()
    food = Food()
    RunGame = True
    while RunGame:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                RunGame =False
        game.k_press()
        game.create_window()
        snake.check_position(game.game_over)
        snake.draw_snake(game.window,game.green)
        food.draw_food(game.window, game.red)
        snake.snake_change_position()
        food.food_pos, score = snake.snake_mekanism(food.food_pos)
        game.show_score(score)
        game.otherthings()
        new_food_pos= food.food_pos
        snake_brain = brain(snake.head_pos,new_food_pos,Traectory,snake.body_pos)
        if snake_brain!=None:
            Traectory= snake_brain
        print('SnakePos: ', snake.head_pos)
        print('Traectory: ', Traectory)
        print('FoodPos: ', new_food_pos)


    pygame.quit()

main()
print('Score: ', score)



