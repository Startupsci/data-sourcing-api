"""Data Sourcing API to search, define, and prepare datasets for data science and machine learning projects."""
import endpoints
from protorpc import message_types
from protorpc import remote

from models import AboutMessage
from models import MetaMiniMessage
from models import MetaMessage

@endpoints.api(name='dataSourcing', version='v1')
class DataSourcing(remote.Service):
    """Data Sourcing API v1."""

    @endpoints.method(message_types.VoidMessage, AboutMessage,
                      path = "about", http_method='GET', name = "about")
    def about(self, request):
        return AboutMessage(about="API to search, define, and prepare datasets for data science and machine learning projects.")

    @endpoints.method(MetaMiniMessage, MetaMessage,
                      path = "meta/summary", http_method='POST',
                      name = "meta.summary")
    def meta_summary(self, request):
        return MetaMessage(datasetName = request.datasetName,
                           sourceUrl = request.sourceUrl)

api = endpoints.api_server([DataSourcing])
