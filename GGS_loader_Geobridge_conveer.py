##### ГГС с сайта geobridge.ru
import base64, json,requests


def download_by_filym(fi1,lym1,fi2,lym2):
    link='https://geobridge.ru/maps/pp/api/'+str(fi1)+'_'+str(lym1)+'_'+str(fi2)+'_'+str(lym2)+'_13_0__'
    headers = {'Referer':'https://geobridge.ru/maps?lat=54.72&lng=55.88&zoom=11','Cookie':'PHPSESSID=i0mbrnk14mq009158j2oi4aef0; _ym_uid=1559827136628727491; _ym_d=1559827136; _ga=GA1.2.1553244663.1559827137; _gid=GA1.2.1314497359.1559827137; _ym_visorc_25298441=w; _gat_gtag_UA_46330041_1=1; last_visit=1559891321441::1559902121441; _ym_isad=2; tmr_detect=0%7C1559902129950'}
    req_link=link
    #Запрос к серваку
    req=requests.get(req_link,headers=headers)
    #Декодирование в json обычный
    req_out=base64.b64decode(req.text)
    if len(req_out) > 2:
        json_dict=json.loads(req_out)
        #Декодирование в geojson 
        try:
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
            print(len(req_out))
            #Запись Json
            name='GGS_Geobridge'+str(fi1).replace('.','-')+'_'+str(lym1).replace('.','-')+'_'+str(fi2).replace('.','-')+'_'+str(lym2).replace('.','-')+'.json'
            output = open(name, 'w')
            json.dump(geojson, output)
        except Exception as e:
            with open('Error'+str(fi1).replace('.','-')+'_'+str(lym1).replace('.','-')+'.log','w') as f:
                f.write(str(e)+'\n')
                f.write(req_out)
            return 1
    else:
        return 0
        pass
    #return req_out

def main():
    #fi_niz=[30.0+x/10.0 for x in range(800)]
    fi_niz=[43.5+x/10.0 for x in range(800)]
    lym_left=[35.0+x/10.0 for x in range(400)]
    print fi_niz
    print lym_left
    for fi in fi_niz:
        for lym in lym_left:
            with open('logfile.log','a') as log:
                log.write('start'+str(fi).replace('.','-')+'_'+str(lym).replace('.','-')+'\n')
            #print('start_'+str(fi).replace('.','-')+'_'+str(lym).replace('.','-'))
            status=download_by_filym(fi,lym,(fi+0.1),(lym+0.1))
            with open('logfile.log','a') as log:
                log.write(str(status)+'\n')
                log.write('finish_'+str(fi).replace('.','-')+'_'+str(lym).replace('.','-')+'\n')

if __name__ == '__main__':
    main()