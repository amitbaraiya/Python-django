from django.shortcuts import render
from .models import Destination
from .models import Data_base
from django.contrib.auth.models import User, auth
# from django.travel.models 
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.title = 'Traval'
    dest1.add = 'Ahmedabad'
    dest1.contact_no = 9979581956
    dest1.mail_id = 'amitbaraiya82@gmail.com'
    dest1.dis =' "Hi, I’m Amit Baraiya, an India Times best-selling author of How to Travel India on Lowest cost and Ten Years a Nomad as well as the founder of this website! Have you ever said to yourself one of the following:“How do I find the money to travel? It seems too expensive for me.“Where do I find the best travel deals?”       “How do I save money on flights, accommodation, and other big expenses?” “How do I plan my trip?”   “How do I stay safe and healthy?” “How do I maximize my time?” “I want to travel more but I don’t know the first step.”You are not alone. Over the past eleven years, I’ve helped millions of people answer those questions and travel more for less with time tested and proven tips and advice. By using this website, you can spend less time searching the Internet and being overwhelmed with information and more time doing the one thing you want to do: travel more." '

    # tours1 = Abc()
    # tours1.name = 'Mumbai' 
    # tours1.discription = 'uiuiwejkhjkqqqqqqqw123'
    database1 = Data_base()

    
    # if request.method == 'POST':
    #     user_name = request.POST['name']
    #     user_email = request.POST['email']
    #     user_dis = request.POST['dis']

    # database1 = Data_base.objects.create(user_name=database1.name, user_email=database1.email, user_dis= database1.dis)
    # database1.save();   
    # print('data stored')    

    return render(request, 'index.html',{'dest1': dest1,'database1':database1})
