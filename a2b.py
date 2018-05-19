import sys
zeros = "00000000"

te = sys.stdin.read().split('\n')
def generate_binary(s):
	blist = []
	for i in range(len(s)):
		c =  s[i]
		binary =  str(bin(ord(c))[2:])
		if len(binary)<8:
			binary = zeros[0: 8-len(binary)] + binary
		blist.append(binary)
	return "".join(blist)


if te[2]=="plain text:":
	mode = "enc"
else:
	mode = "dec"

input_key = te[1]
input_text = te[3]

key=generate_binary(input_key)
text = generate_binary(input_text)

if mode=="enc":
	fo = open("./encode/enc", "w")
	fo.write( "key:\n")
	fo.write(key+"\n")
	fo.write("plain text:\n")
	fo.write(text+"\n")

if mode == "dec":
	fo = open("./decode/dec", "w")
	fo.write( "key:\n")
	fo.write(key+"\n")
	fo.write("cypher:\n")
	fo.write(text+"\n")