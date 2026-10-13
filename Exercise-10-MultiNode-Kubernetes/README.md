# Exercise 10: Multi-Node Kubernetes Cluster
## Objective
Deploy a Product Catalog and Shopping Cart on a three-node Minikube cluster with replicas distributed across different nodes.
## Technologies
- Docker
- Minikube
- Kubernetes
- Python and Flask
- PowerShell
## Applications
- Product Catalog: Returns Laptop, Phone, and Headphones through GET /products.
- Shopping Cart: Supports GET /cart and POST /cart to view and add items.
## Replicas
- Product Catalog: 2 replicas.
- Shopping Cart: 3 replicas.
Pod anti-affinity is configured to distribute each application's replicas across separate nodes.
## Docker Images
- product-catalog:latest
- shopping-cart:latest
## Kubernetes Resources
- product_catalog_deployment.yaml
- shopping_cart_deployment.yaml
- product_catalog_service.yaml
- shopping_cart_service.yaml
## Verification
- All three Kubernetes nodes reached Ready status.
- All five application pods ran successfully.
- Both Kubernetes Services were created.
- Product Catalog returned three products.
- Shopping Cart successfully accepted and returned a Laptop item.
## Screenshots
See the screenshots folder for evidence of cluster setup, pod distribution, services, and application testing.
