# Exercise 6: Delivery Monitoring and Alerting

## Objective
To monitor delivery-service metrics in real time and configure alerts using Python, Prometheus, Grafana, Docker, and Jenkins.

## Technologies Used
- Python and prometheus-client
- Prometheus for metrics collection and alert evaluation
- Grafana for monitoring dashboards
- Docker for running monitoring services
- Jenkins for pipeline validation

## Implementation
1. Created a Python application to simulate delivery statistics.
2. Exposed delivery metrics through the `/metrics` endpoint on port 8000.
3. Configured Prometheus to scrape the delivery application.
4. Created alert rules for high pending deliveries and high average delivery time.
5. Connected Grafana to Prometheus and created a dashboard displaying delivery metrics.
6. Configured a Jenkins pipeline to check the monitoring files, validate Python source patterns, and check Prometheus and Grafana readiness.
7. Tested the high-pending-deliveries alert and verified that it reached the **Firing** state.

## How to Run
1. Start the Python application using `python delivery_metrics.py`.
2. Open `http://localhost:8000/metrics` to view the exposed metrics.
3. Open `http://localhost:9090` to access Prometheus.
4. Open `http://localhost:9090/targets` to verify the delivery-service target.
5. Open `http://localhost:9090/alerts` to view alert states.
6. Open `http://localhost:3000` to access Grafana.
7. Run the `Exercise-6-Monitoring` job in Jenkins and verify that the pipeline succeeds.

Prometheus, Grafana, and Jenkins must be running in Docker for the corresponding steps to work.

## Evidence
Screenshots are stored in the `screenshots` folder. Docker and monitoring service logs are stored in the `outputs` folder.

## Result
The delivery metrics were exposed and collected successfully, the Grafana dashboard displayed the metrics, the high-pending-deliveries alert reached the Firing state during testing, and the Jenkins validation pipeline completed successfully.