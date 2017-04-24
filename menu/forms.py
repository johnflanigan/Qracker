from django import forms
from menu.models import Order, Item
from datetime import datetime
from userprofile.models import UserProfile
from django.contrib.auth.models import User

class AddItemForm(forms.ModelForm):
    name=forms.CharField(help_text="Please enter the Item name: ",max_length=128,required=True)
    food_or_drink=forms.ChoiceField(choices=(
        ("Food","Food"),
        ("Drink","Drink")))
    is_breakfast=forms.BooleanField(help_text = 'Breakfast Item?', required=False)
    is_lunch=forms.BooleanField(help_text = 'Lunch Item?', required=False)
    price=forms.DecimalField(help_text="Please enter the price: ", min_value=0,required=True)
    supplier = forms.ModelChoiceField(queryset=User.objects.filter(id = UserProfile.objects.filter(supplier_flag__exact=True).values_list('user_id')))

    class Meta:
        model = Item
        exclude = ['promo_flag']

class McDonaldsOrderForm(forms.ModelForm):
    user_name = forms.CharField(help_text="Please enter your name: ", max_length=128, required=True)
    item_name = forms.ChoiceField(choices=(
        ("Hash Brown", "Hash Brown"),
        ("Coffee", "Coffee"),
        ("Egg McMuffin", "Egg McMuffin"),
        ("Sausage", "Sausage")))
    restaurant_name = forms.CharField(widget=forms.HiddenInput(), initial='McDonalds')
    creation_time = forms.DateTimeField(widget=forms.HiddenInput(), initial=datetime.now)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Order
        fields = ('user_name', 'item_name', 'restaurant_name', 'creation_time')


class TacoBellOrderForm(forms.ModelForm):
    user_name = forms.CharField(help_text="Please enter your name: ", max_length=128, required=True)
    item_name = forms.ChoiceField(choices=(
        ("Taco", "Taco"),
        ("Burrito", "Burrito"),
        ("Crunch Wrap", "Crunch Wrap"),
        ("Baja Blast", "Baja Blast")))
    restaurant_name = forms.CharField(widget=forms.HiddenInput(), initial='Taco Bell')
    creation_time = forms.DateTimeField(widget=forms.HiddenInput(), initial=datetime.now)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Order
        fields = ('user_name', 'item_name', 'restaurant_name', 'creation_time')

# search form
class SearchForm(forms.ModelForm):
    searchstring = forms.CharField(max_length=128)
    food_or_drink = forms.ChoiceField(choices=(
        ('Food', 'Food'),
        ('Drink', 'Drink'),
    ))
    is_breakfast = forms.BooleanField(initial=False)
    is_lunch = forms.BooleanField(initial=False)
    class Meta:
        model = Item
        fields = ('searchstring', 'food_or_drink', 'is_breakfast', 'is_lunch') 

class BrowseForm(forms.ModelForm):
    restaurant_name = forms.ModelChoiceField(queryset=UserProfile.objects.filter(supplier_flag__exact=True), required=True)
    is_food = forms.BooleanField(initial=False, required=False)
    is_drink = forms.BooleanField(initial=False, required=False)
    is_breakfast = forms.BooleanField(initial=False, required=False)
    is_lunch = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = Item
        fields = ('restaurant_name', 'is_breakfast', 'is_lunch')

class BrowseResultsForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'price', 'supplier')
