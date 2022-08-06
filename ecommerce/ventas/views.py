from django.shortcuts import HttpResponse
from django.shortcuts import render


html_base = """
 <h1>Shopping Car</h1>
 <ul>
   <li><a href="/">Inicio</a></li>
   <li><a href="/articulo/">Articulos</a></li>
   <li><a href="/cliente/">Clientes</a></li>
   <li><a href="/venta/">Ventas</a></li>
   <li><a href="/consulta/">Consultas</a></li>
 </li>
"""
def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)


def articulo(request):
  return HttpResponse(html_base+
    """<h2>Mantenimiento de Articulo</h2>
       <p>List de articulos</p>""")

def cliente(request):
  data = {
      'titulo':'GESTION DE CLIENTES',
      'crear_url': '/crearcliente',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/listCliente.html",data)

def crearCliente(request):
  data = {
      'titulo':'MANTENIMIENTO DE CLIENTES',
      'crear_url':'/crearcliente',
      'action':'add',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/formCliente.html",data)

def venta(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "ventas/ventas.html",data)


def empleado(request):
  data = {
      'titulo': 'Nomina',
      'crear_url': '/crearEmpleado',
      'listar_url': '/empleado',
  }
  return render(request, "fichadepersonal/empleado/listEmpleado.html",data)

def crearEmpleado(request):
  data = {
      'titulo': 'Mantenimiento',
      'crear_url': '/crearEmpleado',
      'action': 'add',
      'listar_url': '/empleado',
  }
  return render(request, "fichadepersonal/empleado/form.Empleados.html",data)
def formEmpleado(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/crearEmpleado',
      'action':'add',
      'listar_url': '/empleado',
  }
  return render(request, "fichadepersonal/empleado/form.Empleados.html",data)


def Cargo(request):
  data = {
      'titulo': 'GESTION ',
      'crear_url': '/crearCargo',
      'listar_url': '/Cargo',
  }
  return render(request, "fichadepersonal/cargo.html",data)

def crearCargo(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/crearCargo',
      'action':'add',
      'listar_url': '/Cargo',
  }
  return render(request, "fichadepersonal/empleado/formCargo.html",data)
def formcargo(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/crearcargo',
      'action':'add',
      'listar_url': '/cargo',
  }
  return render(request, "fichadepersonal/empleado/formCargo.html",data)

def departamento(request):
  data = {
      'titulo':'DEPARTAMENTOS',
      'crear_url': '/crearDepartamento',
      'listar_url': '/departamento',
  }
  return render(request, "fichadepersonal/departamento.html",data)

def crearDepartamento(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/crearDepartamento',
      'action':'add',
      'listar_url': '/departamento',
  }
  return render(request, "fichadepersonal/empleado/formdepartamento.html",data)
def formdepartamento(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/creardepartamento',
      'action':'add',
      'listar_url': '/empleado',
  }
  return render(request, "fichadepersonal/empleado/formdepartamento.html",data)


def fichadepersonal(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "fichadepersonal/fichapersonal.html",data)

def Academico(request):
  data = {
      'titulo': 'INFORMACION ',
      'crear_url': '/crearAcademico',
      'action': 'add',
      'listar_url': '/Academico',
  }
  return render(request, "fichadepersonal/empleado/academico.html",data)
def crearAcademico(request):
  data = {
      'titulo': 'MANTENIMIENTO ',
      'crear_url': '/crearAcademico',
      'action': 'add',
      'listar_url': '/Academico',
  }
  return render(request, "fichadepersonal/empleado/form.academico.html",data)
def sueldo(request):
    data = {
        'titulo': 'GESTION ',
        'crear_url': '/crearsueldo',
        'action': 'add',
        'listar_url': '/sueldo',
    }
    return render(request, "fichadepersonal/empleado/sueldos.html", data)
def crearsueldo(request):
  data = {
      'titulo':'MANTENIMIENTO',
      'agregar_url':'/crearsueldo',
      'action':'add',
      'listar_url': '/sueldo',
  }
  return render(request, "fichadepersonal/empleado/formsueldo.html",data)

def fichamedica(request):
    data = {
        'titulo': 'INFORMACION',
        'crear_url': '/crearfichamedica',
        'action': 'add',
        'listar_url': '/fichamedica',
    }
    return render(request, "fichadepersonal/empleado/fichamedica.html", data)
def contactoemergencia(request):
  data = {
      'titulo':'INFORMACION',
      'crear_url':'/crearcontactoemergencia',
      'action':'add',
      'listar_url': '/contactoemergencia',
  }
  return render(request, "fichadepersonal/empleado/contactoemergencia.html",data)
def crearfichamedica(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/crearfichamedica',
      'action':'add',
      'listar_url': '/fichamedica',
  }
  return render(request, "fichadepersonal/empleado/formfichamedica.html",data)
def crearcontactoemergencia(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/crearcontactoemergencia',
      'action':'add',
      'listar_url': '/contactoemergencia',
  }
  return render(request, "fichadepersonal/empleado/formcontactoemergencia.html",data)
def eliminarEmpleado(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/eliminarempleado',
      'action':'add',
      'listar_url': '/empleado',
  }
  return render(request, "fichadepersonal/empleado/form.Empleados.html",data)
def capacitacion(request):
  data = {
      'titulo':'GESTION ',
      'crear_url':'/crearcapacitacion',
      'action':'add',
      'listar_url': '/capacitacion',
  }
  return render(request, "fichadepersonal/empleado/capacitacion.html",data)
def crearcapacitacion(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/crearcapacitacion',
      'action':'add',
      'listar_url': '/capacitacion',
  }
  return render(request, "fichadepersonal/empleado/formcapacitacion.html",data)
def formAcademico(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/crearacademico',
      'action':'add',
      'listar_url': '/academico',
  }
  return render(request, "fichadepersonal/empleado/form.academico.html",data)
def formfichamedica(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/crearfichamedica',
      'action':'add',
      'listar_url': '/fichamedica',
  }
  return render(request, "fichadepersonal/empleado/formfichamedica.html",data)
def formcapacitacion(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/crearcapacitacion',
      'action':'add',
      'listar_url': '/capacitacion',
  }
  return render(request, "fichadepersonal/empleado/formcapacitacion.html",data)
def formcontactoemergencia(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/crearcontactoemergencia',
      'action':'add',
      'listar_url': '/contactoemergencia',
  }
  return render(request, "fichadepersonal/empleado/formcontactoemergencia.html",data)
def formsueldo(request):
  data = {
      'titulo':'MANTENIMIENTO ',
      'crear_url':'/crearsueldo',
      'action':'add',
      'listar_url': '/sueldo',
  }
  return render(request, "fichadepersonal/empleado/formsueldo.html",data)




