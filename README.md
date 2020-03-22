# CoronaInfoWebApp

## Disclaimer
This project was created as a prototype during the WirvsVirus hackathon. It serves as a technical protoype but is far from completion or stabilty. The provided Information are also only for example regions.

# Idea
A website providing official information about the Covid-19 pandemic in Germany. Information are chosen according to a selected region. 
For stroing and updating those information we have chosen google spreadsheets so that third party authorities are easyly able to edit those informtation via an google spreadsheet invite link. In addition some information are crawled from the websites of local German authorities.


## Run backend
install python packages from requirements.txt

run backend/startbackendserver.sh

If you want to run the automatic web crawling of faq quesions also run:
python startwebcrawler.py

## Run frontend
npm install

npm run serve
