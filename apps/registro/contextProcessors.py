from .forms import LoginForm
def variable(request):
    return{
        'login':LoginForm
          }