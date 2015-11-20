from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep
BASE_URL = "http://data.ok.gov/browse?f[0]=bundle_name%3ADataset&f[1]=im_field_categories%3A4081"

def get_dataset_links(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	pane_content = soup.find("ol", "search-results apachesolr_search-results")
	dataset_links = [h3.a["href"] for h3 in pane_content.findAll("h3")]
	return dataset_links  
	#print dataset_links  


#testing code
#get_dataset_links(BASE_URL)


def get_dataset(dataset_url):
	html = urlopen(dataset_url).read()
	soup = BeautifulSoup(html, "lxml")
	resource_list = soup.findAll("ul", {"class":"resource-list"}) 
	datasets = [li for li in resource_list ]
	dataset_list = []
	#print datasets 
	for dataset in datasets:
		name = [a["title"] for a in dataset.findAll("a",{"class":"heading"})]
		# description = [p["string"] for p in dataset.findAll("p",{"class":"description"})]  
		link =  [a["href"] for a in dataset.findAll("a",{"class":"btn btn-primary"})]

		dataset_list.append( {"name": name,
			        	# "description": description,
			        	"link": link}) 
	return dataset_list

datasets_main = get_dataset_links(BASE_URL)
data = []

for dataset_one in datasets_main:
	info = get_dataset(dataset_one)
	data.append(info)
	sleep(1)

print data 



