# 99 Nights with a Bear - Survival Game

A Python-based survival game using Pygame where you must survive 99 nights with a dangerous bear in a cave.

## Game Features

- **Day/Night Cycle**: The bear sleeps during the day but is aggressive at night
- **Forest Exploration**: Large forest area with trees to chop, animals to hunt, and abandoned houses with loot chests
- **Cave System**: A hidden cave with a big rock door that requires finding a secret button to open
- **Survival Mechanics**:
  - Hunt animals for meat
  - Cook food to increase hunger restoration
  - Gather vegetables and fish
  - Chop wood to make fire
  - Sleep in bed at night to survive (while avoiding the bear)
  
- **Dangerous Animals**: Wolves and other meat-eating creatures that will attack you
- **Water Area**: Fish in the sea and clean yourself in the water

## Installation

1. Install Python 3.7+
2. Install pygame:
   ```bash
   pip install pygame
   ```

## Running the Game

```bash
python main.py
```

## Controls

- **WASD**: Move around
- **E**: Interact with objects (chests, doors, animals)
- **C**: Cook raw meat
- **SPACE**: Sleep in bed (only at night)
- **ESC**: Pause game

## Game Objective

Survive 99 nights without getting caught by the bear!

## Strategy Tips

- During the day: Explore, hunt, gather resources, and chop wood
- Before night: Return to the cave and get into bed
- At night: Sleep in bed to avoid the bear
- Build up food supplies for emergencies
- Find and open chests for valuable loot

## Game Over Conditions

- Health reaches 0 (bear caught you or you starved)
- Successfully survive 99 nights = Victory!
