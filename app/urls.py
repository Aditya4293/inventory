from django.urls import path
from . import views,client,master,entry,modify,report,summary,tools
from .views import index
from .client import *
from .master import *
from .entry import packing
from .modify import *
from .report import *
from .summary import *
from .tools import *


urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.main, name='main'),
    path('register/', client.register, name='register'),
    path('login/', client.login_view, name='login'),
    path('forgot_password/', client.client_ForgotPassword, name='forgot_password'),
    path('verify_otp/', client.client_OtpVerify, name='verify_otp'),
    path('reset_password/', client.client_ResetPassword, name='reset_password'),
    path('logout_view/',client.logout_view, name = 'logout_view'),

    
    path('customer_main/', master.customer_main, name='customer_main'),
    path('customer/', master.customer, name='customer'),
    path('edit/<int:pk>/', master.edit_customer, name='edit_customer'),
    path('delete/<int:pk>/', master.delete_customer, name='delete_customer'),

    path('quality_main/', master.quality_main, name='quality_main'),
    path('quality/', master.quality, name='quality'),
    path('edit_quality/<int:pk>/', master.edit_quality, name='edit_quality'),
    path('delete_quality/<int:pk>/', master.delete_quality, name='delete_quality'),

    path('point_main/', master.point_main, name='point_main'),
    path('gauge/', master.point, name='point'),
    path('edit_point/<int:pk>/', master.edit_point, name='edit_point'),
    path('delete_point/<int:pk>/', master.delete_point, name='delete_point'),
    
    path('brand/', master.brand, name='brand'),
    path('brand_main/', master.brand_main, name='brand_main'),
    path('edit_brand/<int:pk>/', master.edit_brand, name='edit_brand'),
    path('delete_brand/<int:pk>/', master.delete_brand, name='delete_brand'),


    path('packing/', entry.packing, name='packing'),
    path('selectedpage/', entry.selectedpage, name='selectedpage'),
    path('lot/', entry.lot, name='lot'), 
    path('dispatch/', entry.dispatch, name='dispatch'),

    
    path('modify_packing/', modify.modify_packing, name='modify_packing'),
    path('edit_packing/<int:pk>/', modify.edit_packing, name='edit_packing'),
    path('delete_bundle/<int:bundle_id>/', modify.delete_bundle, name='delete_bundle'),
    path('modify_dispatch/', modify.modify_dispatch, name='modify_dispatch'),
    path('edit_dispatch/<int:pk>/', modify.edit_dispatch, name='edit_dispatch'),
    path('recall_dispatch/<int:packing_id>/', modify.recall_dispatch, name='recall_dispatch'),


    path('packing_book/', report.packing_book, name='packing_book'),
    path('stock_book/', report.stock_book, name='stock_book'),
    path('dispatch_book/', report.dispatch_book, name='dispatch_book'),
    path('size_book/', report.size_book, name='size_book'),
    path('stock_summary/', report.stock_summary, name='stock_summary'),
    path('lot_summary/', report.lot_summary, name='lot_summary'),
    path('production_register/', report.production_register, name='production_register'),
    path('lot_register/', report.lot_register, name='lot_register'),


    path('dispatch_summary/', summary.dispatch_summary, name='dispatch_summary'),
    path('customer_report/', summary.customer_report, name='customer_report'),
    path('transport_report/', summary.transport_report, name='transport_report'),


    path('packing_slip/', tools.packing_slip, name='packing_slip'),
    path('packing_slip_new/', tools.packing_slip_new, name='packing_slip_new'),
    path('remove_data/', tools.remove_data, name='remove_data'),

]
