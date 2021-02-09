'''config file'''
import os

FPS = 24
SCREENSIZE = (600, 500)

IMAGE_PATHS = {
    'grass': os.path.join(os.getcwd(), 'resources/images/grass.png'),
    'arrow': os.path.join(os.getcwd(), 'resources/images/bullet.png'),
    'healthbar': os.path.join(os.getcwd(), 'resources/images/healthbar.png'),
    'health': os.path.join(os.getcwd(), 'resources/images/health.png'),
    'gameover': os.path.join(os.getcwd(), 'resources/images/gameover.png'),
    'youwin': os.path.join(os.getcwd(), 'resources/images/youwin.png'),
    'sk': os.path.join(os.getcwd(), 'resources/images/sk.jpg'),
    'type': os.path.join(os.getcwd(), 'resources/images/type.png'),
    'newgrass': os.path.join(os.getcwd(), 'resources/images/newgrass.png'),
    'ground': os.path.join(os.getcwd(), 'resources/images/back.png'),
    'train': os.path.join(os.getcwd(), 'resources/images/train.png'),
    'snake': os.path.join(os.getcwd(), 'resources/images/snake.png'),
    'apple': os.path.join(os.getcwd(), 'resources/images/apple.jpg')
}

SOUNDS_PATHS = {
    'hit': os.path.join(os.getcwd(), 'resources/audio/explode.wav'),
    'enemy': os.path.join(os.getcwd(), 'resources/audio/enemy.wav'),
    'shoot': os.path.join(os.getcwd(), 'resources/audio/shoot.wav'),
    'moonlight': os.path.join(os.getcwd(), 'resources/audio/moonlight.wav')
}

