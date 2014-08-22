import ply.lex as lex
import re

tokens = ( 'SECTION',
           'IDENTIFIER',
           'STRING',
           'LBRACE',
           'RBRACE',
           'SEMI',
           'EQU',
           'TRUE',
           'FALSE' )
           

def t_SECTION(t):
    r'section'
    return t

def t_TRUE(t):
    r'(true|1)'
    return t

def t_FALSE(t):
    r'(false|0)'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z\-0-9]+'
    return t

def t_STRING(t):
    r'(\".*\"|\'.*\')'
    t.value = t.value[1:-1]
    return t

def t_LBRACE(t):
    r'{'
    return t

def t_EQU(t):
    r'='
    return t

def t_RBRACE(t):
    r'}'
    return t

def t_SEMI(t):
    r';'
    return t

def t_NEWLINE(t):
    r'\n+'

    t.lexer.lineno += len(t.value)
    return t

t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    t.lexer.skip(1)

lexer = lex.lex()
