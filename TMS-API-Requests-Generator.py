def main():
    file = open("TMS-API-Requests.txt", "w+")

    for month in range(1,13):
        if month == 2:
            for date in range(1,29):
                for hour in range(0,24,6):
                    file.write('curl -v  -X GET "https://api.flightstats.com/flex/\
flightstatus/historical/rest/v3/xml/airport/status/TMS/dep/2019/'+ str(month) + '/\
' + str(date) + '/' + str(hour) + '?appId=46581572&appKey=fbb93d4e4994d52fb2a42\
e0053e40a4b&utc=false&numHours=6" >> TMS.txt' + '\n')

        elif month in (1,3,5,7,8,10,12):
            for date in range(1,32):
                for hour in range(0,24,6):
                    file.write('curl -v  -X GET "https://api.flightstats.com/flex/\
flightstatus/historical/rest/v3/xml/airport/status/TMS/dep/2019/'+ str(month) + '/\
' + str(date) + '/' + str(hour) + '?appId=46581572&appKey=fbb93d4e4994d52fb2a42\
e0053e40a4b&utc=false&numHours=6" >> TMS.txt' + '\n')

        else:
            for date in range(1,31):
                for hour in range(0,24,6):
                    file.write('curl -v  -X GET "https://api.flightstats.com/flex/\
flightstatus/historical/rest/v3/xml/airport/status/TMS/dep/2019/'+ str(month) + '/\
' + str(date) + '/' + str(hour) + '?appId=46581572&appKey=fbb93d4e4994d52fb2a42\
e0053e40a4b&utc=false&numHours=6" >> TMS.txt' + '\n')

    file.close()

if __name__== "__main__":
    main()
