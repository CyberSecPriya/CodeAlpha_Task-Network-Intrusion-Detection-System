import csv
import re

# Updated path since the file is now in the same folder
input_file = "snort.alert.fast"
output_file = "snort_alerts.csv"

# Define a pattern to extract alert info
pattern = r'(\d{2}/\d{2}-\d{2}:\d{2}:\d{2}\.\d+)\s+\[\*\*\]\s+\[(.*?)\]\s+(.*?)\s+\[\*\*\]\s+\[Classification: (.*?)\]\s+\[Priority: (\d+)\]\s+\{(.*?)\}\s+(.*?):(\d+) -> (.*?):(\d+)'

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Timestamp', 'SID', 'Message', 'Classification', 'Priority', 'Protocol', 'Src IP', 'Src Port', 'Dst IP', 'Dst Port'])

    for line in infile:
        match = re.match(pattern, line)
        if match:
            writer.writerow(match.groups())

print("✅ Alerts parsed and saved to snort_alerts.csv")
