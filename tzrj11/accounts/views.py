# accounts/views.py
from django.shortcuts import render 
from .forms import CustomerForm
from .models import Agent  # إضافة استيراد المناديب
from django.shortcuts import render, get_object_or_404
from .forms import ServiceRequestForm

# عرض صفحة التسجيل
def home(request):
    return render(request, 'accounts/home.html')

def intro_page(request):
    return render(request, 'accounts/about.html')  # هنا نستخدم القالب "about.html"

def role_selection(request):
    return render(request, 'accounts/role_selection.html')


def register(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agents_list')  # بعد التسجيل يتم توجيه العميل إلى قائمة المناديب
    else:
        form = CustomerForm()
    return render(request, 'accounts/register.html', {'form': form})

# عرض قائمة المناديب
def agent_list(request):
    agents = Agent.objects.all()  # جلب جميع المناديب
    return render(request, 'agent_list.html', {'agents': agents})
def best_agent(request):
    return render(request,'best_agent.html')

# عرض تفاصيل المناديب
def agent_detail(request, agent_id):
    agent = Agent.objects.get(id=agent_id)
    return render(request, 'agent_detail.html', {'agent': agent})




def discounted_purchases(request):
    return render(request, 'accounts/discounted_purchases.html')

def service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # م
    else:
        form = ServiceRequestForm()

    return render(request, 'accounts/service_request.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def next_page(request):
    return render(request, 'next.html')  # صفحة متابعة المستقبلية

def register_agent(request):
   return render(request, 'accounts/register_agent.html')
#notfications pages
def notfication(request):
    return render(request,'notfication.html')
def importantnot(request):
    return render(request,'importantnot.html')

def setting(request):
    return render(request,'setting.html')





#claient pages:
def client(request):
    return render(request,'client.html')

def new_clients(request):
    return render(request, 'new.html')

def incomplete_payments(request):
    return render(request, 'uncount.html')

def complete_payments(request):
    return render(request, 'done.html')

def host_client(request):
    return render(request, 'ess.html')

#slat pages
def sla(request):
    return render(request, 'sla.html')
def uncomp_sla(request):
    return render(request, 'uncomplete.html')
def notresponse_sla(request):
    return render(request, 'notresponse.html')

#reports pages
def reports(request):
    return render(request,'reports.html')
def repochoose(request):
    return render(request,'repochoose.html')

def agentwell(request):
    return render(request,'agentwell.html')
def home_view(request):
    return render(request, 'home.html')    
def about(request):
    return render(request, 'accounts/about.html')

def wellcome(request):
    return render(request, 'wellcome.html')

def viewer(request):
    return render(request,"viewer.html")






