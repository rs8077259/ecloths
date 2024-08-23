from rest_framework import serializers
from .models import MenWear

class MenWearSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenWear
        fields = ['url',
                  'title',
                  'price',
                  'mrp',
                  'image_link',
                  'last_7_day_sale',
                  'fit',
                  'fabric',
                  'neck',
                  'sleeve',
                  'pattern',
                  'length',
                  'description',
                  'links',
                  'available_skus'
                  ]