import App
import Custom.CrazyShipAbilities.Abilities

ET_INPUT_USE_ABILITY = 9999
USE_ABILITY_BUTTON_TITLE = "Use ability"

HasSetUpKeyHandler = 0

def SetUpKeyHandler():
    global HasSetUpKeyHandler
    if HasSetUpKeyHandler:
        return

    HasSetUpKeyHandler = 1
    App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(ET_INPUT_USE_ABILITY, __name__ + '.UseAbility')

def UseAbility(_pObject, _pEvent):
    Custom.CrazyShipAbilities.Abilities.UseAbility()