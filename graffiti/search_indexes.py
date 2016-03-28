import datetime

from haystack import indexes
from taggit.models import Tag

class TagIndex(indexes.SearchIndex, indexes.Indexable):

  text = indexes.CharField(document=True, use_template=True)

  def get_model(self):
      return Tag

  def index_queryset(self, using=None):
      """Used when the entire index for model is updated."""
      return self.get_model().objects.all()
