from BDD.BDD import BDD
from Menu.Menu import Menu


def main():
    menu = Menu()
    menu.get_menu_choice()
    db.create_player_table()
    db.create_stats_table()
    db.create_game_info()
    db.close_connexion()


db = BDD()
main()
