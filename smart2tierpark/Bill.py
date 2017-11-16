from .Platform import Platform
from django.utils import timezone

class Bill():
    def __init__(self,platform):
        self.start_time=platform.start_park
        self.endtime=timezone.now()
        self.pnum=platform.pnum
        self.totaltime=self.endtime-self.start_time
        ts=self.totaltime.seconds/3600
        self.totalcost=ts*50
