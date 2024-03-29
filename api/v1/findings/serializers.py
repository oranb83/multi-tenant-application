from rest_framework import serializers
from typing import Dict, Any

from api.exceptions import DuplicatedExternalIdException
from api.models.resources.models import Resource
from api.models.findings.models import Finding
from api.models.tenants.models import Tenant


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('unique_id', 'name', 'cloud_account')


class AddNewFindingSerializer(serializers.ModelSerializer):
    """
    Serializer for adding a new finding.

    This serializer is used to validate and create a new finding object.
    """
    resource = ResourceSerializer()

    class Meta:
        model = Finding
        fields = (
            'external_id', 'type', 'title', 'severity', 'created_at', 'sensor', 'resource'
        )

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate the data before creating a new finding.

        @raises DuplicatedExternalIdException: If a finding with the same external ID already exists for the tenant.
        """
        tenant_id = self.context['request'].parser_context['kwargs']['id']
        external_id = data.get('external_id')
        if Finding.objects.filter(external_id=external_id, resource__tenant=tenant_id).exists():
            raise DuplicatedExternalIdException(
                {"error": "Finding with this external ID already exists for this tenant"}
            )

        return data

    def create(self, validated_data: Dict[str, Any]) -> Finding:
        """
        Create a new finding object.
        """
        tenant_id = self.context['request'].parser_context['kwargs']['id']
        # Check if the tenant already exists or create a new one.
        tenant_instance, _ = Tenant.objects.get_or_create(id=tenant_id)

        resource_data = validated_data.pop('resource')
        unique_id = resource_data['unique_id']

        # Try to retrieve an existing Resource instance.
        resource_instance, _ = Resource.objects.get_or_create(
            unique_id=unique_id, tenant=tenant_instance, defaults=resource_data
        )

        finding = Finding.objects.create(
            resource=resource_instance,
            **validated_data
        )

        return finding


class FindingListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing findings.

    This serializer formats the response for listing findings.
    """
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
