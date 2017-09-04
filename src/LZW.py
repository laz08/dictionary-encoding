#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Utils


#Encodes using the LZW algorithm
#Txt: text to encode
#Returns a tuple containing:
#   1.- Bits to encode
#   2.- Dictionary
#   3.- List of tokens
def encode(txt):

    #INITIALIZATION
    dic = {}
    for l in set(txt):
        dic[l] = len(dic)

    bs = 0
    #COMPRESSION
    word = ""
    tokens = []
    for c in txt:

        newWord = word + c
        if newWord in dic:
            word = newWord

        else:

            pointer = Utils.getPointer(word, dic)
            tokens.append(pointer)

            dic[newWord] = len(dic)
            word = c

            bs = bs + Utils.getNumberOfBitsPerEntry(pointer)

    if word:
        p = Utils.getPointer(word, dic)
        tokens.append(p)
        bs = bs + Utils.getNumberOfBitsPerEntry(p)

    bsTotal = bs/len(tokens)
    return (bsTotal, dic, tokens)

#Decodes LZW
#dic: Dictionary of text's letters to decode
#tok: List of tokens
def decode(dic, tokens):

    decoded = ""
    for tok in tokens:

        word = Utils.findKeyOfValue(dic, tok)
        decoded = decoded + word

    return decoded
