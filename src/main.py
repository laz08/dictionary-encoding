#!/usr/bin/python3.4
# -*- coding: UTF-8 -*-
import EncodingManager, Utils
import sys, getopt

def usage():

    print ('Usage: main.py -i <inputfile>')
    sys.exit(2)

def main(argv):

    if len(argv) < 2:
         usage()
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-i", "--ifile"):
            filein = arg
        elif opt in ("-s", "--source"):
            filein = arg


    print ("Reading from file " + filein)
    result = Utils.readFromFile(filein)


##------------------------------------------------------------------------------
##----------------------------------- PARAMS -----------------------------------
##------------------------------------------------------------------------------
    LZ77_OFFSET = 4
    LZ77_LENGTH = 4
    MATCH = 1

    doLZ77 = True
    doLZSS = True
    doLZ78 = True
    doLZW = True

##------------------------------------------------------------------------------
##-----------------------------------  LZ77 ------------------------------------
##------------------------------------------------------------------------------

    if(doLZ77):

        print ('')
        print("LZ77 encoding")
        tokens = EncodingManager.encodeLZ77(result, LZ77_OFFSET, LZ77_LENGTH)
        print (tokens)

        print("LZ77 decoding")
        decodedLz77 = EncodingManager.decodeLZ77(tokens[1])
        #print (decodedLz77)

        #print("Before: " +  result)
        #print("After:  " + decodedLz77)
        print("Is the same: " +  str(result == decodedLz77))


##------------------------------------------------------------------------------
##-----------------------------------  LZSS ------------------------------------
##------------------------------------------------------------------------------

    if(doLZSS):

        print ("------------------")
        print ('')
        print("LZSS encoding")
        tokens = EncodingManager.encodeLZSS(result, LZ77_OFFSET, LZ77_LENGTH, MATCH)
        print (tokens)

        print("LZSS decoding")
        decodedLzSS = EncodingManager.decodeLZSS(tokens[1])
        #print (decodedLzSS)

        #print ("Before: " +  result)
        #print ("After:  " + decodedLzSS)
        print ("Is the same: " +  str(result == decodedLzSS))


##------------------------------------------------------------------------------
##-----------------------------------  LZ78 ------------------------------------
##------------------------------------------------------------------------------

    if(doLZ78):

        print ("------------------")
        print ('')
        print("LZ78 encoding")
        tokens = EncodingManager.encodeLZ78(result)
        print (tokens)

        print("LZ78 decoding")
        decodedLz78 = EncodingManager.decodeLZ78(tokens[1])
        #print (decodedLz78)

        #print ("Before: " +  result)
        #print ("After:  " + decodedLz78)
        print ("Is the same: " +  str(result == decodedLz78))


##------------------------------------------------------------------------------
##-----------------------------------  LZW  ------------------------------------
##------------------------------------------------------------------------------

    if(doLZW):

        print ("------------------")
        print ('')
        print("LZW encoding")
        resultLZW = EncodingManager.encodeLZW(result)
        print("Number of bits: " + str(resultLZW[0]))
        print (resultLZW[2])

        print("LZW decoding")
        decodedLZW = EncodingManager.decodeLZW(resultLZW[1], resultLZW[2])
        #print (decodedLZW)

        #print ("Before: " +  result)
        #print ("After:  " + decodedLZW)
        print ("Is the same: " +  str(result == decodedLZW))

if __name__ == "__main__":
   main(sys.argv[1:])
