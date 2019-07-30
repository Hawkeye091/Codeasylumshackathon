from django.contrib import admin
from .models import Clgsdb
from .models import Clgtagsdb
from .models import Detailsdb
from .models import Eventsdb
from .models import Followsdb
from .models import Tagsdb

# Register your models here.
admin.site.register(Clgsdb)
admin.site.register(Clgtagsdb)
admin.site.register(Detailsdb)
admin.site.register(Eventsdb)
admin.site.register(Followsdb)
admin.site.register(Tagsdb)