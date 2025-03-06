# TODO

## Bugs

- FIXED: Crashes on close - Saving used file() instead of open()
- Enabling black holes disables planets (may also make planets invisible)

## Interface

- DONE: Add WASD controls
- Add mouse controls for menu

## Graphics

### Add screen resolution options
- Poll system for available resolutions

### Centre fullscreen mode
- Options for fullscreen or centred at current resolution

### Animate sprites
- Glowing lights
-  Damage animations (sparks, fire etc)

## Features

### Optional SFX
- Optional because in space no-one can hear you 
- Option to hear resonance when projectile approaches/passes
- Using SFXR (configurable)
- Menu sound (DONE)

### MUSIC
- Create some spacey loops / tracks (configurable)

### Add debug screen
- F12 to switch
- FPS
- Bounding boxes
- Path prediction

### Cinematic camera
- Limit switching between close and wide views for dramatic effect:
- if only leaving current view for very short time
- if collision or near-collision is predicted

### Add more planet types
- Ice planets
- Atmospheric planets
- Inhabited worlds with defences

### Collectable power-ups
- Weapon upgrades:
    - abortable projectile
    - magnetic projectile (seeks enemy ship within certain range)
    - multiple projectiles with spread
- Other power-ups:
    - Shields
    - One-time booster to change ship location
    - Teleport self to power-up location
    - Teleport enemy to power-up location
    - Swap player positions
