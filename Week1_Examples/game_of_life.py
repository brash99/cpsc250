import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def initialize_grid(size):
    grid = np.random.choice([0, 1], size=(size, size), p=[0.7, 0.3])
    return grid


def update_grid(grid):
    size = grid.shape[0]
    new_grid = np.zeros_like(grid)

    for i in range(size):
        for j in range(size):
            neighbors = grid[max(0, i - 1):min(i + 2, size), max(0, j - 1):min(j + 2, size)]
            num_alive = np.sum(neighbors) - grid[i, j]

            if grid[i, j] == 1 and (num_alive < 2 or num_alive > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and num_alive == 3:
                new_grid[i, j] = 1
            else:
                new_grid[i, j] = grid[i, j]

    return new_grid


def animate_grid(grid):
    fig = plt.figure()
    plt.axis('off')
    ims = []

    for i in range(400):
        ims.append((plt.imshow(grid, cmap='binary'),))
        grid = update_grid(grid)

    ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True, repeat_delay=1000)
    plt.show()


# Example usage
grid_size = 50
grid = initialize_grid(grid_size)
animate_grid(grid)