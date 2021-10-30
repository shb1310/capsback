from rest_framework import serializers
from .models import AnsimDataset as ans
from .models import PublicPDataset as pp

class AnsimSerializer(serializers.ModelSerializer):
	class Meta:
		model = ans
		fields = '__all__'
        
class PublicPSerializer(serializers.ModelSerializer):
	class Meta:
		model = pp
		fields = '__all__'