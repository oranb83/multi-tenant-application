from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.v1.resource.models import Resource
from .models import Finding


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('unique_id', 'name', 'cloud_account')


class AddNewFindingSerializer(serializers.ModelSerializer):
    resource = ResourceSerializer()

    class Meta:
        model = Finding
        fields = (
            'external_id', 'type', 'title', 'severity', 'created_at', 'sensor', 'resource'
        )

    def validate(self, data):
        tenant_id = self.context['request'].parser_context['kwargs']['tenant_id']
        external_id = data.get('external_id')

        # Check if external_id already exists for this tenant
        # Assumption: external_id is unique per tenant
        if Finding.objects.filter(external_id=external_id, tenant_id=tenant_id).exists():
            raise ValidationError(  # TODO: Add a custom exception that will return 422 instead of 400
                {"error": "Finding with this external ID already exists for this tenant"}
            )

        return data

    def create(self, validated_data):
        resource_data = validated_data.pop('resource')
        resource = Resource.objects.create(**resource_data)

        finding = Finding.objects.create(resource=resource, **validated_data)

        return finding


class FindingListSerializer(serializers.ModelSerializer):
    # The response is based on the findings examples
    id = serializers.ReadOnlyField(source='external_id')
    resource_id = serializers.CharField(source='resource.unique_id')
    resource_name = serializers.CharField(source='resource.name')
    account = serializers.CharField(source='resource.cloud_account')

    class Meta:
        model = Finding
        fields = (
            'id', 'type', 'title', 'severity', 'created_at', 'sensor', 'resource_id',
            'resource_name', 'account'
        )
