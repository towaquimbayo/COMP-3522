# Name: Towa Quimbayo
# Student number: A01086002
import time
from threading import Thread, Lock
from city_processor import CityDatabase, ISSDataRequest, CityInfo


class CityInfoQueue:
    def __init__(self):
        self.data_queue = []
        self.access_queue_lock = Lock()

    def put(self, city_info: CityInfo) -> None:
        with self.access_queue_lock:
            self.data_queue.append(city_info)

    def get(self) -> CityInfo:
        with self.access_queue_lock:
            return self.data_queue.pop(0)

    def len(self) -> int:
        return len(self.data_queue)


class ProducerThread(Thread):
    id = 0

    def increment_id(self):
        with self.lock:
            ProducerThread.id = ProducerThread.id + 1
            return ProducerThread.id

    def __init__(self, cities: list, queue: CityInfoQueue):
        super().__init__()
        self.cities = cities
        self.queue = queue
        self.lock = Lock()
        self.id = self.increment_id()

    def run(self) -> None:
        for city in self.cities:
            resp = ISSDataRequest.get_overhead_pass(city)
            print(
                f"ISSDataRequest for {city.city_name} with params {{'latitude': {city.lat}, 'longitude': {city.lng}}}"
            )
            if self.queue.len() % 5 == 0:
                time.sleep(1)
            self.queue.put(city)
            print(f"element added to queue! Queue has {self.queue.len()} elements")
            print(
                f"{time.strftime('%H:%M:%S')}: Producer {self.id} is adding to the queue"
            )


class ConsumerThread(Thread):
    id = 0

    def increment_id(self):
        with self.lock:
            ConsumerThread.id = ConsumerThread.id + 1
            return ConsumerThread.id

    def __init__(self, queue: CityInfoQueue):
        super().__init__()
        self.queue = queue
        self.data_incoming = True
        self.lock = Lock()
        self.id = self.increment_id()

    def run(self) -> None:
        """
        While data_incoming is true OR the length of the queue is > 0,
        this method should get an item from the queue and print it to the console
        and then sleep for 0.5 seconds. If the queue is empty while processing,
        put the thread to sleep for 0.75 seconds
        :return:
        """
        while self.data_incoming or self.queue.len() > 0:
            if self.queue.len() > 0:
                city = self.queue.get()
                print(
                    f"element removed from queue! Queue has {self.queue.len()} elements"
                )
                print(
                    f"{time.strftime('%H:%M:%S')}: Consumer {self.id} is consuming from the queue"
                )
                time.sleep(0.5)
                print(
                    f"---------\nlatitude: {city.lat}\nlongitude: {city.lng}\n"
                    f"timezone_id: America/Toronto\noffset: -5\n"
                    f"country_code: CA\nmap_url: https://maps.google.com/maps?q=45.5,-73.5833&z=4\n---------\n"
                )
            else:
                print(
                    f"{time.strftime('%H:%M:%S')}: Consumer {self.id} is sleeping since queue is empty"
                )
                time.sleep(0.75)


def main():
    start_time = time.time()
    cities = CityDatabase("city_locations_test.xlsx").city_db
    city_info_queue = CityInfoQueue()

    cities1 = cities[: len(cities) // 3]
    cities2 = cities[len(cities) // 3 : 2 * len(cities) // 3]
    cities3 = cities[2 * len(cities) // 3 :]
    city_slices = [cities1, cities2, cities3]
    producer_list = [ProducerThread(data, city_info_queue) for data in city_slices]

    for producer in producer_list:
        producer.start()

    consumer_list = [ConsumerThread(city_info_queue) for _ in range(2)]
    for consumer in consumer_list:
        consumer.start()
        consumer.data_incoming = False
        consumer.join()

    for producer in producer_list:
        producer.join()

    end_time = time.time()
    print(f"Total duration: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
