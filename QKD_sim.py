import random

# Generate a random bit string of length n
def generate_random_bit(length):
    return ''.join(str(random.randint(0, 1)) for _ in range(length))

# Generate random bases for the bit string
def generate_random_bases(length, available_bases):
    return ''.join(random.choice(available_bases) for _ in range(length))

# Simulate the transmission of photonic states
def transmit(photonic_states):
    print("Transmitting Photons...")
    return "Transmission Successful", 0

# Measure the qubits based on Bob's bases
def measure_states(photonic_states, bob_bases):
    measurement_bits = ""
    for state, basis in zip(photonic_states, bob_bases):
        if state in ['0', '90'] and basis == '+':
            measurement_bits += '0' if state == '0' else '1'
        elif state in ['45', '135'] and basis == 'x':
            measurement_bits += '0' if state == '45' else '1'
        else:
            measurement_bits += '?'
    return measurement_bits

# Check the bases alignment between Alice and Bob
def check_bases(alice_bases, bob_bases):
    return ''.join('1' if a == b else '0' for a, b in zip(alice_bases, bob_bases))

# Receive function to process the photonic states
def receive(photonic_states, bob_bases, bases, alice_bases):
    print("Receiving Photons...")
    measurement_bits = measure_states(photonic_states, bob_bases)
    resulting_bits = check_bases(alice_bases, bob_bases)
    final_key = ''.join(m if r == '1' else '' for m, r in zip(measurement_bits, resulting_bits))
    
    print("Measurement Bits: ", measurement_bits)
    print("Resulting Bits: ", resulting_bits)
    print("Final Key: ", final_key)
    if '?' in final_key:
        print("Not Matched, some eavesdropping has been done")
    else:
        print("Key is secure")

if __name__ == "__main__":
    # Input the length of the bit string
    n = int(input("Enter the length of the bit string: "))

    # Generate the bit string as an initial key
    bit_string = generate_random_bit(n)
    
    # Define the bases; assuming the rectilinear basis as + and diagonal basis as x
    bases = {'+': {'0': '0', '1': '90'}, 'x': {'0': '45', '1': '135'}}
    available_bases = ['+', 'x']
    
    # Generate random bases for the bit string (Alice)
    alice_bases = generate_random_bases(n, available_bases)
    
    # Bob's randomly generated bases
    bob_bases = generate_random_bases(n, available_bases)
    
    # Measure the bit string in the bases and store the result, then start the transmission of the photons
    transmission_states = [bases[alice_bases[i]][bit_string[i]] for i in range(n)]
    
    # Photonic transmission simulation
    message, status_code = transmit(transmission_states)
    if status_code == 0:
        # Call the receive function by sending photonic states and Bob's bases as parameters
        receive(transmission_states, bob_bases, bases, alice_bases)
