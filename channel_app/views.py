from django.shortcuts import render

# Create your views here.




def home(request):

    data={}
    return render(request, 'home.html',data)

def chat(request):

    data={}
    return render(request, 'chat.html',data)

def tchat(request):
    user = request.user.username
    print(user, 'uuuuuuuuu')
    
    data={
        'user': user,
    }
    return render(request, 'tchat.html',data)