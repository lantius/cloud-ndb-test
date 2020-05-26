#!/usr/bin/env bash

# gcloud beta emulators datastore start --project=cloud-ndb-test \
#                                       --no-store-on-disk \
#                                       --consistency=1.0 \
#                                       --host-port=localhost:8089 \
#                                       < /dev/null >& /dev/null &
# dev_appserver.py \
# --support_datastore_emulator=true \
# --enable_host_checking=false \
# --application=cloud-ndb-test \
# app.yaml

source Venv/bin/activate
export DATASTORE_DATASET=cloud-ndb-test
export DATASTORE_EMULATOR_HOST_PATH=localhost:8089/datastore
export DATASTORE_EMULATOR_HOST=localhost:8089
export DATASTORE_HOST=http://localhost:8089
export DATASTORE_PROJECT_ID=cloud-ndb-test
export DATASTORE_APP_ID=cloud-ndb-test

RESULT=`curl -s http://localhost:8089`
if [ "$RESULT" = "Ok" ]; then
  # python cloudndb.py
  python appenginendb.py
else
  echo "Datastore emulator not detected on localhost:8089. Try running 'gcloud beta emulators datastore start --no-store-on-disk --consistency=1.0 --host-port=localhost:8089' in another terminal first."
fi
