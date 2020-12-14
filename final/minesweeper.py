import random
import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1graphics import *


def initialize_value(tiles):
    """Initializes value of each Tile object in tiles"""
    # Write codes for initialize_value() here
    n = len(tiles)
    m = len(tiles[0])
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    def is_out(x, y):
        return x < 0 or x > n-1 or y < 0 or y > m-1

    for i in range(n):
        for j in range(m):
            if not tiles[i][j].mine:
                cnt = 0
                for x in dx:
                    for y in dy:
                        if (not is_out(i+x, j+y)) and tiles[i+x][j+y].mine:
                            cnt += 1
                tiles[i][j].value = cnt
    # END
    pass


def speed_dig(board):
    """Performs speed dig"""
    # Write codes for speed_dig() here
    n = board.height
    m = board.width
    def is_out(x, y):
        return x < 0 or x > n-1 or y < 0 or y > m-1
    
    dx_ = [-1, 0, 1]
    dy_ = [-1, 0, 1]
    y, x = board.cursor

    def perform_dig(x, y):
        if board.tiles[x][y].hidden:
            return
        flag_cnt = 0
        for dx in dx_:
            for dy in dy_:
                if (not is_out(dx+x, dy+y)) and board.tiles[x+dx][y+dy].flagged:
                    flag_cnt += 1
        if flag_cnt != board.tiles[x][y].value:
            return
        for dx in dx_:
            for dy in dy_:
                if (not is_out(dx+x, dy+y)) and not board.tiles[x+dx][y+dy].flagged:
                    board.dig([y+dy, x+dx])
    
    perform_dig(x, y)
    # END
    pass


def check_win(tiles):
    """Checks if every tile not containing mine in tiles is uncovered

    :return: True if the player has won, otherwise False
    """
    # Write codes for check_win() here
    n = len(tiles)
    m = len(tiles[0])

    for i in range(n):
        for j in range(m):
            if not tiles[i][j].mine and tiles[i][j].hidden:
                return False
    return True
    # END
    pass


_board = None


def create_board():
    """To start the game, create Minesweeper object and call draw_scene function"""

    global _board
    if _board:
        raise RuntimeError("A world already exists!")
    _board = Minesweeper(10, 9,
                         13)  # It is okay to change the board's size or the number of mines for debugging purposes
    _board.draw_scene()


def restart_board():
    """To restart the game, close scene and call create_board function"""

    global _board
    if not _board:
        raise RuntimeError("A world doesn't exist!")
    _board._scene.close()
    _board = None
    create_board()


class Tile(object):
    def __init__(self):
        self.hidden = True  # if the tile is hidden or not
        self.flagged = False  # if the tile is flagged or not
        self.mine = False  # if the tile has a mine or not
        self.value = 0  # the number of adjacent mines


