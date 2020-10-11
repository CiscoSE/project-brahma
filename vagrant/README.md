# Vagrant alternative for API and Web service

Yes, yes. This could have been done in a container too. However,
we had already built the "production" instance (with its hardcode
DNS name pointing to the API service... oops) as a container and
it was just easier creating a separate mechanism.

## Requirements

- Vagrant
- Virtualbox
- ACI Model and Cobra files from ACI APIC

## Instructions

- Copy the ACI Cobra and Model files to this directory
- **vagrant up** to download image, boot VM, and configure VM
- **vagrant ssh** into the running VM
- **source brahma-python/bin/activate** to activate the Python virtual environment
- **cd project-brahma && bash ./brahma-server.sh --vbox** to run the web service

## Outcome

- API Service running on port 3000 (passed through to localhost:3000)
- Brahma Web Service running on port 4200 (passed through to localhost:4200)
