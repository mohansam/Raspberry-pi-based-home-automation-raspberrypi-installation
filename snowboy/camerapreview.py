import sys
import pygame
import pygame.camera
import maingui
pygame.init()
pygame.camera.init()
Display= pygame.display.set_mode((800,480))
cam = pygame.camera.Camera("/dev/video0",(800,480))
def cam_init():
      global cam
      cam.start()
      cam.set_controls(hflip = False, vflip = True)
def close(msg=None):
      global cam
      cam.stop()
      maingui.main_window()
      
def cam_window():
      cam_init()
      single_click=True
      while True:
            image = cam.get_image()
            Display.blit(image,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        close()
                  elif event.type==pygame.MOUSEBUTTONDOWN:
                        close()
            
 

if __name__ == "__main__":
     cam_window()
