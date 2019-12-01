#!/usr/bin/env python3
from time import sleep

keyStrokeDelay = .005

# Keycode Setup Shortcuts
_NULL = chr(0)
_BEGIN = _NULL*2
_CLOSE = _NULL*5
_CLEAR = _NULL*8
_SHIFT = chr(2)+_NULL

_CTRL = chr(1)+_NULL
_ALT = chr(4)+_NULL
_META = chr(8)+_NULL

_CTRL_R = chr(16)+_NULL
_SHIFT_R = chr(32)+_NULL
_ALT_R = chr(64)+_NULL
_META_R = chr(128)+_NULL

# Alphabet
_a = _BEGIN+chr(4)+_CLOSE
_A = _SHIFT+chr(4)+_CLOSE
_b = _BEGIN+chr(5)+_CLOSE
_B = _SHIFT+chr(5)+_CLOSE
_c = _BEGIN+chr(6)+_CLOSE
_C = _SHIFT+chr(6)+_CLOSE
_d = _BEGIN+chr(7)+_CLOSE
_D = _SHIFT+chr(7)+_CLOSE
_e = _BEGIN+chr(8)+_CLOSE
_E = _SHIFT+chr(8)+_CLOSE
_f = _BEGIN+chr(9)+_CLOSE
_F = _SHIFT+chr(9)+_CLOSE
_g = _BEGIN+chr(10)+_CLOSE
_G = _SHIFT+chr(10)+_CLOSE
_h = _BEGIN+chr(11)+_CLOSE
_H = _SHIFT+chr(11)+_CLOSE
_i = _BEGIN+chr(12)+_CLOSE
_I = _SHIFT+chr(12)+_CLOSE
_j = _BEGIN+chr(13)+_CLOSE
_J = _SHIFT+chr(13)+_CLOSE
_k = _BEGIN+chr(14)+_CLOSE
_K = _SHIFT+chr(14)+_CLOSE
_l = _BEGIN+chr(15)+_CLOSE
_L = _SHIFT+chr(15)+_CLOSE
_m = _BEGIN+chr(16)+_CLOSE
_M = _SHIFT+chr(16)+_CLOSE
_n = _BEGIN+chr(17)+_CLOSE
_N = _SHIFT+chr(17)+_CLOSE
_o = _BEGIN+chr(18)+_CLOSE
_O = _SHIFT+chr(18)+_CLOSE
_p = _BEGIN+chr(19)+_CLOSE
_P = _SHIFT+chr(19)+_CLOSE
_q = _BEGIN+chr(20)+_CLOSE
_Q = _SHIFT+chr(20)+_CLOSE
_r = _BEGIN+chr(21)+_CLOSE
_R = _SHIFT+chr(21)+_CLOSE
_s = _BEGIN+chr(22)+_CLOSE
_S = _SHIFT+chr(22)+_CLOSE
_t = _BEGIN+chr(23)+_CLOSE
_T = _SHIFT+chr(23)+_CLOSE
_u = _BEGIN+chr(24)+_CLOSE
_U = _SHIFT+chr(24)+_CLOSE
_v = _BEGIN+chr(25)+_CLOSE
_V = _SHIFT+chr(25)+_CLOSE
_w = _BEGIN+chr(26)+_CLOSE
_W = _SHIFT+chr(26)+_CLOSE
_x = _BEGIN+chr(27)+_CLOSE
_X = _SHIFT+chr(27)+_CLOSE
_y = _BEGIN+chr(28)+_CLOSE
_Y = _SHIFT+chr(28)+_CLOSE
_z = _BEGIN+chr(29)+_CLOSE
_Z = _SHIFT+chr(29)+_CLOSE

# Numbers

_1 = _BEGIN+chr(30)+_CLOSE
_2 = _BEGIN+chr(31)+_CLOSE
_3 = _BEGIN+chr(32)+_CLOSE
_4 = _BEGIN+chr(33)+_CLOSE
_5 = _BEGIN+chr(34)+_CLOSE
_6 = _BEGIN+chr(35)+_CLOSE
_7 = _BEGIN+chr(36)+_CLOSE
_8 = _BEGIN+chr(37)+_CLOSE
_9 = _BEGIN+chr(38)+_CLOSE
_0 = _BEGIN+chr(39)+_CLOSE
_TENKEY1 = _BEGIN+chr(89)+_CLOSE
_TENKEY2 = _BEGIN+chr(90)+_CLOSE
_TENKEY3 = _BEGIN+chr(91)+_CLOSE
_TENKEY4 = _BEGIN+chr(92)+_CLOSE
_TENKEY5 = _BEGIN+chr(93)+_CLOSE
_TENKEY6 = _BEGIN+chr(94)+_CLOSE
_TENKEY7 = _BEGIN+chr(95)+_CLOSE
_TENKEY8 = _BEGIN+chr(96)+_CLOSE
_TENKEY9 = _BEGIN+chr(97)+_CLOSE
_TENKEY0 = _BEGIN+chr(98)+_CLOSE

