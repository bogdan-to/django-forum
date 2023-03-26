from .forms import MemberAuthenticationForm, MemberCreationForm

def login_form(request):
    login_form = MemberAuthenticationForm()
    return {'login_form' : login_form}

def register_form(request):
    register_form = MemberCreationForm()
    return {'register_form': register_form}