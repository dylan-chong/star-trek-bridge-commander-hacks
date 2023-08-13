# File: D (Python 1.5)

import App
import Custom.CrazyShipAbilities.KeyBinds

def Initialize():
    App.g_kKeyboardBinding.BindKey(App.WC_BACKQUOTE, App.TGKeyboardEvent.KS_NORMAL, App.ET_INPUT_TOGGLE_CONSOLE, App.KeyboardBinding.GET_EVENT, 0, App.KeyboardBinding.KBT_LOCKOUT_CHANGE)
    App.g_kKeyboardBinding.BindKey(App.WC_ESCAPE, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TOGGLE_OPTIONS, App.KeyboardBinding.GET_EVENT, 0, App.KeyboardBinding.KBT_LOCKOUT_CHANGE)
    App.g_kKeyboardBinding.BindKey(App.WC_EQUALS, App.TGKeyboardEvent.KS_NORMAL, App.ET_INPUT_ZOOM, App.KeyboardBinding.GET_FLOAT_EVENT, 0.25)
    App.g_kKeyboardBinding.BindKey(App.WC_MINUS, App.TGKeyboardEvent.KS_NORMAL, App.ET_INPUT_ZOOM, App.KeyboardBinding.GET_FLOAT_EVENT, -0.25)
    App.g_kKeyboardBinding.BindKey(App.WC_ADD, App.TGKeyboardEvent.KS_NORMAL, App.ET_INPUT_ZOOM, App.KeyboardBinding.GET_FLOAT_EVENT, 0.25)
    App.g_kKeyboardBinding.BindKey(App.WC_SUBTRACT, App.TGKeyboardEvent.KS_NORMAL, App.ET_INPUT_ZOOM, App.KeyboardBinding.GET_FLOAT_EVENT, -0.25)
    App.g_kKeyboardBinding.BindKey(App.WC_NUMPAD1, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SELECT_X, App.KeyboardBinding.GET_INT_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_NUMPAD2, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SELECT_X, App.KeyboardBinding.GET_INT_EVENT, 2)
    App.g_kKeyboardBinding.BindKey(App.WC_NUMPAD3, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SELECT_X, App.KeyboardBinding.GET_INT_EVENT, 3)
    App.g_kKeyboardBinding.BindKey(App.WC_NUMPAD4, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SELECT_X, App.KeyboardBinding.GET_INT_EVENT, 4)
    App.g_kKeyboardBinding.BindKey(App.WC_NUMPAD5, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SELECT_X, App.KeyboardBinding.GET_INT_EVENT, 5)
    App.g_kKeyboardBinding.BindKey(App.WC_NUMPAD6, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SELECT_X, App.KeyboardBinding.GET_INT_EVENT, 6)
    App.g_kKeyboardBinding.BindKey(App.WC_NUMPAD7, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SELECT_X, App.KeyboardBinding.GET_INT_EVENT, 7)
    App.g_kKeyboardBinding.BindKey(App.WC_NUMPAD8, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SELECT_X, App.KeyboardBinding.GET_INT_EVENT, 8)
    App.g_kKeyboardBinding.BindKey(App.WC_NUMPAD9, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SELECT_X, App.KeyboardBinding.GET_INT_EVENT, 9)
    App.g_kKeyboardBinding.BindKey(App.WC_ALT_T, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_OTHER_BEAM_TOGGLE_CLICKED, App.KeyboardBinding.GET_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_ALT_C, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_OTHER_CLOAK_TOGGLE_CLICKED, App.KeyboardBinding.GET_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_UP, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SELECT_OPTION, App.KeyboardBinding.GET_INT_EVENT, -1)
    App.g_kKeyboardBinding.BindKey(App.WC_DOWN, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SELECT_OPTION, App.KeyboardBinding.GET_INT_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_RIGHT, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_PRE_SELECT_OPTION, App.KeyboardBinding.GET_INT_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_RIGHT, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_SELECT_OPTION, App.KeyboardBinding.GET_INT_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_NUMPADENTER, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_PRE_SELECT_OPTION, App.KeyboardBinding.GET_INT_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_NUMPADENTER, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_SELECT_OPTION, App.KeyboardBinding.GET_INT_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_LEFT, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_CLOSE_MENU, App.KeyboardBinding.GET_INT_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_R, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SET_IMPULSE, App.KeyboardBinding.GET_FLOAT_EVENT, -2.0 / 9.0)
    App.g_kKeyboardBinding.BindKey(App.WC_0, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SET_IMPULSE, App.KeyboardBinding.GET_FLOAT_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_1, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SET_IMPULSE, App.KeyboardBinding.GET_FLOAT_EVENT, 1.0 / 9.0)
    App.g_kKeyboardBinding.BindKey(App.WC_2, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SET_IMPULSE, App.KeyboardBinding.GET_FLOAT_EVENT, 2.0 / 9.0)
    App.g_kKeyboardBinding.BindKey(App.WC_3, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SET_IMPULSE, App.KeyboardBinding.GET_FLOAT_EVENT, 3.0 / 9.0)
    App.g_kKeyboardBinding.BindKey(App.WC_4, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SET_IMPULSE, App.KeyboardBinding.GET_FLOAT_EVENT, 4.0 / 9.0)
    App.g_kKeyboardBinding.BindKey(App.WC_5, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SET_IMPULSE, App.KeyboardBinding.GET_FLOAT_EVENT, 5.0 / 9.0)
    App.g_kKeyboardBinding.BindKey(App.WC_6, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SET_IMPULSE, App.KeyboardBinding.GET_FLOAT_EVENT, 6.0 / 9.0)
    App.g_kKeyboardBinding.BindKey(App.WC_7, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SET_IMPULSE, App.KeyboardBinding.GET_FLOAT_EVENT, 7.0 / 9.0)
    App.g_kKeyboardBinding.BindKey(App.WC_8, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SET_IMPULSE, App.KeyboardBinding.GET_FLOAT_EVENT, 8.0 / 9.0)
    App.g_kKeyboardBinding.BindKey(App.WC_9, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SET_IMPULSE, App.KeyboardBinding.GET_FLOAT_EVENT, 9.0 / 9.0)
    App.g_kKeyboardBinding.BindKey(App.WC_EXCLAMATION, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_SET_ALERT_LEVEL, App.KeyboardBinding.GET_INT_EVENT, App.CharacterClass.EST_ALERT_GREEN)
    App.g_kKeyboardBinding.BindKey(App.WC_AT_SIGN, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_SET_ALERT_LEVEL, App.KeyboardBinding.GET_INT_EVENT, App.CharacterClass.EST_ALERT_YELLOW)
    App.g_kKeyboardBinding.BindKey(App.WC_NUMBER_SIGN, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_SET_ALERT_LEVEL, App.KeyboardBinding.GET_INT_EVENT, App.CharacterClass.EST_ALERT_RED)
    App.g_kKeyboardBinding.BindKey(App.WC_SHIFT, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_ALLOW_CAMERA_ROTATION, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_SHIFT, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_ALLOW_CAMERA_ROTATION, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_Z, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_ZOOM_TARGET, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_Z, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_ZOOM_TARGET, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_W, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TURN_UP, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_W, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_TURN_UP, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_A, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TURN_LEFT, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_A, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_TURN_LEFT, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_S, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TURN_DOWN, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_S, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_TURN_DOWN, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_D, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TURN_RIGHT, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_D, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_TURN_RIGHT, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_Q, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_ROLL_LEFT, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_Q, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_ROLL_LEFT, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_E, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_ROLL_RIGHT, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_E, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_ROLL_RIGHT, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_F, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_FIRE_PRIMARY, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_F, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_FIRE_PRIMARY, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_X, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_FIRE_SECONDARY, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_X, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_FIRE_SECONDARY, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_G, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_FIRE_TERTIARY, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_G, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_FIRE_TERTIARY, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_LBUTTON, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_FIRE_PRIMARY, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_LBUTTON, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_FIRE_PRIMARY, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_RBUTTON, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_FIRE_SECONDARY, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_RBUTTON, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_FIRE_SECONDARY, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_MBUTTON, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_FIRE_TERTIARY, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_MBUTTON, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_FIRE_TERTIARY, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_PRINTSCREEN, App.TGKeyboardEvent.KS_KEYUP, App.ET_INPUT_PRINT_SCREEN, App.KeyboardBinding.GET_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_OPEN_BRACKET, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TOGGLE_SCORE_WINDOW, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_CLOSE_BRACKET, App.TGKeyboardEvent.KS_NORMAL, App.ET_INPUT_TOGGLE_CHAT_WINDOW, App.KeyboardBinding.GET_BOOL_EVENT, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_BACKSLASH, App.TGKeyboardEvent.KS_NORMAL, App.ET_INPUT_TOGGLE_CHAT_WINDOW, App.KeyboardBinding.GET_BOOL_EVENT, 1)
    App.g_kKeyboardBinding.BindKey(App.WC_BACKSPACE, App.TGKeyboardEvent.KS_NORMAL, App.ET_INPUT_SKIP_EVENTS, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_F1, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TALK_TO_HELM, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_F2, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TALK_TO_TACTICAL, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_F3, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TALK_TO_XO, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_F4, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TALK_TO_SCIENCE, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_F5, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TALK_TO_ENGINEERING, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_F6, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TALK_TO_GUEST, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_SPACE, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TOGGLE_BRIDGE_AND_TACTICAL, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_F9, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TOGGLE_CINEMATIC_MODE, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_T, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TARGET_NEXT, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_Y, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TARGET_PREV, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_U, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TARGET_NEAREST, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_I, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TARGET_NEXT_ENEMY, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_J, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TARGET_TARGETS_ATTACKER, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_N, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TARGET_NEXT_NAVPOINT, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_P, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TARGET_NEXT_PLANET, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_M, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TOGGLE_MAP_MODE, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_SCROLL, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_VIEWSCREEN_TARGET, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_HOME, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_VIEWSCREEN_FORWARD, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_DELETE, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_VIEWSCREEN_LEFT, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_PAGEDOWN, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_VIEWSCREEN_RIGHT, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_END, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_VIEWSCREEN_BACKWARD, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_PAGEUP, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_VIEWSCREEN_UP, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_INSERT, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_VIEWSCREEN_DOWN, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_C, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_CYCLE_CAMERA, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_V, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_REVERSE_CHASE, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_TAB, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TAB_FOCUS_CHANGE, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_CAPS_K, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_DEBUG_KILL_TARGET, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_CAPS_R, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_DEBUG_QUICK_REPAIR, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_CAPS_G, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_DEBUG_GOD_MODE, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_CTRL_Q, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_DEBUG_LOAD_QUANTUMS, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_H, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_TOGGLE_PICK_FIRE, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_SCROLL_WHEEL_UP, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_INCREASE_SPEED, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_SCROLL_WHEEL_DOWN, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_DECREASE_SPEED, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_CTRL_D, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_SELF_DESTRUCT, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_CTRL_T, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_CLEAR_TARGET, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_CTRL_I, App.TGKeyboardEvent.KS_KEYDOWN, App.ET_INPUT_INTERCEPT, 0, 0)
    App.g_kKeyboardBinding.BindKey(App.WC_CTRL_1, App.TGKeyboardEvent.KS_NORMAL, App.ET_MANEUVER, App.KeyboardBinding.GET_INT_EVENT, 1, App.KeyboardBinding.KBT_SINGLE_KEY_TO_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_CTRL_2, App.TGKeyboardEvent.KS_NORMAL, App.ET_MANEUVER, App.KeyboardBinding.GET_INT_EVENT, 2, App.KeyboardBinding.KBT_SINGLE_KEY_TO_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_CTRL_3, App.TGKeyboardEvent.KS_NORMAL, App.ET_MANEUVER, App.KeyboardBinding.GET_INT_EVENT, 3, App.KeyboardBinding.KBT_SINGLE_KEY_TO_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_CTRL_4, App.TGKeyboardEvent.KS_NORMAL, App.ET_MANEUVER, App.KeyboardBinding.GET_INT_EVENT, 4, App.KeyboardBinding.KBT_SINGLE_KEY_TO_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_ALT_1, App.TGKeyboardEvent.KS_NORMAL, App.ET_MANAGE_POWER, App.KeyboardBinding.GET_INT_EVENT, 0, App.KeyboardBinding.KBT_SINGLE_KEY_TO_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_ALT_2, App.TGKeyboardEvent.KS_NORMAL, App.ET_MANAGE_POWER, App.KeyboardBinding.GET_INT_EVENT, 1, App.KeyboardBinding.KBT_SINGLE_KEY_TO_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_ALT_3, App.TGKeyboardEvent.KS_NORMAL, App.ET_MANAGE_POWER, App.KeyboardBinding.GET_INT_EVENT, 2, App.KeyboardBinding.KBT_SINGLE_KEY_TO_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_ALT_4, App.TGKeyboardEvent.KS_NORMAL, App.ET_MANAGE_POWER, App.KeyboardBinding.GET_INT_EVENT, 3, App.KeyboardBinding.KBT_SINGLE_KEY_TO_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_ALT_5, App.TGKeyboardEvent.KS_NORMAL, App.ET_MANAGE_POWER, App.KeyboardBinding.GET_INT_EVENT, 4, App.KeyboardBinding.KBT_SINGLE_KEY_TO_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_ALT_6, App.TGKeyboardEvent.KS_NORMAL, App.ET_MANAGE_POWER, App.KeyboardBinding.GET_INT_EVENT, 5, App.KeyboardBinding.KBT_SINGLE_KEY_TO_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_ALT_7, App.TGKeyboardEvent.KS_NORMAL, App.ET_MANAGE_POWER, App.KeyboardBinding.GET_INT_EVENT, 6, App.KeyboardBinding.KBT_SINGLE_KEY_TO_EVENT)
    App.g_kKeyboardBinding.BindKey(App.WC_ALT_8, App.TGKeyboardEvent.KS_NORMAL, App.ET_MANAGE_POWER, App.KeyboardBinding.GET_INT_EVENT, 7, App.KeyboardBinding.KBT_SINGLE_KEY_TO_EVENT)