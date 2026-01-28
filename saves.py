import json
import os

from world import Player, Bottyamon


def save(filename: str = "save.json"):
    # Importálás függvényen belül: elkerüli a körkörös importok miatti meglepetéseket,
    # és mindig a world aktuális globális állapotát olvassa.
    import world

    save_data = {
        "player": world.player.to_dict(),
        # Új formátum: több Bottyamon támogatása
        "bottyamons": [b.to_dict() for b in world.Bottyamons],
        # Régi (legacy) kulcs: visszafelé kompatibilitás régi mentésekkel / kódrészekkel
        "bottyamon": world.Bottyamons[0].to_dict() if world.Bottyamons else None,
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(save_data, f, indent=4, ensure_ascii=False)

def read_save(filename="save.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    player = Player(**data["player"])

    # Új formátum: lista
    if isinstance(data.get("bottyamons"), list):
        bottyamons = [Bottyamon(**b) for b in data["bottyamons"]]
    # Régi formátum: egyetlen objektum
    elif isinstance(data.get("bottyamon"), dict):
        bottyamons = [Bottyamon(**data["bottyamon"])]
    else:
        bottyamons = []

    return player, bottyamons