from xml.parsers.expat import model
from django.forms import ModelForm
from product.models import Brand, Category, Product, ProductImage, ProductSpecification,Coupon
from django.forms import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *
from .specification import *


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name','parent']


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['name']


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-12'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('price'),
                Field('description'),
                Field('long_description'),
                Field('category'),
                Field('brand'),
                Fieldset('Add Image',
                         Formset('product_meta_formset')),
                HTML("<br>"),
                Fieldset('Add Specification',
                         SpecificationFormset('product_specifiaction')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
            )
        )

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'long_description', 'category', 'brand']


class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductSpecificationForm(ModelForm):
    class Meta:
        model = ProductSpecification
        fields = ['key', 'value']

class CoupuanForm(ModelForm):
    class Meta:
        model = Coupon
        fields = ['name','price','status']

ProductMetaInlineFormset = inlineformset_factory(
    Product,
    ProductImage,
    form=ProductImageForm,
    extra=1, can_delete=True,
)

ProductSpecificationMetaInlineFormset = inlineformset_factory(
    Product,
    ProductSpecification,
    form=ProductSpecificationForm,
    extra=1, can_delete=True,
)

