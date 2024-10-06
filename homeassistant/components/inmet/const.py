"""Define constants for the InMet integration."""

from datetime import timedelta

from homeassistant.const import Platform

DOMAIN = "inmet"

PLATFORMS = [Platform.GEO_LOCATION, Platform.SENSOR]

FEED = "feed"

CONF_CATEGORIES = "categories"

DEFAULT_ICON = "mdi:alert"
DEFAULT_RADIUS = 500.0
DEFAULT_SCAN_INTERVAL = timedelta(minutes=5)
