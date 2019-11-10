if __name__ == '__main__':

    # writing boy names to csv
    outputFile = open('2000_BoysNames.csv', 'w')
    print >> outputFile, '"FirstName",Count'
    with open('2000_BoysNames.txt') as fp:
        for line in fp:
            line = line.strip('\n')
            firstName, count = line.split(' ', 1)
            print >> outputFile, '"' + firstName + '"' + ',' + count

    # writing girl names to csv
    outputFile = open('2000_GirlsNames.csv', 'w')
    print >> outputFile, '"FirstName",Count'
    with open('2000_GirlsNames.txt') as fp:
        for line in fp:
            line = line.strip('\n')
            firstName, count = line.split(' ', 1)
            print >> outputFile, '"' + firstName + '"' + ',' + count 


