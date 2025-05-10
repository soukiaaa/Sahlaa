# tasks.py
from celery import shared_task
from .models import add_prodact

@shared_task
def process_images(product_id):
    product = add_prodact.objects.get(id=product_id)
    product.resize_image(product.Image, (800, 600))
    product.resize_image(product.Image_2, (800, 600))
    product.resize_image(product.Image_center, (800, 600))
    product.resize_image(product.Image_foter_1, (800, 600))
    product.resize_image(product.Image_foter_2, (800, 600))
    product.resize_image(product.Image_foter_3, (800, 600))
    product.save()
