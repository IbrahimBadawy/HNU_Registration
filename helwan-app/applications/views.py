from rest_framework import generics, permissions
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser

from django.template.loader import get_template

from django.http import HttpResponse
from django.template.loader import render_to_string

# from weasyprint import HTML

from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from django.http import HttpResponseForbidden
from xhtml2pdf import pisa

from .models import StudentApplication

User = get_user_model()


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not email or not password:
            return Response({"error": "كل الحقول مطلوبة"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "اسم المستخدم موجود بالفعل"}, status=400)

        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        return Response(
            {"message": "تم إنشاء الحساب بنجاح"}, status=status.HTTP_201_CREATED
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def check_student_access(request):
    if request.user.is_admin:
        return Response({"access": "denied"}, status=403)
    return Response({"access": "granted", "type": "student"})


@api_view(["GET"])
@permission_classes([IsAdminUser])
def check_admin_access(request):
    return Response({"access": "granted", "type": "admin"})


@api_view(["GET"])
@permission_classes([IsAdminUser])
def admin_summary_report(request):
    total = StudentApplication.objects.count()
    accepted = StudentApplication.objects.filter(status="accepted").count()
    rejected = StudentApplication.objects.filter(status="rejected").count()
    pending = StudentApplication.objects.filter(status="pending").count()

    return Response(
        {"total": total, "accepted": accepted, "rejected": rejected, "pending": pending}
    )


# class ApplicationPDFView(APIView):
#     permission_classes = [IsAdminUser]

#     def get(self, request, pk):
#         app = StudentApplication.objects.get(pk=pk)
#         html_string = render_to_string("pdf_template.html", {"application": app})
#         pdf_file = HTML(string=html_string).write_pdf()

#         response = HttpResponse(pdf_file, content_type="application/pdf")
#         response["Content-Disposition"] = (
#             f'attachment; filename="application_{app.id}.pdf"'
#         )
#         return response


class ApplicationPDFView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        application = StudentApplication.objects.get(pk=pk)
        template = get_template("pdf_template.html")
        html = template.render({"application": application})
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="application_{pk}.pdf"'

        pisa_status = pisa.CreatePDF(src=html, dest=response)
        if pisa_status.err:
            return HttpResponse("Error generating PDF", status=500)
        return response


class ApplicationRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.queryset.get(user=self.request.user)


class DocumentUploadView(generics.CreateAPIView):
    queryset = UploadedDocument.objects.all()
    serializer_class = UploadedDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class PaymentView(generics.RetrieveUpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.queryset.get(application__user=self.request.user)


class ApplicationListAdmin(generics.ListAPIView):
    serializer_class = StudentApplicationSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = StudentApplication.objects.all()
        college = self.request.query_params.get("college")
        status = self.request.query_params.get("status")
        if college:
            queryset = queryset.filter(desired_college=college)
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class ApplicationDetailAdmin(generics.RetrieveAPIView):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "pk"


class ApplicationReviewAdmin(generics.CreateAPIView):
    serializer_class = ApplicationReviewSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        review = serializer.save(reviewer=self.request.user)
        app = review.application
        app.status = review.status
        app.rejection_reason = (
            review.rejection_reason if review.status == "rejected" else ""
        )
        app.save()
