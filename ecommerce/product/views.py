from django.shortcuts import render
from base.views import *
from product.forms import *
from product.models import *
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.forms import modelformset_factory
from django.db.models import Q

# Category.
class CategoryListView(BaseListView):
    """ Admin List category """
    model = Category
    template_name = 'adminportol/category_list.html'
    context_object_name = 'cateories'


class CategoryCreateView(BaseCreateView):
    """ Admin create category """
    form_class = CategoryForm
    model = Category
    template_name = 'adminportol/category_create.html'
    success_url = reverse_lazy("custadmin:category_list")


class CategoryUpdateView(BaseUpdateView):
    """ Admin update category """
    form_class = CategoryForm
    model = Category
    template_name = 'adminportol/category_update.html'
    success_url = reverse_lazy("custadmin:category_list")


class CategoryDeleteView(BaseDeleteView):
    """ Admin delete category """
    model = Category
    template_name = 'adminportol/category_list.html'
    success_url = reverse_lazy("custadmin:category_list")


# Barnd.
class BrandListView(BaseListView):
    """ Admin List brand """
    model = Brand
    template_name = 'adminportol/brand_list.html'
    context_object_name = 'brands'


class BrandCreateView(BaseCreateView):
    """ Admin create brand """
    form_class = BrandForm
    model = Brand
    template_name = 'adminportol/brand_create.html'
    success_url = reverse_lazy("custadmin:brand_list")


class BrandUpdateView(BaseUpdateView):
    """ Admin update brand """
    form_class = BrandForm
    model = Brand
    template_name = 'adminportol/brand_update.html'
    success_url = reverse_lazy("custadmin:brand_list")


class BrandDeleteView(BaseDeleteView):
    """ Admin delete brand """
    model = Brand
    template_name = 'adminportol/brand_list.html'
    success_url = reverse_lazy("custadmin:brand_list")


# product
class ProductListView(BaseListView):
    """ Admin List Product """
    model = Product
    template_name = 'adminportol/product_list.html'
    context_object_name = 'products'


class ProductCreateView(BaseCreateView):
    """ Admin create Product """
    form_class = ProductForm
    model = Product
    template_name = 'adminportol/product_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['product_meta_formset'] = ProductMetaInlineFormset(self.request.POST, self.request.FILES)
            print(context['product_meta_formset'])
            context['product_specifiaction'] = ProductSpecificationMetaInlineFormset(self.request.POST)
            print(context['product_specifiaction'])
        else:
            context['product_meta_formset'] = ProductMetaInlineFormset()
            context['product_specifiaction'] = ProductSpecificationMetaInlineFormset()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        product_meta_formset = ProductMetaInlineFormset(self.request.POST, self.request.FILES)
        product_specifiaction = ProductSpecificationMetaInlineFormset(self.request.POST)
        if form.is_valid() and product_meta_formset.is_valid() and product_specifiaction.is_valid():
            return self.form_valid(form, product_meta_formset, product_specifiaction)
        else:
            return self.form_invalid(form, product_meta_formset, product_specifiaction)

    def form_valid(self, form, product_meta_formset, product_specifiaction):
        context = self.get_context_data()
        product_meta_formset = context['product_meta_formset']
        product_specifiaction = context['product_specifiaction']
        self.object = form.save(commit=False)
        self.object.save()

        product_metas = product_meta_formset.save(commit=False)
        for meta in product_metas:
            meta.product = self.object
            meta.save()

        specification = product_specifiaction.save(commit=False)
        for speci in specification:
            speci.product = self.object
            speci.save()

        return redirect(reverse_lazy("custadmin:product_list"))

    def form_invalid(self, form, product_meta_formset, product_specifiaction):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  product_meta_formset=product_meta_formset,
                                  product_specifiaction=product_specifiaction
                                  )
        )


