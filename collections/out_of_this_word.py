import random

WORDS = (
    'treehouse',
    'python',
    'learner',
)

# def prompt_for_words(challenge):
#     guesses = set()
#     print('What words can you find in the word {}'.format(challenge))
#     print('(Enter Q to Quit)');
#     while True:
#         guess = input('{} words > '.format(len(guesses)))

# challenge_word = random.choice(WORDS)

# def get_locations(cells):
#     _output = random.sample(cells, 3)
#     output = set(_output)
#     return output

# print(get_locations(WORDS))

# def move(player, direction):
#     x, y, hp = player
#     _x, _y = direction
#     horizontal_destination = x + _x
#     vertical_destination = y + _y
#     hit_wall = horizontal_destination < 0
#     hit_ceiling = vertical_destination > 9
#     if hit_wall or hit_ceiling:
#         hp -= 5
#     if hit_wall:
#         x = 0
#     if hit_ceiling:
#         y = 9
#     if hit_wall != True and hit_ceiling != True:
#         x = horizontal_destination
#         y = vertical_destination
#     return x, y, hp

# print(move((0, 9, 5), (0, 1)))

TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for tile in TILES:
    new_line = '\n'
    empty = ''
    is_pipe = tile == '||'
    is_not_pipe = is_pipe == False
    if is_not_pipe:
        print(tile, end=empty)
    if is_pipe:
        print(new_line)