# Non-Printing Keys

_ENTER = _BEGIN+chr(40)+_CLOSE
_ESCAPE = _BEGIN+chr(41)+_CLOSE
_BACKSPACE = _BEGIN+chr(42)+_CLOSE
_TAB = _BEGIN+chr(43)+_CLOSE
_SPACE =  _BEGIN+chr(44)+_CLOSE
_CAPSLOCK = _BEGIN+chr(57)+_CLOSE
_PRINTSCREEN = _BEGIN+chr(70)+_CLOSE
_SCROLLLOCK = _BEGIN+chr(71)+_CLOSE
_PAUSE = _BEGIN+chr(72)+_CLOSE
_INSERT = _BEGIN+chr(73)+_CLOSE
_HOME = _BEGIN+chr(74)+_CLOSE
_PAGEUP = _BEGIN+chr(75)+_CLOSE
_DELETE = _BEGIN+chr(76)+_CLOSE
_END = _BEGIN+chr(77)+_CLOSE
_PAGEDOWN = _BEGIN+chr(78)+_CLOSE
_RIGHT = _BEGIN+chr(79)+_CLOSE
_LEFT = _BEGIN+chr(80)+_CLOSE
_DOWN = _BEGIN+chr(81)+_CLOSE
_UP = _BEGIN+chr(82)+_CLOSE
_NUMBERLOCK = _BEGIN+chr(83)+_CLOSE
_TENKEYENTER = _BEGIN+chr(88)+_CLOSE

# Symbols

_HYPHEN = _BEGIN+chr(45)+_CLOSE
_UNDERSCORE = _SHIFT+chr(45)+_CLOSE
_EQUALS = _BEGIN+chr(46)+_CLOSE
_PLUS = _SHIFT+chr(46)+_CLOSE
_LEFTBRACKET = _BEGIN+chr(47)+_CLOSE
_LEFTBRACE = _SHIFT+chr(47)+_CLOSE
_RIGHTBRACKET = _BEGIN+chr(48)+_CLOSE
_RIGHTBRACE = _SHIFT+chr(48)+_CLOSE
_BACKSLASH = _BEGIN+chr(49)+_CLOSE
_PIPE = _SHIFT+chr(49)+_CLOSE
_ELLIPSIS = _BEGIN+chr(50)+_CLOSE
_SEMICOLON = _BEGIN+chr(51)+_CLOSE
_COLON = _SHIFT+chr(51)+_CLOSE
_SINGLEQUOTE = _BEGIN+chr(52)+_CLOSE
_DOUBLEQUOTE = _SHIFT+chr(52)+_CLOSE
_BACKQUOTE = _BEGIN+chr(53)+_CLOSE
_TILDE = _SHIFT+chr(53)+_CLOSE
_COMMA = _BEGIN+chr(54)+_CLOSE
_LESSTHAN = _SHIFT+chr(54)+_CLOSE
_PERIOD = _BEGIN+chr(55)+_CLOSE
_GREATERTHAN = _SHIFT+chr(55)+_CLOSE
_SLASH = _BEGIN+chr(56)+_CLOSE
_QUESTIONMARK = _SHIFT+chr(56)+_CLOSE
_TENKEYDIVIDE = _BEGIN+chr(84)+_CLOSE
_TENKEYMULTIPLY = _BEGIN+chr(85)+_CLOSE
_TENKEYSUBTRACT = _BEGIN+chr(86)+_CLOSE
_TENKEYADD = _BEGIN+chr(87)+_CLOSE
_BANG = _SHIFT+chr(30)+_CLOSE
_AT = _SHIFT+chr(31)+_CLOSE
_HASH = _SHIFT+chr(32)+_CLOSE
_DOLLAR = _SHIFT+chr(33)+_CLOSE
_PERCENT = _SHIFT+chr(34)+_CLOSE
_CARET = _SHIFT+chr(35)+_CLOSE
_AMPERSAND = _SHIFT+chr(36)+_CLOSE
_ASTERISK = _SHIFT+chr(37)+_CLOSE
_LEFTPARENTHESIS = _SHIFT+chr(38)+_CLOSE
_RIGHTPARENTHESIS = _SHIFT+chr(39)+_CLOSE

