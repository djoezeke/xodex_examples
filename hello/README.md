# hello Project.

## Overview
This project is built using Xodex.

## Project Structure
```
hello
├── hello
│   ├── __init__.py
│   ├── __main__.py        # Entry point to run project as module.
│   ├── settings.py        # Project Configurations and Settings. 
│   ├── objects            # Directory to Create and Register Objects.
│   │   ├── __init__.py
│   │   └── objects.py     # To Register Project Game Objects.
│   └── scenes             # Directory to create and register Scenes.
│       ├── __init__.py
│       └── scenes.py      # To Register Project Game Scenes.
├── manage.py              # Project Management utilities. 
├── .gitignore             # Project Git Ignore Files
└── README.md              # Project Documentation.
```


## Getting Started
To run the hello game, follow these steps:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd hello
   ```

2. **Install dependencies**:
   Ensure you have Python installed. You may need to install additional libraries depending on your game implementation.

   ```
   pip install -r requirements.txt
   ```

3. **Run the game**:
   Execute the following command:
   ```
   python manage.py run
   ```
   or 
   ```
   python -m hello
   ```
   
4. **Building the game**:
To build the game executable using PyInstaller, run:
```
python manage.py build
```
This will create a standalone executable in the `dist` directory.


## Gameplay
- Use the arrow keys to control the paddles.
- The game features a main menu where you can start the game or exit.
- You can pause the game by pressing the designated pause key (to be defined in settings).

## Usage
After building the game, you can distribute the executable found in the `dist` folder. Users can run the game without needing to install Python or any dependencies.

## Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements for the game.

## License
This project is licensed under the MIT License. See the LICENSE file for details.