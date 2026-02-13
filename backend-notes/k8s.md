## Components

- Cluster — The whole system. It consists of a control plane (the brain) and worker nodes (the machines that run your apps).
- Node — A single machine (physical or virtual) in the cluster. Each node runs containers.
- Pod — The smallest deployable unit. A pod wraps one or more containers that share networking and storage. Usually it's one container per pod.
- Deployment — A declaration of "I want 3 replicas of my API server running at all times." Kubernetes ensures that's always true, restarting pods if they crash.
- Service — A stable network endpoint that routes traffic to the right pods. Pods are ephemeral (they come and go), but a Service gives you a consistent address.
- Namespace — A way to logically separate resources within a cluster (e.g., staging vs production).
- ConfigMap / Secret — Ways to inject configuration and sensitive data (like DB passwords) into your pods without hardcoding them.
- Ingress — Manages external HTTP/HTTPS access to services, handling routing rules and TLS termination.

## Flow Example

```
$ kubectl get endpoints edlink-api -n production

NAME         ENDPOINTS                                            AGE
edlink-api   10.244.1.15:3000,10.244.2.23:3000,10.244.1.47:3000  5d
```

When a pod fails its readiness probe, its IP gets removed from this list. Traffic stops flowing to it _before it's killed_. When a new pod passes its readiness probe, its IP gets added. This is why readiness probes are critical — without them, traffic can be routed to a pod that isn't ready to serve requests.

---

### The Big Picture — How Everything Connects

Here's how a Service relates to every other major K8s concept:

```
                              ┌─────────────────────────────────────┐
                              │           INGRESS                   │
                              │   ┌───────────────────────────┐     │
                              │   │  Rules:                   │     │
         External Traffic     │   │  /v2/* → edlink-api-svc   │     │
         (api.edlink.com) ────┤   │  /docs/* → docs-svc       │     │
                              │   │  /admin/* → admin-svc      │     │
                              │   └───────────┬───────────────┘     │
                              └───────────────┼─────────────────────┘
                                              │
                    ┌─────────────────────────┼──────────────────────────┐
                    │                         │                          │
          ┌─────────▼──────────┐  ┌──────────▼─────────┐  ┌────────────▼────────┐
          │  SERVICE           │  │  SERVICE            │  │  SERVICE             │
          │  edlink-api-svc    │  │  docs-svc           │  │  admin-svc           │
          │  ClusterIP:        │  │  ClusterIP:         │  │  ClusterIP:          │
          │  10.96.45.12:80    │  │  10.96.51.7:80      │  │  10.96.62.3:80       │
          │                    │  │                     │  │                      │
          │  selector:         │  │  selector:          │  │  selector:           │
          │    app=edlink-api  │  │    app=docs         │  │    app=admin         │
          └─────────┬──────────┘  └──────────┬──────────┘  └────────────┬─────────┘
                    │                        │                          │
       ┌────────────┼────────────┐           │                         │
       │            │            │           │                         │
  ┌────▼───┐  ┌────▼───┐  ┌────▼───┐  ┌────▼───┐              ┌──────▼──┐
  │ Pod A  │  │ Pod B  │  │ Pod C  │  │ Pod D  │              │  Pod E  │
  │        │  │        │  │        │  │        │              │         │
  │ :3000  │  │ :3000  │  │ :3000  │  │ :8080  │              │  :4000  │
  └────┬───┘  └────┬───┘  └────┬───┘  └────────┘              └─────────┘
       │           │           │
       │    All created and managed by
       │
  ┌────▼──────────────────────────────┐
  │  DEPLOYMENT                       │
  │  edlink-api                       │
  │                                   │
  │  replicas: 3                      │
  │  image: myregistry/api:v2.1.0    │
  │  labels: app=edlink-api           │
  │                                   │
  │  ┌─────────────────────────────┐  │
  │  │  REPLICASET                 │  │
  │  │  edlink-api-7d4f8b6c9      │  │
  │  │  (manages the actual pods)  │  │
  │  └─────────────────────────────┘  │
  └──────────────────┬────────────────┘
                     │
              watched by
                     │
  ┌──────────────────▼────────────────┐
  │  HPA                              │
  │  edlink-api-hpa                   │
  │                                   │
  │  min: 3, max: 50                  │
  │  target: 60% CPU                  │
  │                                   │
  │  Scales the Deployment up/down    │
  │  which creates/removes pods       │
  │  which the Service auto-discovers │
  └───────────────────────────────────┘
```

