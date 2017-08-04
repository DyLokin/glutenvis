
#IMPORTING CSV
import csv
import sys

#ASSIGNING THE STUFF#
cDict = {}
tableDict = {}
uList = []
seenColours = set()

#COUNTER VARIABLES#
iFound = 0
iNFound = 0

#IMPORTING DATA TO BECOME COMPARATIVE DICTIONARY#
with open("S05.csv", "rb") as csvfile:
	tableReader05 = csv.reader(csvfile, delimiter = "\t")
	for row in tableReader05:
		
#ASSIGNING VARIABLES TO EACH ROW:#
		scaffoldComparative = row[0].split("_")
		chromosomeIDC = row[1]
		posID = row[2]
		scaffoldIDC = (scaffoldComparative[4])
#ENTRING INTO DICTIONARY:#
		cDict[scaffoldIDC] = chromosomeIDC, int((float(posID)) * 3000)
		
#IMPORTING DATA TO BE COMPARED:#
print "\n" "Table of shared genes:" "\n"
with open("S22.csv", "rb") as csvfile, open ("colours.txt", "wb") as coloursFile, open ("mappedglutens.txt", "wb") as mappedFile, open ("unmapped.txt", "wb") as unmappedFile:
	tableReader22 = csv.reader(csvfile, delimiter = "\t")
	for row in tableReader22:

#IGNORING ROWS THAT START WITH A HASH, OR AREN'T A GENE OR PSEUDOGENE:#
		if row[0][0] == "#" or row[2] not in ("gene", "pseudogene"):
			continue

#EXTRACTING DATA INTO VARIABLES:#
		row0 = row[0].split("_")
		row8 = row[8].split(";")
		scaffoldID= row0[5]
		chromosomeID = row0[6]
		geneID = row[2]
		classID = row8[2].split("=")[1]
		subclassID = row8[3].split("=")[1]
#COMPARING:#
		if scaffoldID in cDict:
#OUTPUTTING MATCHES AS FORMATTED TABLE:#

			gColour = classID + subclassID
			if gColour not in seenColours:
				coloursFile.write ("{}=\n".format(str(gColour)))
				seenColours.add(gColour)
			
			if classID == "Glutenin":
				gGlyph = "circle"
			if classID == "Gliacin":
				gGlyph = "triangle"
			if classID == "Prolamin":
				gGlyph = "square"
			
			mappedFile.write("".join(("chr{}".format(cDict[scaffoldID][0]), "\t", str(cDict[scaffoldID][1]), "\t", str(cDict[scaffoldID][1] + 3000), "\t", str(1), "\t", "color={},glyph={}\n".format(str(gColour), str(gGlyph)))))
			iFound += 1
		else:
			unmappedFile.write(row[0] + "\n")
			iNFound += 1

sys.stderr.write("{}/{} found \n".format(iFound, iFound+iNFound))			
sys.stderr.write("\n \n Property of Earlham institute (2017).\n Programmed by Dylan Osborne and Christian Schudoma.\n")
