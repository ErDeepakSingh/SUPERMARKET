from django.db import models

class Category(models.Model):
    name            =models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name            =models.CharField(max_length=150)
    category        =models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name+"  <-  "+str(self.category)

class Item(models.Model):
    name            =models.CharField(max_length=150)
    category        =models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory     =models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    amount         =models.PositiveIntegerField(default=0,null=True)

    def __str__(self):
        return str(self.name)+"  <-  "+str(self.subcategory)