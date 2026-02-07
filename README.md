# MyMagicPencil- AI Teaching Software for Civilytix Pvt Ltd
Repository to hold testing stats,scripts and plugins for https://www.mymagicpencil.com/

## Current phase: `Scalability testing`
Phase breakdown:
1. Scenario Based Testing
2. Backend Testing
   
> [!IMPORTANT]
> Testing is done using locust,their version numbers are necessary for large scale testing.
Current Status:`testing`

```py
locust 2.43.2 on Python 3.12.10
```
Stats:
200 users tested concurrently with 0% Failure<br>
4 scenarios tested
### Next Steps
- [x] Set up `locustfile.py` for large-scale testing
- [ ] Create 4 vm's on `AWS/AZURE` and set up 1 master 3 workers
- [ ] Load test 500 users concurrently without DDoSing the site

Metrics are based on a combination of scenarios + backend testing
#### How testing is done?
> The code is loaded onto a system and `locust` is called. This generates a localhost link [http:localhost:8089/](http:localhost:8089/)<br>
and settings can be edited, No of users, Ramp up and host will be [https://www.mymagicpencil.com/](https://www.mymagicpencil.com/). <br>

*`Testing runs for roughly 4-5mins for a valid readout.`*
