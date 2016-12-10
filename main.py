from game import GameOfLife

def main():
    pattern = [(20, 20),(20, 21), (20, 22), (20, 23), (20, 24), (20, 25)]
    game = GameOfLife(pattern)
    game.play()

if __name__ == "__main__":
   main()
