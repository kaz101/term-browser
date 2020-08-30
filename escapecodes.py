''' A module that is a repository of ansi escape codes'''

class Ansi:
    ''' ASNI escape codes '''
    def __init__(self):
        self.reset = '\u001b[0m'
        self.color_list = ['red', 'green', 'black', 'yellow', 'blue', 'magenta',
                           'cyan', 'white', 'br_black', 'br_red', 'br_green',
                           'br_yellow', 'br_blue', 'br_magenta', 'br_cyan',
                           'br_white']
    def color(self, color):
        ''' Returns ANSI code for forground color '''
        colors = {}
        colors['red'] = '\u001b[31m'
        colors['green'] = '\u001b[32m'
        colors['black'] = '\u001b[30m'
        colors['yellow'] = '\u001b[33m'
        colors['blue'] = '\u001b[34m'
        colors['magenta'] = '\u001b[35m'
        colors['cyan'] = '\u001b[36m'
        colors['white'] = '\u001b[37m'
        colors['br_black'] = '\u001b[90m'
        colors['br_red'] = '\u001b[91m'
        colors['br_green'] = '\u001b[92m'
        colors['br_yellow'] = '\u001b[93m'
        colors['br_blue'] = '\u001b[94m'
        colors['br_magenta'] = '\u001b[95m'
        colors['br_cyan'] = '\u001b[96m'
        colors['br_white'] = '\u001b[97m'
        try:
            return colors[color]
        except KeyError:
            print('color not found')

    def bg_color(self, color):
        ''' Returns ANSI code for Background colors '''
        # Background Colours
        colors = {}
        colors['red'] = '\u001b[41m'
        colors['green'] = '\u001b[42m'
        colors['black'] = '\u001b[40m'
        colors['yellow'] = '\u001b[43m'
        colors['blue'] = '\u001b[44m'
        colors['magenta'] = '\u001b[45m'
        colors['cyan'] = '\u001b[46m'
        colors['white'] = '\u001b[47m'
        colors['br_black'] = '\u001b[100m'
        colors['br_red'] = '\u001b[101m'
        colors['br_green'] = '\u001b[102m'
        colors['br_yellow'] = '\u001b[103m'
        colors['br_blue'] = '\u001b[104m'
        colors['br_magenta'] = '\u001b[105m'
        colors['br_cyan'] = '\u001b[106m'
        colors['br_white'] = '\u001b[107m'
        try:
            return colors[color]
        except KeyError:
            print('color not found')

    def effects(self, effect):
        ''' Returns ANSI code for text effects '''
        # Text effects
        effects = {}
        effects['bold'] = '\u001b[1m'
        effects['faint'] = '\u001b[2m'
        effects['italic'] = '\u001b[3m'
        effects['underline'] = '\u001b[4m'
        effects['rapid_blink'] = '\u001b[6m'
        effects['invert'] = '\u001b[7m'
        effects['hide'] = '\u001b[8m'
        effects['strikethrough'] = '\u001b[9m'
        effects['double_underline'] = '\u001b[21m'
        effects['underline_off'] = '\u001b[24m'
        effects['blink_off'] = '\u001b[25m'
        effects['inverse_off'] = '\u001b[27m'
        effects['show'] = '\u001b[28m'
        effects['strikthrough_off'] = '\u001b[29m'
        effects['framed'] = '\u001b[51m'
        effects['encircled'] = '\u001b[52m'
        effects['overlined'] = '\u001b[53m'
        effects['framed_off'] = '\u001b[54m'
        effects['overlined_off'] = '\u001b[55m'
        try:
            return effects[effect]
        except KeyError:
            print('effect not found')

    def cursor(self, direction, spaces=1):
        ''' Codes for cursor movement '''
        moves = {}
        moves['up'] = f'\u001b[{str(spaces)}A'
        moves['down'] = f'\u001b[{str(spaces)}B'
        moves['right'] = f'\u001b[{str(spaces)}C'
        moves['left'] = f'\u001b[{str(spaces)}D'
        moves['next_ln'] = f'\u001b[{str(spaces)}E'
        moves['previous_ln'] = f'\u001b[{str(spaces)}F'
        moves['horizontal_abs'] = f'\u001b[{str(spaces)}G'
        moves['clr_ln_ahead'] = '\u001b[0K'
        moves['clr_ln_behind'] = '\u001b[1K'
        moves['clr_ln'] = '\u001b[2K'
        moves['clr_scr'] = '\u001b[2J'
        moves['clr_scr_ahead'] = '\u001b[0J'
        moves['clr_scr_behind'] = '\u001b[1J'
        moves['scroll_up'] = f'\u001b[{str(spaces)}S'
        moves['scroll_down'] = f'\u001b[{str(spaces)}T'
        try:
            return moves[direction]
        except KeyError:
            print('woops!')
