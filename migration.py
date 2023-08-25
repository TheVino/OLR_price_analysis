import bs4 as bs
import urllib.request, os, sys, requests, time
from datetime import date

# Var declaration
start_time = time.time()	# Module to count Python runtime
today=date.today()
filesPath= './Files/'
intelProxy='http://proxy-chain.intel.com:911'

# Functions
def startTime():
	#null point just to organize the def's and functon's
	return
def proxySetup(proxy): 		# Defines the intel proxy so we can run the program while VPN is on
	# proxy = 'http://proxy-chain.intel.com:911'
	os.environ['http_proxy'] 	= proxy 
	os.environ['HTTP_PROXY']	= proxy
	os.environ['https_proxy'] 	= proxy
	os.environ['HTTPS_PROXY'] 	= proxy
	return proxy
def getTodayDate(today):	# Get today's date
	#null point just to organize the def's and functon's
	return today
def pageData(processor): 	# Open Website and save the sku name + price
	# Request check if the website its ok
	r = requests.get(processor)
	if (r.ok):
		print("A conexão com esse link está saudável :)")

	# Request (Get) info about the sku
	link = urllib.request.urlopen(processor).read()
	soup = bs.BeautifulSoup(link,'lxml')
	# print(soup)
	name=soup.title.string
	cropped=find(name)
	name=cropped+"_test.txt"
	print(name)

	# Request (Get) info about the price
	dirtPrice 		= soup.select_one('div[class^="price"]').text
	commaPrice 		= dirtPrice[9:17]
	priceDiscount 	= commaPrice.replace(".","")
	priceDiscount 	= priceDiscount.replace(",", ".")
	print("O processador referente à pesquisa é: " + cropped + ", e seu preço é: " + priceDiscount)

	# Open the file to save these data
	try:
		f=open(filesPath+name,"a+")
		f.write(str(today)+",")
		f.write(priceDiscount+"\n")
	except FileNotFoundError:
		print("Arquivo não existe. Criando um novo arquivo para esse produto")
		f=open(filesPath+name,"w+")
		f.write(str(today)+",")
		f.write(priceDiscount+"\n")
		f.close()
	finally:
		f.close()
def find(name):				# Find the sku name inside the full string return
	blank=" "
	cores=["i3","i5","i7","i9"]

	for n in range(len(cores)):
		result=name.find(cores[n])
		if result!=-1: 		# Means this word is out of index
			n=len(cores)
			break

	if 	 name[result+9]	==" ":
		croppedSku=str(name[result:result+9])
	elif name[result+8]	==" ":
		croppedSku=str(name[result:result+8])
	else:
		croppedSku=str(name[result:result+7])
	return croppedSku
def showTime(start_time):
	print("[%.2f seconds]" % (time.time() - start_time)) # Module to print the runtime
	return

# Procs cross links
i513600k = "https://www.kabum.com.br/produto/386975/processador-intel-core-i5-13600k-13-geracao-5-1ghz-max-turbo-cache-24mb-14-nucleos-lga-1700-video-integrado-bx8071513600k"
i513700kf  = "https://www.kabum.com.br/produto/386974/processador-intel-core-i7-13700kf-13-geracao-5-4ghz-max-turbo-cache-30mb-16-nucleos-24-threads-lga-1700-bx8071513700kf"

class main:					#Starts the program
	startTime()
	print("\nIniciando programa de análise de preços")
	print("Analisando neste momento o site da Kabum\n")
	getTodayDate(today)
	# proxySetup(intelProxy)
	pageData(i513600k)
	pageData(i513700kf)
	showTime(start_time)

if __name__ == "__main__":
	main()