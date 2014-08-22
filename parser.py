#!/usr/bin/env python
import sys
import pprint
import ply.yacc as yacc

from lexer import tokens

def p_config(p):
    ''' config : sections '''
    p[0] = p[1]

def p_sections(p):
    ''' sections : sections section
                 | section
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_section(p):
    ''' section : SECTION IDENTIFIER LBRACE statements RBRACE '''
    p[0] = { 'name': p[2], 'content': p[4] }

def p_statements(p):
    ''' statements : statements statement
                   | statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    ''' statement : IDENTIFIER EQU value SEMI '''
    p[0] = {'name': p[1], 'value': p[3]}

def p_value(p):
    ''' value : IDENTIFIER
              | STRING
              | boolean
    '''
    p[0] = p[1]

def p_boolean(p):
    ''' boolean : TRUE
                | FALSE
    '''
    p[0] = p[1]

start = 'config'

filename = sys.argv[1]

parser = yacc.yacc()

pp = pprint.PrettyPrinter(indent=4)

with open(filename, 'r') as f:
    input = f.read()
    pp.pprint(parser.parse(input))

