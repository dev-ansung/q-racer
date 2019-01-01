import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from world import World
from test_maps import rectangle

# Initialize new world
world = World()
world.set_map(rectangle)

# For demo:
world.add_racer((5,5), 0)
world.racers[0].velocity=(0,1)

# Game update
def gameUpdate(*args):
    world.update()
    im.set_data(world.world_map)
    return im,

# Initialize renderer
screen = plt.figure()
im = plt.imshow(world.world_map, cmap='gray', vmin=0, vmax=255, animated=True)
ani = animation.FuncAnimation(screen, gameUpdate, frames=1000, interval=1, blit=False)
plt.show()