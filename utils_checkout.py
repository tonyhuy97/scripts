import requests
querystring = {"limit":"2","offset":"0","sort":"created_at","order":"desc"}
apikey = "PUT IN API KEY HERE"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {apikey}",
    "Content-Type": "application/json"
}

def originalid():
    assetTag = ''
    while assetTag != 'exit':
        print("==========================")
        assetTag=input("Input asset(type exit to close)#: ")
        if assetTag == 'exit':
            print("Exiting...")
            break
        url = "https://site.com/api/v1/hardware/bytag/"
        newurl = url + "0" + assetTag
        response = requests.request("GET", newurl, headers=headers, params=querystring)
        iddict = response.json()
        trueID = iddict['id']
        print(trueID)
        checkinURL = f"site.com/api/v1/hardware/{trueID}/checkin"
        checkin_response = requests.request("POST", checkinURL, headers=headers)
        print(checkin_response.text)


def main():
    originalid()

if __name__ == '__main__':
    main()
