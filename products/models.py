from django.db import models

# Create your models here.
class Categories(models.Model):
    class Meta:
        db_table = 'products_categories'

    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name

class Option(models.Model):
    class Meta:
        db_table = 'options'

    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

class OptionGroup(models.Model):
    class Meta:
        db_table = 'option_groups'

    name = models.CharField(max_length=250, blank=True, null=True)
    options = models.ManyToManyField(Option, related_name='options_groups', verbose_name='options_groups')
    def __str__(self):
        return self.name

class OptionItem(models.Model):
    class Meta:
        db_table = 'option_items'

    name = models.CharField(max_length=250, blank=True, null=True)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        db_table = 'prodcuts_products'

    name = models.CharField(max_length=250, blank=False, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ManyToManyField(Brand)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(default=3) # 1 = Catalogue, 2 = Approved, 3 = Pending

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    class Meta:
        db_table = 'products_product_variants'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(max_length=200, blank=True, null=False)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    qty = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.sku

class ProductVariantValues(models.Model):
    class Meta:
        db_table = 'products_product_variant_values'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE)
    option_item = models.ForeignKey(OptionItem, on_delete=models.CASCADE)




