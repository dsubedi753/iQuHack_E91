import tkinter as tk
from protocol import e91protocol


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(text="CONNECTION SETTINGS").grid(column=0, row=0, sticky=tk.W)

        self.addresses_frm = tk.Frame()
        self.addresses_frm.grid(column=0, row=1, sticky=tk.W)

        tk.Label(master=self.addresses_frm, text="Interface-IP: ").grid(column=0, row=0, sticky=tk.W)
        self.interface_ip_field = tk.Entry(master=self.addresses_frm)
        self.interface_ip_field.grid(column=1, row=0, sticky=tk.W)
        self.interface_ip = tk.StringVar()
        self.interface_ip_field["textvariable"] = self.interface_ip

        tk.Label(master=self.addresses_frm, text="Interface-Port: ").grid(column=2, row=0, sticky=tk.W)
        self.interface_port_field = tk.Entry(master=self.addresses_frm)
        self.interface_port_field.grid(column=3, row=0, sticky=tk.W)
        self.interface_port = tk.IntVar()
        self.interface_port_field["textvariable"] = self.interface_port

        tk.Label(master=self.addresses_frm, text="Target-IP: ").grid(column=0, row=1, sticky=tk.W)
        self.target_ip_field = tk.Entry(master=self.addresses_frm)
        self.target_ip_field.grid(column=1, row=1, sticky=tk.W)
        self.target_ip = tk.StringVar()
        self.target_ip_field["textvariable"] = self.target_ip

        tk.Label(master=self.addresses_frm, text="Target-Port: ").grid(column=2, row=1, sticky=tk.W)
        self.target_port_field = tk.Entry(master=self.addresses_frm)
        self.target_port_field.grid(column=3, row=1, sticky=tk.W)
        self.target_port = tk.IntVar()
        self.target_port_field["textvariable"] = self.target_port

        tk.Label(text="E91 PROTOCOL PARAMETERS").grid(column=0, row=2, sticky=tk.W)

        self.e91_params_frm = tk.Frame()
        self.e91_params_frm.grid(column=0, row=3, sticky=tk.W)

        tk.Label(master=self.e91_params_frm, text="Bitstring length: ").grid(column=0, row=0, sticky=tk.W)
        self.length_field = tk.Entry(master=self.e91_params_frm)
        self.length_field.grid(column=1, row=0, sticky=tk.W)
        self.length = tk.IntVar()
        self.length_field["textvariable"] = self.length

        tk.Label(master=self.e91_params_frm, text="Seed: ").grid(column=0, row=1, sticky=tk.W)
        self.seed_field = tk.Entry(master=self.e91_params_frm)
        self.seed_field.grid(column=1, row=1, sticky=tk.W)
        self.seed = tk.IntVar()
        self.seed_field["textvariable"] = self.seed

        tk.Button(text="RUN", command=self.run).grid(column=0, row=4, sticky=tk.W)

    def run(self):
        print(f"Interface ip: {self.interface_ip.get()}:{self.interface_port.get()}\n"
              f"Target ip: {self.target_ip.get()}:{self.target_port.get()}\n"
              f"E91 length: {self.length.get()}\nE91 seed: {self.seed.get()}")


root = tk.Tk()
root.geometry("700x500+40+50")
root.title("E91 protocol client")
myapp = App(root)

if __name__ == '__main__':
    myapp.mainloop()
