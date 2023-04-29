import pygame
import os
import main
import PygameUtils as pu
import draw_main
import wget

pygame.init()
pygame.font.init()
WIDTH = 1600
HEIGHT = 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont('Comic Sans MS', 30)
FPS = 60
radar_d = pu.checkbox((0, 0, 0), 123, 123, 50, 50, outline=4, text="Visualize")
download_c = pu.checkbox((0, 0, 0), 123, 200, 50, 50, outline=4, text="Download my assets and config files")

try:
    START = pygame.image.load(os.path.join("start.jpg"))
    DRAW = pygame.image.load(os.path.join("draw_track.png"))
except:
    start_btn_url = "https://raw.githubusercontent.com/timo42453189/car_drive_ai_files/main/start.jpg"
    draw_track_url = "https://raw.githubusercontent.com/timo42453189/car_drive_ai_files/main/draw_track.png"
    wget.download(start_btn_url)
    wget.download(draw_track_url)
    START = pygame.image.load(os.path.join("start.jpg"))
    DRAW = pygame.image.load(os.path.join("draw_track.png"))
DRAW = pygame.transform.scale(DRAW, (400, 300))


buttons = []

class Button():
	def __init__(self, WIN, IMG, name, x, y):
		self.IMG = IMG
		self.WIN = WIN
		self.NAME = name
		self.x = x
		self.y = y
		self.width = self.IMG.get_width()
		self.height = self.IMG.get_height()

	def show(self):
		# show img
		self.WIN.blit(self.IMG, (self.x, self.y))

	def get_name(self):
		return self.NAME

	def hit_mouse(self):
		# calculate if you press on the img
		mouse_pressed = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		if mouse_pressed[0]:
			if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
				return True
			else:
				return False

start = Button(WIN, START, "start", 500, 500)
buttons.append(start)
draw = Button(WIN, DRAW, "draw", 540, 600)
buttons.append(draw)

def main_screen():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        WIN.fill([255, 255, 255])
        for button in buttons:
            button.show()
            mouse_hit = button.hit_mouse()
            if mouse_hit:
                name = button.get_name()
                if name == "start":
                    main.run(draw_radar=radar_d.isChecked(), d=download_c.isChecked())
                if name == "draw":
                      draw_main.main()
		    
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos() 
        if mouse_pressed[0]:
            r = radar_d.isOver(mouse_pos)
            if r:
                  radar_d.convert()
            c = download_c.isOver(mouse_pos)
            if c:
                download_c.convert()

        radar_d.draw(WIN)
        download_c.draw(WIN)
        pygame.display.update()
	
main_screen()