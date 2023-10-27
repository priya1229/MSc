import random

def ams_algorithm(stream, num_buckets):
    buckets = [0] * num_buckets
    
    # Hash function to determine bucket
    hash_fn = lambda x: hash(str(x)) % num_buckets
    
    for data_point in stream:
        bucket = hash_fn(data_point)
        buckets[bucket] += 1
    
    # Estimate the second moment
    estimate = sum(bucket_count ** 2 for bucket_count in buckets)
    
    # Correct the estimate
    correction_factor = num_buckets * (num_buckets - 1) / 2
    corrected_estimate = estimate / correction_factor
    
    return corrected_estimate

def main():
    # Generate a stream of data points (e.g., integers)
    stream = [random.randint(1, 100) for _ in range(1000)]
    
    num_buckets = 100  # Number of buckets (adjust as needed)
    
    estimated_second_moment = ams_algorithm(stream, num_buckets)
    
    print(f"Estimated Second Moment: {estimated_second_moment:.2f}")

if __name__ == "__main__":
    main()
