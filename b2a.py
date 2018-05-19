import binascii
import sys
te = sys.stdin.read().split('\n')

def generate_word(s):
	word_list = []

	for i in range(0,8):
		str_num = s[i*8:i*8+8]
		num = int(str_num,2)
		word_list.append(str(chr(num)))
	word = "".join(word_list)
	return word

if te[2]=="cypher:":
	mode = "enc"
else:
	mode = "dec"

key = generate_word(te[1])

text = generate_word(te[3])

if mode=="enc":
	fo = open("./encode/ans0", "w")
	fo.write("key:\n")
	fo.write(key+"\n")
	fo.write("cypher:\n")
	fo.write(text+"\n")	

if mode == "dec":
	fo = open("./decode/ans0", "w")
	fo.write("key:\n")
	fo.write(key+"\n")
	fo.write( "plain text:\n")
	fo.write(text+"\n")	

