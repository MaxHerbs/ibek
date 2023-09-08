# EPICS IOC Startup Script generated by https://github.com/epics-containers/ibek

cd "/repos/epics/ioc"

epicsEnvSet REF_OBJECT_NAME AsynPort1
epicsEnvSet REF_OBJECT_NAME AsynPort2

dbLoadDatabase dbd/ioc.dbd
ioc_registerRecordDeviceDriver pdbbase


# TestValues testValue
TestValues AsynPort1.127.0.0.1
TestValues AsynPort2.10.0.0.2

# ExampleTestFunction asynPortIP name port value
ExampleTestFunction 10.0.0.2 Consumer of another port AsynPort2 AsynPort2.10.0.0.2
ExampleTestFunction 10.0.0.2 Another Consumer of the 2nd port AsynPort2 AsynPort2.10.0.0.2

dbLoadRecords /tmp/ioc.db
iocInit

