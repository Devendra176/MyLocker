from rest_framework import serializers

from users.models import CustomUser
from backend.websites.models import WebsitesData


class WebsitesDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = WebsitesData
        exclude = ('user',)
        extra_kwargs = {'id': {'read_only': False, 'required': True}, 'user':{'read_only': True, 'required': False}}


class ActiveUserSerializer(serializers.ModelSerializer):
    website_data  = WebsitesDataSerializers(source='user_website_data', many=True)

    class Meta:
        model = CustomUser
        fields = ['pk', 'email', 'phone', 'website_data']
        extra_kwargs = {'email': {'read_only': True, 'required': False}, 
                        'user':{'read_only': True, 'required': False},
                        'phone':{'read_only': True, 'required': False},}
    
    def update(self, instance, validated_data):
        if 'user_website_data' in validated_data:
            nested_data = validated_data.pop('user_website_data')
            for data in nested_data:
                id = data.get('id', None)
                website_data = WebsitesData.objects.filter(pk=id)

                if website_data.exists():
                    website_data.update(**data)
                else:
                    raise serializers.ValidationError({'errors': 'ID: {} not exists'.format(id), 'data':nested_data})
        return super(ActiveUserSerializer, self).update(instance, validated_data)

      
class WebsitesAddDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = WebsitesData
        fields = '__all__'
        read_only_fields = ('user',)