And here's the flow when a new version is deployed:

```
                    Developer pushes new image tag
                              │
                              ▼
                 ┌───────────────────────┐
                 │  DEPLOYMENT updated   │
                 │  image: api:v2.2.0    │
                 └───────────┬───────────┘
                             │
                  creates new ReplicaSet
                             │
              ┌──────────────┼──────────────┐
              │              │              │
         ┌────▼───┐    ┌────▼───┐    ┌────▼───┐
         │New Pod │    │New Pod │    │New Pod │
         │ v2.2.0 │    │ v2.2.0 │    │ v2.2.0 │
         │        │    │        │    │        │
         │Readiness│   │Readiness│   │Readiness│
         │Probe:  │    │Probe:  │    │Probe:  │
         │passing │    │passing │    │pending │
         └───┬────┘    └───┬────┘    └───┬────┘
             │             │             │
             ▼             ▼             │
     ┌──────────────────────────┐        │
     │  SERVICE endpoints       │        │
     │  updated automatically   │        │
     │                          │        │
     │  10.244.1.50:3000  ✓ new│        │  Not added until
     │  10.244.2.61:3000  ✓ new│        │  readiness probe
     │  10.244.1.15:3000  ✗ old│        │  passes!
     │  (being terminated)      │        │
     └──────────────────────────┘        │
                                         │
         Old pods are terminated only
         after new pods are ready.
         This is how zero-downtime
         deployments work.
```

### Service Types Compared

```
┌─────────────────────────────────────────────────────────────────┐
│                        OUTSIDE WORLD                            │
│                             │                                   │
│   ┌─────────────────────────┼──────────────────────────┐        │
│   │  LoadBalancer            │                          │        │
│   │  (cloud LB provisioned)  │                          │        │
│   │  External IP: 54.23.1.8 │                          │        │
│   │                          ▼                          │        │
│   │   ┌──────────────────────────────────────────┐      │        │
│   │   │  NodePort                                │      │        │
│   │   │  Opens port 30080 on EVERY node          │      │        │
│   │   │                                          │      │        │
│   │   │  Node A:30080  Node B:30080  Node C:30080│      │        │
│   │   │       │             │             │      │      │        │
│   │   │       ▼             ▼             ▼      │      │        │
│   │   │   ┌──────────────────────────────────┐   │      │        │
│   │   │   │  ClusterIP                       │   │      │        │
│   │   │   │  Internal virtual IP: 10.96.45.12│   │      │        │
│   │   │   │                                  │   │      │        │
│   │   │   │  Only reachable inside cluster   │   │      │        │
│   │   │   │       │         │         │      │   │      │        │
│   │   │   │    Pod A     Pod B     Pod C     │   │      │        │
│   │   │   └──────────────────────────────────┘   │      │        │
│   │   └──────────────────────────────────────────┘      │        │
│   └─────────────────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────────────────┘

Each type BUILDS on the previous one.
LoadBalancer creates a NodePort which creates a ClusterIP.
```

And then there's the **Headless Service** (`clusterIP: None`), which is used for StatefulSets like Postgres:

