class Order:

    orders = []

    orderid: int = 0
    shipping_address: str = ""
    expedited: bool = False
    shipped: bool = False
    customer: object = None

    @staticmethod
    def get_filtered_info(predicate, func):
        output = []

        for order in Order.orders:
            if predicate(order):
                output.append(func(order))
        return output

    @staticmethod
    def test_expedited(order):
        return order.expedited

    @staticmethod
    def get_customer_name(order):
        return order.customer.name

    @staticmethod
    def get_shipping_address(order):
        return order.customer.address

    @staticmethod
    def get_customer_address(order):
        return order.customer.address

    @staticmethod
    def get_expedited_orders_customer_addresses():
        return Order.get_filtered_info(Order.test_expedited, Order.get_customer_address)

    @staticmethod
    def get_expedited_orders_customer_names():
        return Order.get_filtered_info(Order.test_expedited, Order.get_customer_name)
