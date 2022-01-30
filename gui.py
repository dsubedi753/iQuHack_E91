import tkinter as tk
import protocol
import random
from tkinter import messagebox


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
    popup = None

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
    client_addr_list = None
    client_addr = None

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
        self.server_socket, own_addr = protocol.q_establish_connection((self.interface_ip.get(),
                                                                        self.interface_port.get(),))
        self.upper_text.config(text="SELECT PARTNER")
        self.connect_bttn.destroy()
        self.interface_frm.destroy()
        self.connection_frm = tk.Frame()
        self.connection_frm.grid(column=0, row=1, sticky=tk.W)
        tk.Label(master=self.connection_frm, text=f"your IP: {own_addr[0]}:{own_addr[1]}").grid(column=0, row=0)
        self.client_list = tk.Listbox(master=self.connection_frm, selectmode=tk.SINGLE)
        self.client_list.grid(column=0, row=1, sticky=tk.W)
        button_frm = tk.Frame(master=self.connection_frm)
        button_frm.grid(column=0, row=2)
        tk.Button(master=button_frm, text="update", command=self.update_users).\
            grid(column=0, row=0, sticky=tk.W)
        tk.Button(master=button_frm, text="choose", command=self.choose_user).\
            grid(column=1, row=0, sticky=tk.E)

    def update_users(self):
        self.client_addr_list, connection_req = protocol.q_update(self.server_socket)
        if connection_req is not None:
            popup = tk.Toplevel(self.master)
            popup.geometry("300x200+200+200")
            tk.Label(popup, text=f"{connection_req[0]}:{connection_req[1]} want to communicate.").pack(fill=tk.BOTH)

            def accept(app):
                app.role = False
                app.client_addr = connection_req
                app.draw_parameter_screen()
                protocol.q_accept_user(app.server_socket, True)
                popup.destroy()

            def refuse(app):
                protocol.q_accept_user(app.server_socket, app.client_addr, False)
                popup.destroy()

            tk.Button(popup, text="accept", command=lambda: accept(self)).pack(side=tk.LEFT, fill=tk.BOTH)
            tk.Button(popup, text="refuse", command=lambda: refuse(self)).pack(side=tk.RIGHT, fill=tk.BOTH)

        else:
            self.client_list.delete(0, tk.END)
            for i in range(len(self.client_addr_list)):
                self.client_list.insert(i, f"{self.client_addr_list[i][0]}:{self.client_addr_list[i][1]}")

    def choose_user(self):
        if len(self.client_list.curselection()) != 0:
            addr = self.client_addr_list[self.client_list.curselection()[0]]
            if protocol.q_choose_user(self.server_socket, addr):
                self.role = True
                self.client_addr = addr
                self.draw_parameter_screen()
            else:
                messagebox.showinfo(title="Connection Refused", message="The chosen client has refused the connection")

    def draw_parameter_screen(self):
        self.connection_frm.destroy()
        self.upper_text.config(text="E91 PARAMETERS")
        self.e91_params_frm = tk.Frame()
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
        self.run_bttn.grid(column=0, row=2, sticky=tk.W)

    def run(self):
        self.e91_params_frm.destroy()
        self.run_bttn.destroy()
        self.upper_text.config(text="running...")
        delta_s, key = protocol.e91protocol(self.length.get(), self.seed.get(), random,
                                            self.server_socket, self.role, self.client_addr)

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
