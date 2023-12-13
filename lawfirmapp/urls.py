from django.urls import path
from lawfirmapp import views
urlpatterns = [
     path('',views.index,name='index'),
     path('login/',views.login,name='login'),
     path('contact',views.contact,name='contact'),
     path('signup',views.signup,name='signup'),
     path('mycases',views.mycases,name='mycases'),
     path('advocate',views.advocate,name='advocate'),
     path('advipc',views.advipc,name='advipc'),
     path('caseman',views.caseman,name='caseman'),
     path('advclman',views.advclman,name='advclman'),
     path('client',views.client,name='client'),
     path('cladvlist',views.cladvlist,name='cladvlist'),
     path('clcase',views.clcase,name='clcase'),
     path('clfeedback',views.clfeedback,name='clfeedback'),
     path('admin',views.admin,name='admin'),
     path('adcl',views.adcl,name='adcl'),
     path('adadv',views.adadv,name='adadv'),
     path('adcase',views.adcase,name='adcase'),
     path('adipc',views.adipc,name='adipc'),
     path('adfeedback',views.adfeedback,name='adfeedback'),
     path('practiceareas',views.practiceareas,name='practiceareas'),
     path('user_register',views.user_register,name='user_register'),
     path('home',views.home,name='home'),
]