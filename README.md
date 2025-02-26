This repo is meant to act as a general template for starting up a data engineering project with technologies including:

1. Astronomer
2. GitHub
3. Snowflake
4. dbt

This can be expanded further to include technologies like Terraform and Google Cloud Platform.

Two important notes:

1. To develop locally, you will need a .env file to store credentials for dbt to use. As you can see the profiles.yml in the dbt folder uses environment variables for the connection to be made with Snowflake. However, a Snowflake connection is used in deployment on Astronomer, so that functions independently when the dbt dag is kicked off. Here is what the .env file should look like. Put this in the root directory of the repo an then all subsequent dbt commands should use: uv run --env-file ../.env dbt <command>

export DBT_ENV_SECRET_SF_PASS=<your sf password>
export DBT_ENV_SECRET_SF_ACCOUNT=<your sf account url>
export DBT_ENV_SECRET_SF_USER=<your sf user name>
export DBT_ENV_SECRET_SF_DATABASE=<your sf database>

2. The Astronomer instance is also linked with this repo to automate building the Docker image that Astronomer uses to host our Airflow instance. It is set so that every time a PR is merged, the image will be updated and build again. 

Will add more to this as I build out project...