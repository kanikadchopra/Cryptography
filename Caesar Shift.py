import check 

## IMPORTANT CONSTANTS AND DICTIONARIES:
loweralphabet = list("abcdefghijklmnopqrstuvwxyz")
upperalphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowerdictionary = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,\
                   'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,\
                   'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25, \
                   'z':26}

upperdictionary = {'A':101,'B':102,'C':103,'D':104,'E':105,'F':106,'G':107,\
                   'H':108,'I':109,'J':110,'K':111,'L':112,'M':113,'N':114,\
                   'O':115,'P':116,'Q':117,'R':118,'S':119,'T':120,'U':121,\
                   'V':122,'W':123,'X':124,'Y':125, 'Z':126}

## This part of the code focuses on the encoding of a message using the Caesar shift.

## max_freq(s) will consume a String, s, and return the number of times that 
## the most frequent letter appears in s  
## max_freq: Str -> Nat 
## Examples:
## max_freq("") => 0 
## max_freq("a") => 1 
## max_freq("apple") => 2

def max_freq(s):
    
    characters = {}
    s = s.lower()
    for i in range(len(s)):
        if s[i] in characters:
            characters[s[i]] = characters[s[i]] + 1 
        else:
            characters[s[i]] = 1
            
    most_common = " "
    maxsofar = 0 
    for curr_char in characters:
        if characters[curr_char] >maxsofar:
            most_common = curr_char 
            maxsofar = characters[curr_char]
    return maxsofar

## lst_code(s) consumes a String, s, and returns a list that is the length of 
## the string but based on the numeric values associated with each letter in 
## the string using lowerdictionary and upperdictionary after adding the 
## maximum frequency of a character in s 
## lst_code: String -> (listof Nat)
## Examples:
## lst_code("") => []
## lst_code("a") => [2]
## lst_code("apple") => [3, 18,  18, 14, 7]

def lst_code(s): 
    lst = list(s)
    shift = max_freq(s)
    for i in range(len(lst)):
        if lst[i] in lowerdictionary:
            lst[i] = lowerdictionary[lst[i]] + shift 
            while lst[i]>26:
                lst[i] = lst[i] - 26 
        elif lst[i] in upperdictionary:
            lst[i] = upperdictionary[lst[i]] + shift
            while lst[i] > 126: 
                lst[i] = lst[i] - 26

    return lst
        
## shift_encode(s) consumes a String, s, and returns a new string that is 
## encoded based on the Cipher shift. It takes the number of appearances of the 
## most frequent character in s, and shifts each letter up the alphabet by 
## that factor and results in a new string (encrypts the message)
## shift_encode: String -> String 
## Examples:
## shift_encode("") => ""
## shift_encode("a") => "b"
## shift_encode("abc") => "bcd"
## shift_encode("abba") => "cddc"

def shift_encode(s):
    lst = lst_code(s)
    pos = 0 
    while pos<len(lst):
        for i in loweralphabet:
            if lowerdictionary[i]==lst[pos]:
                lst[pos] = i 
        pos = pos + 1
    pos = 0 
    while pos<len(lst):
        for i in upperalphabet:
            if upperdictionary[i]==lst[pos]:
                lst[pos] = i 
        pos = pos + 1 
    new = "".join(lst)
    return new 
    
## Tests for encrpying the messages 
## Test 1 - len(s) = 1 
check.expect("Q1AT1", shift_encode("a"), "b")
## Test 2 - len(s) > 1 with max frequency 1
check.expect("Q1AT2", shift_encode("abc"), "bcd")
## Test 3 - len(s) > 1 with max frequency 2 
check.expect("Q1AT3", shift_encode("abba"), "cddc")
## Test 4 - len(s) > 1 with two letters appearing the same number of times
check.expect("Q1AT4", shift_encode("abab"), "cdcd")
## Test 5 - Max frequency above 26 times (lowercase)
check.expect("Q1AT5", shift_encode("apple"*28), "ettpi"*28)
## Test 6 - Empty string 
check.expect("Q1AT6", shift_encode(""), "")
## Test 7 - all lowercase letters 
check.expect("Q1AT7", shift_encode("apple"), "crrng")
## Test 8 - all uppercase letters 
check.expect("Q1AT8", shift_encode("APPLE"), "CRRNG")
## Test 9 - same number of uppercase 'A's as lowercase 'a's
check.expect("Q1AT9", shift_encode("ababABAB"), "efefEFEF")
## Test 10 - more uppercase than lowercase letters
check.expect("Q1AT10", shift_encode("MARAHMARAh"), 'QEVELQEVEl')
## Test 11 - more lowercase than uppercase letters 
check.expect("Q1AT11", shift_encode('marahmaraH'), 'qevelqeveL')
## Test 12 - Max frequency above 26 times (uppercase)
check.expect("Q1AT12", shift_encode("APPLE"*28), "ETTPI"*28)
## Test 13 - mix of uppercase and lowercase letters (different frequencies)
check.expect("Q1AT13", shift_encode("hey WHATS UP? hows it going?"), 
             'mjd BMFYX ZU? mtbx ny ltnsl?')
