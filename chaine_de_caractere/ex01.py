def palindrome_check (mot):
   mot_invert = ""
   nb = len(mot)
   nb = nb - 1
   for i in range(nb, -1, -1):
       mot_invert = mot_invert + mot[i]
   print (mot_invert)
   if mot_invert == mot:
       return True
   else:
       return False    
print(palindrome_check("kayak"))