from protorpc import messages
from google.appengine.ext import ndb

class AboutMessage(messages.Message):
    """String that stores an about message."""
    about = messages.StringField(1)

class Meta(ndb.Model):
    """Object storing metadata about a dataset"""
    datasetName = ndb.StringProperty()
    sourceUrl = ndb.StringProperty()
    origin = ndb.StringProperty(default='UNKNOWN')
    domain = ndb.StringProperty(default='UNKNOWN')
    sampleCount = ndb.IntegerProperty()
    featureCount = ndb.IntegerProperty()
    datasetFormat = ndb.StringProperty(default='UNKNOWN')
    license = ndb.StringProperty(default='UNKNOWN')
    cloud = ndb.StringProperty(default='UNKNOWN')
    structure = ndb.StringProperty(default='UNKNOWN')
    size = ndb.StringProperty(default='UNKNOWN')

class MetaMiniMessage(messages.Message):
    """Object storing minimal metadata about a dataset"""
    datasetName = messages.StringField(1)
    sourceUrl = messages.StringField(2)

class MetaMessage(messages.Message):
    """Object storing metadata about a dataset"""
    datasetName = messages.StringField(1)
    sourceUrl = messages.StringField(2)
    about = messages.StringField(3)
    sampleCount = messages.IntegerField(4)
    featureCount = messages.IntegerField(5)
    datasetFormat = messages.EnumField('Format', 6)
    license = messages.EnumField('License', 7)
    cloud = messages.EnumField('Cloud', 8)
    structure = messages.EnumField('Structure', 9)
    size = messages.EnumField('Size', 10)
    origin = messages.StringField(11)
    domain = messages.StringField(12)

class Format(messages.Enum):
    """Format -- what format is data"""
    UNKNOWN = 1
    CSV = 2
    JSON = 3
    XML = 4
    GEOJSON = 5
    PDF = 6
    EXCEL = 7
    SQL_DB = 8
    NOSQL_DB = 9
    GRAPH_DB = 10
    IMAGE = 11
    AUDIO = 12
    VIDEO = 13
    KML = 14
    OTHER = 15

class License(messages.Enum):
    """License -- usage information"""
    UNKNOWN = 1
    PUBLIC = 2
    PAID = 3
    ACADEMIC = 4
    OTHER = 5

class Cloud(messages.Enum):
    """Cloud -- does data source originate on a specific Cloud"""
    UNKNOWN = 1
    ANY = 2
    AWS = 3
    GCP = 4
    AZURE = 5
    IBM = 6
    OTHER = 7

class Structure(messages.Enum):
    """Structure -- what is the nature of this dataset"""
    UNKNOWN = 1
    TABULAR = 2
    TIMESERIES = 3
    MATRIX = 4
    UNSTRUCTURED = 5
    HIERARCHICAL = 6
    GRAPH = 7
    BINARY = 8
    OTHER = 9

class Size(messages.Enum):
    """Size -- uncompressed storage size for the data"""
    UNKNOWN = 1
    MB = 2
    GB = 3
    TB = 4
