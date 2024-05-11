from django.urls import path, include
from rest_framework import routers
from absensi import views

router = routers.DefaultRouter()
router.register(r'siswa', views.SiswaViewSet)
router.register(r'kelas', views.KelasViewSet)
router.register(r'absensi', views.AbsensiViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
