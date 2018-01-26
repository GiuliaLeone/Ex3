#! /usr/bin/env python
#Leone Giulia s3494225
#EX9
#build a program that takes a string of text represeting a DNA sequence
#I define the sequence that I want to use
#I am going to do now EX11 so I will keep everything I did previously but marked as a comment the part that are not specifically needed for ex11

DNASeq = 'ATGAAC'

#This function added immidiatly after the existing DNASeq definition presents a prompt to the user consisting of the string within the parentheses
DNASeq= raw_input("Enter a DNAsequence: ")

#the function .upper() .returns an uppercase version of that strig. this function doesn't require any paramters in parentheses
DNASeq = DNASeq.upper()

#to remove the spaces it is possible to use the string function .replace() In this case we will remove a space " " and replace it with an empty set of quotes, ""
DNASeqA = DNASeq.replace(" ","")

#I'm printing the ohrase 'sequence' and then the sequence itself
print 'Sequence:', DNASeq

#float() can also convert integers to floats. Modify the SeqLength line of your code 
SeqLength = float(len(DNASeq))

#This provide the sequence itself an the length

print 'Sequence Length:', SeqLength

#The method .count() counts how many times a particular substring occurs in a string 

NumberA = DNASeq.count( 'A' )
NumberC = DNASeq.count( 'C ')
NumberG = DNASeq.count( 'G' )
NumberT = DNASeq.count( 'T' )

#calculate the percentage and output to 1 decimal 
#print "A: %.1f" % (100 * NumberA / SeqLength)
#print "C: %.1f" % (100 * NumberC / SeqLength)
#print "G: %.1f" % (100 * NumberG / SeqLength)
#print "T: %.1f" % (100 * NumberT / SeqLength)


#SeqLength = len(DNASeq)
#the str() function helps converting other data type including numbers to strings
#print '7'+ str(3*2)

#the float() function converts a string or integer to a floating point number
#print float( '7.5' )+3*2

#the float() function is flexible and it can interpret scientific notation as well
#print float( '2.454e-2' )


#print 'A:', NumberA/SeqLength
#print 'C:', NumberC/SeqLength
#print 'G:', NumberG/SeqLength
#print 'T:', NumberT/SeqLength

#print "There are %d A bases." % (NumberA)
#the value of the integer NumberA to the right of the lone % is inserted in thw position held by %d in the string

#print "A occurs in %d bases out of %d." % (NumberA, SeqLength)
#one of the most common use of this operator is to control the number of decimal places that are printed, using the floating point
#placeholder modified by the isertion of a decimal precision specifier

#print "A occurs in %.2f of %d bases." % (NumberA/SeqLength, SeqLength)
#the %.2f placeholder inserts the corresponding float into the string, but only with two digits of precision to the right of the decimal point


#the operator % doesn't need to be in conjuction with print function. the formatted string can be assigned to a variable

#pctA = "%.1f" % (100*NumberA/SeqLength)

#EX11

#Tm is based on the number of strongly binding nucleotides pair (C*G) and the mumber of the weak ones(A+T) 
TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT

#I used tab before MeltTemp = (4 * TotalStrong) + (2 * TotalWeak) and before print "Tm Short: %.1f C" % (MeltTemp)
#the if statment will execute one block of code if the sentence is 14 or more character long and another block of code if the sentence is less than 14 character long
#since using the statement if i want one block of commands to be executed only if the condition is true and another one if it is false I use the statement else:which provide an alternative route to be executed only when the main condition is false
# a short way to use the to if and else is to write elif

if SeqLength >= 14:
	MeltTempLong = 64.9 +41 * (TotalStrong - 16.4) / SeqLength
	print "Tm Long (>14): %.1f C" % (MeltTempLong)
else:
	MeltTemp = (4 * TotalStrong) + (2 * TotalWeak)
	print "Tm Short: %.1f C" % (MeltTemp)