```
┌──────────────────────────────────────────────┐
│  Headless Service (clusterIP: None)          │
│  postgres-headless                           │
│                                              │
│  No virtual IP. Instead, DNS returns         │
│  individual pod IPs directly.                │
│                                              │
│  DNS query: postgres-headless                │
│  Returns: 10.244.1.5, 10.244.2.8, 10.244.3.2│
│                                              │
│  Each pod also gets its own DNS:             │
│  postgres-0.postgres-headless → 10.244.1.5   │
│  postgres-1.postgres-headless → 10.244.2.8   │
│  postgres-2.postgres-headless → 10.244.3.2   │
│                                              │
│  This is how replicas find the primary       │
│  and how clients connect to specific         │
│  instances.                                  │
└──────────────────────────────────────────────┘
```

### Complete Relationship Map

Here's the full picture of how every major K8s concept connects:

```
┌─────────────────────────────── CLUSTER ────────────────────────────────┐
│                                                                        │
│  ┌──── NAMESPACE: production ───────────────────────────────────────┐  │
│  │                                                                  │  │
│  │  CONFIGMAP ─────────────────┐                                    │  │
│  │  (env vars, config files)   │                                    │  │
│  │                             │ mounted into                       │  │
│  │  SECRET ────────────────────┤                                    │  │
│  │  (passwords, API keys)      │                                    │  │
│  │                             ▼                                    │  │
│  │  ┌─────────── DEPLOYMENT ──────────────┐                         │  │
│  │  │                                     │                         │  │
│  │  │  ┌─── REPLICASET ───────────────┐   │                         │  │
│  │  │  │                              │   │ ◄── HPA watches         │  │
│  │  │  │  ┌─── POD ──────────────┐    │   │     and scales          │  │
│  │  │  │  │                      │    │   │                         │  │
│  │  │  │  │  ┌── CONTAINER ───┐  │    │   │                         │  │
│  │  │  │  │  │  edlink-api    │  │    │   │                         │  │
│  │  │  │  │  │  :3000         │  │    │   │                         │  │
│  │  │  │  │  └────────────────┘  │    │   │                         │  │
│  │  │  │  │                      │    │   │                         │  │
│  │  │  │  │  Liveness probe ──── │ ── │ ──│── K8s restarts if fail  │  │
│  │  │  │  │  Readiness probe ─── │ ── │ ──│── Service removes if    │  │
│  │  │  │  │                      │    │   │   fail                  │  │
│  │  │  │  │  VOLUME MOUNT ──────►│ PVC│   │                         │  │
│  │  │  │  │                      │  │ │   │                         │  │
│  │  │  │  └──────────────────────┘  │ │   │                         │  │
│  │  │  │                            │ │   │                         │  │
│  │  │  │  (... more pods ...)       │ │   │                         │  │
│  │  │  └────────────────────────────┘ │   │                         │  │
│  │  └─────────────────────────────────┘   │                         │  │
│  │                │                       │                         │  │
│  │         label: app=edlink-api          │                         │  │
│  │                │                       │                         │  │
│  │         ┌──────▼──────────┐            │                         │  │
│  │         │  SERVICE        │            │  PV (Persistent Volume) │  │
│  │         │  edlink-api-svc │            │  ▲                      │  │
│  │         │  ClusterIP      │ ◄── PVC ───┘  │                      │  │
│  │         └──────┬──────────┘    (binds)    │                      │  │
│  │                │                          │                      │  │
│  │         ┌──────▼──────────┐     ┌─────────┴──────┐               │  │
│  │         │  INGRESS        │     │ STORAGE CLASS   │               │  │
│  │         │  Routes external│     │ (gp3, ssd, etc) │               │  │
│  │         │  traffic        │     └────────────────┘               │  │
│  │         └──────┬──────────┘                                      │  │
│  │                │                                                 │  │
│  └────────────────┼─────────────────────────────────────────────────┘  │
│                   │                                                    │
│            ┌──────▼──────────────────────────────────┐                 │
│            │  NODE (worker machine)                   │                 │
│            │                                         │                 │
│            │  kubelet ── manages pods on this node    │                 │
│            │  kube-proxy ── programs network rules    │                 │
│            │  container runtime ── runs containers    │                 │
│            │                                         │                 │
│            │  (Karpenter / Cluster Autoscaler         │                 │
│            │   provisions more nodes when needed)     │                 │
│            └─────────────────────────────────────────┘                 │
│                                                                        │
│  CONTROL PLANE:                                                        │
│  ┌────────────┐ ┌───────────┐ ┌──────────┐ ┌────────────────────────┐  │
│  │ API Server │ │ Scheduler │ │  etcd    │ │ Controller Manager     │  │
│  │            │ │ (decides  │ │ (stores  │ │ (runs control loops:   │  │
│  │ All kubectl│ │  which    │ │  all     │ │  ReplicaSet controller │  │
│  │ commands   │ │  node a   │ │  cluster │ │  Endpoint controller   │  │
│  │ go here    │ │  pod runs │ │  state)  │ │  Node controller       │  │
│  │            │ │  on)      │ │          │ │  HPA controller)       │  │
│  └────────────┘ └───────────┘ └──────────┘ └────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
```

