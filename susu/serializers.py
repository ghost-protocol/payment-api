from .models import Client, Account, Payment
from rest_framework import serializers

# Using ModelSerializers
class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'lastName', 'firstName', 'otherName', 'phoneNumber', 'address', 'created')

# Using custom Serializers
# class ClientSerializer(serializers.Serializer):
#
#     # define the fields that get serialized/deserialized
#
#     id = serializers.IntegerField(read_only=True)
#     lastName = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     firstName = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     otherName = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     phoneNumber = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     address = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     # address = serializers.CharField(style={'base_template': 'textarea.html'})
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Client` instance, given the validated data.
#         """
#         return Client.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Client` instance, given the validated data.
#         """
#         instance.lastName = validated_data.get('lastName', instance.lastName)
#         instance.firstName = validated_data.get('firstName', instance.firstName)
#         instance.otherName = validated_data.get('otherName', instance.otherName)
#         instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
#         instance.address = validated_data.get('address', instance.address)
#         instance.save()

