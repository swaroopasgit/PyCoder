import heapq


def find_rebuffering_time(arrivalRate, packets):
    buffer = []  # Min heap for buffered packets
    expected_packet = 1  # Next packet to play
    time = 0
    i = 0  # Index for packet list

    while i < len(packets) or buffer:  # Process until all packets are handled
        time += 1  # Increase time step

        # Process arriving packets at this time
        for _ in range(arrivalRate):
            if i < len(packets):  # If packets are still available
                heapq.heappush(buffer, packets[i])  # Add to buffer
                i += 1

        # Remove outdated packets (packets smaller than expected)
        while buffer and buffer[0] < expected_packet:
            heapq.heappop(buffer)

        # Check if the required packet is available
        if buffer and buffer[0] == expected_packet:
            heapq.heappop(buffer)  # Play the expected packet
            expected_packet += 1  # Move to the next expected packet
        else:
            return time  # Re-buffering occurs here

    return -1  # No re-buffering if all packets arrive in order


# Example Usage
arrivalRate = 2
packets = [1, 3, 2, 4, 5]
print(find_rebuffering_time(arrivalRate, packets))  # Expected Output: 2
