class Solution(object):
    def dayOfYear(self, date):
        from datetime import datetime
        date_object = datetime.strptime(date, '%Y-%m-%d')
        day_of_year = date_object.timetuple().tm_yday
        return(day_of_year)