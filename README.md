## Task Description

Using Python, please create the application which adds/modifies/removes user account.

Using Pytest, please create test cases which will test the application.

Please also create a Dockerfile and provide instructions for the user on how to run tests from docker container
Details:
1. For the application operations (REST calls) please use https://gorest.co.in/


## How to run tests from Docker

* Install **Docker**

[Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

[Create a Unix group called `docker` and add user to it.](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)

* Clone the project

Before, make sure there is an [SSH key](https://gitlab.com/profile/keys) in your profile in Gitlab.

`git clone git@github.com:Rybintseva/gl_test_task.git`

* Run tests

`bash run_docker.sh`

**Note:** Command should be run from the **project root folder**.

* Test Report

Open the **report.html** file to see the report.