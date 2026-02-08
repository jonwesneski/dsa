\* By this I mean data centers, regions, and countries

## Same Data Center

- Having your app in just 1 data center

Pros:

- High availability
- Scalability (easy)

Cons:

- Latency (when accessing from far away)

## Same Region (multiple Data Centers)

like us-east-1 or us-west-2. Each has multiple data centers separated by **Availability Zones**:

- us-east-2a
- us-east-2b
- us-east-2c

Pros:

- High availability (Even higher; because if 1 data center/availability zone goes down, you have other instances in other availability zones)
- Scalability

Cons:

- Latency (when accessing from another country)

## Same Country Different Region

Used to help improve latency and even load balance certain regions (incase traffic at a certain region just happens to be much higher). You need some kind of Geo DNS to help direct the traffic

```
               +-------------------+
               |      Geo DNS      |
               +-------------------+
                       / \
                      /   \
                     /     \
                    /       \
                   /         \
                  /           \
       +----------------+   +----------------+
       |  Cloud Region 1|   |  Cloud Region 2|
       +----------------+   +----------------+
               |                    |
               |                    |
       +----------------+   +----------------+
       | Load Balancer 1|   | Load Balancer 2|
       +----------------+   +----------------+
          / |  |  \              / |  |  \
         /  |  |   \            /  |  |   \
        /   |  |    \          /   |  |    \
+------+ +------+ +------+ +------+ +------+ +------+
|Server1| |Server2| |Server3| |Server1| |Server2| |Server3|
+------+ +------+ +------+ +------+ +------+ +------+
```

\* Load Balancers can also connect to an Availability Zone and then to the server

Pros:

- High availability (Even higher; because if 1 Region goes down, you have other Regions that can handle it)
- Scalability
- Latency

Cons:

- Complexities with keeping the data correct and consistent (solved with multiple write/master/leader db nodes)
- Cost
- Still slow for different countries

## Different Country

Pros:

- High availability (Even higher; because if 1 Country goes down, you have other Countries that can handle it)
- Scalability
- Latency

Cons:

- Localization requirements
- Data privacy laws (where it can be stored, what can be displayed, what devs have access to, etc.)
