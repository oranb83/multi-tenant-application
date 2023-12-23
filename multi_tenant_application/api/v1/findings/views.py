from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ...models.findings.models import Finding
from .serializers import FindingListSerializer, AddNewFindingSerializer


class FindingListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating findings for a specific tenant.
    """
    serializer_class = FindingListSerializer

    def get_queryset(self):
        tenant_id = self.kwargs.get('tenant_id')
        return Finding.objects.filter(tenant_id=tenant_id)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('tenant_id', openapi.IN_PATH, description="Tenant ID",
                              type=openapi.TYPE_STRING)
        ],
        responses={
            201: AddNewFindingSerializer(),
            422: "Validation error"
        },
        operation_summary="Create a Finding for a single Tenant",
        operation_description="This endpoint allows listing and creating findings for a specific tenant."
    )
    def post(self, request, *args, **kwargs):
        """
        View for creating findings for a specific tenant.
        """
        return self.create(request, *args, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('tenant_id', openapi.IN_PATH, description="Tenant ID",
                              type=openapi.TYPE_STRING)
        ],
        responses={
            200: FindingListSerializer(many=True),
            422: "Validation error"
        },
        operation_summary="List Findings for a single Tenant",
        operation_description="This endpoint allows retrieving findings for a specific tenant."
    )
    def get(self, request, *args, **kwargs):
        """
        View for listing and creating findings for a specific tenant.
        """
        return self.list(request, *args, **kwargs)
