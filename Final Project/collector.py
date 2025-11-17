class Collector:
    def __init__(self, collector_name, collector_manager):
        self.collector_name = collector_name
        self.collector_manager = collector_manager
        self.customers = []

    def assign_customer(self, customer_id):
        self.customers.append(customer_id)
