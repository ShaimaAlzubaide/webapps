from django.urls import path
from . import views  # تأكد من استيراد views قبل استخدامه
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view  # تأكد من أنك استوردت الـ View الصحيحة
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'), 
    path('', home_view, name='home'), 
    path('about/', views.about, name='about'),
    path('intro/', views.intro_page, name='intro_page'),  # صفحة المقدمة بعد "ابدأ"
    path('role-selection/', views.role_selection, name='role_selection'),  # صفحة الاختيار بين مندوب وعميل 
    path('register/', views.register, name='register'),
    path('agents/', views.agent_list, name='agent_list'),
    path('best_agent/',views.best_agent,name='best_agent'),
    path('agent/<int:agent_id>/', views.agent_detail, name='agent_detail'),
    path('discounts/', views.discounted_purchases, name='discounted_purchases'),
    path('service-request/', views.service_request, name='service_request'),  # مسار طلب الخدمة
    path('about/', views.about, name='about'),  # صفحة "ما هو الموقع؟"
    path('next/', views.next_page, name='next_page'),  # صفحة "متابعة"
    path('register/agent/', views.register_agent, name='register_agent'),
    #notes
    path('notfication/',views.notfication,name='notfication'),
    path('importantnotp/',views.importantnot,name='importantnot'),
     path('setting/',views.setting,name='setting') ,
     #clients
    path('client/',views.client,name='client'),
    path('clients/new/', views.new_clients, name='new_clients'),
    path('clients/incomplete/', views.incomplete_payments, name='incomplete_payments'),
    path('clients/complete/', views.complete_payments, name='complete_payments'),
    path('clients/host/', views.host_client, name='host_client'),
    #slat
    path('sla/',views.sla,name='sla'),
    path('sla/uncomplete/', views.uncomp_sla, name='uncomp_sla'),
    path('sla/not_response/', views.notresponse_sla, name='notresponse_sla'),

    #viewers
    path('viewer/',views.viewer,name='viewer'),
    #reports
    path('reports/',views.reports,name='reports'),
    path('repochoose/',views.repochoose,name='repochoose'),
    path('agentwell/',views.agentwell,name='agentwell'),
    path('wellome/', views.wellcome, name='wellcome'),
    
    


    


]
# إضافة المسار لملفات images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
