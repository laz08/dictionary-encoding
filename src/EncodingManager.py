#!/usr/bin/python
# -*- coding: UTF-8 -*-

import LZ77, LZ78, LZSS, LZW

##--------------------------------------------------------------
##-------------------------- ENCODING --------------------------
##--------------------------------------------------------------

def encodeLZ77(txt, s, t):
    return LZ77.encode(txt, s, t)

def decodeLZ77(tok):
    return LZ77.decode(tok)


def encodeLZSS(txt, s, t, m):
    return LZSS.encode(txt, s, t, m)

def decodeLZSS(tok):
    return LZSS.decode(tok)


def encodeLZ78(txt):
    return LZ78.encode(txt)

def decodeLZ78(tokens):
    return LZ78.decode(tokens)


def encodeLZW(txt):
    return LZW.encode(txt)

def decodeLZW(dic, tokens):
    return LZW.decode(dic, tokens)
