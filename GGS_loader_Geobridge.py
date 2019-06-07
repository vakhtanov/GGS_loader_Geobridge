##### ГГС с сайта geobridge.ru
import base64, json,requests


link='https://geobridge.ru/maps/pp/api/55.98059733029029_37.962857203305006_56.06404535068312_38.15786452752374_13_0__'
headers = {'Referer':'https://geobridge.ru/maps?lat=54.72&lng=55.88&zoom=11','Cookie':'PHPSESSID=i0mbrnk14mq009158j2oi4aef0; _ym_uid=1559827136628727491; _ym_d=1559827136; _ga=GA1.2.1553244663.1559827137; _gid=GA1.2.1314497359.1559827137; _ym_visorc_25298441=w; _gat_gtag_UA_46330041_1=1; last_visit=1559891321441::1559902121441; _ym_isad=2; tmr_detect=0%7C1559902129950'}

req_link=link
#Запрос к серваку
req=requests.get(req_link,headers=headers)
#Декодирование в json обычный
req_out=base64.b64decode(req.text)
json_dict=json.loads(req_out)

#Декодирование в geojson 
geojson = {
           "type": "FeatureCollection",
           "features": 
               [
                {
                 "type": "Feature",
                 "geometry" : {
                 "type": "Point",
                 "coordinates": [d["lng"], d["lat"]],
                 },
           "properties" : d,
                } 
               for d in json_dict]
          }
		  
#Запись Json
output = open('data.json', 'w')
json.dump(geojson, output)
