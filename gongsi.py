import requests, json, os
from io import BytesIO
from zipfile import ZipFile

if True:
    ll = os.listdir('./rcept')
    for rcept_no in ll:

        url = 'https://opendart.fss.or.kr/api/document.xml?crtfc_key=f6da322d53588f6ba3ce123358d3e0c65f14872e&rcept_no='+(rcept_no[:-5])
        # print(url)
        try:
            res = requests.get(url)
            print(res)
            # print(res.content)
            with ZipFile(BytesIO(res.content)) as zipfile:
                zipfile.extractall('./gongsi/')
        except:
            print(rcept_no)
            print('pass')
        # break


########################################

#
# def getDcmNo(rcpNo):
#     url = 'http://dart.fss.or.kr/dsaf001/main.do?rcpNo='+rcpNo
#     res = requests.get(url).text
#     return res.split("alertInvestNotice('"+rcpNo+"', '")[1].split("'")[0]
#
#
# def getGongsiDoc(rcpNo):
#     dcmNo = getDcmNo(rcpNo)
#     url = 'http://dart.fss.or.kr/report/viewer.do?rcpNo='+rcpNo+'&dcmNo='+dcmNo+'&eleId=0&offset=0&length=0&dtd=HTML'
#     res = requests.get(url).text
#     return res
#
#
# ll = os.listdir('./rcept')
# for rcept_no in ll:
#     rcpno = (rcept_no[:-5])
#     # print(rcpno)
#     doc = getGongsiDoc(rcpno)
#     f=open('gongsi/'+rcpno+'.html','w')
#     f.write(doc)
#     f.close()

#http://dart.fss.or.kr/dsaf001/main.do?rcpNo=20210525900630

#http://dart.fss.or.kr/report/viewer.do?rcpNo=20210525900630&dcmNo=8083905&eleId=0&offset=0&length=0&dtd=HTML