class ProductUpdateView(BaseUpdateView):
    """ Admin update Product """
    form_class = ProductForm
    model = Product
    template_name = 'adminportol/product_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['product_meta_formset'] = ProductMetaInlineFormset(self.request.POST, self.request.FILES,
                                    instance=self.object)
            print(context['product_meta_formset'])
            # context['product_specifiaction'] = ProductSpecificationMetaInlineFormset(self.request.POST,self.object)
            # print(context['product_specifiaction'])
        else:
            context['product_meta_formset'] = ProductMetaInlineFormset(instance=self.object)
            # context['product_specifiaction'] = ProductSpecificationMetaInlineFormset(self.object)
        # print(">>>>>>>>",context['product_specifiaction'])
        print(">>>>>>>>>>>",context['product_meta_formset'])
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        product_meta_formset = ProductMetaInlineFormset(self.request.POST, self.request.FILES,instance=self.object)
        # print('product_meta_formset',product_meta_formset)
        if form.is_valid() and product_meta_formset.is_valid():
            return self.form_valid(form, product_meta_formset,instance=self.object)

        else:
            return self.form_invalid(form, product_meta_formset)

    def form_valid(self, form, product_meta_formset,instance):
        context = self.get_context_data()
        product_meta_formset = context['product_meta_formset']
        instance = form.save(commit=False)
        instance.save()
        product_metas = product_meta_formset.save(commit=False)
        for meta in product_metas:
            meta.instance = self.object
            meta.save()
        return redirect(reverse_lazy("product:product_list"))

    def form_invalid(self, form, product_meta_formset):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  product_meta_formset=product_meta_formset
                                  )
        )

    success_url = reverse_lazy("custadmin:category_list")


class ProductDeleteView(BaseDeleteView):
    """ Admin delete Product """
    model = Product
    template_name = 'adminportol/product_list.html'
    success_url = reverse_lazy("custadmin:category_list")


class HomeView(BaseTemplateView):
    template_name = "userportal/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ProductListView(BaseListView):
    template_name = 'userportal/category.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["products"] = Product.objects.all().order_by('-create_at')
        context["categories"] = Category.objects.all()
        context["brands"] = Brand.objects.all()
        return context

    def get_queryset(self):
        category_slug = self.request.GET.get("category", '')
        brand_list = self.request.GET.getlist("brand", [])
        search = self.request.GET.get("q", '')
        products = Product.objects.all()

        if brand_list:
            products = products.filter(Q(brand__slug__in=brand_list))
        if category_slug:
            products = products.filter(Q(category__slug=category_slug))
        if search:
            products = products.filter(name__icontains=search)
        return products

        # if category_slug and brand_list and product:
        #     products = Product.objects.filter(category__slug = category_slug, brand__slug = brand_list,name__icontains=product)
        #     print('>>>>>>>>>>6',products)
        #     return products
        # elif category_slug and brand_list:
        #     products = Product.objects.filter(category__slug = category_slug, brand__slug = brand_list)
        #     print('>>>>>>>>>>7',products)
        #     return products
        # elif category_slug and product:
        #     products = Product.objects.filter(category__slug = category_slug , name__icontains = product)
        #     print('>>>>>>>>>>8',products)
        #     return products
        # elif brand_list and product:
        #     print(brand_list)
        #     products = Product.objects.filter(brand__slug = brand_list , name__icontains =product)
        #     print('>>>>>>>>>>9',products)
        #     return products
        # elif brand_list:
        #     print(brand_list)
        #     products = Product.objects.filter(brand__slug =  brand_list)
        #     print('>>>>>>>>>>10',products)
        #     return products
        # elif category_slug:
        #     products = Product.objects.filter(category__slug = category_slug)
        #     print('>>>>>>>>>>11',products)
        #     return products
        # elif product:
        #     products = Product.objects.filter(name__icontains=product)
        #     print('>>>>>>>>>>12',products)
        #     return products
        # else:
        #     products = Product.objects.all()
        #     print('>>>>>>>>>>0',products)
        #     return products


# Product.objects.filter(Q(brand__slug="adidas")&Q(name__icontains="101")&Q(category__slug="adidas"))
# Product.objects.filter(Q(brand__slug="adidas")&Q(name__icontains="101")|Q(category__slug="adidas")&Q(name__icontains="101")|Q(category__slug="adidas")&Q(brand__slug="adidas"))
# Product.objects.filter(Q(brand__slug="adidas")|Q(name__icontains="101")|Q(category__slug="adidas"))
# Product.objects.all()
class ProdectDetailView(BaseDetailView):
    template_name = 'userportal/single-product.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get('pk')
        print(product_id)
        context['productspecifications'] = ProductSpecification.objects.filter(product_id=product_id)
        return context

class test(BaseTemplateView):
    template_name = 'userportol/single-product.html'