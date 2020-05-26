# cloud-ndb-test

## Steps to run

1. Create a virtualenv if you don't already have one and activate it
2. `$ pip install -r requirements.txt`
3. In terminal one, run `$ gcloud beta emulators datastore start --no-store-on-disk --consistency=1.0 --host-port=localhost:8089 --project=cloud-ndb-test`
4. In terminal two, run `$ ./demo.sh`
