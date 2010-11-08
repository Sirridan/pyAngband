#Commands.py

MAX_CMDS = 9

(   CMD_NONE,
    CMD_MOVE,
    CMD_WAIT,
    CMD_CHARACTER,
    CMD_INVENTORY,
    CMD_EXAMINE,
    CMD_BUY,
    CMD_SELL,
    CMD_DROP_ITEM,
 ) = range(0, MAX_CMDS)