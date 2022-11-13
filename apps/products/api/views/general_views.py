from apps.base.api import GeneralListApiView
from apps.products.api.serializers.genaral_serializers import MeasureUnitSerializer, IndicatorSerializar,CategoryProductSerializer


class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer


class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializar



class CategoryProdutsListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer
