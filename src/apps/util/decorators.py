from django.shortcuts import redirect


def verificar_permisos():

    def deco_verificar_permisos(f):

        def check(request, *arg, **kgars):
            print("ESTOY DENTRO DEL DECORADOR")
            print(request.user)

            if not request.user.is_authenticated:
                return redirect("login")
            # if not request.user.es_admin:
            #     return redirect("error_permisos")
            
            return f(request, *arg, **kgars)
        
        return check
    
    return deco_verificar_permisos