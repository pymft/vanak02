import time



class MyTimer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        print(f"Elapsed time = {self.stop - self.start:.5f} seconds")


with MyTimer() as mt:
    time.sleep(2)

print("Hello")