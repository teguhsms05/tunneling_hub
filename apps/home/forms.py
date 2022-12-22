from django import forms

from .models import GroupDomain

class GroupDomainCreate(forms.ModelForm):
    group_domain = forms.CharField( 
                    widget=forms.TextInput(
                        attrs={
                            "placeholder": "Please insert a group domain",
                            "class": "form-control"
                        })
                    )
    cpanel_domain = forms.CharField(
                    widget=forms.TextInput(
                        attrs={
                            "placeholder": "Please insert a cpanel link from group domain ",
                            "class": "form-control"
                        })
                    )
    class Meta:
        model   = GroupDomain
        fields  = ('group_domain', 'cpanel_domain')
        