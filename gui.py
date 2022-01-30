import tkinter as tk
import protocol
import random


class App(tk.Frame):
    upper_text = None

    interface_frm = None
    interface_ip_field = None
    interface_ip = None
    interface_port_field = None
    interface_port = None
    interface_connect_bttn = None

    connection_frm = None
    client_list = None
    update_bttn = None

    e91_params_frm = None
    length_field = None
    length = None
    seed_field = None
    seed = None
    run_bttn = None

    results_frm = None
    key_field = None
    delta_s_field = None

    server_socket = None
    role = None
    client_addr_arr = None

    def __init__(self, master):
        super().__init__(master)
        self.grid()

        self.upper_text = tk.Label(text="CONNECTION SETTINGS")
        self.upper_text.grid(column=0, row=0, sticky=tk.W)

        self.interface_frm = tk.Frame()
        self.interface_frm.grid(column=0, row=1, sticky=tk.W)

        tk.Label(master=self.interface_frm, text="Interface-IP: ").grid(column=0, row=0, sticky=tk.W)
        self.interface_ip_field = tk.Entry(master=self.interface_frm)
        self.interface_ip_field.grid(column=1, row=0, sticky=tk.W)
        self.interface_ip = tk.StringVar()
        self.interface_ip_field["textvariable"] = self.interface_ip

        tk.Label(master=self.interface_frm, text="Interface-Port: ").grid(column=2, row=0, sticky=tk.W)
        self.interface_port_field = tk.Entry(master=self.interface_frm)
        self.interface_port_field.grid(column=3, row=0, sticky=tk.W)
        self.interface_port = tk.IntVar()
        self.interface_port_field["textvariable"] = self.interface_port

        self.connect_bttn = tk.Button(text="connect", command=self.connect_to_interface)
        self.connect_bttn.grid(column=0, row=2, sticky=tk.W)

    def connect_to_interface(self):
        self.server_socket, self.role = protocol.q_establish_connection((self.interface_ip.get(),
                                                                         self.interface_port.get(),))
        self.upper_text.config(text="SELECT PARTNER")
        self.connect_bttn.destroy()
        self.interface_frm.destroy()
        self.connection_frm = tk.Frame()
        self.connection_frm.grid(column=0, row=1, sticky=tk.W)
        self.client_list = tk.Listbox(master=self.connection_frm, selectmode=tk.SINGLE)
        self.client_list.grid(column=0, row=0, sticky=tk.W)
        self.update_bttn = tk.Button(master=self.connection_frm, text="update", command=self.update_users())
        self.update_bttn.grid(column=0, row=1, sticky=tk.W)

    def update_users(self):
        pass

    def choose_user(self):
        self.upper_text.config(text="E91 PARAMETERS")
        self.e91_params_frm = tk.Frame
        self.e91_params_frm.grid(column=0, row=1, sticky=tk.W)

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

        self.run_bttn = tk.Button(text="run", command=self.run)
        self.run_bttn.grid(column=0, row=2)

    def run(self):
        if len(self.client_list.cursorselection()) != 0:
            self.e91_params_frm.destroy()
            self.run_bttn.destroy()
            self.upper_text.config(text="running...")
            delta_s, key = protocol.e91protocol(self.length.get(), self.seed.get(), random,
                                                self.server_socket, self.role,
                                                self.client_addr_arr[self.client_list.cursorselection()[0]])

            self.upper_text.config(text="RESLUTS")
            self.results_frm = tk.Frame()
            self.results_frm.grid(column=0, row=1, sticky=tk.W)

            tk.Label(master=self.results_frm, text="key: ").grid(column=0, row=0)
            self.key_field = tk.Entry(master=self.results_frm)
            self.key_field.grid(column=1, row=0)
            self.key_field["textvariable"] = key

            tk.Label(master=self.results_frm, text="delta s: ").grid(column=0, row=1)
            self.delta_s_field = tk.Entry(master=self.results_frm)
            self.delta_s_field.grid(column=1, row=1)
            self.delta_s_field["textvariable"] = delta_s


root = tk.Tk()
root.geometry("700x500+40+50")
root.title("E91 protocol client")
myapp = App(root)

if __name__ == '__main__':
    myapp.mainloop()
