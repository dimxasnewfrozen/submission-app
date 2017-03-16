from django.conf.urls import url
from django.contrib.auth import views as auth_views
from views import home, app

urlpatterns = [
	url(r'^login/$', auth_views.login, name='login'),

    # Main index page -- where the user first lands
    url(r'^$', app.submit_app, name='submit-app'),

    # App specific routes    
    url(r'^apps$', app.apps, name='apps'),
    url(r'^app/(?P<app_id>[0-9]+)$', app.app_details, name='app-details'),
    url(r'^submit-app$', app.submit_app, name='submit-app'),
    url(r'^success$', app.success, name='success'),

]
