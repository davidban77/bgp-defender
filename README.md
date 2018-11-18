# bgp-defender
Python application that analyses BGP table and alerts (at the moment) against hijacking

The project is focused on a python script to poll and detect for BGP anomalies in a device BGP table.

## How do I get started?


You can clone the project locally to start using it:
```
git clone https://github.com/davidban77/bgp-defender 
```
In principle this script will work on a BGP routes from a Juniper router and do the following.

 It will parse the bgp table information and check for anomalies on routes BGP AS-path against and initial baseline BGP route in "Normal Conditions"

 It will report if any anomalies compared to the baselines

 Then it will alert about the diferences found between the  Routes gathered.


## Future/expected features

.Webhooks messages --> slack
.Scheduled script to get the BGP routes from APIs/Netmiko pull methods.

