import psutil
import time

def get_network_stats():
    net_io = psutil.net_io_counters(pernic=True)
    return net_io

def display_network_stats(previous_stats):
    current_stats = get_network_stats()
    
    print(f"{'Interface':<15} {'Bytes Sent':<15} {'Bytes Received':<15} {'Sent/sec':<15} {'Received/sec':<15}")
    print("=" * 80)

    for interface, stats in current_stats.items():
        if interface in previous_stats:
            sent_bytes = stats.bytes_sent - previous_stats[interface].bytes_sent
            recv_bytes = stats.bytes_recv - previous_stats[interface].bytes_recv
            sent_speed = sent_bytes / 1  # bytes per second
            recv_speed = recv_bytes / 1  # bytes per second
        else:
            sent_bytes = stats.bytes_sent
            recv_bytes = stats.bytes_recv
            sent_speed = 0
            recv_speed = 0

        print(f"{interface:<15} {stats.bytes_sent:<15} {stats.bytes_recv:<15} {sent_speed:<15.2f} {recv_speed:<15.2f}")

    return current_stats

def main():
    print("Monitoring network traffic. Press Ctrl+C to stop.")
    previous_stats = get_network_stats()

    try:
        while True:
            display_network_stats(previous_stats)
            previous_stats = get_network_stats()
            time.sleep(1)  # обновление каждую секунду
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()

