import pygame
from random import randint

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
FPS = 40
class TextArea:
    def __init__(self, x=10, y=10, weight=10, height=10, color = GREEN ):
        self.rect = pygame.Rect(x, y, weight, height)
        self.fill_color = color
    def set_text(self, text, font_size=12, color=BLACK):
        self.font = pygame.font.Font('Comic Neue', font_size).render(text, True, color)
        self.text = text

    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.font, (self.rect.x + shift_x, self.rect.y + shift_y))
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    

    



pygame.init()

back = (100, 90, 255)
mw = pygame.display.set_mode((500,500))

#С большой буквы - класс, с маленькой - экземпляр
clock = pygame.time.Clock()
ketchup = [TextArea(15 + 120*x, 115, 110, 180, RED) for x in range(4)]
clicker = [TextArea(20 + 120*x, 120, 100, 170, YELLOW) for x in range(4)]
time_machine = pygame.font.Font('Comic Neue', 60).render('Время:', True, BLACK)
click_counter = pygame.font.Font('Comic Neue', 60).render('Счётчик:', True, BLACK)
winned = pygame.font.Font('Comic Neue', 60).render('ВЫ ПОБЕДИЛИ!!!', True, BLACK)
loser = pygame.font.Font('Comic Neue', 60).render('ВЫ ПРОИГРАЛИ(((', True, BLACK)
#question = TextArea(50, 120, 100, 170, YELLOW)
#question.set_text('click', 65,)
#answer = TextArea(120, 200, 290, 70)
#answer.set_text('Click', 27)
num = randint(0,3)
sleep = 18
time_data = 0
timer = pygame.font.Font('Comic Neue', 60).render(str(time_data) , True, BLACK)
poshuk = 0
game = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for cl in range(len(clicker)):
                clicker[cl].fill_color = YELLOW
                if clicker[cl].collidepoint(x, y):
                    if cl == num:
                        clicker[cl].fill_color = GREEN
                        poshuk += 1
                    else:
                        clicker[cl].fill_color = RED
                        poshuk -= 1
    if poshuk >= 5:
        game = False
        mw.fill(GREEN)
        mw.blit(winned,(110, 200))
    if time_data >= 11:
        game = False
        mw.fill(RED)
        mw.blit(loser,(110,200))
    if game:
        mw.fill(back)
        schet_poshuk = pygame.font.Font('Comic Neue', 60).render(str(poshuk) , True, BLACK)
        for ketch in ketchup:
            ketch.set_text("")
            ketch.draw()
        if sleep == 0:
            sleep = 18
            num = randint(0,3)
            time_data += 0.5
            timer = pygame.font.Font('Comic Neue', 60).render(str(int(time_data)) , True, BLACK)

        else:
            sleep -= 1
        for i, click in enumerate(clicker):
            if i == num:
                click.set_text('click', 65)
                
                
            else:
                click.set_text('')
            click.draw(shift_y = 55, shift_x = 8)
        mw.blit(time_machine, (10, 10))
        mw.blit(click_counter, (280, 10))
        mw.blit(timer, (20, 45))
        mw.blit(schet_poshuk, (300, 45))
    pygame.display.update()
    clock.tick(FPS)
