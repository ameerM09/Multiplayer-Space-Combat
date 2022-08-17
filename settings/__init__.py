import pygame
import random
import os

from pygame.locals import *	

# Initializing pygame libraries
pygame.init()
pygame.display.init()
pygame.font.init()
pygame.mixer.init()

from .setup import *
from .assets import *
from .button import *
from .heart_health import *