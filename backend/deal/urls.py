from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('opportunity',OpportunityViewSet)
router.register('opportunity_documents',OpportunityDocumentViewSet)
router.register(r'proposal', ProposalViewSet, basename='proposal')

urlpatterns = router.urls
