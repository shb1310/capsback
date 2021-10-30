from testapp.models import AnsimDataset as ans
from testapp.kapi import getLatLng
import csv,json
from datetime import datetime

def dateconv(str):
	if (str == "null"):
		return None
	return datetime.strptime(str,"%Y-%m-%d")

def intconv(str):
	print(str,":",type(str))
	if (str==None):
		return str
	print(int(str))	
	return int(str)
	
def gpsconv(str):
	gps = getLatLng(str)
	if (gps):
		return gps
	else:
		return [-1,-1]
	
def fileinsert(filename):

	f = open(filename,'r')	
	rdr = csv.reader(f)
	
	i = 0
	for line in rdr:		
		if(i==0):
			print(i)
			i+=1			
			continue
		i+=1
		gps = gpsconv(line[7])
		print(i," line: ",line)
		print("gps: ",gps)

		asm = ans(lat=gps[1],lon=gps[0],ansimseq=intconv(line[0]),statecode=intconv(line[1]),statename=line[2],wardname=line[3],workplacename=line[4],owner=line[5],ansimdate=dateconv(line[6]),address1=line[7],address2=line[8],category=line[9],categorydetail=line[10],tel=line[11],isansim=line[12],cancledate=dateconv(line[13]),note=line[14],modifydate=dateconv(line[15]))
#		print(asm)
		asm.save()
	 
	print(ans.objects.all())
	print(i)	
	f.close()
