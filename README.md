This code is written in C++ and python.

For simplicity,
you can run, ./encode.sh to get a demo encode. 
The 8 byte plain text is in ./encode/enc0, the 64 bit plain text is in ./encode/enc.
The 8 byte encoded cypher text is in ./encode/ans0, the 64 bit encoded cypher text is in ./encode/ans.

You can run ./decode.sh to get a demo decode
The 8 byte cypher text is in ./decode/dec0, the 64 bit cypher text is in ./decode/dec.
The 8 byte decoded plain text is in ./decode/ans0, the 64 bit decoded plain text is in ./decode/ans.


Details:

%-----------------------------------------------------------------

Encoding: all example I/O files are in directory "encode"

%-----------------------------------------------------------------
1. If your inputs are 8-byte askii code:
   You should build a file named "enc0"
       Format:
       key:
       8-byte key
       plain text:
       8-byte text
   Example file in ./encode/enc0
   and run python a2b.py < ./encode/enc0
   The output is a file named "enc"
   	   Format:
   	   key:
   	   64-bit key
   	   plain text:
   	   64-bit text
   Example file in ./encode/enc

2. If your inputs are 64-bit binary code:
   You should build a file named "enc", 
   the format is the same as the output of step 1.
   Example file in ./encode/enc

3. run make
   Then run
   ./DES --mode enc --file ./encode/enc
   The output file is named "ans":
	   Format:
	   key:
       64-bit key
       cypher:
       64-bit text
    Example file in ./encode/ans

4. If you want to get a 8-byte cypher text,
   run python b2a.py < ./encode/ans
   The output file is named "ans0"
   	   Format:
   	   key:
       8-byte key
       cypher:
       8-byte text
    Example file in ./encode/ans0

Step 3 and 4 get the file with the encoded cypher.


%-----------------------------------------------------------------

Decoding: all example I/O files are in directory "decode"

%-----------------------------------------------------------------
1. If your inputs are 8-byte askii code:
   You should build a file named "dec0"
       Format:
       key:
       8-byte key
       cypher:
       8-byte text
   Example file in ./decode/dec0
   and run python a2b.py < ./decode/dec0
   The output is a file named "dec"
   	   Format:
   	   key:
   	   64-bit key
   	   cypher:
   	   64-bit text
   Example file in ./decode/dec

2. If your inputs are 64-bit binary code:
   You should build a file named "dec", 
   the format is the same as the output of step 1.
   Example file in ./decode/dec

3. run make
   Then run
   ./DES --mode dec --file ./decode/dec
   The output file is named "ans":
	   Format:
	   key:
       64-bit key
       plain text:
       64-bit text
   Example file in ./decode/ans

4. If you want to get a 8-byte cypher text,
   run python b2a.py < ./decode/ans
   The output file is named "ans0"
   	   Format:
   	   key:
       8-byte key
       plain text:
       8-byte text
   Example file in ./decode/ans0

Step 3 and 4 get the file with the decoded plain text.

