from engine.constants.pallete.greyshades import GreyShades
from engine.roots.alt.sprite import Sprite
from engine.characters.playable.polys.fighter import Fighter
from engine.tools.turntable import Turntable
from engine.tools.collections.interacts import Interacts
from engine.tools.collections.solids import Solids
from engine.blocks.trampoline import Trampoline
from engine.blocks.death import DeathWheel
from engine.blocks.rotated import Rotated
from engine.blocks.healer import Healer
from engine.blocks.spike import Spike
from engine.blocks.boat import Boat
from engine.blocks.lift import Lift
from engine.characters.base.monos.mobster import Mobster
from engine.constants.animates import Animates
from engine.constants.window import Window
from engine.tools.camera import Camera
import engine.roots.tiles.gym as rm
import pygame as pg
import random as rd
pg.init()


def main():
    grey = GreyShades()
    anime = Animates()
    wnd = Window()
    surface = pg.display.set_mode(wnd.wnd_size, pg.HWSURFACE)
    clock = pg.time.Clock()
    running: bool = True
    # path_dummy = 'Game_Objects/Hellish/Animals/Deadman_pixian_ai.png'
    sizes = (wnd.size, wnd.size * 2)
    pos = (wnd.size * 10, wnd.wnd_size[1] + wnd.size * 165)
    com_beg = 'Game_Objects/Turtles/Boss/Spirit/Movements/'
    com_end = '_pixian_ai.png'
    stay = com_beg + 'Stay' + com_end
    step1 = com_beg + 'Step1' + com_end
    step2 = com_beg + 'Step2' + com_end
    turtle_paths = [stay, step1, step2]
    turtle = Fighter(sizes,
                     pos,
                     turtle_paths,
                     gravity=wnd.size * 12,
                     jump=-wnd.size * 80,
                     speed=wnd.size * 6,
                     attack=wnd.size * 80)
    dx = wnd.wnd_size[0] * .5 - turtle.rect.width
    dy = wnd.wnd_size[1] - wnd.size * 5 - turtle.rect.height
    camera = Camera(delta=(dx, dy))
    music_path = 'Music/Battlefield-.ogg'
    turntable = Turntable(music_path)
    group = Solids()
    interacts = Interacts()
    path_tramp = 'Game_Objects/Textures/Blocks/Red.png'
    path_block = 'Game_Objects/Textures/Blocks/Gray80.png'
    path_spike = 'Game_Objects/Extra1/Windows/Wastebasket_pixian_ai.png'
    path_wheel = 'Game_Objects/Extra1/Windows/TotalSecurity_pixian_ai.png'
    path_healer = 'Game_Objects/Extra2/WeirdPlants/Gidnora_pixian_ai.png'
    path_mobster = 'Game_Objects/Extra1/Demons/Demon1_pixian_ai.png'
    path_rotated = 'Game_Objects/Numbers/1_pixian_ai.png'
    wheel_radius = wnd.size * 5
    wheel_speed = 3
    tramp_jump = -wnd.size * 160
    spike_attack = wnd.size * 6
    mobster_attack = wnd.size * 8
    mobster_speed = wnd.size * 5
    for row_index, row in enumerate(rm.tile):
        y = row_index * wnd.size
        for col_index, cell in enumerate(row):
            x = col_index * wnd.size
            pos_b, sizes_b = (x, y), (wnd.size, wnd.size)
            if cell == 'G':
                block = Sprite(sizes_b, pos_b, path_block)
                group.append(block)
            elif cell == 'T':
                block = Trampoline(sizes_b, pos_b, path_tramp, tramp_jump)
                interacts.append(block)
            elif cell == 'S':
                pos_b, sizes_b = (x, y - wnd.size), (wnd.size, wnd.size * 2)
                spike = Spike(sizes_b, pos_b, path_spike, tramp_jump, spike_attack)
                interacts.append(spike)
            elif cell == 'W':
                n = rd.randint(0, 1)
                if n == 1:
                    wheel_speed *= -1
                wheel = DeathWheel(sizes_b, wheel_radius, path_wheel, pos_b,
                                   wheel_speed, tramp_jump, spike_attack)
                interacts.append(wheel)
            elif cell == 'H':
                sizes_b = (wnd.size * 3, wnd.size * 3)
                pos_b = (x, y - wnd.size * 2)
                healer = Healer(sizes_b, pos_b, path_healer)
                interacts.append(healer)
            elif cell == 'M':
                end = x + wnd.size * 9
                sizes_b = (wnd.size * 3, wnd.size * 3)
                pos_b = (x, y - wnd.size * 2)
                mobster = Mobster(sizes_b, pos_b, path_mobster, tramp_jump,
                                  mobster_attack, mobster_speed, end=end)
                interacts.append(mobster)
            elif cell == 'L':
                end = y + wnd.size * 14
                sizes_b = (wnd.size * 3, wnd.size * 2)
                lift = Lift(sizes_b, pos_b, path_block, mobster_speed, end=end)
                group.append(lift)
            elif cell == 'R':
                sizes_b = wnd.size, wnd.size * 6
                pos_b = x, y - wnd.size * 4
                rotated = Rotated(sizes_b, pos_b, path_rotated, points=111)
                rotated.rotation.frame_time = .007
                n = rd.randint(0, 1)
                if n == 0:
                    rotated.right = not rotated.right
                group.append(rotated)
            elif cell == 'B':
                sizes_b = wnd.size * 5, wnd.size * 2
                pos_b = x, y - wnd.size
                end = x + wnd.size * 72
                boat = Boat(sizes_b, pos_b, path_block, mobster_speed, end=end)
                group.append(boat)
            else:
                continue
    while running:
        clock.tick(anime.fps1)
        turntable.play()
        surface.fill(grey.aluminum)
        group.draws(surface)
        group.updates()
        group.shifts()
        interacts.draws(surface)
        interacts.updates()
        interacts.shifts()
        interacts.interacts(turtle)
        turtle.draw(surface)
        turtle.update()
        group.hor_collisions(turtle)
        turtle.shifting()
        group.ver_collisions(turtle)
        camera.world_shift(character=turtle, blocks=group, interacts=interacts)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    running = False
                else:
                    continue
            else:
                continue


if __name__ == '__main__':
    main()
