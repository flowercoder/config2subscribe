
import json
import base64

# input config
# read vless config file and read it.
# win path
# filepath = 'D:\PythonStudy\config2subscribe\config.json'
# server path
# filepath = '/usr/local/etc/xray/config.json'
# file = open(filepath, "r")

# read Hysteria config file and read it.
# server path
# filepath = '/root/config.json'
# file = open(filepath, "r")

def vlessfig():
    # project path
    file = open('config.json', "r")
    allcontents = json.load(file)

    # Get what you need
    apart = allcontents.get('inbounds')[0].get('protocol')
    bpart = allcontents.get('inbounds')[0].get('settings').get('clients')[0].get('id')
    cpart = allcontents.get('inbounds')[0].get('streamSettings').get('xtlsSettings').get('serverName')
    dpart = allcontents.get('inbounds')[0].get('port')
    epart = allcontents.get('inbounds')[0].get('settings').get('decryption')
    fpart = allcontents.get('inbounds')[0].get('settings').get('clients')[0].get('flow')
    gpart = allcontents.get('inbounds')[0].get('streamSettings').get('security')
    hpart = cpart
    ipart = allcontents.get('inbounds')[0].get('streamSettings').get('network')
    jpart = cpart
    # print(apart)
    # print(bpart)
    # print(cpart)
    # print(dpart)
    # print(epart)
    # print(fpart)
    # print(gpart)
    # print(hpart)
    # print(ipart)
    # print(jpart)
    file.close()

    # build a url
    url = f"{apart}://{bpart}@{cpart}:{dpart}?encryption={epart}&flow={fpart}&security={gpart}&sni={hpart}&type={ipart}#{jpart}"
    # print(url)
    return url

def hysteriafig():
    file = open('config.json', "r")
    allcontents = json.load(file)
    # print(allcontents)
    apart = allcontents.get('server')
    bpart = allcontents.get('protocol')
    cpart = allcontents.get('auth_str')
    dpart = allcontents.get('server_name')
    #todo if insecure == Ture, you need add some code here.
    epart = allcontents.get('insecure')
    if epart == False:
        epart = 0
    fpart = allcontents.get('up_mbps')
    gpart = allcontents.get('down_mbps')
    hpart = allcontents.get('alpn')
    ipart = dpart

    # print(apart)
    # print(bpart)
    # print(cpart)
    # print(dpart)
    # print(epart)
    # print(fpart)
    # print(gpart)
    # print(hpart)
    # print(ipart)
    file.close()

    url = f"hysteria://{apart}?protocol={bpart}&auth={cpart}&peer={dpart}&insecure={epart}&upmbps={fpart}&downmbps={gpart}&alpn={hpart}#{ipart}"
    # print(url)
    return url

def showurl(url):
    # trans the url to subscribble content
    # tobase64
    burl = bytes(url, encoding = "utf8")
    enurl = base64.urlsafe_b64encode(burl)
    deurl = base64.urlsafe_b64decode(enurl)
    # print(enurl)
    # print(deurl)

    # print the result on screen
    print(str(enurl)[2:-1])

if __name__ == '__main__':
    # vless
    # showurl(vlessfig())
    # Hi Hysteria
    showurl(hysteriafig())