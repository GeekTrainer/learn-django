To upload our app to Azure services we need to first have a local Git repository. With the previous steps a local git repository was already created, but to upload the project to Azure we will now need to initialize it. 

## Initializing Git local repository

1. Go inside the **adoptadog** root folder where you are able to see the **requirements.txt** file, and enter the below command in the command line.

```bash
git init
```

Now that the folder has been initialized we can begin the process to upload the Django project.

## Django project edits for Azure

While our project executes properly on the local environment there are a few more tasks to complete before it will function properly on Azure.

1. First go back to the **adoptadog** project folder to find the **settings.py** file. 

2. In the file find the section `ALLOWED_HOSTS` and add a `*` in the brackets under the comment `# [TODO] Add * to Allowed Hosts to allow site`. 

```python
# [TODO] Add '*' to Allowed Hosts to allow site
ALLOWED_HOSTS = ['*']
```

Since we have now added a `['*']` it will allow Azure as a host. While adding `['*']` will work for this example it should not be used for projects in production and the final URL for the app should be entered.

3. Next go to the **settings.py** file.

4. Starting at the top of the file add code under the comment `# [TODO] Import os` and at the bottom of the file add code under comment `# [TODO] Add static root`

```python
from pathlib import Path
# [TODO] Import os
import os

# [TODO] Add static root
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

Since there are static files within the project a `STATIC_ROOT` needs to be set. When uploading the project to Azure you will notice Django will run a command called `collectstatic`. By adding this line it will tell Django to collect all of the static files in the `STATIC_ROOT` folder.

The last task in editing our Django files is to change the URLpatterns in the project **urls.py** file.

5. Before editing make sure you are in the project **urls.py** file and paste the below code under comment `# [TODO]: Add the needed imports for the Azure urlpatterns` and `# [TODO] Copy over existing urlpatterns with new urlpatterns for Azure`.

```python
# [TODO]: Add the needed imports for the Azure urlpatterns
from django.conf.urls import url
from dog_shelters import views as appviews

# [TODO] Copy over existing urlpatterns with new urlpatterns for Azure
urlpatterns = [
url(r'^$', include('dog_shelters.urls')),
url(r'shelter_spotlight', appviews.spotlight),
url(r'shelter_list', appviews.ShelterList.as_view()),
url(r'contact', appviews.contactForm),
url(r'crispycontact', appviews.crispycontactForm),
url(r'shelter_form', appviews.CreateShelter.as_view()),
url(r'thank_you', appviews.thankyou),
url(r'shelter_form', appviews.CreateShelter.as_view()),
url(r'(?P<pk>\d+)/update', appviews.UpdateShelter.as_view()),
url(r'(?P<pk>\d+)/delete', appviews.DeleteShelter.as_view()),
url(r'(?P<pk>\d+)', appviews.ShelterDetail.as_view()),
url(r'update_delete_shelters', appviews.ShelterEdits.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Now that the final touches to the project have been completed it is time to push our project to Azure. 

## Deploying project

Now that we have the **Git Clone Uri** from Azure we need to add the remote connection to the local repository. 

1. Navigate to the folder that was initialized for your local Git repository and enter the below command in the command line.

```bash
git remote add azure https://dogsforadoptionproject.scm.azurewebsites.net:443/dogsforadoptionproject.git
```

2. When completed run the below commands from the command line in order to stage, commit and finally push the files to the Azure repository.

```bash
git add -A
git commit -m "Initial Commit"
git push azure master
```

The first line adds all of the files that were added to the local repository, the second commits all of the files, and the last line finally pushes all of the files to Azure.

After you have pushed the changes you can view your progress in the **Deployment Center** of Azure. Once the upload has completed go to the previously opened browser, refresh the page and you should now see the homepage of the app.