### Does a Service Need to Scale?

No, and this is an important distinction. A Service is not a running process — it's a **networking abstraction**. There's no Service pod consuming CPU or memory. It's implemented via:

- **A DNS entry** in CoreDNS
- **iptables or IPVS rules** on each node, managed by kube-proxy
- **An Endpoints list** maintained by the controller manager

When traffic goes to a Service IP, the kernel's networking stack (iptables/IPVS) handles the routing. It's extremely lightweight and operates at the kernel level, not in userspace.

That said, there's a nuance. With iptables mode (the default), every Service creates rules on every node, and the rules are evaluated linearly. If you have thousands of Services, rule evaluation can add latency. **IPVS mode** uses hash tables for O(1) lookups and handles massive scale much better:

```
                      iptables mode                 IPVS mode
                      (default)                     (production at scale)

Lookup time:          O(n) rules scanned            O(1) hash lookup
1,000 services:       ~1ms overhead                 ~0.1ms overhead
10,000 services:      ~10ms overhead                ~0.1ms overhead
Load balancing:       Random                        Round-robin, least
                                                    connections, weighted
```

For a company like Edlink with potentially dozens of internal services, iptables is fine. But it's good to know IPVS exists for when things get bigger.

### The Lifecycle in Action

To tie it all together, here's what happens when a request arrives at Edlink's API:

```
1. Browser: GET https://api.edlink.com/v2/districts/123/students
                            │
2. DNS resolves to ALB      │
   (cloud load balancer)    ▼
                     ┌──────────────┐
3. ALB terminates    │  AWS ALB     │
   TLS, forwards     │  (cloud)     │
   to NodePort       └──────┬───────┘
                            │
4. Hits Ingress      ┌──────▼───────┐
   Controller pod    │  INGRESS     │
   which reads       │  path: /v2/* │
   routing rules     └──────┬───────┘
                            │
5. Routes to         ┌──────▼───────────┐
   ClusterIP         │  SERVICE         │
                     │  edlink-api-svc  │
6. kube-proxy/IPVS   │                  │
   selects a pod     │  Endpoints:      │
   (round-robin)     │  10.244.1.15 ✓   │
                     │  10.244.2.23 ✓   │
                     │  10.244.1.47 ✓   │
                     └──────┬───────────┘
                            │
7. Packet forwarded  ┌──────▼───────┐
   to selected pod   │  POD B       │
                     │  10.244.2.23 │
                     │              │
8. Container handles │  Container   │
   the request       │  :3000       │
                     │  Node.js API │
                     └──────┬───────┘
                            │
9. App queries       ┌──────▼───────────┐
   another Service   │  SERVICE         │
                     │  edlink-db-ro    │
                     │  (Postgres read) │
                     └──────┬───────────┘
                            │
10. Response flows   ┌──────▼───────┐
    back up the      │  Postgres    │
    same chain       │  replica pod │
                     └──────────────┘
```
