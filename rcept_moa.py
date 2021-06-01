# 기업 정보 수집



def month2str(month_num):

    if month_num == 1:
        month_str = '01'
    elif month_num == 2:
        month_str = '02'
    elif month_num == 3:
        month_str = '03'
    elif month_num == 4:
        month_str = '04'
    elif month_num == 5:
        month_str = '05'
    elif month_num == 6:
        month_str = '06'
    elif month_num == 7:
        month_str = '07'
    elif month_num == 8:
        month_str = '08'
    elif month_num == 9:
        month_str = '09'
    elif month_num == 10:
        month_str = '10'
    elif month_num == 11:
        month_str = '11'
    elif month_num == 12:
        month_str = '12'

    return month_str


import requests, json
# url = 'https://opendart.fss.or.kr/api/list.json?crtfc_key=f6da322d53588f6ba3ce123358d3e0c65f14872e'

api_key = 'f6da322d53588f6ba3ce123358d3e0c65f14872e'

for year in range(2000, 2022):
    for month in range(1,11):


        month_first = month2str(month)
        month_second = month2str(month + 2)
        print(year)
        print(month_first)
        print(month_second)
        # exit()

        url = 'https://opendart.fss.or.kr/api/list.json?crtfc_key=' + api_key + '&bgn_de='+ str(year) + month_first + '01&end_de='+ str(year) + month_second + '01'

        res = requests.get(url)
        res = json.loads(res.text)
        print(res)
        try:
            for row in res["list"]:
                filename = row["rcept_no"] + '.json'
                f = open('rcept/' + filename, 'w')
                f.write(json.dumps(row))
                f.close()
        except:
            continue
