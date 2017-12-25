import pygame.camera
pygame.camera.init()
cam = pygame.cameraimport pygame.camera
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
img = cam.get_image()
import pygame.image
pygame.image.save(img, "mantour1.jpg")
pygame.camera.quit()
