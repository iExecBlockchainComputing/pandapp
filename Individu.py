# This list show be managed on chain, as application has to registered.
Applist=("heatmap", "social_distance")

class Individu():
    def __init__(self, _status, _geohashes ):
        self.status = _status
#        self.app_heatmap=_app_heatmap
#        self.app_socialdistance=_app_socialdistance
        self.geohashes = _geohashes  # list of tuples

    def __str__(self):
        return "[status %s | %s" % (self.status, self.geohashes)