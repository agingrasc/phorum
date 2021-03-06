from phorum import combat
from phorum import player

DEFAULT_PLAYER_FILE = 'phorum/data/default_players.yml'


def read_raw_yaml(filename):
    with open(filename) as f:
        lines = f.readlines()

    return "".join(lines)


def main():
    raw_players_yaml = read_raw_yaml(DEFAULT_PLAYER_FILE)

    rotovino = player.PlayerLoader.load_from_raw_yaml(raw_players_yaml, 'Rotovino')
    atiay = player.PlayerLoader.load_from_raw_yaml(raw_players_yaml, 'Atiay')
    combat.rounds(rotovino, atiay)
    print("Rotovino: {}\nAtiay: {}".format(rotovino, atiay))

if __name__ == "__main__":
    main()
