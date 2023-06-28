# Dylan's Star Trek Bridge Commander Mods

From before I make them into actual mods

Hacks before they turn into actual mods. NOTE: These are *hacks* and definitely *not* beautiful, tidy code.
One day, I'll tidy it up.

## Git Structure

Only files that have been modified from either the stock game or Bridge Commander Remastered (see installation) have been committed.
The original versions of the files are committed in their own commits formatted as `[Original] Msg...`, throughout various points in time.
The point of this is to allow you to diff the changes to the file that this mod has made.

## Installation

1. Install fresh version of game from `Star.Trek.Bridge.Commander.v1.1.GOG`
    1. Set computer resolution to 1080p at most
    1. Open the game to see if it works
1. Run the `4gb_patch`
    1. Open the game to see if it works
1. Install `BC Remastered V1.2-4012-1-2-1659759164` as per the `INSTALLATION` section in `BCRemastered Features & Installation.txt`
    1. Open the game to see if it works
1. Move all of the contents (including the `.git` directory) into your `/c/GOG Games/Star Trek Bridge Commander` directory.

## Adding new files

1. Add an exclusion `!/path/to/file` to the `.gitignore` file at the bottom
1. Then make a commit committing the original version of that file(s)
1. Then make your changes and commit those

----

# Random other notes

## TODO

- Test: Fix wall ship is not set up properly in multiplayer
    - Investigate?: Client wall does not get scaled
- Test: Shuttle nuke launching in multiplayer
    - Investigate?: Client can't see the explosion
- Test: Can you get someone else to host the game so i can test stuff
- Investigate?: When a client uses Nova, drones to not target anything
- Possible Feature: Speed boost is not based on current velocity, by unitizing the velocity, so you don't need the current speed
- Possible Feature: New ship with a large cutting beam using a stream of non-tracking disruptors (krenim ship?)
- Possible Feature: New mage ship with suck and power drain abilities (breen?)
- Possible Feature: New ship that can launch large rocks
- Maybe unfixable: Multiplayer crashes a lot when theres not that many ships, but still quite a few
- Maybe unfixable: Akira in multiplayer sending torpedoes at high speed doesn't work for clients, but does for the master

## Compile all modules helper

If you get errors in multiplayer about a version mismatch, you'll have to force all python files to be recompiled.
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
