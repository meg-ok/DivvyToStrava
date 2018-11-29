import StravaUploader

def strip_td(string):
    first_stripped = string[4:]
    return first_stripped[:-6]

def split_to_min(time):
    min_i = time.index('m')
    return time[:min_i]

def split_to_sec(time):
    min_i = time.index('m')
    sec_i = time.index('s')
    return time[min_i+2:sec_i]

#distances = {'Clark St & Elm St to Halsted St & Wrightwood Ave': '2.3', 'Halsted St & Wrightwood Ave to Clark St & Elm St': '2.3', 'Lake Shore Dr & Ohio St to Clark St & Elm St': '1.5', 'Clark St & Elm St to Lake Shore Dr & Ohio St': '1.5'};
distances = {'Clark St & Congress Pkwy to Columbus Dr & Randolph St': '1.1', 'Clark St & Congress Pkwy to Dearborn Pkwy & Delaware Pl': '1.7', 'Clark St & Congress Pkwy to Dearborn St & Erie St': '1.3', 'Clark St & Congress Pkwy to Lake Shore Dr & Ohio St': '2.7', 'Clark St & Congress Pkwy to State St & Pearson St': '1.7', 'Clark St & Congress Pkwy to Stetson Ave & South Water St': '1.2', 'Clark St & Elm St to Clark St & Congress Pkwy': '2.0', 'Clark St & Elm St to Clark St & North Ave': '0.6', 'Clark St & Elm St to Halsted St & Wrightwood Ave': '2.3', 'Clark St & Elm St to Lake Shore Dr & Ohio St': '1.5', 'Clark St & Elm St to Lincoln Ave & Fullerton Ave': '1.9', 'Clark St & Elm St to Mies van der Rohe Way & Chicago Ave': '1.0', 'Clark St & Elm St to Sheffield Ave & Wrightwood Ave': '2.3', 'Clark St & Elm St to St. Clair St & Erie St': '1.1', 'Clark St & Elm St to Wilton Ave & Belmont Ave': '2.9', 'Clark St & Lincoln Ave to Halsted St & Wrightwood Ave': '1.4', 'Clark St & North Ave to Clark St & Elm St': '0.6', 'Clark St & North Ave to Dearborn Pkwy & Delaware Pl': '0.9', 'Clark St & Schiller St to Clark St & Elm St': '0.3', 'Clinton St & Madison St to Rush St & Superior St': '1.9', 'Columbus Dr & Randolph St to Clark St & Elm St': '1.8', 'Dearborn Pkwy & Delaware Pl to Clark St & Congress Pkwy': '1.9', 'Dearborn Pkwy & Delaware Pl to Clark St & Schiller St': '0.7', 'Dearborn Pkwy & Delaware Pl to Dearborn St & Monroe St': '1.5', 'Dearborn St & Monroe St to Mies van der Rohe Way & Chicago Ave': '1.6', 'Halsted St & Wrightwood Ave to Clark St & Elm St': '2.3', 'Halsted St & Wrightwood Ave to Dearborn Pkwy & Delaware Pl': '2.6', 'Financial Pl & Congress Pkwy to Lake Shore Dr & Ohio St': '2.8', 'Lake Shore Dr & North Blvd to Michigan Ave & Pearson St': '1.0', 'Lake Shore Dr & Ohio St to Clark St & Elm St': '1.5', 'Lake Shore Dr & Ohio St to Field Blvd & South Water St': '1.2', 'Lake Shore Dr & Ohio St to Rush St & Cedar St': '1.2', 'McClurg Ct & Erie St to Shedd Aquarium': '2.4', 'Michigan Ave & Congress Pkwy to Clark St & Elm St': '2.2', 'Mies van der Rohe Way & Chestnut St to Rush St & Cedar St': '0.5', 'Mies van der Rohe Way & Chicago Ave to Clark St & Elm St': '0.9', 'Millennium Park to Clark St & Elm St': '1.9', 'Millennium Park to Dearborn Pkwy & Delaware Pl': '1.5', 'Rush St & Cedar St to Lake Shore Dr & Oho St': '1.2', 'Rush St & Cedar St to Michigan Ave & Congress Pkwy': '2.2', 'Rush St & Cedar St to St. Clair St & Erie St': '0.9', 'Rush St & Superior to Rush St & Cedar St': '0.5', 'Shedd Aquarium to Dearborn Pkwy & Delaware Pl': '3.4', 'St. Clair St & Erie St to Rush St & Cedar St': '0.7', 'St. Clair St & Erie St to Dearborn Pkwy & Delaware Pl': '0.7', 'State St & Pearson St to Clark St & Congress Pkwy': '1.7', 'Streeter Dr & Illinois St to Rush St & Cedar St': '1.5', 'Wells St & Concord Ln to Lincoln Ave & Fullerton Ave': '1.2'}

def find_distance( path ):
    try:
        return distances[path]
    except KeyError, e:
        print "Path not found: manually input",
        input = raw_input()
        return input

start_station = ""
date = ""
time = ""
end_station = ""
total_time = ""

count_past_duration = 999

for line in open('newdivvyoutput2016'):
    count_past_duration = count_past_duration + 1
    for i in range(len(line)):
        if line[i] == ' ':
            continue
        else:
            if line[i:i+21] == "data-duration-seconds":
                count_past_duration = 0
#            if line[i:i+4] == "<td>" and line[i+4:
#                count_past_duration = 0
            if count_past_duration == 2:
                start_station = strip_td( line[i:] )
            elif count_past_duration == 3:
                date = line[i+4:i+15]
                time = line[i+16:i+23]
            elif count_past_duration == 4:
                end_station = strip_td( line[i:] )
            elif count_past_duration == 6:
                total_time = strip_td( line[i:] )
                print "Doing upload for ride on ", date
                print "Start station is ", start_station
                print "End station is ", end_station
                path = start_station + " to " + end_station
                distance = find_distance( path )
                print 'total_time: ', total_time
                print 'distance: ', distance
                StravaUploader.DoUpload( str(split_to_min(total_time)),
                                         str(split_to_sec(total_time)),
                                         str(distance),
                                         str(date),
                                         str(time) )


        break

#            if line[i:i+21] == "data-duration-seconds":
#                count_past_duration = 0
#                if line[i+26] == "\"":
#                    seconds = line[i+23:i+26]
#                if line[i+27] == "\"":
#                    seconds = line[i+23:i+27]

print "start_station", start_station
print "date", date
print "time", time
print "end_station", end_station
print "total_time", total_time
print "minutes ", split_to_min(total_time)
print "seconds ", split_to_sec(total_time)


path = start_station + " to " + end_station
print "path is ", path
print " looked up distance  =   ", distances[path]

