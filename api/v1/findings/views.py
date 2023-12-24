from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema

from api.models.findings.models import Finding
from .serializers import FindingListSerializer, AddNewFindingSerializer


class FindingListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating findings for a specific tenant.
    """
    def get_queryset(self):
        tenant_id = self.kwargs.get('id')
        return Finding.objects.filter(tenant=tenant_id)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddNewFindingSerializer

        return FindingListSerializer

    @swagger_auto_schema(
        operation_summary='List Findings for a specific Tenant',
        operation_description='This endpoint allows listing findings for a specific tenant.'
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            201: AddNewFindingSerializer(),
            # I'm allowing myself a short cut by not using a serializer for the error response.
            422: 'DuplicatedExternalIdException'
        },
        operation_summary='Create a Finding for a specific Tenant',
        operation_description='This endpoint allows creating a finding for a specific tenant.'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