# Function Keys

_F1 = _BEGIN+chr(58)+_CLOSE
_F2 = _BEGIN+chr(59)+_CLOSE
_F3 = _BEGIN+chr(60)+_CLOSE
_F4 = _BEGIN+chr(61)+_CLOSE
_F5 = _BEGIN+chr(62)+_CLOSE
_F6 = _BEGIN+chr(63)+_CLOSE
_F7 = _BEGIN+chr(64)+_CLOSE
_F8 = _BEGIN+chr(65)+_CLOSE
_F9 = _BEGIN+chr(66)+_CLOSE
_F10 = _BEGIN+chr(67)+_CLOSE
_F11 = _BEGIN+chr(68)+_CLOSE
_F12 = _BEGIN+chr(69)+_CLOSE

# Keyboard Shortcut Combos EXPERIMENTAL

_RUN = _META+chr(21)+_CLOSE
_SAVE = _CTRL+chr(22)+_CLOSE
_OUTPUT = _CTRL+chr(18)+_CLOSE
_CLOSEWINDOW = _ALT+chr(61)+_CLOSE

# Map characters to codes

charDict = {
" ": _SPACE,
"a": _a, 
"b": _b, 
"c": _c, 
"d": _d, 
"e": _e, 
"f": _f, 
"g": _g, 
"h": _h, 
"i": _i, 
"j": _j, 
"k": _k, 
"l": _l, 
"m": _m, 
"n": _n, 
"o": _o, 
"p": _p, 
"q": _q, 
"r": _r, 
"s": _s, 
"t": _t, 
"u": _u, 
"v": _v, 
"w": _w, 
"x": _x, 
"y": _y, 
"z": _z, 
"A": _A, 
"B": _B, 
"C": _C, 
"D": _D, 
"E": _E, 
"F": _F, 
"G": _G, 
"H": _H, 
"I": _I, 
"J": _J, 
"K": _K, 
"L": _L, 
"M": _M, 
"N": _N, 
"O": _O, 
"P": _P, 
"Q": _Q, 
"R": _R, 
"S": _S, 
"T": _T, 
"U": _U, 
"V": _V, 
"W": _W, 
"X": _X, 
"Y": _Y, 
"Z": _Z, 
"1": _1, 
"2": _2, 
"3": _3, 
"4": _4, 
"5": _5, 
"6": _6, 
"7": _7, 
"8": _8, 
"9": _9, 
"0": _0, 
"`": _BACKQUOTE, 
"~": _TILDE, 
"!": _BANG, 
"@": _AT, 
"#": _HASH, 
"$": _DOLLAR, 
"%": _PERCENT, 
"^": _CARET, 
"&": _AMPERSAND, 
"*": _ASTERISK, 
"(": _LEFTPARENTHESIS, 
")": _RIGHTPARENTHESIS, 
"-": _HYPHEN, 
"_": _UNDERSCORE, 
"=": _EQUALS, 
"+": _PLUS, 
"{": _LEFTBRACE, 
"}": _RIGHTBRACE, 
"[": _LEFTBRACKET, 
"]": _RIGHTBRACKET, 
"|": _PIPE, 
":": _COLON, 
";": _SEMICOLON, 
"\"": _DOUBLEQUOTE, 
"'": _SINGLEQUOTE, 
",": _COMMA, 
".": _PERIOD, 
"/": _SLASH, 
"<": _LESSTHAN, 
">": _GREATERTHAN, 
"?": _QUESTIONMARK, 
"\\": _BACKSLASH, 
"\"": _DOUBLEQUOTE, 
"\b": _BACKSPACE, 
"\t": _TAB, 
"\n": _ENTER 
}

def tx(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
        fd.write(_CLEAR.encode())
        sleep(keyStrokeDelay)

def TX(string):
    for c in string:
        tx(getCode(c))

def getCode(character):
    return charDict[character]
