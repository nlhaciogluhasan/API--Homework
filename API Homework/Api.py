""""
Date : 19.05.2022
Prepared by the Program : Hasan
Name Of The Program : API HOMEWORK
###################################################

///

https://api.nasa.gov adresindeki datalardan;
1- NeoWs (Near Earth Object Web Service) is a RESTful web service for near earth Asteroid information. 
With NeoWs a user can: search for Asteroids based on their closest approach date to Earth, lookup a specific Asteroid 
with its NASA JPL small body id, as well as browse the overall data-set.
(1 temmuz 2016 ile 30 temmuz 2016) tarihleri arasinda dunyaya potansiyel tehlike olusturan astroid 
datasini alarak asteorid.csv dosyasina kaydediniz.
"""



from urllib import response
import requests
import csv
######################################################################################################
#I'm not writing the apikey because it's not legal.  ****to line 27
#Everyone should write their own apikey.
#Everyone should create a csv file named asteroid and write their Path. ****to line 64
 
apikey=''
url='https://api.nasa.gov/neo/rest/v1/feed'
a,b,c,d=0,1,0,1
data=[]

######################################################################################################
while True:
    #I will pull the data daily. I used WHILE loop for this. When the date is the last day, the cycle will end.    
    start_date='2016-07-{}{}'.format(a,b)
    end_date='2016-07-{}{}'.format(a,b)
    
    b+=1    #here we will move on to the next day after the process is completed.
    if b==9:
        a,b=a+1,0
    #print(start_date)
    response=requests.get(url, params={
        'start_date':start_date,
        'end_date':end_date,
        'api_key':apikey})

    asteroid=response.json() #We extract the information and convert it to json format.
    #print(response)
    
    l=len(asteroid['near_earth_objects'][start_date])  
    #how many data for that day, we establish a new cycle.
    for i in range(l):
        #Using the IF block, we add 'is_potentially_hazardous_asteroid' : TRUE to the data list.
        if(asteroid['near_earth_objects'][start_date][i]['is_potentially_hazardous_asteroid'])==True:
            data.append(asteroid['near_earth_objects'][start_date][i])
            data.append('\n')                                
            print(asteroid['near_earth_objects'][start_date][i])           
    #When we do the last date of 30-07-2016, we end the loop.                
    if start_date=='2016-07-30':
        break
    
######################################################################################################
#Finally, we write the data to the csv file. 
with open('asteorid.csv','a') as file:
                writer = csv.writer(file)
                writer.writerow(data) 
                
######################################################################################################