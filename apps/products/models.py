from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
# Create your models here.

class MeasureUnit(BaseModel):
    """Model definition for MeasureUnit."""

    # TODO: Define fields here
    description = models.CharField('Description', max_length=50, blank=False, null=False, unique=True)

    class Meta:
        """Meta definition for MeasureUnit."""

        verbose_name = 'unit of measurement'
        verbose_name_plural = 'measurement units'

    def __str__(self):
        """Unicode representation of MeasureUnit."""
        return self.description

class CategoryProduct(BaseModel):
    """Model definition for CategoryProduct."""

    # TODO: Define fields here
    description = models.CharField('Description', max_length=50, unique=True, null=False, blank=False)

    class Meta:
        """Meta definition for CategoryProduct."""

        verbose_name = 'product category'
        verbose_name_plural = 'product categories'

    def __str__(self):
        """Unicode representation of CategoryProduct."""
        return self.description

class Indicator(BaseModel):
    """Model definition for Indicator."""

    # TODO: Define fields here
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Oferta')

    class Meta:
        """Meta definition for Indicator."""

        verbose_name = 'offers indicator'
        verbose_name_plural = 'offer indicators'

    def __str__(self):
        """Unicode representation of Indicator."""
        return f'category offer {self.category_product} : {self.descount_value}%' 

class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField('Product name', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Product description', blank=False, null=False)
    image = models.ImageField('product image', upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='unit of measurement', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='product category', null=True)
    
    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value



    # @property
    # def stock(self):
    #     from django.db.models import Sum
    #     from apps.expense_manager.models import Expense

    #     expenses = Expense.objects.filter(
    #         product=self,
    #         state=True
    #     ).aggregate(Sum('quantity'))

    #     return expenses