Simple tetris game to run via console in Unix based systems.
Its using the lib `curses` to print the game and capture the keyboard events.

# Run the game
```
python main.py
```
Keys:
```
a = move left
s = move down
d = move right
w = rotate the shape
```


# Requirements
- python3.10 >


# Run tests
Its using pytest so you have to install the dependencies:
```
pip install -r requirements.txt

pytest -vv

# to check test coverage

./coverage.sh
```
