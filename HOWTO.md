# How To Install and Operate

## Solution Components

Today, Project Brahma is comprised of two major componest; a CLI front-end,
and a SaaS back-end.  

The [Brahma CLI](./cli) component is written in Python. Python was chosen
because Brahma leverages the ACI Cobra SDK to read and apply configuration
to ACI environments. Python made it extremely simply to integrate the components
together. The brahma-cli also uses ArgParse, so it can be used much like many
of your favorite CLI's from other vendors (AWS as an example).

The [Brahma SaaS](./server) back-end is written in Angular (Javascript) and
served out via NodeJS. Brahma also uses the Cisco-UI kit to skin the
dashboard so that it looks and feels like many other Cisco UI's. Angular
made rapid development a snap as the Angular CLI can quickly build out
skeleton framework in a single command, as well as expand with additional
components & services in a similar fashion. NodeJS enables a simple API
interface for both the brahma-cli as well as the internal web services to
communicate.

All data is stored in a MongoDB database that is running in a Docker container.
Since Brahma is dealing with JSON formats and API calls, a document DB such as
MongoDB was the ideal choice. Not to mention the phenomenal support & integration
with NodeJS.

A fully containerized SaaS option (via docker-compose) has been provided but,
for historical reasons, is only useful within Cisco (hardcoded DNS site names).
Pull requests to make the production container deployment generally accessible
are welcome!

## Prerequisites

- Docker 18.x (or higher)
- Docker-Compose 1.25.x (or higher)
- Node 8.x (or higher)
- Angular CLI 7.x (or higher)
- Python 3.x
- ACI Cobra SDK (https://&lt;apic&gt;/cobra/_downloads/)

## Installation

### Server

(If you don't want to mess with building node.js and its dependencies,
check out the [Vagrant](./vagrant/README.md) approach.  Only this server
section can be skipped with the Vagrant approach.  You still need the CLI
sections below.)

```bash
git clone https://github.com/DCMattyG/brahma-project.git  
cd brahma-project  

npm install -g @angular/cli
npm install

pushd server
npm install
popd

sudo docker volume create mongo_data
sudo docker volume create mongo_config
./brahma-server.sh --dev
```

### CLI environment

```bash
virtualenv -p python3 venv
source venv/bin/activate
pushd brahma-project/cli
python3 setup.py install
popd
```

Install the Cobra SDK and ACI Models (downloaded from APIC):

```bash
pip install acicobra-4.2*.whl acimodel-4.2*.whl
```

### Environment Variables for the SaaS API

```bash
export BRAHMA_URL=&lt;url&gt; (e.g. localhost)  
export BRAHMA_PORT=&lt;port&gt; (e.g. 3000)  
```

## CLI Usage (after server below is operational)

1. Run 'brahma-cli -n' (create a new Brahma token)
2. Navigate to local running SaaS service and paste in your token (e.g. http://localhost:4200)
  - Note: the web server for Brahma "dev" deployments as instructed above runs on port 4200.
  - The API service (referenced by the CLI environment vars) is running in parallel on port 3000.
3. Throw your config settings into the wizard and save
4. Run 'brahma-cli -a' to apply the settings to ACI
5. Done!

## Documentation

- [ACI Cobra SDK](https://github.com/datacenter/cobra) and [Documentation](https://cobra.readthedocs.io/en/latest/)
- [ACI Policy Model](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/policy-model-guide/b-Cisco-ACI-Policy-Model-Guide.html)
- [ACI Management Information Model 4.2](https://developer.cisco.com/site/apic-mim-ref-api/?version=4.2(1))
