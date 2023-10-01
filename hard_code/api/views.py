from django.db.models import Count, Sum
from rest_framework import generics
from rest_framework.response import Response

from api.serializers import (ProductSerializer, UserProductAccessSerializer,
                             LessonSerializer, LessonViewSerializer)
from product.models import Product, UserProductAccess, Lesson, LessonView


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserProductAccessList(generics.ListCreateAPIView):
    queryset = UserProductAccess.objects.all()
    serializer_class = UserProductAccessSerializer

class LessonList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonViewList(generics.ListCreateAPIView):
    queryset = LessonView.objects.all()
    serializer_class = LessonViewSerializer


class UserLessonsList(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        # Получите список уроков, которые доступны пользователю с указанным user_id
        # Это может потребовать запроса к моделям Lesson и LessonView, чтобы определить доступные уроки
        # и их статус (просмотрено/не просмотрено) для данного пользователя.
        # Затем верните список уроков в формате JSON.


class ProductLessonsList(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user_id = self.request.user.id  # Получите идентификатор текущего пользователя (предполагается, что пользователь аутентифицирован)
        product_id = self.kwargs['product_id']
        # Получите список уроков, которые доступны пользователю с указанным user_id
        # и которые связаны с продуктом с указанным product_id.
        # Это может потребовать запроса к моделям Lesson, UserProductAccess и LessonView.
        # Затем верните список уроков в формате JSON.


class ProductStats(generics.ListAPIView):
    def list(self, request):
        # Вычислите статистику по продуктам, используя агрегирующие функции Django ORM.
        # Пример вычисления статистики: количество просмотренных уроков, общее время просмотра, количество учеников и процент приобретения продукта.
        product_stats = Product.objects.annotate(
            num_lessons=Count('lesson'),
            total_view_time=Sum('lesson__lessonview__view_time_seconds'),
            num_students=Count('userproductaccess__user', distinct=True),
            purchase_percentage=Count('userproductaccess') * 100 / Count('user', distinct=True)
        ).values('id', 'name', 'num_lessons', 'total_view_time', 'num_students', 'purchase_percentage')

        return Response(product_stats)

