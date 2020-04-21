from src.board.Color import Color
from src.simulator.Player import Player
from src.simulator.Simulator import Simulator


def main():
    simulator = Simulator(Player(Color.WHITE), Player(Color.BLACK))
    simulator.run()

if __name__ == "__main__":
    main()
