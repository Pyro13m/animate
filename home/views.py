from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout
from home.forms import ReviewForm
from home.models import Review
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
plan="paid-plan"
mailid="gupta.kirti0808@gmail.com"

def index(request):
    return render(request,'home/index.html')

def reviews(request):
    form=ReviewForm()
    form1=form
    # paginator = Paginator(post_list,5)
    review_list= Review.objects.order_by("-id")
    if request.method == 'POST':    
        form= ReviewForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,'home/index.html',{'form':form1,'form_data':review_list})

    return render(request,'home/reviews.html',context={'form':form1,'form_data':review_list})

def freePlan(request):
    request.session['plan']='free-plan' 
    request.session['mailid']='mpriyom02@gmail.com'
    return render(request,'home/login.html',{'plan': "free-plan"})

def paidPlan(request):
    request.session['plan']='paid-plan'
    request.session['mailid']='gupta.kirti0808@gmail.com'
    return render(request,'home/login.html',{'plan': "paid-plan"})

def login(request):
    return render(request,'home/login.html',{'plan': request.session.get('plan'), 'mailid':request.session.get('mailid')})


# def login(request, plan="paid-plan"):
#     if plan=='paid-plan':
#         # plan='paid-plan'
#         mailid="gupta.kirti0808@gmail.com"
#     elif plan=='free-plan':
#         # plan='free-plan'
#         mailid="mpriyom02@gmail.com"
#     return render(request,'home/login.html',{'plan': plan, 'mailid': mailid})

def logout(request):
    # del request.session['plan']
    # del request.session['mailid']
    auth_logout(request)
    return redirect('/')