class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__(a_times)
        self.name = a_name
        self.dob = a_dob
        self.time = a_times
    
    def top3(self):
        return sorted(set([sanitize(t) for t in self.time]))[0:3]

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.spilt(splitter)
    return (mins + '.' + secs)