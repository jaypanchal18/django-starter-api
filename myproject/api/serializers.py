from rest_framework import serializers
from .models import YourModel

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = '__all__'  # Specify the fields you want to include

    def create(self, validated_data):
        try:
            instance = YourModel.objects.create(**validated_data)
            return instance
        except Exception as e:
            raise serializers.ValidationError(f"Error creating instance: {str(e)}")

    def update(self, instance, validated_data):
        try:
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
            return instance
        except Exception as e:
            raise serializers.ValidationError(f"Error updating instance: {str(e)}")