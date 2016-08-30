import requests
from selenium import webdriver
from bs4 import BeautifulSoup

#----------------------------------------------------------------------

# Main

# Base URL
baseURL = 'https://www.whoscored.com/Teams/'

# Teams
eplTeams = ['13', '14', '15', '16', '18', '21', '26',   # Arsenal, Leicester, Chelsea, Sunderland, Middlesbrough, Southampton, Liverpool
            '27', '29', '30', '31', '32', '96', '162',  # Watford, West Ham, Tottenham, Everton, Manchester United, Stoke, Crystal Palace
            '167', '175' '183', '184', '214', '259']    # Manchester City, West Brom, Bournemouth, Burnley, Hull, Swansea 

# Seasons 2009/2010 to 2015/2016
archiveUrls = [ '/Archive?stageId=12496', 
                '/Archive?stageId=9155',
                '/Archive?stageId=7794',
                '/Archive?stageId=6531',
                '/Archive?stageId=5476',
                '/Archive?stageId=4345',
                '/Archive?stageId=3115']

# Each team
for team in eplTeams:
    # Each season
    for archive in archiveUrls:

    	# Retrieve URLs
        finalURL = baseURL + team + archive
       	r = requests.get(finalURL)

       	#extract game ids if response is correct
       	if (r.status_code == 200 and r.content is not None):
			content = r.content.decode("utf-8")
			soup = BeautifulSoup(''.join(content), 'lxml')

			print soup