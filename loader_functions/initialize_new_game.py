from components.equipment import Equipment
from components.equippable import Equippable
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level

from entity import Entity

from equipment_slots import EquipmentSlots

from game_messages import MessageLog

from game_states import GameStates

from map_utils import GameMap, make_map

from render_functions import RenderOrder


def get_constants():
    window_title = 'Roguelike Tutorial Hack'

    screen_width = 80
    screen_height = 50

    bar_width = 20
    panel_height = 7
    panel_y = screen_height - panel_height

    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height - 1

    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    fov_algorithm = 'BASIC'
    fov_light_walls = True
    fov_radius = 10

    max_monsters_per_room = 3
    max_items_per_room = 2

    colors = {
        'dark_wall': (0, 0, 100),
        'dark_ground': (50, 50, 150),
        'light_wall': (130, 110, 50),
        'light_ground': (200, 180, 50),
        'desaturated_green': (63, 127, 63),
        'darker_green': (0, 127, 0),
        'dark_red': (191, 0, 0),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'red': (255, 0, 0),
        'orange': (255, 127, 0),
        'light_red': (255, 114, 114),
        'darker_red': (127, 0, 0),
        'violet': (127, 0, 255),
        'yellow': (255, 255, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0),
        'light_cyan': (114, 255, 255),
        'light_pink': (255, 114, 184),
        'light_yellow': (255, 255, 114),
        'light_violet': (184, 114, 255),
        'sky': (0, 191, 255),
        'darker_orange': (127, 63, 0),

        # Primary color:
        'red_0': (170, 57, 57),
        'red_1': (255,170,170),
        'red_2': (212,106,106),
        'red_3': (128, 21, 21),
        'red_4': ( 85,  0,  0),

        # Secondary color (1):
        'brown_0': (170,108, 57),
        'brown_1': (255,209,170),
        'brown_2': (212,154,106),
        'brown_3': (128, 69, 21),
        'brown_4': ( 85, 39,  0),

        # Secondary color (2):
        'blue_0': ( 34,102,102),
        'blue_1': (102,153,153),
        'blue_2': ( 64,127,127),
        'blue_3': ( 13, 77, 77),
        'blue_4': (  0, 51, 51),

        # Complement color:
        'green_0': ( 45,136, 45),
        'green_1': (136,204,136),
        'green_2': ( 85,170, 85),
        'green_3': ( 17,102, 17),
        'green_4': (  0, 68,  0)
    }

    constants = {
        'window_title': window_title,
        'screen_width': screen_width,
        'screen_height': screen_height,
        'bar_width': bar_width,
        'panel_height': panel_height,
        'panel_y': panel_y,
        'message_x': message_x,
        'message_width': message_width,
        'message_height': message_height,
        'map_width': map_width,
        'map_height': map_height,
        'room_max_size': room_max_size,
        'room_min_size': room_min_size,
        'max_rooms': max_rooms,
        'fov_algorithm': fov_algorithm,
        'fov_light_walls': fov_light_walls,
        'fov_radius': fov_radius,
        'max_monsters_per_room': max_monsters_per_room,
        'max_items_per_room': max_items_per_room,
        'colors': colors
    }

    return constants


def get_game_variables(constants):
    fighter_component = Fighter(hp=100, defense=1, power=2)
    inventory_component = Inventory(26)
    level_component = Level()
    equipment_component = Equipment()
    player = Entity(0, 0, '@', constants['colors'].get('blue_1'), 'Player', blocks=True, render_order=RenderOrder.ACTOR,
                    fighter=fighter_component, inventory=inventory_component, level=level_component,
                    equipment=equipment_component)
    entities = [player]

    equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=2)
    dagger = Entity(0, 0, '-', constants['colors'].get('sky'), 'Dagger', equippable=equippable_component)
    player.inventory.add_item(dagger, constants['colors'])
    player.equipment.toggle_equip(dagger)

    game_map = GameMap(constants['map_width'], constants['map_height'])
    make_map(game_map, constants['max_rooms'], constants['room_min_size'],
             constants['room_max_size'], constants['map_width'], constants['map_height'], player, entities,
             constants['colors'])

    message_log = MessageLog(constants['message_x'], constants['message_width'],
                             constants['message_height'])

    game_state = GameStates.PLAYERS_TURN

    return player, entities, game_map, message_log, game_state
