from django.db import models

# Property model for storing real estate listings
class Property(models.Model):
    """Model representing a property listing."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the title of the property."""
        return self.title
