# Simple-API

commands  
#Create an item to store
curl --location --request PUT "localhost:80/create/?item=<ITEM_NAME>"  

#Delete an item in storage
curl --location --request GET "localhost:80/delete/?item=<ITEM_NAME>"  

#Update an item with a new one
curl --location --request PUT "localhost:80/update/?old-item=<OLD_ITEM_NAME>&replacement-item=<NEW_ITEM_NAME>"  

#Read an item in storage
curl --location --request GET "localhost:80/read/?item=<ITEM_NAME>"  
