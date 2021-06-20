def get_location_json(player, map):
    curr_tile = map.map[player.ypos][player.xpos]
    location_json = {'location': False}
    if curr_tile.location is not None:
        location_json['location'] = True
        location_json['content'] = curr_tile.location.toJson()
    return location_json


def buy_item(player, map, slot):
    curr_tile = map.map[player.ypos][player.xpos]
    item = curr_tile.location.market.wares.pop(slot)
    player.money -= item.value
    player.inventory.append(item)
    return {'bought': item.toJson()}


def heal_player(player):
    player.hp = player.max_hp
    return {'healed': player.toJson()}