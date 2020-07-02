from django import forms





class RegisterForm(forms.Form):
    
    name = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder':  'username',
        'class': 'form-control form-control-lg',
        'id':'username ',
        'name':'name',
        'type' :"text"

       }))
    email = forms.EmailField(widget = forms.TextInput(attrs={
        'placeholder':  'email',
        'class': 'form-control form-control-lg',
        'id':'email ',
        'name':'email',
         'type' :"email"

    }))
    password = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder':  'password',
        'class': 'form-control form-control-lg',
        'id':'pword ',
        'name':'pass1',
        'type' :"password"

    }))
    re_password = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder':  're_password',
        'class': 'form-control form-control-lg',
        'id':'pword2 ',
        'name':'pass2',
        'type' :"password"

    }))

    


    
   