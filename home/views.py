from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout
from home.forms import ReviewForm
from home.models import Review
# from django.views.generic import ListView, DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    return render(request,'home/index.html')

def reviews(request):
    form=ReviewForm()
    form1=form
    review_list= Review.objects.order_by("-id")
    paginator = Paginator(review_list,5)
    page = request.GET.get('page')
    reviews = paginator.get_page(page)
    if request.method == 'POST':    
        form= ReviewForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,'home/index.html',{'form':form1,'reviews':reviews})

    return render(request,'home/reviews.html',context={'form':form1,'reviews':reviews})

def freePlan(request):
    request.session['plan']='free-plan' 
    request.session['mailid']='mpriyom02@gmail.com'
    return render(request,'home/login.html',{'plan': request.session.get('plan'), 'mailid': request.session.get('mailid')})

def paidPlan(request):
    request.session['plan']='paid-plan'
    request.session['mailid']='gupta.kirti0808@gmail.com'
    return render(request,'home/login.html',{'plan': request.session.get('plan'), 'mailid':request.session.get('mailid')})

def login(request):
    plan=request.session.get('plan')
    redirectLink='/'+ plan
    return redirect(redirectLink)
    # return render(request,'home/login.html',{'plan': request.session.get('plan'), 'mailid':request.session.get('mailid')})

def logout(request):
    # del request.session['plan']
    # del request.session['mailid']
    auth_logout(request)
    return redirect('/')


# class PostDetailView(DetailView):
#     model = Review
#     template_name = 'home/reviews.html'
#     context_object_name = 'reviews'