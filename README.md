# Hot-Schedules-Fixer
My job used Hot Schedules for all scheduling. It had this great feature that allowed it to sync my schedule to my google calander. This worked great but there was one issue with it that bugged me. It only set the event in my google calander to 5 minutes long. This messed up the visualization of how much time an event takes up in google calanders so this program attempts to fix that.

It gets the next 30 events in the users google calander. It then checks if anywhere in the title of the event contains the word Hotschedules. If it does, it adds 5 hours to the time for the shift, with a special clause for the weekends as my job had 2 possilbe shifts instead of just one.

The updatehs.py file was then run every wednesday at 00:00 as when the schedule came out was unpredictalbe, and the schedule week started on Wednesdays 
