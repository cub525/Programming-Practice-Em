# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:32:38 2021

@author: Emmett
"""
import numpy as np
import matplotlib.pyplot as plt
import pygame

SCREEN_DIMENSIONS = (90, 90)
BLACK = (0, 0, 0)
RUNNING = True
NUM_PARTICLES = 1
CHUNK_SIZE = 10
GRID_SHAPE = (
    SCREEN_DIMENSIONS[0] // CHUNK_SIZE,
    2,
    SCREEN_DIMENSIONS[1] // CHUNK_SIZE)


pot_data = np.zeros(GRID_SHAPE)
ppos = np.random.randint(1, min(SCREEN_DIMENSIONS), (2, NUM_PARTICLES), ).astype(float)
pvel = np.zeros((2, NUM_PARTICLES))

 
def calc_pot(pos_data: np.ndarray):
    out = np.zeros(GRID_SHAPE)
    x,y = np.mgrid[slice(out.shape[2]), slice(out.shape[0])]
    bin_data = np.floor_divide(pos_data, CHUNK_SIZE).astype(int)
    for b in bin_data.T:
        m = (x - b[0])**2 + (y - b[1])**2
        mask = m == 0
        val = np.ma.array(m, mask=mask)
        a = np.stack(((x - b[0])/val, (y - b[1]))/val, 1)
        out += a
    return out, bin_data

pygame.init()
pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode(SCREEN_DIMENSIONS)

background = pygame.Surface(SCREEN_DIMENSIONS)
background.fill(BLACK)

clock = pygame.time.Clock()
try:
    while RUNNING:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
        dt = clock.tick(60)
        window_surface.blit(background, (0, 0))
        pot_data[:] = 0
        for p in ppos.T:
            pygame.draw.circle(window_surface, (255, 255, 255), p, 2)
    
        pygame.display.update()
        pot_data, bin_data = calc_pot(ppos)
        pvel += pot_data[bin_data[1],:, bin_data[0]].T
        ppos += pvel
except Exception as e:
    pygame.quit()
    
    plt.pcolormesh(np.hypot(pot_data[:,1,:], pot_data[:,0,:]))
    plt.quiver(ppos[1] / CHUNK_SIZE, ppos[0] / CHUNK_SIZE, pvel[1], pvel[0])
    plt.colorbar()
    plt.scatter(ppos[1] / CHUNK_SIZE, ppos[0] / CHUNK_SIZE, color='r')
    raise e
pygame.quit()

plt.pcolormesh(np.hypot(pot_data[:,1,:], pot_data[:,0,:]))
plt.quiver(ppos[1] / CHUNK_SIZE, ppos[0] / CHUNK_SIZE, pvel[1], pvel[0])
plt.colorbar()
plt.scatter(ppos[1] / CHUNK_SIZE, ppos[0] / CHUNK_SIZE, color='r')