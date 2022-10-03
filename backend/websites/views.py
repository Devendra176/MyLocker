from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from websites.models import WebsitesData
from websites.serializers import ActiveUserSerializer, WebsitesAddDataSerializers


class WebsitesDataView(generics.RetrieveUpdateAPIView):
    serializer_class = ActiveUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class WebsitesAddDataView(generics.CreateAPIView):
    queryset = WebsitesData.objects.all()
    serializer_class = WebsitesAddDataSerializers
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        kwargs["many"] = True
        return super(WebsitesAddDataView, self).get_serializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = WebsitesAddDataSerializers(data=data, many=True)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            breakpoint()
            return Response(serializer.data)
        return Response(serializer.errors)