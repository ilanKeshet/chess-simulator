from src.board.Color import Color
from src.simulator.Player import Player
from src.simulator.RandomMovingPlayer import RandomMovingPlayer
from src.simulator.Simulator import Simulator


def main():
    simulator = Simulator(RandomMovingPlayer(Color.WHITE), RandomMovingPlayer(Color.BLACK))
    simulator.run()

if __name__ == "__main__":
    main()
