import time

from src.timer import Timer


def main():
    print("Hello World!")

    t = Timer(10)

    t.start()

    try:
        while not t.is_finished():
            print(f"Remaining time: {t.remaining}")
            t.tick()
            time.sleep(1)

        print("Finished")

    except KeyboardInterrupt:
        print("Stopped by user")


if __name__ == "__main__":
    main()