class Minesweeper(object):
    def __init__(self, width, height, num_mines):
        """Sets up both UI and game logic"""

        self.width = width
        self.height = height
        self.game_over = False  # if the game is finished or not
        self.cursor = [0, 0]  # cursor's initial position / [col, row]
        self.num_flags = num_mines  # the number of flags left to display

        if num_mines > self.width * self.height:
            print('Number of mines cannot exceed number of tiles!')
            exit()

        # Generate mines' positions randomly and apply them to Tile objects
        self.tiles = list()
        mine_indices = random.sample(range(self.width * self.height), k=num_mines)
        for i in range(self.height):  # 1st index indicates which row
            tile_row = list()
            for j in range(self.width):  # 2nd index indicates which column
                tile_obj = Tile()
                if i * self.width + j in mine_indices:
                    tile_obj.mine = True
                    tile_obj.value = -1
                tile_row.append(tile_obj)
            self.tiles.append(tile_row)

        initialize_value(self.tiles)  # to initialize each value of tiles

    def draw_scene(self):
        """Makes the UI using a cs1graphics.Canvas object
        Function for graphics only, which you don't need to read
        """

        multiplier = 2
        self._tile_length = 16 * multiplier
        self._info_height = 32 * multiplier
        self._padding = 10 * multiplier
        self._border_width = 2 * multiplier
        self._scene_width = self.width * self._tile_length + self._padding * 2
        self._scene_height = self.height * self._tile_length + self._padding * 3 + self._info_height
        self._scene = Canvas(self._scene_width, self._scene_height, (192, 192, 192))
        self._scene.setTitle("Minesweeper")

        self._value_to_color = {
            1: (0, 0, 255),
            2: (0, 123, 0),
            3: (255, 0, 0),
            4: (0, 0, 123),
            5: (123, 0, 0),
            6: (0, 123, 123),
            7: (255, 255, 255),
            8: (123, 123, 123),
        }

        half_border_width = self._border_width / 2

        padding_color = (189, 189, 189)
        self._border_color_dark = (123, 123, 123)
        self._border_color_white = (255, 255, 255)

        outline_white_coords = [
            [(half_border_width, self._scene_height - half_border_width), (half_border_width, half_border_width),
             (self._scene_width - half_border_width, half_border_width)],
            [(self._padding - half_border_width, self._padding + self._info_height + half_border_width), (
                self._scene_width - self._padding + half_border_width,
                self._padding + self._info_height + half_border_width),
             (self._scene_width - self._padding + half_border_width, self._padding - half_border_width)],
            [(self._padding - half_border_width, self._scene_height - self._padding + half_border_width), (
                self._scene_width - self._padding + half_border_width,
                self._scene_height - self._padding + half_border_width), (
                 self._scene_width - self._padding + half_border_width,
                 self._padding * 2 + self._info_height - half_border_width)]
        ]
        for coords in outline_white_coords:
            outline = Path(*[Point(*coord) for coord in coords])
            outline.move(0.5, 0.5)
            outline.setBorderColor(self._border_color_white)
            outline.setBorderWidth(self._border_width)
            outline.setDepth(1)
            self._scene.add(outline)

        outline_dark_coords = [
            [(half_border_width, self._scene_height - half_border_width),
             (self._scene_width - half_border_width, self._scene_height - half_border_width),
             (self._scene_width - half_border_width, half_border_width)],
            [(self._padding - half_border_width, self._padding + self._info_height + half_border_width),
             (self._padding - half_border_width, self._padding - half_border_width),
             (self._scene_width - self._padding + self._border_width, self._padding - half_border_width)],
            [(self._padding - half_border_width, self._scene_height - self._padding + half_border_width),
             (self._padding - half_border_width, self._padding * 2 + self._info_height - half_border_width), (
                 self._scene_width - self._padding + half_border_width,
                 self._padding * 2 + self._info_height - half_border_width)]
        ]
        for coords in outline_dark_coords:
            outline = Path(*[Point(*coord) for coord in coords])
            outline.move(-0.5, -0.5)
            outline.setBorderColor(self._border_color_dark)
            outline.setBorderWidth(self._border_width)
            self._scene.add(outline)

        self.text_flags = Text('Flags left: %02d' % self.num_flags, self._tile_length, Point(0, 0))
        self.text_flags.moveTo(self._scene_width / 2, self._padding + self._info_height / 2)
        self.text_flags.setFontColor('red')
        self._scene.add(self.text_flags)

        for i in range(self.height):
            tile_line = Path(Point(self._padding, self._padding * 2 + self._info_height + self._tile_length * i),
                             Point(self._scene_width - self._padding,
                                   self._padding * 2 + self._info_height + self._tile_length * i))
            tile_line.setBorderColor(self._border_color_dark)
            tile_line.setBorderWidth(half_border_width)
            self._scene.add(tile_line)
        for i in range(self.width):
            tile_line = Path(Point(self._padding + self._tile_length * i, self._padding * 2 + self._info_height),
                             Point(self._padding + self._tile_length * i, self._scene_height - self._padding))
            tile_line.setBorderColor(self._border_color_dark)
            tile_line.setBorderWidth(half_border_width)
            self._scene.add(tile_line)

        x0 = self._tile_length / 2 + self._padding
        y0 = self._tile_length / 2 + self._padding * 2 + self._info_height

        self.tile_layers = list()
        for i in range(self.height):
            tile_layer_row = list()
            for j in range(self.width):
                tile_layer = Layer()
                self._create_hidden(tile_layer)

                tile_layer.moveTo(x0 + self._tile_length * j, y0 + self._tile_length * i)
                self._scene.add(tile_layer)
                tile_layer_row.append(tile_layer)
            self.tile_layers.append(tile_layer_row)

        self.cursor_box = Square(self._tile_length, Point(0, 0))
        self.cursor_box.setBorderColor('Red')
        self.cursor_box.setBorderWidth(self._border_width)
        self._scene.add(self.cursor_box)
        self.move_cursor()

    def move_cursor(self):
        """Handles a movement of the cursor
        Function for graphics only, which you don't need to read
        """

        x0 = self._tile_length / 2 + self._padding
        y0 = self._tile_length / 2 + self._padding * 2 + self._info_height
        self.cursor_box.moveTo(x0 + self._tile_length * self.cursor[0], y0 + self._tile_length * self.cursor[1])

    def _create_mine(self, layer):
        """Function for graphics only, which you don't need to read
        """
        unit_length = self._border_width / 2
        mine_layer = Layer()

        mine_line_coords = [[(0, -6), (0, 6)], [(-6, 0), (6, 0)], [(-4, -4), (4, 4)], [(-4, 4), (4, -4)]]
        for mine_line_coord in mine_line_coords:
            mine_line = Path(*[Point(coord[0] * unit_length, coord[1] * unit_length) for coord in mine_line_coord])
            mine_line.setBorderWidth(unit_length)
            mine_layer.add(mine_line)

        mine_circle = Circle(unit_length * 4, Point(0, 0))
        mine_circle.setFillColor('Black')
        mine_circle.setBorderWidth(0)
        mine_layer.add(mine_circle)

        mine_square = Square(unit_length * 2, Point(0, 0))
        mine_square.setFillColor('White')
        mine_square.setBorderWidth(0)
        mine_square.moveTo(-unit_length * 1.5, -unit_length * 1.5)
        mine_layer.add(mine_square)

        layer.add(mine_layer)

    def _create_hidden(self, layer):
        """Function for graphics only, which you don't need to read
        """
        half_border_width = self._border_width / 2

        tile_outline1 = Path(Point(0, self._tile_length - self._border_width - half_border_width / 2), Point(0, 0),
                             Point(self._tile_length - self._border_width, 0))
        tile_outline1.setBorderColor(self._border_color_white)
        tile_outline1.setBorderWidth(self._border_width)
        tile_outline1.move(-self._tile_length / 2 + half_border_width, -self._tile_length / 2 + half_border_width)
        tile_outline1.setDepth(self._border_width)
        layer.add(tile_outline1)

        tile_outline2 = Path(Point(0, self._tile_length - self._border_width),
                             Point(self._tile_length - self._border_width, self._tile_length - self._border_width),
                             Point(self._tile_length - self._border_width, 0))
        tile_outline2.setBorderColor(self._border_color_dark)
        tile_outline2.setBorderWidth(self._border_width)
        tile_outline2.move(-self._tile_length / 2 + half_border_width, -self._tile_length / 2 + half_border_width)
        layer.add(tile_outline2)

    def _mark_flag(self, selected_layer):
        """Function for graphics only, which you don't need to read"""

        half_border_width = self._border_width / 2

        flag_black = Polygon(Point(0, 0), Point(0, half_border_width * 2),
                             Point(half_border_width * 3, half_border_width * 3.5),
                             Point(half_border_width * 3, half_border_width * 4),
                             Point(half_border_width * (-4), half_border_width * 4),
                             Point(half_border_width * (-4), half_border_width * 3), Point(0, half_border_width * 2))
        flag_black.move(half_border_width, 0)
        flag_black.setFillColor('Black')
        flag_black.setBorderWidth(half_border_width)
        selected_layer.add(flag_black)

        flag_red = Polygon(Point(0, 0), Point(0, half_border_width * (-4)),
                           Point(half_border_width * (-1), half_border_width * (-4)),
                           Point(half_border_width * (-4), half_border_width * (-2.5)))
        flag_red.move(half_border_width, 0)
        flag_red.setFillColor('Red')
        flag_red.setBorderWidth(half_border_width)
        flag_red.setBorderColor('Red')
        selected_layer.add(flag_red)

    def dig(self, pos):
        """Performs the dig action on the given coordinate and handles linked UI changes"""

        selected_tile = self.tiles[pos[1]][pos[0]]
        if not selected_tile.hidden:  # skip the process if the tile is already opened
            return
        selected_tile.hidden = False  # open the tile

        selected_layer = self.tile_layers[pos[1]][pos[0]]
        selected_layer.clear()

        if not selected_tile.mine:
            if selected_tile.value > 0:  # display the digit
                # For graphics only, which you don't need to read
                text_value = Text('%1d' % selected_tile.value, self._tile_length / 2, Point(0, 0))
                text_value.setFontColor(self._value_to_color[selected_tile.value])
                selected_layer.add(text_value)
            elif selected_tile.value == 0:  # automatically dig adjacent tiles
                for i in range(pos[1] - 1, pos[1] + 2):
                    for j in range(pos[0] - 1, pos[0] + 2):
                        if i < 0 or i >= self.height or j < 0 or j >= self.width:
                            continue
                        self.dig((j, i))
            self.game_over = check_win(self.tiles)  # to check if the player has won and display it if so
            if self.game_over:  # game is over after digging no mine -> process victory
                # For graphics only, which you don't need to read
                for i in range(self.height):
                    for j in range(self.width):
                        if i == pos[1] and j == pos[0]:
                            continue
                        tile_obj = self.tiles[i][j]
                        if tile_obj.mine:
                            selected_layer = self.tile_layers[i][j]
                            selected_layer.clear()
                            self._create_hidden(selected_layer)
                            self._mark_flag(selected_layer)

                try:
                    self._scene.remove(self.cursor_box)
                    self.text_flags.setMessage('You win!')
                except:
                    pass
        else:  # digging a mine -> process defeat
            # For graphics only, which you don't need to read
            square_mine = Square(self._tile_length, Point(0, 0))
            square_mine.setBorderWidth(0)
            square_mine.setFillColor('Red')
            selected_layer.add(square_mine)

            self._create_mine(selected_layer)

            self.game_over = True
            self.text_flags.setMessage('You lose!')

            for i in range(self.height):
                for j in range(self.width):
                    if i == pos[1] and j == pos[0]:
                        continue
                    tile_obj = self.tiles[i][j]
                    if tile_obj.mine:
                        tile_layer = self.tile_layers[i][j]
                        tile_layer.clear()
                        self._create_mine(tile_layer)

        if self.game_over:  # The game is over in eihter way, no more cursor moves
            try:
                self._scene.remove(self.cursor_box)
            except:
                pass

    def flag(self):
        """Performs the flag action on the given coordinate and handles linked UI changes"""

        selected_tile = self.tiles[self.cursor[1]][self.cursor[0]]
        if not selected_tile.hidden:  # skip the process if the tile is already opened
            return

        selected_layer = self.tile_layers[self.cursor[1]][self.cursor[0]]
        if selected_tile.flagged:  # unflag
            selected_tile.flagged = False
            self.num_flags += 1

            selected_layer.clear()
            self._create_hidden(selected_layer)
        else:  # flag
            selected_tile.flagged = True
            self.num_flags -= 1

            self._mark_flag(selected_layer)

        self.text_flags.setMessage('Flags left: %d' % self.num_flags)


def interact():
    """Handles the player's keyboard input"""

    while True:
        e = _board._scene.wait()
        d = e.getDescription()
        if d == 'keyboard':
            k = e.getKey().lower()
            if k == 'q':  # halts the game
                _board._scene.close()
                break
            elif k == 'r':  # resets the game
                restart_board()
            elif not _board.game_over:
                if k == 'd':  # dig
                    _board.dig(_board.cursor)
                elif k == 'f':  # flag
                    _board.flag()
                elif k == 's':  # speed dig
                    speed_dig(_board)
                else:
                    if k == 'i' and _board.cursor[1] > 0:  # up
                        _board.cursor[1] -= 1
                    elif k == 'k' and _board.cursor[1] < _board.height - 1:  # down
                        _board.cursor[1] += 1
                    elif k == 'j' and _board.cursor[0] > 0:  # left
                        _board.cursor[0] -= 1
                    elif k == 'l' and _board.cursor[0] < _board.width - 1:  # right
                        _board.cursor[0] += 1

                _board.move_cursor()  # redraw the cursor


if __name__ == '__main__':
    create_board()
    interact()
