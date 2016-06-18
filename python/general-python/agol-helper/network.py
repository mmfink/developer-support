from agol import AGOL

class networkService(AGOL):
    """Network Service object, that inherits properties from the AGOL object."""

    def routeNetwork(self):
        """
        This shows how to do a network solve using ArcGIS Online Routing services
        http://resources.arcgis.com/en/help/arcgis-rest-api/index.html#/Solve_Route/02r3000000q3000000/
        """
        url = "https://route.arcgis.com/arcgis/rest/services/World/Route/NAServer/Route_World/solve"
        data = {'token': self.token,
                'f': 'json',
                'stops': {
                            "features"  : [
                                {
                                    "geometry" : {"x" : -122.4079, "y" : 37.78356},
                                    "attributes" : {"Name" : "From", "RouteName" : "Route A"}
                                },
                                {
                                    "geometry" : {"x" : -122.404, "y" : 37.782},
                                    "attributes" : {"Name" : "To", "RouteName" : "Route A"}
                                }
                            ]
                        },
                'barriers': "",
                'polylineBarriers' : "",
                'polygonBarriers' : "",
                'outSR' : 4326,
                'ignoreInvalidLocations' : "true",
                'accumulateAttributeNames' : "",
                'travelMode' : {"distanceAttributeName":"Miles",
                    "description":"Models the movement of cars and other similar small automobiles, such as pickup trucks, and finds solutions that optimize travel time. Travel obeys one-way roads, avoids illegal turns, and follows other rules that are specific to cars. Dynamic travel speeds based on traffic are used where it is available when you specify a start time.",
                    "impedanceAttributeName":"TravelTime",
                    "simplificationToleranceUnits":"esriMeters",
                    "uturnAtJunctions":"esriNFSBAtDeadEndsAndIntersections",
                    "useHierarchy":"true",
                    "name":"Driving Time",
                    "timeAttributeName":"TravelTime",
                    "restrictionAttributeNames":
                        ["Avoid Unpaved Roads",
                        "Avoid Private Roads","Driving an Automobile",
                        "Through Traffic Prohibited",
                        "Roads Under Construction Prohibited",
                        "Avoid Gates","Avoid Express Lanes","Avoid Carpool Roads"],
                    "type":"AUTOMOBILE",
                    "id":"FEgifRtFndKNcJMJ",
                    "attributeParameterValues":[{
                        "parameterName":"Restriction Usage",
                        "attributeName":"Avoid Unpaved Roads",
                        "value":"AVOID_HIGH"},
                    {"parameterName":"Restriction Usage",
                        "attributeName":"Avoid Private Roads",
                        "value":"AVOID_MEDIUM"},
                    {"parameterName":"Restriction Usage",
                        "attributeName":"Driving an Automobile",
                        "value":"PROHIBITED"},
                    {"parameterName":"Restriction Usage",
                        "attributeName":"Through Traffic Prohibited",
                        "value":"AVOID_HIGH"},
                    {"parameterName":"Restriction Usage",
                        "attributeName":"Roads Under Construction Prohibited",
                        "value":"PROHIBITED"},
                    {"parameterName":"Restriction Usage",
                        "attributeName":"Avoid Gates",
                        "value":"AVOID_MEDIUM"},
                    {"parameterName":"Restriction Usage",
                        "attributeName":"Avoid Express Lanes",
                        "value":"PROHIBITED"},
                    {"parameterName":"Restriction Usage",
                        "attributeName":"Avoid Carpool Roads",
                        "value":"PROHIBITED"}],
                    "simplificationTolerance":10},
                'restrictionAttributeNames' : "",
                'attributeParameterValues' : "",
                'restrictUTurns' : "esriNFSBAllowBacktrack",
                'useHierarchy' : "true",
                'returnDirections' : "true",
                'returnRoutes' : "true",
                'returnStops' : "false",
                'returnBarriers' : "false",
                'directionsStyleName' : "NA Desktop",
                'startTime' : 1227663551096,
                'directionsLengthUnits' : "esriNAUMiles" }
        jsonResponse = self.sendRequest(url, data)
        return jsonResponse