## Test 14 - Sentences with spaces in between
check.expect("Q1AT14", shift_encode("HEY! Where you at?"), "KHB! Zkhuh brx dw?")
## Test 15 - max frequency is 26 times 
check.expect("Q1AT15", shift_encode("Q"*26), "Q"*26)
## Test 16 - string with numbers in it
check.expect("Q1AT16", shift_encode("water123bottle456"), 'zdwhu123erwwoh456')
## Test 17 - string with more numbers/other characters than letters
check.expect("Q1AT17", shift_encode("app123456le"), 'crr123456ng')
## Test 18 - string with more letters than numbers/other characters 
check.expect("Q1AT18", shift_encode("a2b"), "b2c")

## This next part of the code will be for decrypting the message that has been encrypted using a Caesar shift. 

## delst(s) consumes a String, s, and returns a list that is the length of 
## the string but based on the numeric values associated with each letter in 
## the string using lowerdictionary and upperdictionary after subtracting the 
## maximum frequency of a character in s 
## delst: String -> (listof Nat)
## Examples:
## delst('') => []
## delst("a") => [26]
## delst("abc") => [26, 1, 2]
## delst("abba") => [25, 26, 26, 25]

def delst(s):
    lst = list(s)
    shift = max_freq(s)
    for i in range(len(lst)):
        if lst[i] in lowerdictionary:
            lst[i] = lowerdictionary[lst[i]] - shift 
            while lst[i]<=0:
                lst[i] = lst[i] + 26 
        elif lst[i] in upperdictionary:
            lst[i] = upperdictionary[lst[i]] - shift
            while lst[i] <=100: 
                lst[i] = lst[i] + 26

    return lst
        

## shift_decode(s) consumes a String, s, and returns a new string that is 
## decoded based on the Cipher shift. It takes the number of appearances of the 
## most frequent character in s and shifts the letters down the alphabet by 
## that factor to create a new string (decrypts the message)
## shift_decode(s): String -> String 
## Examples:
## shift_decode("") => ""
## shift_decode("a") => "z"
## shift_decode("bcd") => "abc"
## shift_decode("cddc") => "abba"

def shift_decode(s):
    lst = delst(s)
    pos = 0 
    while pos<len(lst):
        for i in loweralphabet:
            if lowerdictionary[i]==lst[pos]:
                lst[pos] = i 
        pos = pos + 1
    pos = 0 
    while pos<len(lst):
        for i in upperalphabet:
            if upperdictionary[i]==lst[pos]:
                lst[pos] = i 
        pos = pos + 1 
    new = "".join(lst)
    return new 

## Tests for Decrypting a message
## Test 1 - len(s) = 1 
check.expect("Q1BT1", shift_decode("b"), "a")
## Test 2 - len(s) > 1 with max frequency 1
check.expect("Q1BT2", shift_decode("bcd"), "abc")
## Test 3 - len(s) > 1 with max frequency 2 
check.expect("Q1BT3", shift_decode("cddc"), "abba")
## Test 4 - len(s) > 1 with two letters appearing the same number of times
check.expect("Q1BT4", shift_decode("cdcd"), "abab")
## Test 5 - Max frequency above 26 times (lowercase)
check.expect("Q1BT5", shift_decode("ettpi"*28), "apple"*28)
## Test 6 - Empty string 
check.expect("Q1BT6", shift_decode(""), "")
## Test 7 - all lowercase letters 
check.expect("Q1BT7", shift_decode("crrng"), "apple")
## Test 8 - all uppercase letters 
check.expect("Q1BT8", shift_decode("CRRNG"), "APPLE")
## Test 9 - same number of uppercase 'A's as lowercase 'a's
check.expect("Q1BT9", shift_decode("efefEFEF"), "ababABAB")
## Test 10 - more uppercase than lowercase letters
check.expect("Q1BT10", shift_decode('QEVELQEVEl'), "MARAHMARAh")
## Test 11 - more lowercase than uppercase letters 
check.expect("Q1BT11", shift_decode('qevelqeveL'), 'marahmaraH')
## Test 12 - Max frequency above 26 times (uppercase)
check.expect("Q1AT12", shift_encode("APPLE"*28), "ETTPI"*28)
## Test 13 - mix of uppercase and lowercase letters (different frequencies)
check.expect("Q1AT13", shift_encode("hey WHATS UP? hows it going?"), 
             'mjd BMFYX ZU? mtbx ny ltnsl?')
## Test 14 - Sentences with spaces in between
check.expect("Q1BT14", shift_decode("KHB! Zkhuh brx dw?"), "HEY! Where you at?")
## Test 15 - max frequency is 26 times 
check.expect("Q1BT15", shift_decode("Q"*26), "Q"*26)
## Test 16 - string with numbers in it
check.expect("Q1BT16", shift_decode('zdwhu123erwwoh456'), "water123bottle456") 
## Test 17 - string with more numbers/other characters than letters
check.expect("Q1BT17", shift_decode('crr123456ng'), "app123456le")
## Test 18 - string with more letters than numbers/other characters 
check.expect("Q1BT18", shift_decode("b2c"), "a2b")