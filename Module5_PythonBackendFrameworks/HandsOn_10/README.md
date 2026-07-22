Service Name | Responsibility | Endpoints it owns | Database it owns |
1. Auth Service| Registration, login, token validation | /api/v1/auth/ | auth.db |
2. Course Service| Department and course/module CRUD | /api/courses/ | courses.db |
3. Student Service| Student profiles and enrollment orchestration | /api/students/ | students.db |
4. Notification Service| Async email confirmations | Internal event consumer | No database |

Inter-Service Communication: Synchronous vs Asynchronous

Synchronous Communication (HTTP / REST)
-Advantages: Easy to implement, immediate feedback loop, simple to trace and debug.
-Disadvantages: Tight spatial and temporal coupling, latency amplification across cascading requests, single-point-of-failure risks.

Asynchronous Communication (Message Queue - RabbitMQ / Kafka)
-Pros: Complete operational decoupling, built-in load leveling and queuing, resilient against intermittent service downtime, high system throughput.
-Cons: Eventual consistency model, elevated operational complexity, challenging transaction management and distributed tracing.

When to Use a Message Queue (RabbitMQ / Kafka)
Use a message queue for non-blocking or side-effect operations where the user does not need to wait for immediate processing. 
 Typical use cases include sending email notifications, generating background reports, processing payment webhooks, or syncing search indices across services.