# python easyPEspades.py /media/inesmendes/40EACA77EACA68AC/Users/Ines/Os\ Meus\ Documentos/tese\ -\ seq\ dump/SDSEummiBGI/cdts-wh.genomics.cn/F13TSFEUHT0149_STRuckR/clean_reads
# python easyPEspades.py /home/inesmendes/Documents/spades_script/seq_testes

import sys
import os

try:
	readsDirectory=sys.argv[1]
except IndexError: 
	print "Invalid input." #TODO
	raise SystemExit

currentDir=os.getcwd()

os.chdir(readsDirectory)

l=os.listdir(readsDirectory)

if not l:
	print "No directories found!"
	raise SystemExit

for item in l:
	a=os.listdir(item)
	if not a:
		print "No files found!"
		raise SystemExit

	right=readsDirectory +"/" + item.strip() + "/" + a[0].strip()
	left=readsDirectory +"/" + item.strip() + "/" +  a[1].strip()

	newOutputDir=currentDir+"/assemblies/"+item

	#If you're having trouble with directory spaces in directory name please uncomment this section:
	#right=right.replace(" ","\ ")
	#left=left.replace(" ","\ ")
	#newOutputDir=newOutputDir.replace(" ","\ ")

	os.system("spades.py --careful --pe1-1 %s --pe1-2 %s -m 20 -t 10 -o %s" % (right, left, newOutputDir))

print "The script has finished!"