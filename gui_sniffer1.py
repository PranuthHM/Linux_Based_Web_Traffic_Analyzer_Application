import tkinter as tk
from tkinter import ttk, messagebox
from scapy.all import sniff
import threading
import csv
from collections import deque, defaultdict
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ----------------- Data Variables -----------------
packets_list = []
protocol_counts = {"IPv4": 0, "IPv6": 0, "TCP": 0, "UDP": 0}
packet_rate = deque(maxlen=30)  # packets per second history
last_second = datetime.now().second
packet_counter = 0

# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("Network Traffic Analyzer")
root.geometry("1000x700")

selected_protocol = tk.StringVar(value="All")

# ----------------- Packet Handler -----------------
def capture_packet(packet):
    global packet_counter, last_second

    try:
        src = packet[0][1].src
        dst = packet[0][1].dst
        proto = packet[0][1].name
        size = len(packet)

        # Apply filter
        filter_value = selected_protocol.get()
        if filter_value != "All" and proto.lower() != filter_value.lower():
            return

        packets_list.append((src, dst, proto, size))
        tree.insert("", tk.END, values=(src, dst, proto, size))

        # Count protocol
        proto_key = proto.upper()
        if proto_key in protocol_counts:
            protocol_counts[proto_key] += 1
        elif "IPV4" in proto_key:
            protocol_counts["IPv4"] += 1
        elif "IPV6" in proto_key:
            protocol_counts["IPv6"] += 1

        # Update counters for packet rate
        now = datetime.now()
        if now.second == last_second:
            packet_counter += 1
        else:
            packet_rate.append(packet_counter)
            packet_counter = 1
            last_second = now.second

        summary_label.config(text=get_summary_text())

    except:
        pass

# ----------------- Sniffing Thread -----------------
def start_sniffing_thread():
    sniff_thread = threading.Thread(target=sniff, kwargs={'prn': capture_packet, 'store': 0})
    sniff_thread.daemon = True
    sniff_thread.start()

# ----------------- Export to CSV -----------------
def export_to_csv():
    if not packets_list:
        messagebox.showwarning("No Data", "No packets captured yet.")
        return
    with open("packets.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Source IP", "Destination IP", "Protocol", "Size"])
        writer.writerows(packets_list)
    messagebox.showinfo("Export Complete", "Packets exported to packets.csv")

# ----------------- Summary Text -----------------
def get_summary_text():
    return (
        f"Total Packets: {len(packets_list)}\n"
        f"IPv4: {protocol_counts['IPv4']}    "
        f"IPv6: {protocol_counts['IPv6']}    "
        f"TCP: {protocol_counts['TCP']}    "
        f"UDP: {protocol_counts['UDP']}"
    )

# ----------------- Real-Time Graph Updates -----------------
def update_graphs():
    # Line graph: Packet Rate
    line_ax.clear()
    line_ax.plot(list(packet_rate), label="Packets/sec", color="blue", marker='o')
    line_ax.set_title("Live Packets Per Second")
    line_ax.set_ylim(0, max(packet_rate, default=1) + 5)
    line_ax.set_ylabel("Packets")
    line_ax.set_xlabel("Seconds (last 30)")
    line_ax.grid(True)
    line_ax.legend()

    # Pie chart: Protocol Distribution
    pie_ax.clear()
    labels = []
    sizes = []
    for proto, count in protocol_counts.items():
        if count > 0:
            labels.append(proto)
            sizes.append(count)
    if sizes:
        pie_ax.pie(sizes, labels=labels, autopct="%1.1f%%")
        pie_ax.set_title("Live Protocol Distribution")

    canvas.draw()
    root.after(1000, update_graphs)

# ----------------- UI Layout -----------------
# Filter dropdown
filter_label = tk.Label(root, text="Filter by Protocol:")
filter_label.pack()

protocol_options = ["All", "IPv4", "IPv6", "TCP", "UDP"]
protocol_dropdown = ttk.Combobox(root, values=protocol_options, textvariable=selected_protocol, state="readonly")
protocol_dropdown.pack(pady=5)
protocol_dropdown.current(0)

# Table
tree = ttk.Treeview(root, columns=("Source", "Destination", "Protocol", "Size"), show="headings")
tree.heading("Source", text="Source IP")
tree.heading("Destination", text="Destination IP")
tree.heading("Protocol", text="Protocol")
tree.heading("Size", text="Size (bytes)")
tree.pack(fill=tk.BOTH, expand=True)

# Buttons
start_button = tk.Button(root, text="Start Capture", command=start_sniffing_thread)
start_button.pack(pady=5)

export_button = tk.Button(root, text="Export to CSV", command=export_to_csv)
export_button.pack(pady=5)

# Summary Label
summary_label = tk.Label(root, text=get_summary_text(), font=("Courier", 10), justify="left")
summary_label.pack(pady=10)

# Graph Area
fig, (line_ax, pie_ax) = plt.subplots(1, 2, figsize=(9, 3))
fig.tight_layout()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Start updating graphs
update_graphs()

root.mainloop()
