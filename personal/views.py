from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('This is my personal Gallery')
def picture_of_day(request):
    date = dt.date.today()
    #function to convert date object to find exact day
    day = convert_dates(date) 
   
    html = f'''
        <html>
            <body>
                <h1> Picture for {day} {date.day}-{date.month}-{date.year}</h1>
            <body>
            '''
    return HttpResponse(html)

def convert_dates(dates):
    #Function that gets the weekday number for date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

