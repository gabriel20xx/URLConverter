import re


def extract_ip_port(input_file, output_file):
    # Regex to match IP and port
    ip_port_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+):(\d+)')

    # Open input file for reading and output file for writing
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            match = ip_port_pattern.search(line)
            if match:
                # Write the IP and port to the output file
                outfile.write(f"{match.group(1)}:{match.group(2)}\n")


# Example usage:
input_file = 'C:/Users/gabri/Downloads/proxies.txt'  # Input file with URLs
output_file = 'C:/Users/gabri/Downloads/converted.txt'  # Output file with IP and port
extract_ip_port(input_file, output_file)
