# Self-Driving 2D Car

**Author:** Artak Danielyan

## Project Overview

This project simulates a self-driving car using Python and Pygame.

The car follows a dark track using five simulated line sensors. Its autonomous driving system follows a Sense–Perceive–Plan–Act loop.

The project includes keyboard control, autonomous driving, proportional steering, a safety stop feature, and dynamic speed control.

## Requirements

- Python 3.13
- Pygame 2.6.1

## Installation

Clone the repository:

```bash
git clone https://github.com/artakdanielyanarm/self-driving-2d.git
cd self-driving-2d
```

Create and activate a Python 3.13 virtual environment:

```bash
python3.13 -m venv .venv313
source .venv313/bin/activate
```

Install Pygame:

```bash
python -m pip install pygame==2.6.1
```

## How to Run

Activate the virtual environment and run:

```bash
source .venv313/bin/activate
python main.py
```

## Controls

| Key | Action |
|---|---|
| Arrow Up | Increase speed |
| Arrow Down | Decrease speed |
| A | Toggle autopilot |
| R | Reset the car |
| ESC | Quit |

## Autonomous Driving

The autonomous driving system uses five simulated line sensors positioned at different angles.

The control loop follows three main operations:

1. **Sense:** Read the five sensor values.
2. **Think:** Calculate the steering command.
3. **Act:** Move the car using the steering command.

## Challenges

### Challenge A — Proportional Controller

Implemented proportional steering using:

```python
steer = KP * error
```

The selected proportional gain was `KP = 0.05`.

The controller was tested with different KP values and speeds. The selected value produced the lowest wobble among the tested configurations.

#### KP Tuning Results

| KP | Speed | Frames Off Line | Wobble |
|---|---:|---:|---:|
| 0.01 | 5 | 0 | 0.59 |
| 0.01 | 8 | 0 | 0.52 |
| 0.03 | 5 | 0 | 0.60 |
| 0.03 | 8 | 0 | 0.58 |
| 0.05 | 5 | 0 | 0.43 |
| 0.05 | 8 | 0 | 0.51 |
| 0.08 | 5 | 0 | 0.57 |
| 0.08 | 8 | 0 | 0.58 |
| 0.15 | 5 | 0 | 0.56 |
| 0.15 | 8 | 0 | 0.57 |

### Challenge B — Safety Stop

Added a safety feature that stops the car when all sensors lose the line for 30 consecutive frames.

This demonstrates the importance of a fail-safe system when sensor information becomes unreliable.

### Challenge C — Dynamic Speed Control

Implemented dynamic speed control based on the car's steering error.

The car slows down when it needs a larger steering correction and travels faster when the line is more centered.

Three-lap test results:

| Speed Control | Time |
|---|---:|
| Dynamic speed | 7.95 seconds |
| Constant speed of 8 | 10.00 seconds |

Dynamic speed control improved the three-lap time by approximately 20.5%.

## Project Files

- `main.py` — Main simulation with the implemented challenges.
- `main_proportional.py` — Proportional controller version.
- `main_challenge_b.py` — Safety stop implementation.

## Demo Video

[Watch the three-lap autonomous driving demo](https://drive.google.com/file/d/1qBay6oOnBYF59ULqQqQ4HQeWZeMdo2pu/view?usp=sharing)

## Repository

[GitHub Repository](https://github.com/artakdanielyanarm/self-driving-2d)