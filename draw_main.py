import pygame
from drawing import Draw, Button
import os
import wget

def setup():
    global WIN, fill_color, buttons
    buttons = []
    WIDTH = 800
    HEIGHT = 400
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    fill_color = (255, 255, 255)
    
    try:
        SAVE = pygame.image.load(os.path.join("save.png"))
    except:
        save_url = "https://raw.githubusercontent.com/timo42453189/car_drive_ai_files/main/save.png"
        wget.download(save_url)
        SAVE = pygame.image.load(os.path.join("save.png"))
	
    SAVE = pygame.transform.scale(SAVE, (30, 30))
    save = Button(WIN, SAVE, "save", 760, 10)
    buttons.append(save)


circles = []
def main():
	setup()
	global circles, fill_color
	while 1:
		WIN.fill(fill_color)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.qiut()
				break

		mouse_pressed = pygame.mouse.get_pressed()
		if mouse_pressed[0]:
			drawing = True
			mouse_pos = pygame.mouse.get_pos()
			if drawing:
				draw = Draw(WIN, mouse_pos[0], mouse_pos[1], (0, 117, 255), 20)
				circles.append(draw)
				
		for circle in circles:
			circle.draw()
		
		for button in buttons:
			button.show()
			mouse_hit = button.hit_mouse()
			if mouse_hit:
				name = button.get_name()
				if name == "save":
					pygame.image.save(WIN, 'track.png' )
					exit()
			
		pygame.display.update()

