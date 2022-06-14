## url to hosted app
https://myblogarticles.herokuapp.com/

## address to admin dashboard
https://myblogarticles.herokuapp.com/admin
username: Dennis
password: Dennis0541673487

## Email 
During development mode i used personal email and password to login.
This isnt included in source code so can't replicate on local machine.
 However in the hosted site on Heroku email will work
as expected. 

## git hub repository 
https://github.com/Dennis-Asamoah/mir_media

## CI/CD 
CI with github actions
CD with heroku cmd

## Notes:
** In a more complex project , celery and redis would have been used to run 
the email sending at the backround. 'Email sending' is I/O and blocking, thus advisable
to run at backround(in a different python process)

** Also in a 'real project', application would have been hosted on an IAAS(aws) instead of 
a PAAS (in my case Heroku)

** Then again CI/CD would be done with action and  amazon codedeploy.

## Time Taken
It took me 11 hours to complete the entire project.

** 7 hours for coding
**4 hours for setting email, CI/CD , creating accounts and deploying on Heroku. 