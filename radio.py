import yaml
from mpyg321.MPyg321Player import MPyg321Player
import sys, termios, tty, os

fdInput = sys.stdin.fileno()
termAttr = termios.tcgetattr(0)
player = MPyg321Player()
DIFM_KEY = os.environ.get("DIFM_KEY", "")


with open("stations.yaml", "r") as f:
    station_data = yaml.safe_load(f)
    stations = {str(k):v for k,v in station_data["stations"].items()}
    extra_stations = [v for k,v in station_data["stations"].items() if k not in range(1,8)]


def getch():
    tty.setraw(fdInput)
    ch = sys.stdin.buffer.raw.read(4).decode(sys.stdin.encoding)
    if len(ch) == 1:
        if ord(ch) < 32 or ord(ch) > 126:
            ch = ord(ch)
    elif ord(ch[0]) == 27:
        ch = '\033' + ch[1:]
    termios.tcsetattr(fdInput, termios.TCSADRAIN, termAttr)
    return ch


def play_station(station):
    url = f"http://prem1.di.fm:80/{station['slug']}_hi?{DIFM_KEY}"
    print(f"Playing station: {station['name']} from URL: {url}")
    player.play_song(url)


def main():
  extra_stations_index = 0
  play_station(stations["1"])
  while True:
    print("Choose a station:")
    for i, station in stations.items():
        print(f"{i}. {station['name']}")
    print("Q. Quit")
    c = getch()

    choice = c.strip().upper()
    print(choice)
    if choice == 'Q':
        print("Exiting...")
        sys.exit(0)
    elif choice == "8":
        extra_stations_index = (extra_stations_index + 1) % len(extra_stations)
        play_station(extra_stations[extra_stations_index])
    elif choice in stations:
        play_station(stations[choice])

if __name__ == "__main__":
  main()
