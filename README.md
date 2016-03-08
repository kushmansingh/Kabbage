**Website:**
https://kabbagequal.herokuapp.com

**Running Instructions**
Assuming you have [Python 2.7.*](https://www.python.org/downloads/) installed and [npm](https://www.npmjs.com/package/npm)
- Clone this repo
- Navigate to inside the repo
- Install the python dependencies with the command below (pip should come with python by default)
    `pip install -r requirements.txt`
- Navigate to
    `cd PATH_TO_REPO/kabbage/static`
- Install Bower if you don't have it already with
    `npm install bower`
- Install Bower packages with
    `bower install`
- Navigate back to the top level in the repo ie.
    `cd PATH_TO_REPO/`
- Run the following command
    `python main.py`
- You're all set! The application should be running on `localhost:5000`. If you would like to change ports, set your environment variable `PORT` to one of your liking

**Limitations:**

- CSRF not implemented
- No standard exception throwing class
- Form is not dynamically rendered based on backend
- 'Secret' keys are hardcoded into the project instead of being pulled from environment variables
- Nginx should be used to serve static assets
- JS is not namespaced (due to size of project)
