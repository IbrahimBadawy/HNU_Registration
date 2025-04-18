from django.urls import path
from .views import *
from .views import (
    ApplicationPDFView,
    RegisterView,
    check_student_access,
    check_admin_access,
    admin_summary_report,
)


urlpatterns = [
    path(
        "application/", ApplicationRetrieveUpdate.as_view(), name="application-detail"
    ),
    path("upload/", DocumentUploadView.as_view(), name="upload-document"),
    path("payment/", PaymentView.as_view(), name="payment"),
    path(
        "admin/applications/",
        ApplicationListAdmin.as_view(),
        name="admin-application-list",
    ),
    path(
        "admin/application/<int:pk>/",
        ApplicationDetailAdmin.as_view(),
        name="admin-application-detail",
    ),
    path(
        "admin/review/",
        ApplicationReviewAdmin.as_view(),
        name="admin-application-review",
    ),
]


urlpatterns += [
    path("admin/pdf/<int:pk>/", ApplicationPDFView.as_view(), name="application-pdf"),
    path("register/", RegisterView.as_view(), name="user-register"),
    path("check/student/", check_student_access, name="check-student-access"),
    path("check/admin/", check_admin_access, name="check-admin-access"),
    path("admin/report/", admin_summary_report, name="admin-report"),
]
