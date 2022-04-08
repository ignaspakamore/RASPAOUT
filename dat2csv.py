import sys
import csv

if __name__ == '__main__':

    '''
    # column 1: index 
    # column 2: distance [A]
    # column 3: RDF histogram
    # column 4: unnormalized distance histogram
    '''
    infle = open(sys.argv[1], 'r')
    lines=infle.readlines()
    distance = []
    RDF_hist = []
    for x in lines:
        if not x.startswith('#'):
            distance.append(x.split(' ')[1])
            RDF_hist.append(x.split(' ')[2])


    file = open(f'{sys.argv[1]}.csv', 'w')
    writer = csv.writer(file)
    for i in range(len(distance)):
        writer.writerow([distance[i], RDF_hist[i]])
    file.close()




