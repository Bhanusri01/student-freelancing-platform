'''
from django import forms
from .models import Gig, Category


class GigForm(forms.ModelForm):

    # ===== BASIC TIER =====
    basic_price = forms.DecimalField(
        label="Basic Price",
        widget=forms.NumberInput(attrs={
            'class': 'w-full border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-400',
            'placeholder': 'Enter basic price'
        })
    )

    basic_description = forms.CharField(
        label="Basic Description",
        widget=forms.Textarea(attrs={
            'class': 'w-full border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-400',
            'rows': 3,
            'placeholder': 'Describe what is included in Basic package'
        })
    )

    # ===== STANDARD TIER =====
    standard_price = forms.DecimalField(
        label="Standard Price",
        widget=forms.NumberInput(attrs={
            'class': 'w-full border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-400',
            'placeholder': 'Enter standard price'
        })
    )

    standard_description = forms.CharField(
        label="Standard Description",
        widget=forms.Textarea(attrs={
            'class': 'w-full border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-400',
            'rows': 3,
            'placeholder': 'Describe what is included in Standard package'
        })
    )

    # ===== PREMIUM TIER =====
    premium_price = forms.DecimalField(
        label="Premium Price",
        widget=forms.NumberInput(attrs={
            'class': 'w-full border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-400',
            'placeholder': 'Enter premium price'
        })
    )

    premium_description = forms.CharField(
        label="Premium Description",
        widget=forms.Textarea(attrs={
            'class': 'w-full border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-400',
            'rows': 3,
            'placeholder': 'Describe what is included in Premium package'
        })
    )

    class Meta:
        model = Gig
        fields = ['title', 'description']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-purple-400',
                'placeholder': 'I will build a professional Django website'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-purple-400',
                'rows': 5,
                'placeholder': 'Explain your service in detail...'
            }),
        }
        '''
from django import forms
from .models import Gig, Category


class GigForm(forms.ModelForm):

    # ===== BASIC =====
    basic_price = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'class': 'w-full border border-slate-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-teal-500'
        })
    )

    basic_delivery = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'w-full border border-slate-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-teal-500'
        })
    )

    basic_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full border border-slate-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-teal-500',
            'rows': 3
        })
    )

    # ===== STANDARD =====
    standard_price = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'class': 'w-full border border-slate-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-teal-500'
        })
    )

    standard_delivery = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'w-full border border-slate-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-teal-500'
        })
    )

    standard_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full border border-slate-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-teal-500',
            'rows': 3
        })
    )

    # ===== PREMIUM =====
    premium_price = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'class': 'w-full border border-slate-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-teal-500'
        })
    )

    premium_delivery = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'w-full border border-slate-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-teal-500'
        })
    )

    premium_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full border border-slate-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-teal-500',
            'rows': 3
        })
    )

    class Meta:
        model = Gig
        fields = ['title', 'description', 'category', 'delivery_time']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-teal-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-teal-500',
                'rows': 5
            }),
            'category': forms.Select(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-teal-500'
            }),
            'delivery_time': forms.NumberInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-teal-500',
                'min': 1
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all().order_by('name')
        self.fields['category'].empty_label = "Select category"
