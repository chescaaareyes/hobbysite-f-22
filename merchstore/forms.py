from django import forms

from .models import Product, Transaction

class TransactionForm(forms.ModelForm):
    def __init__(self, *args, product=None, **kwargs):
        self.product = product
        super().__init__(*args, **kwargs)

    class Meta:
        model = Transaction
        fields = ["amount"]

    def clean_amount(self, *args, **kwargs):
        print(args)
        amount = self.cleaned_data.get("amount")
        if amount <= 0:
            raise forms.ValidationError("Please choose a positive amount")
        if amount > self.product.stock:
            raise forms.ValidationError("Not enough stock")
        return amount

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner', 'created_on', ]