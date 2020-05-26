#!/usr/bin/env bash

source Venv/bin/activate
export DATASTORE_DATASET=cloud-ndb-test
export DATASTORE_EMULATOR_HOST_PATH=localhost:8089/datastore
export DATASTORE_EMULATOR_HOST=localhost:8089
export DATASTORE_HOST=http://localhost:8089
export DATASTORE_PROJECT_ID=cloud-ndb-test

RESULT=`curl -s http://localhost:8089`
if [ "$RESULT" = "Ok" ]; then
  python test.py
else
  echo "Datastore emulator not detected on localhost:8089. Try running 'gcloud beta emulators datastore start --no-store-on-disk --consistency=1.0 --host-port=localhost:8089' in another terminal first."
fi
