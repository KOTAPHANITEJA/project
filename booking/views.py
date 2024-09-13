from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
def home(request): 
    return render(request,'home.html',{'name':'Passengers'})

def hotel_list(request):
    df = pd.read_csv('website\hotels.csv')
    print(df)
    hotels_html = df.to_html()
    return render(request, 'hotel_list.html', {'hotels_table': hotels_html})

def movie_list(request):
    return render(request, 'movie_list.html')

def restaurant_list(request):
    return render(request, 'restaurant_list.html')

