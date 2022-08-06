"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ventas.views import inicio,articulo,cliente,crearCliente,venta,fichadepersonal,empleado,Cargo,departamento,\
    crearCargo,crearDepartamento,crearEmpleado,Academico,sueldo,fichamedica,crearAcademico,crearsueldo,\
    crearfichamedica,contactoemergencia,crearcontactoemergencia,formEmpleado,eliminarEmpleado,formcargo, formdepartamento,formAcademico,formfichamedica,formcapacitacion,capacitacion,crearcapacitacion,formcontactoemergencia,formsueldo



from django.conf.urls.static import static
from ecommerce import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('articulo/', articulo, name='articulo'),
    path('cliente/', cliente, name='cliente'),
    path('crearcliente/', crearCliente, name='crearcliente'),
    path('venta/', venta, name='venta'),
    path('fichadepersonal/', fichadepersonal, name='fichadepersonal'),
    path('empleado/', empleado, name='empleado'),
    path('Cargo/', Cargo, name='Cargo'),
    path('departamento/',departamento, name='departamento'),
    path('crearEmpleado/', crearEmpleado, name='crearEmpleado'),
    path('crearCargo/', crearCargo, name='crearCargo'),
    path('crearDepartamento/',crearDepartamento, name='crearDepartamento'),
    path('Academico/',Academico,name='Academico'),
    path('crearAcademico/',crearAcademico,name='crearAcademico'),
    path('sueldo/',sueldo,name='sueldo'),
    path('crearsueldo/',crearsueldo,name='crearsueldo'),
    path('fichamedica/',fichamedica,name='fichamedica'),
    path('crearfichamedica/',crearfichamedica,name='crearfichamedica'),
    path('contactoemergencia/',contactoemergencia,name='contactoemergencia'),
    path('crearcontactoemergencia/',crearcontactoemergencia,name='crearcontactoemergencia'),
    path('formEmpleado/',formEmpleado,name='formEmpleado'),
    path('eliminarEmpleado/',eliminarEmpleado,name='eliminarEmpleado'),
    path('formCargo/', formcargo, name='formCargo'),
    path('formdepartamento/',formdepartamento, name='formdepartamento'),
    path('crearcapacitacion/',crearcapacitacion,name='crearcapacitacion'),
    path('formAcademico/',formAcademico,name='formAcademico'),
    path('formfichamedica/',formfichamedica,name='formfichamedica'),
    path('formcapacitacion/', formcapacitacion, name='formcapacitacion'),
    path('capacitacion/',capacitacion, name='capacitacion'),
    path('formcontactoemergencia/',formcontactoemergencia,name='formcontactoemergencia'),
    path('formsueldo/',formsueldo,name='formsueldo'),





  ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)