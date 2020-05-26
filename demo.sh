#!/usr/bin/env bash

source Venv/bin/activate
RESULT=`curl -s http://localhost:8089`
if [ "$RESULT" = "Ok" ]; then
  python test.py \
    --support_datastore_emulator=true \
    --enable_host_checking=false \
    --application=cloud-ndb-test \
    --env_var DATASTORE_DATASET=cloud-ndb-test \
    --env_var DATASTORE_EMULATOR_HOST_PATH=localhost:8089/datastore \
    --env_var DATASTORE_HOST=http://localhost:8089 \
    --env_var DATASTORE_PROJECT_ID=cloud-ndb-test \
    --project=cloud-ndb-test \
    app.yaml
else
  echo "Datastore emulator not detected on localhost:8089. Try running 'gcloud beta emulators datastore start --no-store-on-disk --consistency=1.0 --host-port=localhost:8089' in another terminal first."
fi
# dev_appserver.py app.yaml --enable_host_checking=false
# python test.py
