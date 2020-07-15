def main():
    ##creates new text file
    file = open("OUA-API-Requests.txt", "w+")

    ##loops through 12 months
    for month in range(1,13):
        ##if Feb, only 28 days
        if month == 2:
            for date in range(1,29):
                for hour in range(0,24,6):
                    ##generates API-request
                    file.write('curl -v  -X GET "https://api.flightstats.com/flex/\
flightstatus/historical/rest/v3/xml/airport/status/OUA/dep/2019/'+ str(month) + '/\
' + str(date) + '/' + str(hour) + '?appId=46581572&appKey=fbb93d4e4994d52fb2a42\
e0053e40a4b&utc=false&numHours=6" >> TMS.txt' + '\n')

        ##if 31 days in month
        elif month in (1,3,5,7,8,10,12):
            for date in range(1,32):
                for hour in range(0,24,6):
                    file.write('curl -v  -X GET "https://api.flightstats.com/flex/\
flightstatus/historical/rest/v3/xml/airport/status/OUA/dep/2019/'+ str(month) + '/\
' + str(date) + '/' + str(hour) + '?appId=46581572&appKey=fbb93d4e4994d52fb2a42\
e0053e40a4b&utc=false&numHours=6" >> TMS.txt' + '\n')

        ##if 30 days in month
        else:
            for date in range(1,31):
                for hour in range(0,24,6):
                    file.write('curl -v  -X GET "https://api.flightstats.com/flex/\
flightstatus/historical/rest/v3/xml/airport/status/OUA/dep/2019/'+ str(month) + '/\
' + str(date) + '/' + str(hour) + '?appId=46581572&appKey=fbb93d4e4994d52fb2a42\
e0053e40a4b&utc=false&numHours=6" >> TMS.txt' + '\n')

    ##closes file
    file.close()

##main
if __name__== "__main__":
    main()
