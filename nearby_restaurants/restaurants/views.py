from googleplaces import GooglePlaces, types, lang
from rest_framework.views import APIView
from rest_framework.response import Response

API_KEY = 'AIzaSyAHZ3on1TCBBkEIXCB_-XVjGiCRJinU73U'

class NearRest(APIView):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            google_places = GooglePlaces(API_KEY)
            query_result = google_places.nearby_search(location='banglore', keyword='RESTAURANT',
            radius=20000, types=[types.TYPE_RESTAURANT], lat_lng={'lat': '12.975686', 'lng': '77.578426'})

            if query_result.has_attributions:
                print(query_result.html_attributions)

            place_names = []
            r_ratings = []
            r_types = []
            r_vicinity = []
            
            for place in query_result.places: # fetch relevent data 
                place_names.append(place.name)
                r_ratings.append(place.rating)
                r_types.append(place.types)
                r_vicinity.append(place.vicinity)
                
            final_result = [] # all the mapped data
            
            for i in zip(place_names, r_ratings, r_types, r_vicinity): #map all information with relevent data
                final_result.append(i)

        return Response(final_result)
