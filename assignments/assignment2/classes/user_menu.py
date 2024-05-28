from datetime import datetime
from classes.order_processor import OrderProcessor
from classes.store import Store


class UserMenu:
    def __init__(self):
        """
        Creates a UserMenu object.
        """
        self.__store = Store()

    def get_store(self):
        """
        Returns the store object.
        :return: Store object
        """
        return self.__store

    def set_store(self, store):
        """
        Sets the store object.
        :param store: Store object
        """
        self.__store = store

    store = property(get_store, set_store)

    def display_menu(self):
        """
        Terminal menu for the store owner that can process web orders
        and check inventory. Prints out the daily transaction report when exited.
        """
        while True:
            print("Please select an option:")
            print("1. Process web order\n2. Check inventory\n3. Exit")
            choice = input("Enter your choice: ")
            try:
                if choice == "1":
                    self.__process_web_order()
                elif choice == "2":
                    self.__check_inventory()
                elif choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")
        self.__daily_transaction_report()

    def __process_web_order(self):
        try:
            order_filename = input("Please enter the name of the order file: ")
            order_processor = OrderProcessor(order_filename)
            orders = order_processor.get_orders()
            for order in orders:
                self.store.process_order(order)
            print("Order processed successfully!\n")
        except Exception as e:
            print(f"Error processing web order: {e}")

    def __check_inventory(self):
        """
        Prints the current inventory.
        """
        try:
            print("\nCurrent inventory:")
            for item, quantity in self.store.inventory.items():
                stock_level = ""
                if quantity >= 10:
                    stock_level = "IN STOCK"
                elif quantity < 10:
                    stock_level = "LOW"
                elif quantity < 3:
                    stock_level = "VERY LOW"
                elif quantity == 0:
                    stock_level = "OUT OF STOCK"
                print(
                    f"Name: {item.name}, Quantity: {quantity}, Stock level: {stock_level}"
                )
            print()
        except Exception as e:
            print(f"Error checking inventory: {e}")

    def __daily_transaction_report(self):
        """
        Writes the daily transaction report to a text file.
        """
        try:
            report_content = self.store.create_daily_transaction_report()
            date = datetime.now().strftime("%d%m%y_%H%M")
            with open(f"DTR_{date}.txt", "w", encoding="UTF-8") as f:
                f.write(report_content)
        except Exception as e:
            print(f"Error writing daily transaction report: {e}")
