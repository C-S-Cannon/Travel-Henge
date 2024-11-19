import astropy.coordinates as coord
from astropy.time import Time
import astropy.units as u


loc = coord.EarthLocation(lon=0.1 * u.deg,
                         lat=51.5 * u.deg)
now = Time.now()

altaz = coord.AltAz(location=loc, obstime=now)
sun = coord.get_sun(now)

print(sun.transform_to(altaz).alt)