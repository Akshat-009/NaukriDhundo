# Naukri Dhundo

## Motive
Due to COVID-19 Outbreak the entire is shook and many people lost there Jobs as well . Since Social Distancing is the only way to stop this virus almost all offline activities has been stopped thus I have created a Job finding Portal where Job seeker can lookup for jobs and Employers can hire new Candidates without any Physical Contact.Job seekers can here look up for jobs and upload there resume instead of sending a physical one to the employer.


## Key Features

- All the Users have to Create an account on the Website .
- A Verification link will be sent to their email upon clicking which they can verify their account .
- In case the email wasn't sent correctly or is not sent at all . users can click on resend button so that another email can be sent.
- All the users registered are redirected to another page where they'll have to fill up other related details like there name and either they are an employer or job seeker.
- Upon successful creation of profile the users will be directed to different pages respectively .
- The Employer's are directed to Employer's Dashboard.
- The Job Seeker's are directed to a different Dashboard.
- The Employers Dashboard has a NavBar where in there are links to post a job and to see the applicants who have applied for the job.
- The Job seeker's section on the other hand has just a search bar where he can search for a job and in the other see applications which he has filled.
- After the Job is posted the Job seeker can apply for the Job by simply filling up a form and uploading the resume over there.
- On the Employer's side a page similar to applicant's page is opened but with three additional buttons namely Hire , Reject , Invite for interview and all already filled up form by the applicant and with a link to download applicant's Resume .
- Integration of Zoom Oauth Service .
- Now coming to the Chat Tab  the employer can directly arrange an zoom meeting by filling up a form for interview , the start url is only shared with employer whereas join url   can be seen by both employer and employee.
-The Chat Tab can also be used for communication of other queries as well.

### Description of various Django Apps:

## Dashboard:
- This is the Job Seeker's Dashboard houses all the views and models for Job Seeker

## Authentication:
- This is the auth app of NaukriDhundo it is a reusable app , can be hosted to pypi for authenticaion in diffrent app
- Uses an Email Verification Method to Verify the account and register it in DB

## Employer:
- This is the Employer's section of the NaukriDhundo 

## Jobs:
- This is where all the jobs related logic is written

## helpers.py:
- A python file where helper functions are written


#### ** DISCLAIMER **
This is an incomplete project . Due to last min changes in my GSOC plan and some issues in my earlier decided to submit project. I couldn't complete this one . Due to some Routing errors and an incomplete Front End I could'nt check all the features wheather they are working are or not thus could'nt do proper debugging . But as people say IMG is a place where all web enthusiasts and curious minds are welcomed I decided to submit it . I have made several nice and interesting projects in my past (please check my portfolio once) which were completed within the deadline , but because of time crunch which mainly happened due to some weird AJAX errors in my earlier project and sudden change of organization in GSOC I didn't get the time to complete this one . 

I have added all the features that I have listed above , ie I have written the code as well as the logic for all the above features but because of time crunch I didn't had the time to debug it and test them. The issues are mainly because of improper routing and an incomplete front end. The indiviual Django Apps are working fine but the app as a whole has routing issues in it .

#### How to run the app 

```shell
open terminal and type 
git clone https://github.com/Akshat-009/NaukriDhundo.git
```
```shell
 cd naukridhundo
 pip install -r requirements.txt
 python manage.py runserver
```

Start your Browser and go to 

http://127.0.0.1:8000/auth/register

after this go to 
http://127.0.0.1:8000/auth/login

after this complete registration details and you'll be landing on the respective dashboard
