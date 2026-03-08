class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        ny_x = self.pos_x + x
        ny_y = self.pos_y + y

        # Vad finns på spelarens nya position
        ny_ruta = grid.get(ny_x, ny_y)

        # Returnera True om det inte är vägg på nya positionen
        return ny_ruta != grid.wall


