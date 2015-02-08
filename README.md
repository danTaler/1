# User-Hash-Convertor
This script takes cracked hashes and user lists and formats them into one readable file.

Supported formats:
-NTDS (windows AD hashes)
-LM
-NTLM

For example:
1. File 1:
      Mike:AVFDBHJYIFHMUILUIJNRTVWGTRH
      Mark:GRYJI&KTEYHEEFETHTJRIKE%^GE
      Smith:GHJFRHYJKE^JTEGREHUWEJRJY
      Bendico:JKYKTYKUETJTYJEGDHAGHADH
      
2. File 2:
      AVFDBHJYIFHMUILUIJNRTVWGTRH:password1
      GRYJI&KTEYHEEFETHTJRIKE%^GE:Secr3t
      JKYKTYKUETJTYJEGDHAGHADH:myPass123
      
Result:
File 3:
    Mike:AVFDBHJYIFHMUILUIJNRTVWGTRH:password1
    Mark:GRYJI&KTEYHEEFETHTJRIKE%^GE:Secr3t
    Bendico:JKYKTYKUETJTYJEGDHAGHADH:myPass123
