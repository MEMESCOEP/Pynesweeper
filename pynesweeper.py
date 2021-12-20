'''
Pynesweeper!


What this code does:

Create an array of list, every element represents a button on the playing field.
Each element can have the following values:
        0: not clicked and no bomb around the element
        1-6: not clicked and 1 to six bombs around the elemenent
        9: not clicked and bomb
        
if a button is pressed the value is changed:
        10: clicked and no bomb
        11-16: clicked and 1 to six bombs around the elemenent
        19: place flag 
        29: display bomb 
'''


try:


        #Imports
        import base64
        import sys
        import os
        import time
        import threading
        import tkinter as tk
        from tkinter import simpledialog
        from tkinter import *
        from PyQt5 import QtGui
        from PyQt5.QtWidgets import QAction, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox, QMainWindow, QApplication
        from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
        from PyQt5.QtCore import QEvent, Qt, QObject
        from functools import partial
        from random import randint



        #Variables
        dataFolder = "MSDT\\"
        icon = b'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'
        tile_1 = b'R0lGODlhEAAQAPcAABwC3OTi5AZBBncgdzQtkZAggwhUBqxyd291qABlYAB2xwBpcbBzADJpAAlvAAJuANAgCLxUAvhhAAFyAABnKABhiQAAJwAqAKguwDJ06wlnEgJhACQA7eZU4BJJAgBGd4AghAEt6yMgEgBUAABh/gBn/wBn/wBl/1BkNgEgACNJAABtALBhbDJnAAllbgIgANhG4BVpZf5sJwFlANggKBVGAv5vAAFyAOhtAnlhACh0AAAAAAAqAAAuAAB0AABpAG9mbAAAAAAAAAAAAAAAAAAAAAAjAAAAAP8gbP+JAAAnAAEAAAD4KADn6QASEgAAAHik4ANdZQAGJwB3AGjTbOZdAAEGAAF3AWAgbOVvABLHCABxAtgA1BUA6P4AEgEAAGCsJvsD6RIjEgAAAO0AAOAAAAIjAHcAAEAzAJ3cANNmAAZ2AP4AB/8Bt/8AZv8AdnAA02UAqQYAZHcA26Z4AGXnAAYSAHcAAACXAAA8AAAGAAB3ANicWBU8U/4GJwF3ANigABVvUP7HJwFxAGoAQCwA6AYAEncAADQAAAABAAAAAMAAANAznBXc6P5mEgF2AGxQ4ufnlxISbQAAdhFor8md9mYnEHYArQBg/gD7/yMS/wAA/wDtBwDgtwACZgB3dtjYVhWUt/7TZgEGdgD+WAD/UwD/JwD/AACI0QHnnQASZwAAdiDLE8naqWZnZHZ227gCAOcAABIAAAAAANgAABUBAP4AAAEAAAygAJ7nAPMSAHQAAAFKzQDZqwBmugB23AI0AX8AAAAAAADAAG5xfGfp6AASElAAAFAMEU1RASBQAC0AACAAYFAA+28AEnIAAHTI4mHol2ISbWwAdmV+ZyDc3FBmEWl2rXiA/mVt/2xQ/20A/2G00XB5nQBQZyoAdi40WHAAqnAAQm3AAADEWFLnU0ESJ1cAACAAAC0BACAAAFIAAEGfcVfc6SBmEkl2AG0BZGEAAGcAAGUAACAAd0QAqWEwZHQA20MCZDoAAAAAAC4AAHIueWFn3XdpSABmACH5BAAAAAAALAAAAAAQABAABwgwAAMIHEiwoMGDCBMqBABA4UCGDR1CjLgQosOHFCVmrHhRIMOLEz8mDLmxo8mTBgMCADs='
        tile_2 = b'R0lGODlhEAAQAPcAAGwC3OTi5AZBBncgd1UtkdIggwhUBo9yd3N1YABlfwB2xwBpcUhzAABpABJvAARuAEAgCM1UAhJhAARyAABnKABhiQAAJQAqAEAuwAB06xJnEgRhACQA7eZU4BJJAgBGd4AghAEt6yEgEgBUAABh/gBn/wBn/wBl/1BkNgEgACFJAABtAEhhbABnABJlbgQgAAhG4GlpZQ9sJQRlAAggKGlGAg9vAARyADBtAgVhACh0AAAAAAAqAAAuAAB0AABpAHNmbAAAAAAAAAAAAAAAAAAAAAAhAAAAAP8gbP+JAAAlAAEAAAD4KADn6QASEgAAAJik4ANdZQAGJQB3AGjTbOZdAAEGAAF3AWDobOVwABLHCABxAggA1GkA6A8AEgQAAGCsJvsD6RIhEgAAAO0AAOAAAAIhAHcAAIgzAILcANNmAAZ2AP4AB/8Bt/8AZv8AdnAA5GUAIAYAh3cAwaZ4AGXnAAYSAHcAAACXAAA8AAAGAAB3AAicWGk8Uw8GJQR3AAhoAGlwUA/HJQRxAGoAQCwA6AYAEncAADQAAAABAAAAAMAAAAAznGnc6A9mEgR2AGxQ4ufnlxISbQAAdhFomMmdf2Yl83YAtwBg/gD7/yES/wAA/wDtBwDgtwACZgB3dggQVmmLtw/TZgQGdgD+WAD/UwD/JQD/AACI0QHnnQASZwAAdiDLJMnaIGZnh3Z2wbgCAOcAABIAAAAAAAgAAGkBAA8AAAQAAAygAJ7nAPMSAHQAAAFKzQDZqwBmugB23AI0AX8AAAAAAADAAG5xfGfp6AASElAAAFAMEU1RASBQAC0AACAAYFAA+28AEnIAAHTI4mHol2ISbWwAdmV+UCDcVVBm8ml2t3iA/mVt/2xQ/20A/2G00XB5nQBQZyoAdi40WHAAqnAAQm3AAADEWFLnU0ESJVcAACAAAC0BACAAAFIAAEGfcVfc6SBmEkl2AG0BZGEAAGcAAGUAACAAQEQAIGEwh3QAwUMCZDoAAAAAAC4AAHIueWFn3XdpSABmACH5BAAAAAAALAAAAAAQABAABwgzAAMIHEiwoMGDCBMiBMCwYcKGEAEslDiQ4cSKFhUGcKiRo0KPDzN+jCiyIMmSGlOqTBkQADs='
        tile_3 = b'R0lGODlhEAAQAPcAALwC3OTi5AZBBncgd/otkdkggwhUBityd291PwBlkgB2wABpceBzAPBpABpvAARuABggCDBUAhxhAARyAABnKABhiQAAHQAqANguwPB06xpnEgRhACQA7eZU4BJJAgBGd4AghAEt6xkgEgBUAABh/gBn/wBn/wBl/1BkNgEgABlJAABtAOBhbPBnABplbgQgAABG4EFpZW9sHQRlAAAgKEFGAm9vAARyAFhtAi5hACJ0AAAAAAAqAAAuAAB0AABpAG9mbAAAAAAAAAAAAAAAAAAAAAAZAAAAAP8gbP+JAAAdAAEAAAD4KADn6QASEgAAAHik4ANdZQAGHQB3AGjTbOZdAAEGAAF3AWC3bOWdABLACABxAgAA1EEA6G8AEgQAAGCsJvsD6RIZEgAAAO0AAOAAAAIZAHcAANczAG/cANRmAAZ2AP4AB/8Bt/8AZv8AdnAAZ2UA1wYA+XcA2KZ4AGXnAAYSAHcAAACXAAA8AAAGAAB3AACcWEE8U28GHQR3AAA3AEGdUG/AHQRxAGoAQCwA6AYAEncAADQAAAABAAAAAMAAAPgznEDc6G9mEgR2AGxQ4ufnlxISbQAAdhFoG8mdiGYdjXYArgBg/gD7/xkS/wAA/wDtBwDgtwACZgB3dgBPVkFmt2/UZgQGdgD+WAD/UwD/HQD/AACI0QHnnQASZwAAdiDLp8na12Zn+XZ22LgCAOcAABIAAAAAAAAAAEEBAG8AAAQAAAygAJ7nAPMSAHQAAAFKzQDZqwBmugB23AI0AX8AAAAAAADAAG5xfGfp6AASElAAAFAMEU1RASBQAC0AACAAYFAA+28AEnIAAHTI4mHol2ISbWwAdmV+0yDcolBmjGl2rniA/mVt/2xQ/20A/2G00XB5nQBQZyoAdi40WHAAqnAAQm3AAADEWFLnU0ESHVcAACAAAC0BACAAAFIAAEGfcVfc6SBmEkl2AG0BZGEAAGcAAGUAACAAw0QA12Ew+XQA2EMCZDoAAAAAAC4AAHIueWFn3XdpSABmACH5BAAAAAAALAAAAAAQABAABwg0AAMIHEiwoMGDCBMmBMCQocKGEBcCGOhQIcWJFhtaFKhxI0eMBysGEGkQYkeEJj2qXGkxIAA7'
        tile_4 = b'R0lGODlhEAAQAPcAANwCpOTi5AZBBncgd5AtkYQggwhUBhxyd3B1TgBlhQB2wABpcbhzAB9pACZvAABuALggCEdUAmthAARyAABnKABhiQAAIwAqALAuwB906yZnEgBhACQA7eZU4BJJAgBGd4AghAEt6x8gEgBUAABh/gBn/wBn/wBl/1BkNgEgAB9JAABtALhhbB9nACZlbgAgAKhG4MBpZSZsIwBlAKggKMBGAiZvAAByAKhtAoFhACl0AAAAAAAqAAAuAAB0AABpAHBmbAAAAAAAAAAAAAAAAAAAAAAfAAAAAP8gbP+JAAAjAAEAAAD4KADn6QASEgAAAICk4ANdZQAGIwB3AGjTbOZdAAEGAAF3AWDGbOWKABLACABxAqgA1MAA6CYAEgAAAGCsJvsD6RIfEgAAAO0AAOAAAAIfAHcAAKYzAHjcANRmAAZ2AP4AB/8Bt/8AZv8AdnAAvmUANAYAPXcA36Z4AGXnAAYSAHcAAACXAAA8AAAGAAB3AKicWMA8UyYGIwB3AKhGAMCKUCbAIwBxAGoAQCwA6AYAEncAADQAAAABAAAAAMAAAKAznMDc6CZmEgB2AGxQ4ufnlxISbQAAdhFowsmda2YjSXYAqQBg/gD7/x8S/wAA/wDtBwDgtwACZgB3dqg+VsBxtybUZgAGdgD+WAD/UwD/IwD/AACI0QHnnQASZwAAdiDLfsnaNGZnPXZ237gCAOcAABIAAAAAAKgAAMABACYAAAAAAAygAJ7nAPMSAHQAAAFKzQDZqwBmugB23AI0AX8AAAAAAADAAG5xfGfp6AASElAAAFAMEU1RASBQAC0AACAAYFAA+28AEnIAAHTI4mHol2ISbWwAdmV+CiDcQVBmSGl2qXiA/mVt/2xQ/20A/2G00XB5nQBQZyoAdi40WHAAqnAAQm3AAADEWFLnU0ESI1cAACAAAC0BACAAAFIAAEGfcVfc6SBmEkl2AG0BZGEAAGcAAGUAACAAGkQANGEwPXQA30MCZDoAAAAAAC4AAHIueWFn3XdpSABmACH5BAAAAAAALAAAAAAQABAABwg1AAMIHEiwoMGDCBMiBABgIMOEDwVGNDgxQEWCFS86ZMhRo8SOHBVibCjyY0mTJz2eXMlyYEAAOw=='
        tile_5 = b'R0lGODlhEAAQAPcAANwCVOTi5AZBBncgd4AtkYQggwBUBgRyd3B1lABltAB2wABpcchzALFpACtvAABuADAgCDxUAmxhAARyAABnKABhiQAAKQAqAMAuwLF06ytnEgBhACQA7eZU4BJJAgBGd4AghAEt6yUgEgBUAABh/gBn/wBn/wBl/1BkNgEgACVJAABtAMhhbLFnACtlbgAgANBG4E9pZSxsKQBlANAgKE9GAixvAAByAMBtAtZhAD10AAMAAAAqAAAuAAB0AABpAHBmbAAAAAAAAAAAAAAAAAAAAAAlAAAAAP8gbP+JAAApAAEAAMD4KNbn6T0SEgMAAICk4ANdZQAGKQB3AGjTbOZdAAEGAAF3AWAcbOW7ABLACABxAtAA1E8A6CwAEgAAAGCsJvsD6RIlEgAAAO0AAOAAAAIlAHcAAHwzAEncANRmAAZ2AP4AB/8Bt/8AZv8AdnAAd2UAcgYAr3cA3qZ4AGXnAAYSAHcAAACXAAA8AAAGAAB3ANCcWE88UywGKQB3ANCcAE+7UCzAKQBxAGoAQCwA6AYAEncAADQAAAABAAAAAMAAAMgznE/c6CxmEgB2AGxQ4ufnlxISbQAAdhFoC8mdLWYp23YAqABg/gD7/yUS/wAA/wDtBwDgtwACZgB3dtDkVk9AtyzUZgAGdgD+WAD/UwD/KQD/AACI0QHnnQASZwAAdiDLt8nacmZnr3Z23rgCAOcAABIAAAAAANAAAE8BACwAAAAAAAygAJ7nAPMSAHQAAAFKzQDZqwBmugB23AI0AX8AAAAAAADAAG5xfGfp6AASElAAAFAMEU1RASBQAC0AACAAYFAA+28AEnIAAHTI4mHol2ISbWwAdmV+wyDcB1Bm2ml2qHiA/mVt/2xQ/20A/2G00XB5nQBQZyoAdi40WHAAqnAAQm3AAADEWFLnU0ESKVcAACAAAC0BACAAAFIAAEGfcVfc6SBmEkl2AG0BZGEAAGcAAGUAACAA00QAcmEwr3QA3kMCZDoAAAAAAC4AAHIueWFn3XdpSABmACH5BAAAAAAALAAAAAAQABAABwgyAAMIHEiwoMGDCBMeBMCwIUOEDh1CBKCQ4MOKAiNSTKjxIkaPBUGCtNiRY0SMKFOmDAgAOw=='
        tile_6 = b'R0lGODlhEAAQAPcAANwCBOTi5AZBBncgdwAtkQAggwBUBgByd/B1eXZlo2h2wANpcfBzAHZpAGhvAANuAKAgCLdUAlFhAAByAABnKABhiQAAMAAqAOguwHZ062hnEgNhACQA7eZU4BJJAgBGd0gghNUt62YgEnZUAABh/gBn/yxn/wBl/wBkNgAgAABJAABtAPBhbHZnAGhlbgMgALBG4KFpZWZsMANlAAAgKABGAgBvAAByAABtAgBhAAB0AAAAAAAqAAAuAAB0AABpAABmbAAAAAAAAAAAAAAAAAAAAAAsAAAAAAAgbACJACwwAAAAALD4KKHn6WYSEgMAAACk4ABdZQAGMAB3AGjTbOZdABIGAAB3AQjxbACsAG/ACABxAg0A1AAA6AAAEgAAAHesJtED6WYsEnYAABQAAP8AANUsANMAAKAzALfcAFFmAAB2AJgAB6EBt2YAZgMAdgEAEAAA8QAA1QAA06h4AKHnAGYSAAMAAGCXAOY8ABIGAAB3AOicWCw8UwYGMHd3ALBxAKGsUGbAMANxAGoAQCwA6AYAEncAADQAAAABAAAAAMAAAKgznKHc6GZmEgN2AGxQ4ufnlxISbQAAdhFobMmdrmYwoXYApQBg/gD7/ywS/wAA/wDtBwDgtwACZgB3drAJVqFXt2bUZgMGdgD+WAD/UwD/MAD/AACI0QHnnQASZwAAdiDL0Mna8WZn1XZ207gCAOcAABIAAAAAALAAAKEBAGYAAAMAAAygAJ7nAPMSAHQAAAFKzQDZqwBmugB23AI0AX8AAAAAAADAAG5xfGfp6AASElAAAFAMEU1RASBQAC0AACAAYFAA+28AEnIAAHTI4mHol2ISbWwAdmV+pCDchFBmoGl2pXiA/mVt/2xQ/20A/2G00XB5nQBQZyoAdi40WHAAqnAAQm3AAADEWFLnU0ESMFcAACAAAC0BACAAAFIAAEGfcVfc6SBmEkl2AG0BZGEAAGcAAGUAACAAtEQA8WEw1XQA00MCZDoAAAAAAC4AAHIueWFn3XdpSABmACH5BAAAAAAALAAAAAAQABAABwg2AAMIHEiwoMGDCBMiBMCwYcKGEAEslKhwIMOKFiNSPKjxIseNATwaFBkSJMGOJk9GxMiyZcuAADs='
        tile_7 = b'R0lGODlhEAAQAPcAANwCBOTi5G1BBgQgd00tkZgggwhUBt1yd291DABl0gB2wABpcUhzAKxpAG1vAARuAAAgCB9UAp5hAANyAABnKABhiQAAMwAqAEAuwKx0621nEgRhACQA7eZU4BJJAgBGd4AghAEt6y8gEgBUAABh/gBn/wBn/wBl/1BkNgEgAC9JAABtAEhhbKxnAG1lbgQgAChG4F9pZaNsMwNlACggKF9GAqNvAANyAJBtAsxhAHB0AAQAAAAqAAAuAAB0AABpAG9mbAAAAAAAAAAAAAAAAAAAAAAvAAAAAP8gbP+JAAAzAAEAAAD4KADn6QASEgAAAHik4ANdZQAGMwB3AGjTbOZdAAEGAAF3AWCEbOXdABLACABxAigA1F8A6KMAEgMAAGCsJvsD6RIvEgAAAO0AAOAAAAIvAHcAAOQzAC/cANRmAAZ2AP4AB/8Bt/8AZv8AdnAAN2UAHwYAwXcA1KZ4AGXnAAYSAHcAAACXAAA8AAAGAAB3ACicWF88U6MGMwN3ACgEAF/dUKPAMwNxAGoAQCwA6AYAEncAADQAAAABAAAAAMAAACAznF/c6KNmEgN2AGxQ4ufnlxISbQAAdhFoS8mdQGYztXYAogBg/gD7/y8S/wAA/wDtBwDgtwACZgB3dih8Vl8mt6PUZgMGdgD+WAD/UwD/MwD/AACI0QHnnQASZwAAdiDL98naH2ZnwXZ21LgCAOcAABIAAAAAACgAAF8BAKMAAAMAAAygAJ7nAPMSAHQAAAFKzQDZqwBmugB23AI0AX8AAAAAAADAAG5xfGfp6AASElAAAFAMEU1RASBQAC0AACAAYFAA+28AEnIAAHTI4mHol2ISbWwAdmV+gyDcalBmtGl2oniA/mVt/2xQ/20A/2G00XB5nQBQZyoAdi40WHAAqnAAQm3AAADEWFLnU0ESM1cAACAAAC0BACAAAFIAAEGfcVfc6SBmEkl2AG0BZGEAAGcAAGUAACAAk0QAH2EwwXQA1EMCZDoAAAAAAC4AAHIueWFn3XdpSABmACH5BAAAAAAALAAAAAAQABAABwgwAAMIHEiwoMGDCBMeBMCwIUOEDh0qJPhwYoCKFjEq1LgRgMWLHj9yTDjyo8mTBwMCADs='
        tile_8 = b'R0lGODlhEAAQAPcAANwCBOTi5AZBBncgdwAtkYYggwhUBo5yd3N1jwBlxQB2wABpcXhzAM5pADZvAABuAOggCB9UAoRhAARyAABnKABhiQAALwAqAHAuwM506zZnEgBhACQA7eZU4BJJAgBGd4AghAEt6ysgEgBUAABh/gBn/wBn/wBl/1BkNgEgACtJAABtAHhhbM5nADZlbgAgAFhG4K9pZa1sLwNlAFggKK9GAq1vAANyAFBtAi5hADJ0AAAAAAAqAAAuAAB0AABpAHNmbAAAAAAAAAAAAAAAAAAAAAArAAAAAP8gbP+JAAAvAAEAAAD4KADn6QASEgAAAJik4ANdZQAGLwB3AGjTbOZdAAEGAAF3AWAHbOXKABLACABxAlgA1K8A6K0AEgMAAGCsJvsD6RIrEgAAAO0AAOAAAAIrAHcAAGczADjcANRmAAZ2AP4AB/8Bt/8AZv8AdnAArGUAbwYA03cA16Z4AGXnAAYSAHcAAACXAAA8AAAGAAB3AFicWK88U60GLwN3AFiHAK/KUK3ALwNxAGoAQCwA6AYAEncAADQAAAABAAAAAMAAAFAznK/c6K1mEgN2AGxQ4ufnlxISbQAAdhFo0MmdMGYvp3YAoQBg/gD7/ysS/wAA/wDtBwDgtwACZgB3dlj/Vq8xt63UZgMGdgD+WAD/UwD/LwD/AACI0QHnnQASZwAAdiDLbMnab2Zn03Z217gCAOcAABIAAAAAAFgAAK8BAK0AAAMAAAygAJ7nAPMSAHQAAAFKzQDZqwBmugB23AI0AX8AAAAAAADAAG5xfGfp6AASElAAAFAMEU1RASBQAC0AACAAYFAA+28AEnIAAHTI4mHol2ISbWwAdmV+GCDcGlBmpml2oXiA/mVt/2xQ/20A/2G00XB5nQBQZyoAdi40WHAAqnAAQm3AAADEWFLnU0ESL1cAACAAAC0BACAAAFIAAEGfcVfc6SBmEkl2AG0BZGEAAGcAAGUAACAACEQAb2Ew03QA10MCZDoAAAAAAC4AAHIueWFn3XdpSABmACH5BAAAAAAALAAAAAAQABAABwg2AAMIHEiwoMGDCBMiBMCwYcKGEAEslDiQ4USCFidCVBiR4sGMAkEWFCkSY0ePBjsqXMmy5cGAADs='
        tile_clicked = b'R0lGODlhEAAQAPcAAOTi5CNHcHBBBgMgdzAtkcgggwhUBvByd3J19QBlrQB25ABpd9BzACNpAHBvAANuAGggCB5UAnFhAANyAABnmABhngAAJwAqAMguwCN063BnEgNhACQA7eZU4BJJAgBGd4AghAEt6yMgEgBUAABh/gBn/wBn/wBl/1BkNgEgACNJAABtANBhbCNnAHBlbgMgAJBGSJdpty9sJwBlAJAgKJdGAi9vAAByAGBtAsBhACt0AAAAAAAqAAAuAAB0AABpAHJmbAAAAAAAAAAAAAAAAAAAAAAjAAAAAP+QbP+eAAAnAAEAAAD4KADn6QASEgAAAJCkSANdtwAGJwB3AGjTbOZdAAEGAAF3AWB9bOWiABLkCAB3ApAA1JcA6C8AEgAAAGCsJvsD6RIjEgAAAO0AAOAAAAIjAHcAAB0zAFDcAPBmAAB2AP4AB/8Bt/8AZv8AdnAA8mUAdAYAqXcAH6Z4AGXnAAYSAHcAAACXAAA8AAAGAAB3AJCcuJc8hy8GJwB3AJD9AJeigC/kJwB3AGoAQCwA6AYAEncAADQAAAABAAAAAMAAAIgznJfc6C9mEgB2AGxQ4ufnlxISbQAAdhEIjsm6K2Yn3XYAaQBg/gD7/yMS/wAA/wDtBwDgtwACZgB3dpCFVpdZty/wZgAAdgD+uAD/hwD/JwD/AACI0QHnnQASZwAAdiDLMsnadGZnqXZ2H7gCAOcAABIAAAAAAJAAAJcBAC8AAAAAAAygAJ7nAPMSAHQAAAFKzQDZqwBmugB23AI0AX8AAAAAAADAAG5xfGfp6AASElAAAFAMEU1RASBQAC0AACAAYFAA+28AEnIAAHTI4mHol2ISbWwAdmV+RiDcAVBm3Gl2aXiA/mVt/2xQ/20A/2G00XB5nQBQZyoAdi40WHAAqnAAQm3AAADEuFLnh0ESJ1cAACAAAC0BACAAAFIAAEGfcVfc6SBmEkl2AG0BZGEAAGcAAGUAACAAVkQAdGEwqXQAH0MCZDoAAAAAAC4AAHIueWFn3XdpSABmACH5BAAAAAAALAAAAAAQABAABwgdAAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw=='
        tile_flag = b'R0lGODlhEAAQAPcAAAQCBHx6fJyenFRWVLy6vNwCBKyqrHZyd3F1awBlQwB2PQBpcahzAEFpAA5vAARuABggCGpUAhNhAARyAABncABhewAANAAqAKAuwEF06w5nEgRhACQA7eZU4BJJAgBGd4AghAEt6zAgEgBUAABh/gBn/wBn/wBl/1BkNgEgADBJAABtAKhhbEFnAA5lbgQgAFBGsI9peGZsNARlAFAgKI9GAmZvAARyAPhtAh5hADd0AAAAAAAqAAAuAAB0AABpAHFmbAAAAAAAAAAAAAAAAAAAAAAwAAAAAP9obP97AAA0AAEAAAD4KADn6QASEgAAAIiksANdeAAGNAB3AGjTbOZdAAEGAAF3AWDjbOVMABI9CABxAlAA1I8A6GYAEgQAAGCsJvsD6RIwEgAAAO0AAOAAAAIwAHcAAIMzAL7cAClmAAZ2AP4AB/8Bt/8AZv8AdnAAXGUAaAYAoHcAiqZ4AGXnAAYSAHcAAACXAAA8AAAGAAB3AFCccI88a2YGNAR3AFBjAI9MYGY9NARxAGoAQCwA6AYAEncAADQAAAABAAAAAMAAAEgznI/c6GZmEgR2AGxQ4ufnlxISbQAAdhEQIMmuN2Y01HYA/ABg/gD7/zAS/wAA/wDtBwDgtwACZgB3dlAbVo+3t2YpZgQGdgD+cAD/awD/NAD/AACI0QHnnQASZwAAdiDLnMnaaGZnoHZ2irgCAOcAABIAAAAAAFAAAI8BAGYAAAQAAAygAJ7nAPMSAHQAAAFKzQDZqwBmugB23AI0AX8AAAAAAADAAG5xfGfp6AASElAAAFAMEU1RASBQAC0AACAAYFAA+28AEnIAAHTI4mHol2ISbWwAdmV+6CDcHVBm1Wl2/HiA/mVt/2xQ/20A/2G00XB5nQBQZyoAdi40WHAAqnAAQm3AAADEcFLna0ESNFcAACAAAC0BACAAAFIAAEGfcVfc6SBmEkl2AG0BZGEAAGcAAGUAACAA+EQAaGEwoHQAikMCZDoAAAAAAC4AAHIueWFn3XdpSABmACH5BAAAAAAALAAAAAAQABAABwhjAAkQMCCQ4MCCCAkIWMiwYUOBAgxInEhRogCIFQ0UqHhRYcUCGyl2jDgRZMiJIyma5AiRpMmTFjFKBKlRZMqZOEXKnDigwACdHikCKAAAKMmJAQAEMJox40iHUBcKnEq16tSAADs='
        tile_mine = b'R0lGODlhEAAQAPcAAAQCBJyenLy6vKyqrBEtUKYg6AhUEr9yAHN18ABl6wB2EgBpANBzoaRpFnxvAQRu0WAgAM9UACthAARyAABnDwBhAAAAAAAqAMguDKR0AHxnAARhAJAAA+ZUABJJAABGAIAgAwEtAHEgAABUAABhAABnAABnAABlAFBkBgEgAHFJAABtANBhF6RnAHxlAAQgABBGjLRp6HhsEgBlABAgRrRGXnhvbwBydehtxBxhkCh0/QQAfwAqAAAu8AB0/QBpf3NmAAAAAAAAAAD/AAAgAAAAAAAAAAAAAP9IQf/qfgASbwEAdQCXKwBNfgDubwB0dZihoQMWFgABAQDR0dQAD+YAAAEAAAEAAMwAGOUAABIAAAAAABDAL7TqAHgSAAAAAMwAOPsA6hIAEgAAAO0I+uAA6wIAEncAAMAzQGjcB89mjwB2Af4AB/8Bt/8AZv8AdnAA82UAcgYAwXcAYabkAGXnAAYSAHcAAACXAAA8AAAGAAB3ABCcuLQ8h3gGdQB3ABC8ALSagHjbdQB3AGoArCwA6AYAEncAADQAAAABAAAAAMAAAAgzCLTc6XhmEgB2ANi84ufnlxISbQAAdhEDO8kALWYAtXYAFwDM/gD7/3ES/wAA/wDtBwDgtwACZgB3dhBYVrRht3jPZgAAdgD+uAD/hwD/dQD/AAD00QHnnQASZwAAdiDLM8nac2ZnwXZ2YSQCAOgAABIAAAAAABAAALQBAHgAAAAAAAwMAJ7oAPMSAHQAAAFKagDZAABmAAB2AAI0AX8AAAAAAADAAG7d6Gfp6AASElAAAFAM/01R/yBQ/y0A/yAAzFAA+28AEnIAAHQ04mHpl2ISbWwAdmV+8yDcB1BmtGl2F3iA/mVt/2xQ/20A/2G00XB5nQBQZyoAdi40WHAAqnAAQm3AAAAwuFLoh0ESdVcAACAAAC0BACAAAFIAAEGf3Vfc6SBmEkl2AG0BZGEAAGcAAGUAACAAH0QAc2EwwXQAYUOkZDroAAASAC4AAHIueWFn3XdpSABmACH5BAAAAAAALAAAAAAQABAABwheAAUMECCQ4MCCCAUEWMiwYUOCAQZInEhRYgCIFTMOuKhQY0WOESUCGABg5EiLGCeWLDlxIcSQK1e2TEky5smNNGuynNlRZE2SPEN6RNlzKM6iQ0E6XOqSoNOnUAkGBAA7'
        tile_plain = b'R0lGODlhEAAQAPcAAJyenLy6vKyqrHcgAAAtAiggAAhUACByAHB19ABl5wB2EgBpAFhzsMBpfxZvBgRud+ggzE9U6BhhEgZyAABnAABhAAAAAAAqAFAubMB0ABZnbgRhACQAzOZU6BJJEgBGAIAgAgEtABwgAABUAABhmABn6ABnEgBlAFBk8gEgcBxJBgBtd1hhkcBngxZlBgQgdyBGBJppfhZstwRldyAgAJpGABZvAARyABBtCOJhAiR0AAAAAAAqWAAu4wB0IwBpAHBm6AAA6wAAEgAAAABQ7QDj4AAjAgAAd/8ArP8A6wAcEgEAAADg/gDv/wAj/wAA/4ABNgMAAAAAAAAAAGjubOYDAAGFbgEBAGAJmOUA4BIAIwAAACAAKJoAAhYAAAQAAGBNAvsBABIAAAAAAO0gAODoAAISAHcAAAQzbIPcAKNmAAB2AP4AB/8Bt/8AZv8AdnAAZGUAeAYAyncAfqZ4AGXnAAYSAHcAAACXAAA8AAAGAAB3ACCcuJo8hxYGIAR3ACDkAJpxgBa3IAR3AGoAQCwA6AYAEncAADQATgAB6QAAEsAAABgznJrc6BZmEgR2AGxQ4ufnlxISbQAAdhEEGMnpJ2YSvnYACABg/gD7/xwS/wAA/wDtBwDgtwACZgB3diCcVpqKtxajZgQAdgD+uAD/hwD/IAD/AACI0QHnnQASZwAAdiDLpMnaeGZnynZ2frgCAOcAABIAAAAAACAAAJoBABYAAAQAAAygAJ7nAPMSAHQAAAFKAADZAABmAAB2AAI0AX8AAAAAAADAAG5xfGfp6AASElAAAFAMqE1R6CBQEi0AACAAYFAA+28AEnIAAHTI4mHol2ISbWwAdmV+0CDcDVBmv2l2CHiA/mVt/2xQ/20A/2G00XB5nQBQZyoAdi40WHAAqnAAQm3AAADEuFLnh0ESIFcAACAAAC0BACAAAFIAAEGfcVfc6SBmEkl2AG0BZGEAAGcAAGUAACAAwEQAeGEwynQAfkMAZDoAAAAAAC4AAHIueWFn3XdpSABmACH5BAAAAAAALAAAAAAQABAABwhIAAMIFCiAoMEABQMAWMiwYUOEAARInEhRIgCBEStqvKhQ40aMHityzBjSIkaSIUeWtKhypYCWK2GWlJkSpMuRDnMuHMizZ8+AADs='
        cellNum = 20
        currScriptName = sys.argv[0]
        currentDifficulty = 1
        global ex
        global app
        global Debug
        global timePassed
        global TimerThread
        global UseTimer
        global Score
        global StartTimer
        global HiScore
        global BreakThread
        global SwitchingDiff
        SwitchingDiff = False
        BreakThread = False
        HiScore = 0
        UseTimer = False
        StartTimer = False
        timePassed = 0
        Debug = 0
        Score = 0
        global file1 #favicon
        global file2 #tile_1
        global file3 #tile_2
        global file4 #tile_3
        global file5 #tile_4
        global file6 #tile_5
        global file7 #tile_6
        global file8 #tile_7
        global file9 #tile_8
        global file10 #tile_clicked
        global file11 #tile_flag
        global file12 #tile_mine
        global file13 #tile_plain

        file1 = None #favicon
        file2 = None  #tile_1
        file3 = None  #tile_2
        file4 = None  #tile_3
        file5 = None  #tile_4
        file6 = None  #tile_5
        file7 = None  #tile_6
        file8 = None  #tile_7
        file9 = None  #tile_8
        file10 = None  #tile_clicked
        file11 = None  #tile_flag
        file12 = None  #tile_mine
        file13 = None  #tile_plain
        








        #Functions
        def Timer():
                global timePassed
                global UseTimer
                global StartTimer
                while BreakThread == False:
                        time.sleep(1)
                        if UseTimer == True and StartTimer == True:
                            timePassed += 1
                            if Debug == 1:
                                print("Seconds Passed: {}".format(timePassed))
                        
                        






        def WriteIMGtoFiles():
            file1 = open(dataFolder + "favicon.png", "wb")
            file2 = open(dataFolder + "tile_1.gif", "wb")
            file3 = open(dataFolder + "tile_2.gif", "wb")
            file4 = open(dataFolder + "tile_3.gif", "wb")
            file5 = open(dataFolder + "tile_4.gif", "wb")
            file6 = open(dataFolder + "tile_5.gif", "wb")
            file7 = open(dataFolder + "tile_6.gif", "wb")
            file8 = open(dataFolder + "tile_7.gif", "wb")
            file9 = open(dataFolder + "tile_8.gif", "wb")
            file10 = open(dataFolder + "tile_clicked.gif", "wb")
            file11 = open(dataFolder + "tile_flag.gif", "wb")
            file12 = open(dataFolder + "tile_mine.gif", "wb")
            file13 = open(dataFolder + "tile_plain.gif", "wb")


            file1.write(base64.b64decode(icon))
            file2.write(base64.b64decode(tile_1))
            file3.write(base64.b64decode(tile_2))
            file4.write(base64.b64decode(tile_3))
            file5.write(base64.b64decode(tile_4))
            file6.write(base64.b64decode(tile_5))
            file7.write(base64.b64decode(tile_6))
            file8.write(base64.b64decode(tile_7))
            file9.write(base64.b64decode(tile_8))
            file10.write(base64.b64decode(tile_clicked))
            file11.write(base64.b64decode(tile_flag))
            file12.write(base64.b64decode(tile_mine))
            file13.write(base64.b64decode(tile_plain))

            file1.close()
            file2.close()
            file3.close()
            file4.close()
            file5.close()
            file6.close()
            file7.close()
            file8.close()
            file9.close()
            file10.close()
            file11.close()
            file12.close()
            file13.close()


        #Main Class
        class Window(QMainWindow):
            global file1 #favicon
            global file2 #tile_1
            global file3 #tile_2
            global file4 #tile_3
            global file5 #tile_4
            global file6 #tile_5
            global file7 #tile_6
            global file8 #tile_7
            global file9 #tile_8
            global file10 #tile_clicked
            global file11 #tile_flag
            global file12 #tile_mine
            global file13 #tile_plain
            

            def __init__(self):
                
                global cellNum
                global TimerThread
                global file1
                super(Window, self).__init__()


                






                # set title
                self.setWindowTitle("Pynesweeper")
                # set icon
                self.setWindowIcon(QtGui.QIcon(dataFolder + "tile_pain.gif"))       


                self.cells = cellNum
                self.initialArray = []
                
                # create empty array
                for row in range(self.cells):
                    line = [0]*self.cells
                    self.initialArray.append(line)


                def Easy():
                        global currentDifficulty
                        global cellNum
                        global ex
                        global Debug
                        global SwitchingDiff

                        if currentDifficulty != 0:
                                SwitchingDiff = True
                                currScriptName = sys.argv[0]
                                self.close()
                                cellNum = 10
                                ex = None
                                ex = Window()
                                if(Debug == 1):
                                        print("<Difficulty changed to easy>")
                                currentDifficulty = 0
                                SwitchingDiff = False
                        

                def Normal():
                        global currentDifficulty
                        global cellNum
                        global ex
                        global Debug
                        global SwitchingDiff

                        if currentDifficulty != 1:
                                SwitchingDiff = True
                                currScriptName = sys.argv[0]
                                self.close()
                                cellNum = 20
                                ex = None
                                ex = Window()
                                if(Debug == 1):
                                        print("<Difficulty changed to normal>")
                                currentDifficulty = 1
                                SwitchingDiff = False

                def Hard():
                    
                        global currentDifficulty
                        global cellNum
                        global ex
                        global Debug
                        global SwitchingDiff

                        if currentDifficulty != 2:
                                SwitchingDiff = True
                                currScriptName = sys.argv[0]
                                self.close()
                                cellNum = 30
                                ex = None
                                ex = Window()
                                if(Debug == 1):
                                        print("<Difficulty changed to hard>")
                                currentDifficulty = 2
                                SwitchingDiff = False


                def Custom():
                        USER_INP = simpledialog.askstring(title="Custom", prompt="Tiles per row:")

                        global currentDifficulty
                        global cellNum
                        global ex
                        global Debug
                        global SwitchingDiff

                        if str.isnumeric(USER_INP):
                                if int(USER_INP) >= 10 and int(USER_INP) <= 50: 
                                        SwitchingDiff = True               
                                        currScriptName = sys.argv[0]
                                        self.close()
                                        cellNum = int(USER_INP)
                                        ex = None
                                        ex = Window()
                                        if(Debug == 1):
                                                print("<Difficulty changed to custom ({} tiles per row)>".format(cellNum))
                                                if cellNum > 25:
                                                    print("[ WARNING! ]\n\tUsing large grid sizes will result in slowdowns!")
                                        SwitchingDiff = False     
                                else:
                                        print("Invalid entry!")
                                        Custom()
                        else:
                                print("Entry was not a number!")
                                Custom()

                

                def Quit():
                        reply = QMessageBox.question(self, 'Are you sure?', 'Are you sure you want to close the game?',
                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                        if reply == QMessageBox.Yes:
                            global UseTimer
                            global StartTimer
                            global BreakThread

                            StartTimer = False
                            UseTimer = False
                            BreakThread = True
                            #event.accept()
                            print('Game closed')
                            sys.exit(0)
                        else:
                            0+0
                            #event.ignore()
                             
                                    

                # create menu bar with menu File=>New to start a new game
                file_action = QAction("New Game", self)
                file_action.triggered.connect(self.init_game)
                
                file_action2 = QAction("Easy", self)
                file_action2.triggered.connect(Easy)
                
                file_action3 = QAction("Normal", self)
                file_action3.triggered.connect(Normal)
                
                file_action4 = QAction("Hard", self)
                file_action4.triggered.connect(Hard)

                file_action5 = QAction("Custom", self)
                file_action5.triggered.connect(Custom)

                file_action6 = QAction("Exit", self)
                file_action6.triggered.connect(Quit)
                
                main_menu = self.menuBar()
                file_menu = main_menu.addMenu('&File')
                file_menu.addAction(file_action)
                file_menu.addAction(file_action6)
                diff_menu = main_menu.addMenu('&Difficulty')
                diff_menu.addAction(file_action2)
                diff_menu.addAction(file_action3)
                diff_menu.addAction(file_action4)
                diff_menu.addAction(file_action5)

                

                # load page at startup
                self.main_page()

                # start new game at startup
                self.init_game()


            def closeEvent(self, event):
                global SwitchingDiff
                if SwitchingDiff == False:
                    reply = QMessageBox.question(self, 'Are you sure?', 'Are you sure you want to close the game?',
                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                    if reply == QMessageBox.Yes:
                        global UseTimer
                        global StartTimer
                        global BreakThread

                        StartTimer = False
                        UseTimer = False
                        BreakThread = True
                        event.accept()
                        print('Game closed')
                    else:
                        event.ignore()

            def main_page(self):
                global file1 #favicon
                global file2 #tile_1
                global file3 #tile_2
                global file4 #tile_3
                global file5 #tile_4
                global file6 #tile_5
                global file7 #tile_6
                global file8 #tile_7
                global file9 #tile_8
                global file10 #tile_clicked
                global file11 #tile_flag
                global file12 #tile_mine
                global file13 #tile_plain


                file1 = QtGui.QIcon(dataFolder + 'favicon.png')
                file2 = QtGui.QIcon(dataFolder + "tile_1.gif")
                file3 = QtGui.QIcon(dataFolder + "tile_2.gif")
                file4 = QtGui.QIcon(dataFolder + "tile_3.gif")
                file5 = QtGui.QIcon(dataFolder + "tile_4.gif")
                file6 = QtGui.QIcon(dataFolder + "tile_5.gif")
                file7 = QtGui.QIcon(dataFolder + "tile_6.gif")
                file8 = QtGui.QIcon(dataFolder + "tile_7.gif")
                file9 = QtGui.QIcon(dataFolder + "tile_8.gif")
                file10 = QtGui.QIcon(dataFolder + "tile_clicked.gif")
                file11 = QtGui.QIcon(dataFolder + "tile_flag.gif")
                file12 = QtGui.QIcon(dataFolder + "tile_mine.gif")
                file13 = QtGui.QIcon(dataFolder + 'tile_plain.gif')
                #print("NewGaem Lmao")
                global cellNum
                global Debug
                self.cells = cellNum
                # create central widget
                self.centralwidget = QWidget()
                self.setCentralWidget(self.centralwidget)

                # create all the buttons of the minesweeper game
                self.button = {}

                horizontal_layout = QHBoxLayout(self.centralwidget)
                for column in range(0, self.cells):
                    vertical_layout = QVBoxLayout()
                    for row in range(0, self.cells):
                        self.button[row, column] = QPushButton(self)
                        self.button[row, column].setFixedHeight(20)
                        self.button[row, column].setFixedWidth(20)
                        self.button[row, column].setIcon(QtGui.QIcon(dataFolder + 'tile_plain.gif'))
                        # set filter to detect right mouse click button
                        self.button[row, column].installEventFilter(self)
                        self.button[row, column].setObjectName(str(row) + ',' + str(column))
                        self.button[row, column].clicked.connect(partial(self.button_pressed, row, column))
                        vertical_layout.addWidget(self.button[row, column])
                    horizontal_layout.addLayout(vertical_layout)
                    horizontal_layout.setSpacing(0)
                self.show()
                # set screen to fixed size
                #self.setFixedSize(400,400)
                self.setFixedSize(self.size())
                #print(self.size())

            def eventFilter(self, obj, event):
                global Debug
                global StartTimer
                # right mouse click event
                if event.type() == QEvent.MouseButtonPress:
                    if event.button() == Qt.RightButton:
                        row, column = obj.objectName().split(',')
                        if StartTimer == False:
                            StartTimer = True
                            if Debug == 1:
                                print("Timer Started.")
                        if(Debug == 1):
                                print("Mouse right clicked at ({},{})".format(row, column))
                        # check for flags
                        if self.initialArray[int(row)][int(column)] == 19:
                            # flag present therefore remove flag
                            self.initialArray[int(row)][int(column)] = 9
                        else:
                            # no flag present therefore add flag
                            self.initialArray[int(row)][int(column)] = 19
                    self.update_display()
                return QObject.event(obj, event)

            def init_game(self):
                global file1 #favicon
                global file2 #tile_1
                global file3 #tile_2
                global file4 #tile_3
                global file5 #tile_4
                global file6 #tile_5
                global file7 #tile_6
                global file8 #tile_7
                global file9 #tile_8
                global file10 #tile_clicked
                global file11 #tile_flag
                global file12 #tile_mine
                global file13 #tile_plain

                global Debug
                global timePassed
                if(Debug == 1):
                        print("Starting new game with {} tiles per row.".format(self.cells))
                
                # reset counter of turns and timer
                self.counterTurns = 0
                timePassed = 0

                # initialize array with values
                self.initialArray=[[0 for i in range(self.cells)]for j in range(self.cells)]

                # add bombs and adjust surrounding cells
                numofBombs = 0
                for column in range(self.cells):
                    for row in range(self.cells):
                        # it is randomly decided whether a cell has a bomb, therefore the number of bombs is not fixed
                        # the chance of having a bomb can be adjusted by changing the range of randint
                        bomb = randint(0, 6)
                        if bomb == 0:
                            # if we have a bomb, we add 1 to the surrounding cells and write 9 to the current cell
                            self.initialArray[row][column] = 9
                            numofBombs += 1
                            if row - 1 >= 0 and self.initialArray[row - 1][column] != 9:
                                self.initialArray[row - 1][column] += 1
                            if row + 1 <= 9 and self.initialArray[row + 1][column] != 9:
                                self.initialArray[row + 1][column] += 1
                            if column - 1 >= 0 and self.initialArray[row][column - 1] != 9:
                                self.initialArray[row][column - 1] += 1
                            if column + 1 <= 9 and self.initialArray[row][column + 1] != 9:
                                self.initialArray[row][column + 1] += 1
                            if row - 1 >= 0 and column - 1 >= 0 and self.initialArray[row - 1][column - 1] != 9:
                                self.initialArray[row - 1][column - 1] += 1
                            if row + 1 <= 9 and column - 1 >= 0 and self.initialArray[row + 1][column - 1] != 9:
                                self.initialArray[row + 1][column - 1] += 1
                            if row - 1 >= 0 and column + 1 <= 9 and self.initialArray[row - 1][column + 1] != 9:
                                self.initialArray[row - 1][column + 1] += 1
                            if row + 1 <= 9 and column + 1 <= 9 and self.initialArray[row + 1][column + 1] != 9:
                                self.initialArray[row + 1][column + 1] += 1
                # update the display to default
                self.update_display()

                #Start Timer
                global TimerThread
                global UseTimer
                
                #UseTimer = False                
                #time.sleep(1)
                UseTimer = True
                
                
                
                if(Debug == 1):
                        print("{} bombs added.".format(numofBombs))

                
            def message_button(self):
                # if the button is pressed on the message box, a new game is started
                self.init_game()

            def button_pressed(self, row, column):
                global Debug
                global UseTimer
                global timePassed
                global Score
                global StartTimer
                global HiScore

                if StartTimer == False:
                            StartTimer = True
                            if Debug == 1:
                                print("Timer Started.")
                
                # change number of turns
                self.counterTurns += 1
                if(Debug == 1):
                        print("Mouse left clicked at ({},{})".format(row, column))

                # if the value is 19, a flag is on the button and the button can not be pressed
                if self.initialArray[row][column] != 19:
                    # check if the clicked cell has a bomb (value=9)
                    if self.initialArray[row][column] == 9:
                        self.button[row, column].setIcon(QtGui.QIcon(dataFolder + 'tile_mine.gif'))
                        game_busy = 0
                        message = "Game over, better luck next time!"
                        if(Debug == 1):
                                print("Player lost after {} turns.".format(self.counterTurns))

                    else:
                        # call method to display all the empty cells (value=0)
                        Score += 1000
                        self.display_empty_buttons(row, column)
                        
                        self.update_display()

                        # check whether all the cells (except bombs) are displayed
                        game_busy = 0
                        message = "Congratulations, you won!"
                        #print("Player won after {} turns.".format(self.counterTurns))
                        for x in self.initialArray:
                            if any(i in range(9) for i in x):
                                game_busy = 1

                    if game_busy == 0:
                        
                        # display all remaining cells when the game is finished
                        for row in range(self.cells):
                            for column in range(self.cells):
                                if self.initialArray[row][column] < 9:
                                    self.initialArray[row][column] += 10
                                elif self.initialArray[row][column] == 9 or self.initialArray[row][column] == 19:
                                    self.initialArray[row][column] = 29
                        self.update_display()

                        # pop-up when the game is finished
                        if(message == "Congratulations, you won!" and Debug == 1):
                                print("Player won after {} turns.".format(self.counterTurns))

                        UseTimer = False
                        game_finished = QMessageBox()
                        game_finished.setIcon(QMessageBox.Information)
                        game_finished.setText(message)
                        if timePassed > 0:
                            if int(int(Score*1000 / timePassed)/1000) > HiScore:
                                if timePassed > 0 and message == "Congratulations, you won!":
                                    

                                    if int(int(Score*1000 / timePassed)/1000) > 0:
                                        game_finished.setInformativeText("NEW HIGH SCORE!: " + str(int(int(Score*1000 / timePassed)/1000)))
                                        print("NEW HIGH SCORE!: " + str(int(int(Score*1000 / timePassed)/1000)))
                                        hiscore = open(dataFolder + "hiscore.lmfao", "w")
                                        hiscore.writelines(str(int(int(Score*1000 / timePassed)/1000)))
                                        hiscore.close()
                                        HiScore = int(int(Score*1000 / timePassed)/1000)
                                    
                                    else:
                                        game_finished.setInformativeText("Score: " + str(0))
                                else:
                                    game_finished.setInformativeText("Score: " + str(0))

                                
                                
                            
                            else:
                                if timePassed > 0 and message == "Congratulations, you won!":
                                    
                                    if int(int(Score*1000 / timePassed)/1000) > 0:
                                        game_finished.setInformativeText("Score: " + str(int(int(Score*1000 / timePassed)/1000)))
                                    else:
                                        game_finished.setInformativeText("Score: " + str(0))
                                else:
                                    game_finished.setInformativeText("Score: " + str(0))
                        StartTimer = False
                        game_finished.setWindowTitle("Pynesweeper")
                        game_finished.setStandardButtons(QMessageBox.Ok)
                        game_finished.buttonClicked.connect(self.message_button)
                        game_finished.exec_()
                        

            def display_empty_buttons(self, row, column):
                # the value of initialArray can be 0-8, 9 is for a bomb, 10-16 if it has been opened
                if self.initialArray[row][column] == 0:
                    # if it is a bomb check the surrounding areas
                    self.initialArray[row][column] += 10
                    if row - 1 >= 0:
                        self.display_empty_buttons(row - 1, column)
                    if row + 1 < self.cells:
                        self.display_empty_buttons(row + 1, column)
                    if column - 1 >= 0:
                        self.display_empty_buttons(row, column - 1)
                    if column + 1 < self.cells:
                        self.display_empty_buttons(row, column + 1)
                    if row - 1 >= 0 and column - 1 >= 0:
                        self.display_empty_buttons(row - 1, column - 1)
                    if row + 1 < self.cells and column - 1 >= 0:
                        self.display_empty_buttons(row + 1, column - 1)
                    if row - 1 >= 0 and column + 1 < self.cells:
                        self.display_empty_buttons(row - 1, column + 1)
                    if row + 1 < self.cells and column + 1 < self.cells:
                        self.display_empty_buttons(row + 1, column + 1)
                else:
                    # if it is not a bomb just mark it as clicked
                    if self.initialArray[row][column] < 9:
                        self.initialArray[row][column] += 10

            Col = 0
            rw = 0
            def update_display(self):
                if(Debug == 1):
                                print("[Updating Cells...]")
                            
                for column in range(self.cells):
                    #print(column)
                    for row in range(self.cells):
                        #print(row)
                        #print("R:{} || C:{}".format(row, column))
                        #if(Debug == 1):
                        #        print("[Changing tile ({},{})]".format(row,column))
                        #x = threading.Thread(target=self.DrawCell, args=(column, row))
                        #x.start()
                        #x = None
                        #print(row + column)
                        self.DrawCell(column, row)
                        #continue
                        0+0
                        
                        


            def DrawCell(self, column, row):
                global file1 #favicon
                global file2 #tile_1
                global file3 #tile_2
                global file4 #tile_3
                global file5 #tile_4
                global file6 #tile_5
                global file7 #tile_6
                global file8 #tile_7
                global file9 #tile_8
                global file10 #tile_clicked
                global file11 #tile_flag
                global file12 #tile_mine
                global file13 #tile_plain
                
                if self.initialArray[row][column] <= 9:
                    self.button[row, column].setIcon(file13)
                elif self.initialArray[row][column] == 10:
                    self.button[row, column].setIcon(file10)
                elif self.initialArray[row][column] == 11:
                    self.button[row, column].setIcon(file2)
                elif self.initialArray[row][column] == 12:
                    self.button[row, column].setIcon(file3)
                elif self.initialArray[row][column] == 13:
                    self.button[row, column].setIcon(file4)
                elif self.initialArray[row][column] == 14:
                    self.button[row, column].setIcon(file5)
                elif self.initialArray[row][column] == 15:
                    self.button[row, column].setIcon(file6)
                elif self.initialArray[row][column] == 16:
                    self.button[row, column].setIcon(file7)
                elif self.initialArray[row][column] == 19:
                    self.button[row, column].setIcon(file11)
                elif self.initialArray[row][column] == 29:
                    self.button[row, column].setIcon(file12)


        if __name__ == '__main__':
                print("Pynesweeper!\nCreated by Andrew Maney! (Main Game Code from github.com)")

                try:
                    if os.path.isdir(dataFolder):
                        0+0
                    else:
                            os.mkdir(dataFolder)
                            WriteIMGtoFiles()    

                    if(os.path.exists(dataFolder + "hiscore.lmfao")):
                        0+0
                    else:
                        hiscore = open(dataFolder + "hiscore.lmfao", "w")
                        hiscore.writelines("0")
                        hiscore.close()

                    



                    try:
                            if(sys.argv[1] == "-debug" or sys.argv[1] == "-d"):
                                    print("Started in debug mode.")
                                    Debug = 1
                    except:
                            0+0

                    
                    hiscore2 = open(dataFolder + "hiscore.lmfao", "r")
                    HiScore = int(hiscore2.read())
                    print("Current high score: {}".format(HiScore))
                    hiscore2.close()
                    UseTimer = True
                    TimerThread = threading.Thread(target=Timer)
                    TimerThread.start()
                    app = QApplication(sys.argv)
                    ex = Window()
                    
                    ex.setWindowIcon(QtGui.QIcon(file1)) 
                    
                    #open(dataFolder + "tile_plain.gif", "rb")
                    
                    sys.exit(app.exec_())
                except Exception as e:
                        exception_type, exception_object, exception_traceback = sys.exc_info()
                        filename = exception_traceback.tb_frame.f_code.co_filename
                        line_number = exception_traceback.tb_lineno

                        print("Exception type: ", exception_type)
                        print("File name: ", filename)
                        print("Line number: ", line_number)
                        print("E: {}".format(e))
                        sys.exit(0)

except Exception as ex:
        print(ex)
        sys.exit(0)















#  🙰□︎♏︎ ♌︎♓︎♎︎□︎❍︎♏︎ ♑︎♋︎♏︎ ●︎❍︎♋︎□︎
