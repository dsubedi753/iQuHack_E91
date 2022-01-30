import tkinter as tk
from protocol import e91protocol
import random


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

        self.run_bttn = tk.Button(text="RUN", command=self.run)
        self.run_bttn.grid(column=0, row=4, sticky=tk.W)

        tk.Label(text="RESLUTS").grid(column=0, row=5, sticky=tk.W)
        self.result_frm = tk.Frame()
        self.result_frm.grid(column=0, row=6, sticky=tk.W)

        tk.Label(master=self.result_frm, text="key: ").grid(column=0, row=0)
        self.key_field = tk.Entry(master=self.result_frm)
        self.key_field.grid(column=1, row=0)
        self.key = tk.IntVar()
        self.key_field["textvariable"] = self.key

        tk.Label(master=self.result_frm, text="delta s: ").grid(column=0, row=1)
        self.delta_s_field = tk.Entry(master=self.result_frm)
        self.delta_s_field.grid(column=1, row=1)
        self.delta_s = tk.IntVar()
        self.delta_s_field["textvariable"] = self.delta_s

    def run(self):
        self.run_bttn.destroy()
        running_label = tk.Label(text="running...")
        running_label.grid(column=0, row=4, sticky=tk.W)
        s_delta, key = e91protocol(self.length.get(), self.seed.get(), random,
                                   (self.interface_ip.get(), self.interface_port.get(),),
                                   (self.target_ip.get(), self.target_port.get(),))
        running_label.destroy()
        tk.Label(text="done.").grid(column=0, row=4, sticky=tk.W)
        self.key.set(key)
        self.delta_s.set(s_delta)


root = tk.Tk()
root.geometry("700x500+40+50")
root.title("E91 protocol client")
myapp = App(root)

if __name__ == '__main__':
    myapp.mainloop()
