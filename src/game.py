from .grid import Grid
from .player import Player
from . import pickups



player = Player(2, 1)
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)

# Räkna ut mitten av spelplanen
mid_x = g.width // 2
mid_y = g.height // 2

# Placera spelaren till mitten av spelplanen
player = Player(mid_x, mid_y)
g.set_player(player)

def player_move(player, grid, dx, dy):
    global score
    # Vi tittar på om spelaren kan röra sig (vad som finns på rutan vi ska flytta oss till)
    if player.can_move(dx, dy, grid):
        # Drar av ett poäng för varje steg spelaren kan ta
        score -= 1
        maybe_item = grid.get(player.pos_x + dx, player.pos_y + dy)
        player.move(dx, dy)

        if isinstance(maybe_item, pickups.Item):
            # Ökar totala poängen med
            score += maybe_item.value
            # Sparar items i listan 'inventory'
            inventory.append(maybe_item.name)
            print(f'You found a {maybe_item.name}, +{maybe_item.value} points.')
            grid.clear(player.pos_x, player.pos_y)




# TODO: flytta denna till en annan fil
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g)
    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    dx = 0
    dy = 0

    # Riktningsval
    if command == 'w':
        player_move(player, g, 0, -1)
    elif command == 'a':
        player_move(player, g, -1, 0)
    elif command == 's':
        player_move(player, g, 0, 1)
    elif command == 'd':
        player_move(player, g, 1, 0)
    elif command == 'i':
        print('Ditt inventory:\n')
        if not inventory:
            print('Ditt inventory är tomt')
        else:
            # Här loopar vi igenom hela listan och skriver ut det som plockats upp
            for item in inventory:
                print(item)



# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
