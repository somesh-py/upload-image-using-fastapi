from tortoise.models import Model
from tortoise import Tortoise, fields


class Category(Model):
    name = fields.CharField(200, unique=True)
    slug = fields.CharField(200)
    category_image = fields.TextField()
    description = fields.TextField()
    is_active = fields.BooleanField(default=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)


class Subcategory(Model):
    Category=fields.ForeignKeyRelation("models.Category",related_name="subcategory",on_delete="CASCADE")
    name = fields.CharField(200, unique=True)
    slug = fields.CharField(200)
    category_image = fields.TextField()
    description = fields.TextField()
    is_active = fields.BooleanField(default=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)


Tortoise.init_models(["app.models"], "models")
