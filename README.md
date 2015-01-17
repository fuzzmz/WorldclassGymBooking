# WorldclassGymBooking
This script is used to perform gym class bookings for WorldClass Romania. It was written as a quick and dirty method of avoiding missing a class because you forgot to book it.

The following variables must be updated in the `make_res.py` file:

1. `memberemail` must correspond to the email address used for the online account
2. `memberpin` must be the password of your WorldClass account
3. `classid` is the class you want to book. It can be found by going to `http://www.worldclass.ro/health-academy-at-the-grand/schedule` and looking at the page source.
4. `centerid` is the WorldClass gym you want to make the reservation at. The ID can be found on the schedule page for your particular gym.

I know there's a lot of things to update by hand, but this was used for a single class that got instantly booked so the variables didn't change that often, if at all :)
