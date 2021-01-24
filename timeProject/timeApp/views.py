from django.shortcuts import render
import datetime
# Create your views here.
def displaytime(request):
    dt=datetime.datetime.now()
    hr=dt.strftime('%H')
    hour=int(hr)
    if(hour<12):
        res="Good Morning"
    elif(hour<15):
        res="Good Afternoon"
    elif(hour<20):
        res="Good Evening"
    else:
        res="Good Night"
    d={'time':hour,'wish':res}
    return render(request,'timeApp/1.html',d)

    