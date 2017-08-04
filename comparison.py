
#IMPORTING CSV
import csv

#ASSIGNING THE DICTIONARIES#
cDict = {}
tableDict = {}




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
		cDict[scaffoldIDC] = chromosomeIDC, posID

#IMPORTING DATA TO BE COMPARED:#
print "\n" "Table of shared genes:" "\n"
with open("S22.csv", "rb") as csvfile:
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
			
			gColour = classID + "-" + subclassID
			
			if classID == "Glutenin":
				gGlyph = "circle"
			if classID == "Gliacin":
				gGlyph = "triangle"
			if classID == "Prolamin":
				gGlyph = "square"
			
			print "chr{}".format(chromosomeIDC), "\t", int(float(posID) * 3000), "\t", int(float(posID) * 3000 + 3000), "\t", 1, "\t", "colour=" + str(gColour), "glyph=" + str(gGlyph)
		else:
			continue
print "\n \n Property of Earlham institute (2017).\n Programmed by Dylan Osborne and Christian Schudoma."
