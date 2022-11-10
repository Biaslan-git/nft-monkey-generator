import os
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
    return random.choice(imgs)

@snoop()
def main(iter=1):
    for i in range(iter):
        rand_fon = choose_random_img(FONS_DIR)
        fon = Image.open(rand_fon)

        rand_monkey = choose_random_img(MONKEYS_DIR)
        monkey = Image.open(rand_monkey).convert('RGBA')

        rand_kep = choose_random_img(KEPS_DIR)
        kep = Image.open(rand_kep).convert('RGBA')

        rand_glasses = choose_random_img(GLASSES_DIR)
        glasses = Image.open(rand_glasses).convert('RGBA')

        rand_mask = choose_random_img(MASKS_DIR)
        mask = Image.open(rand_mask).convert('RGBA')

        fon.paste(monkey, (0,0), monkey)
        fon.paste(kep, (0,0), kep)
        fon.paste(glasses, (0,0), glasses)
        fon.paste(mask, (0,0), mask)

        fon.show()

main()
