import openrouteservice

coords = ((8.34234,48.23424),(8.34423,48.26424))
mk="5b3ce3597851110001cf6248b092059e58f0474c88618af7252a3db9"
client = openrouteservice.Client(key=mk) # Specify your personal API key
routes = client.directions(coords, profile='wheelchair', optimize_waypoints=True)

print(routes)
