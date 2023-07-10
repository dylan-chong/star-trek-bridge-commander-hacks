# Dylan's Star Trek Bridge Commander Mods

From before I make them into actual mods

Hacks before they turn into actual mods. NOTE: These are *hacks* and definitely *not* beautiful, tidy code.
One day, I'll tidy it up.

## Features

- A bunch of modifications to existing ships, completely changing their gameplay.
    - Each of the ships also have their own ability that can be triggered by the key `B`.
    - The ships that can be used are listed by their filename in `scripts\Custom\CrazyShipAbilities\PerShip\SOME_SHIP_NAME.py`
        - You can try a ship and it's abilities out in Quick Battle.
        - To choose a ship for the campaign, see [Choosing a ship for campaign](#choosing-a-ship-for-the-campaign)
    - Each of these ships have been balanced so that you can play the campaign with a reasonable level of challenge
        - (of course, you can customise the difficulty on the main menu screen before you start a mission)
        - Note that you may not be able to load your saves, but you can still start from the mission where you left off
    - NOTE: Ships that create other ships do not work in multiplayer yet (unless you are playing that ship as the host; still the game is unstable as it cannot handle many ships).

## Custom keybinds

This mod creates some unconfigurable keybinds. Make sure that you don't configure your own keybinds that conflict with this key:

- `B`: Use ability

## Choosing a ship for the campaign

- Open the `scripts\MissionLib.py` file in a text editor, e.g., Notepad++
- Find `def CreatePlayerShip` using CTRL-F
- A few lines below it says `sShipClass = 'SomeShipNameHere'`
- Replace the ship name in the quotes with the ship name of whatever you like

---

## Installation

1. Install Git Bash for Windows
1. Install fresh version of game from GOG Games
    1. Set the `C:\GOG Games\Star Trek Bridge Commander\stbc.exe` compatibility mode to 'Windows XP Service Pack 3'
    1. (Sanity check) Open the game and it should open, and you should be able to start a quick battle
1. Download the 4GB memory mod from <https://www.nexusmods.com/startrekbridgecommmander/mods/4012>
    1. Run the `4gb_patch.exe`
    1. (Sanity check) Open the game and it should open, and you should be able to start a quick battle
1. Download the Bridge Commander Remastered mod from <https://www.nexusmods.com/startrekbridgecommmander/mods/4012>:
    1. Install the mod as per the `INSTALLATION` section in `BCRemastered Features & Installation.txt`
    1. (Sanity check) Open the game and it should open, and you should be able to start a quick battle
1. Clone this repo
    1. Move the `.git` directory from the repo into your `/c/GOG Games/Star Trek Bridge Commander` directory.
    1. You can now delete the cloned project
1. Inside the `/c/GOG Games/Star Trek Bridge Commander` directory, run (using `bash`):
    1. `git checkout .gitignore` to create the `.gitignore file`
    1. `rm -r py` to remove the unnecessary python folder
1. Open the game
    1. Go to *Configure > Controls > Default* to set up the default keybinds for this mod
    1. If you have custom keybinds, feel free to configure them now. Just beware, of the custom keybinds this mod defines in [Custom Keybinds](#custom-keybinds)
1. (Sanity check) You should be able to start a quick battle
    1. Use the `Defiant` as the player ship.
    2. In combat, you should be able to press `B` to trigger a dash ability
1. Create a ZIP/RAR of the `C:\GOG Games\Star Trek Bridge Commander` folder as a backup. This game is mildly unstable and it is useful to have a backup of the game to restore to if the game stops loading up for some reason.

---

# Developer stuff

## Git Structure

Only files that have been modified from either the stock game or Bridge Commander Remastered (see installation) have been committed.
The original versions of the files are committed in their own commits formatted as `[Original] Msg...`, throughout various points in time.
The point of this is to allow you to diff the changes to the file that this mod has made.

## Adding new files

1. Add an exclusion `!/path/to/file` to the `.gitignore` file at the bottom
1. Then make a commit committing the original version of that file(s)
1. Then make your changes and commit those

## TODO

- Fix: Engineer menu ability and report buttons are blank in multiplayer
- Fix: Rebalance Prometheus for campaign
- Feature: Implement sending ship modifications across stream
    - This will fix:
        - Client wall does not get scaled
        - When a client uses Nova, drones to not target anything
        - When a client launches nuke, speed is not set on server
    - Need to:
        - Mission6.py
            - Add a new custom message type below `AI_LIST_MESSAGE =`
            - Add a new elif case for the new message type at the end of `def ProcessMessageHandler`
            - Add new MultiplayerLib function `MPUpdateShipPropsOnHost(shipName)` or something.
                - Go with speed updating first
            - In XOMenuHandlers, replace nuke speed then trigger MP update if MP
- Feature: Defiant speed boost is not based on current velocity, by unitizing the velocity, so you don't need the current speed
- Feature: Scimitar Speed boost is not based on current velocity, by unitizing the velocity, so you don't need the current speed
- Feature: Nova Speed boost is not based on current velocity, by unitizing the velocity, so you don't need the current speed
- Test: Shuttle nuke launching in multiplayer
    - Investigate?: Client can't see the explosion
        - Explosion mods may not have applied
- Test: Can you get someone else to host the game so i can test stuff

## Possible TODO

- Feature: Nuke has a glow effect (may make it clearer in multiplayer)
- Feature: New ship with a large cutting beam using a stream of non-tracking disruptors (krenim ship?)
- Feature: New mage ship with suck and power drain abilities (breen?)
- Feature: New ship that can launch large rocks

## Not TODO

- Maybe unfixable: Multiplayer crashes a lot when theres not that many ships, but still quite a few
- Maybe unfixable: Akira in multiplayer sending torpedoes at high speed doesn't work for clients, but does for the master
- Feature: Prometheus sniper beam just drains shields and does little to hull
    - See scripts\Effects.py `PhaserHullHit`
    - Full impulse makes it hard to do knock back. Event handler does not allow cancelling propagation of event to prevent damage

## Compile all modules helper

If you get errors in multiplayer about a version mismatch, you'll have to force all python files to be recompiled on the server.
You can do this by simply importing all of the modules.

```bash
find . -name '*.py' | \
   perl -pe 's/\.\/scripts\///' | \
   perl -pe 's/.py$//' | \
   perl -pe 's/\/__init__//' | \
   perl -pe 's/\//./g' | \
   perl -pe 's/(.*)/"$1",/' \
   > all_modules.txt
```

Then inside `XOMenuHandlers.py`, inside the `CreateMenus` function, slap this in

```python
modules = [
    # Insert all_modules.txt here
]
for module in modules:
    print(__import__(module))

raise "Woohoo all modules successfully compiled + imported"
```

Note that this doesn't always work. I had an issue where the above would not recompile a single
Python file, but deleting the .pyc file and then running the above worked.
