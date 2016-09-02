# -*- coding: utf-8 -*-
from selenium import webdriver
from random import randint
from bs4 import BeautifulSoup
import time

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
    print ("HOLD THE DOOR")
    # Each season
    for archive in archiveUrls:
        print ("HOLDTHEDOOR")

        # Connect webdriver
        finalURL = baseURL + team + archive
        browser =  webdriver.PhantomJS()
        browser.get(finalURL)
        time.sleep(10)

        # The different tables
        tables = ['summary', 'defensive', 'offensive', 'passing']

        # waiting time
        wtime = [3, 4]

        # Load all tables in list
        data = []

        # Get all tables
        while len(data) != 4:
            print ("HOLDDOOR")
            for table in tables:
                try:
                    # browser.switch_to.frame(browser.find_element_by_css_selector("a[href*='#team-squad-archive-stats-" + table + "']"))
                    # print(browser.find_element_by_css_selector("a[href*='#team-squad-archive-stats-" + table + "']").click())
                    element = browser.find_elements_by_css_selector("a[href*='#team-squad-archive-stats-" + table + "']")
                    element.send_keys("keysToSend")
                    element.submit()
                    element.click()
                    ttime.sleep(randint(wtime[0], wtime[1]))
                except:
                    print "Problems with loading webpage in browser."
                    time.sleep(60)
                    print 'Sleeping for one minute. They I will try again'

                # Get content
                content = browser.page_source
                soup = BeautifulSoup(''.join(content), 'lxml')

                print (soup.find("tbody", {"id": "player-table-statistics-body"}))

                #Save data
                data.append(soup.find("tbody", {"id": "player-table-statistics-body"}))

                print 'Data has length ' + str(len(data)) + " at the moment."

        print (data)

        # Get players
        players = thetable.findAll("tr")

        #Get stats
        i = 0

        while i < len(players):
            print ("HODOR")
            stats = players[i].findAll("td")

            index = stats[0].get_text()
            nation = stats[1].find("span").get("class")[2].rsplit('-', 1)[1]
            name = stats[2].findChildren()[0].get_text().encode('utf-8')
            team = stats[2].findChildren()[2].get_text().rsplit(',', 1)[0]
            age = stats[2].findChildren()[3].get_text()
            position = stats[2].findChildren()[4].get_text().split(',', 1)[1].strip()
            height = stats[3].get_text()
            weight = stats[4].get_text()
            apps = stats[5].get_text()
            mins = stats[6].get_text()
            goals = stats[7].get_text()
            assists = stats[8].get_text()
            yellow = stats[9].get_text()
            red = stats[10].get_text()
            SpG = stats[11].get_text()
            PassPer = stats[12].get_text()
            AerialsWon = stats[13].get_text()
            MotM = stats[14].get_text()

            print (name)

            i += 1

            break
            
    break
