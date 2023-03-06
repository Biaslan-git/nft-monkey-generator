import os, sys
import random

from PIL import Image
from pysnooper import snoop

FONS_DIR = 'fons'
MONKEYS_DIR = 'monkeys'
KEPS_DIR = 'keps'
GLASSES_DIR = 'glasses'
MASKS_DIR = 'masks'

cur_dir = os.getcwd()+'/'
# print(cur_dir)

def choose_random_img(dir_name):
    dir = cur_dir+dir_name
    imgs = os.listdir(dir)
    imgs = [dir+'/'+x for x in imgs ]
    if dir_name not in [FONS_DIR, MONKEYS_DIR]:
        imgs += [None]
    return random.choice(imgs)

@snoop()
def main(iter=1):
    for _ in range(iter):
        layers = []

        # choose bg
        fon = choose_random_img(FONS_DIR) 
        fon = Image.open(fon)
        # choose monkey
        monkey = choose_random_img(MONKEYS_DIR)
        monkey = Image.open(monkey).convert('RGBA')
        layers.append(monkey)

        # Other elements
        kep = choose_random_img(KEPS_DIR)
        glasses = choose_random_img(GLASSES_DIR)
        mask = choose_random_img(MASKS_DIR)

        kep = Image.open(kep).convert('RGBA') if kep else None
        glasses = Image.open(glasses).convert('RGBA') if glasses else None
        mask = Image.open(mask).convert('RGBA') if mask else None

        layers += [kep, glasses, mask]

        # Clean list from NoneTypes
        layers = [x for x in layers if x]

        for layer in layers:
            fon.paste(layer, (0,0), layer)

        fon.show()

if len(sys.argv) > 1 and sys.argv[1].isdigit():
    main(int(sys.argv[1]))
else:
    main()
