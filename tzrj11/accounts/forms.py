from django import forms
from .models import Store, Customer, Agent, Order, ShoppingCart, Offer

# 1. نموذج المتجر
class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name']
        labels = {
            'name': 'اسم المتجر',
        }


# 2. نموذج العميل
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'national_id', 'email', 'phone', 'location']
        labels = {
            'name': 'الاسم',
            'national_id': 'الرقم الوطني',
            'email': 'البريد الإلكتروني',
            'phone': 'رقم الهاتف',
            'location': 'رابط الموقع (Google Maps)',
        }
        widgets = {
            'location': forms.URLInput(attrs={'placeholder': 'مثال: https://maps.google.com/...'}),
        }


# 3. نموذج المنوب
class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = [
            'name',
            'image',
            'phone_number',
            'email',
            'location',
            'description',
            'password',
            'stores',
        ]
        labels = {
            'name': 'الاسم',
            'image': 'الصورة الشخصية',
            'phone_number': 'رقم الهاتف',
            'email': 'البريد الإلكتروني',
            'location': 'رابط الموقع (Google Maps)',
            'description': 'الوصف',
            'password': 'كلمة المرور',
            'stores': 'المتاجر التي يعمل بها',
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'أدخل كلمة المرور'}),
            'stores': forms.CheckboxSelectMultiple(),
            'location': forms.URLInput(attrs={'placeholder': 'https://maps.google.com/...'}),
        }


# 4. نموذج الطلب
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'company_name',
            'description',
            'image',
            'image_url',
            'price',
            'required_number',
            'customer',
        ]
        labels = {
            'company_name': 'اسم الشركة',
            'description': 'الوصف',
            'image': 'صورة المنتج (اختياري)',
            'image_url': 'رابط الصورة (اختياري)',
            'price': 'السعر',
            'required_number': 'العدد المطلوب',
            'customer': 'العميل',
        }


# 5. نموذج السلة
class ShoppingCartForm(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        fields = ['store_name', 'payment_date', 'delivery_date', 'customers']
        labels = {
            'store_name': 'اسم المتجر',
            'payment_date': 'تاريخ الدفع',
            'delivery_date': 'تاريخ التسليم',
            'customers': 'العملاء',
        }
        widgets = {
            'payment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'delivery_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'customers': forms.CheckboxSelectMultiple(),
        }


# 6. نموذج التخفيضات
class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['image', 'offer_type', 'stores', 'price', 'available_quantity']
        labels = {
            'image': 'صورة العرض',
            'offer_type': 'نوع العرض',
            'stores': 'المتاجر',
            'price': 'السعر',
            'available_quantity': 'الكمية المتاحة',
        }
        widgets = {
            'stores': forms.CheckboxSelectMultiple(),
        }
