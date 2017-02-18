#Parse digikey url to get digikeyPN and manufacturerPN
#I agreed to make a group order, but told people to send me component url
#I didn't think on how time consuming it is to paste 50/100 urls and to add them to the chart
#Happy python script to solve this clusterf**k
#Carlo Maragno 18/02/2017

import csv

import os.path

#the file in which we will be writing all of ours PN
with open('lista_ordine.csv', 'w') as csvfile:
	
	#creating some filds just to be cool
	fieldnames = ['QTY', 'digikeyPN', 'manufacturerPN', 'URL']
   	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	#the file in which the raw urls are stored, together with PN
	with open('lista_completa.csv') as csvfile:

		reader = csv.DictReader(csvfile)
		
		#debug to tty just in case
		#print('digikeyPN' + ',	' + 'manufacturerPN' +'\n')
		
		#for every row of the input file we do some things, first we get PN from url
		#then we craft a new file with all of the info that we have

		for row in reader:
			
			#take the dirname from the url
			path = os.path.dirname(row['url'])
			#get the last dir name and store in in digikeyPN for obvius reason
			digikeyPN = os.path.basename(path)
			#this effectively strips the digikeyPN form the url
			path = os.path.dirname(path)
			#the last name now is the manufacturerPN so we save it
			manufacturerPN = os.path.basename(path)
			
			#debug to tty just in case
			#print(digikeyPN + ',	' + manufacturerPN +'\n')
			
			#write everything to a new csv with all of the infos
			writer.writerow({'QTY':row['qty'], 'digikeyPN':digikeyPN, 'manufacturerPN':manufacturerPN, 'URL':row['url']})


