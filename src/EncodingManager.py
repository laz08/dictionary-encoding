#!/usr/bin/python
# -*- coding: UTF-8 -*-

import algs.LZ77 as LZ77
import algs.LZ78 as LZ78
import algs.LZSS as LZSS
import algs.LZW as LZW

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
