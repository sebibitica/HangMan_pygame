import pygame
import random
import os
import math

pygame.init()

#pentru WINDOW
WIDTH = 1280
HEIGHT = 720
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPANZURATOAREA")
icon=pygame.transform.scale(pygame.image.load(os.path.join('grafica','icon.png')),(32,32)) #imaginea icon
pygame.display.set_icon(icon) #seteaza iconita sus stanga in window

#pentru a rula jocul cu 60 fps
FPS = 60
clock=pygame.time.Clock()
run = True

#GRAFICA (IMAGINI) :
pBackground=pygame.image.load(os.path.join('grafica','back.png')) #imaginea fundal
#imaginile cu spanzuratoarea:
p=[] #un vector (fiecare pozitie are imaginea lui)
poza=pygame.image.load(os.path.join('grafica','0.png'))
p.append(poza) #punem poza in p[0]...
poza=pygame.image.load(os.path.join('grafica','1.png'))
p.append(poza) #punem poza in p[1]... si asa mai departe
poza=pygame.image.load(os.path.join('grafica','2.png'))
p.append(poza)
poza=pygame.image.load(os.path.join('grafica','3.png'))
p.append(poza)
poza=pygame.image.load(os.path.join('grafica','4.png'))
p.append(poza)
poza=pygame.image.load(os.path.join('grafica','5.png'))
p.append(poza)
poza=pygame.image.load(os.path.join('grafica','6.png'))
p.append(poza)
pozaver=pygame.image.load(os.path.join('grafica','6.png'))

greseli = 0 #tine cont de greseli -> pentru a putea seta imaginea corespunzatoare
cuvinte = ["LUCEAFARUL", "ELEV", "CALCULATOR","MONITOR","MANCARE","PROGRAMARE","VACANTA","IARNA","GHIOZDAN","CHITARA","FEMEIE"]
cuvant = random.choice(cuvinte)
gasite = []


#font: pentru a lua literele si a le pune ulterior in Butoane
pygame.font.get_fonts()
font = pygame.font.SysFont('calibri',45,15)
font_cuvant = pygame.font.SysFont('calibri',60,30)


#butoanele pentru litere
RADIUS = 30
GAP = 20
letters= []
startx = round((WIDTH-(RADIUS*2 + GAP)*13)/2)
starty = 100

A=65 #caracterul A are codul ASCII 65, B-66, C-67,...


#aici setam distanta intre butoane
for i in range(26):
	x=startx+ GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13)) #formula poz x(centru)
	y=starty+ ((i // 13)*(GAP + RADIUS * 2)) #formula poz y(centru)
	letters.append([x,y,chr(A+i),True]) #salvam in vectorul letters 3 elemente(x,y,si litera)


#grafica jocului:
def draw():
	#imaginea de fundal
	WIN.blit(pBackground,(0,0))
	#cuvantul
	cuvant_afisat="" #cuvantul de afisat e gol daca nicio litera nu a fost ghicita
	for letter in cuvant:
		if letter in gasite:
			cuvant_afisat+=letter + " " #daca se gaseste litera -> se afiseaza in loc de "_" : LITERA
		else:
			cuvant_afisat+="_ " #daca nu se gaseste litera -> continua sa se afiseze "_"
	text = font_cuvant.render(cuvant_afisat,1,(0,0,0))
	WIN.blit(text,(50,330))
	#butoane
	for letter in letters:
		x, y, litera,visible = letter #fiecare punct "letter" are 3 elemente(pozitia x, pozitia y, litera coresp.a)
		if(visible):
			pygame.draw.circle(WIN, (211,123,15), (x,y) , RADIUS, 100) #aici se deseneaza butoanele(cercuri)
			text = font.render(litera, 1 ,(255,255,255)) #aici punem in variabila text-> litera corespunzatoare (A,B,..)
			WIN.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2)) #in interiorul cercului: plasam litera (in centru)
	#spanzuratoarea baza
	WIN.blit(p[greseli],(700,300))
	pygame.display.update()



def main():
	global greseli
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: #daca se apasa X -> se inchide
				run = False
			if event.type == pygame.MOUSEBUTTONUP: #afla pozitia mouse-ului pe ecran cand este apasat CLICK
				mousex,mousey=pygame.mouse.get_pos() #pozitia x si pozitia y a mouse-ului in momentul CLICK-ului
				for letter in letters:
					x,y,litera,visible=letter
					if visible: # daca litera(butonul) respectiv nu a fost apasat -> e vizibil || altfel acesta dispare
						distanta=math.sqrt((x - mousex)**2 + (y - mousey)**2) #distanta intre centrul Butonului si pozitia MOUSE-ului
						if distanta<RADIUS:  #daca mouse-ul e in interiorul butonului-> atunci se prelucreaza litera respectiva
							letter[3] = False #aici setam vizibilitatea cu FALS dupa ce am apasat litera coresp. odata
							gasite.append(litera)
							if litera not in cuvant:
								greseli+=1
		draw()
		verif=True
		for leter in cuvant:
			if leter not in gasite:
				verif=False
				break
		if verif:
			pygame.time.delay(300)
			WIN.fill((0,255,0))
			textcuv=font_cuvant.render(cuvant,1,(0,0,0))
			text=font_cuvant.render("AI CASTIGAT! :)", 1 , (0,0,0))
			WIN.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2))
			WIN.blit(textcuv,(WIDTH/2-text.get_width()/2,HEIGHT/4-text.get_height()/2))
			pygame.display.update()
			pygame.time.delay(3000)
			break;
		if greseli == 6:
			pygame.time.delay(300)
			WIN.fill((255,0,0))
			textcuv=font_cuvant.render(cuvant,1,(0,0,0))
			text=font_cuvant.render("AI PIERDUT! :(", 1 , (0,0,0))
			WIN.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2))
			WIN.blit(textcuv,(WIDTH/2-text.get_width()/2,HEIGHT/4-text.get_height()/2))
			pygame.display.update()
			pygame.time.delay(3000)
			break;

main()

pygame.quit()
