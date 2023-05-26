import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def initialize_grid(size, type):
    if type == 0:
        starting_grid = np.random.choice([0, 1], size=(size, size), p=[0.7, 0.3])
    else:
        starting_grid = np.zeros((size, size))

        if type == 1:
            starting_coords = [
                (1, 1), (2, 1), (3, 1)
            ]
        else:
            if type == 2:
                starting_coords = [
                    (1, 2), (2, 0), (2, 2), (3, 1), (3, 3)
                ]
            else:
                if type == 3:
                    starting_coords = [
                        (41, 1), (41, 4),
                        (42, 0),
                        (43, 0), (43, 4),
                        (44, 0), (44, 1), (44, 2), (44, 3)
                    ]
                else:
                    if type == 4:
                        starting_coords = [
                            (2, 4), (2, 5), (2, 6), (2, 10), (2, 11), (2, 12),
                            (4, 2), (4, 7), (4, 9), (4, 14),
                            (5, 2), (5, 7), (5, 9), (5, 14),
                            (6, 2), (6, 7), (6, 9), (6, 14),
                            (7, 4), (7, 5), (7, 6), (7, 10), (7, 11), (7, 12),
                            (9, 4), (9, 5), (9, 6), (9, 10), (9, 11), (9, 12),
                            (10, 2), (10, 7), (10, 9), (10, 14),
                            (11, 2), (11, 7), (11, 9), (11, 14),
                            (12, 2), (12, 7), (12, 9), (12, 14),
                            (14, 4), (14, 5), (14, 6), (14, 10), (14, 11), (14, 12)
                        ]

        # Place the coordinates on the grid
        for coord in starting_coords:
            x, y = coord
            starting_grid[x, y] = 1

    return starting_grid


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
if __name__ == "__main__":
    grid_size = 100
    game_type = 0
    my_grid = initialize_grid(grid_size, game_type)
    animate_grid(my_grid)

