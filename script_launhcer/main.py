class Launcher:
    def __init__(self):
        self.root = Tk()
        self.height = 800
        self.width = 1000
        self.server = Server()
        self.port = 8888
        self.server_adress = ("", self.port)
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.minsize(self.width, self.height)
        self.root.maxsize(self.width, self.height)
        self.root.config(background='#acc0e4')
        self.root.title("Launcher")
        self.logo = PhotoImage(file="../img/logo.png").zoom(19).subsample(19)
        self.message = "jean 3 : 16 car DIEU à tant aimé le monde  qu'IL à donné son Fils unique, enfin que quiconque" \
                       "croit en Lui ne périsse point, mais qu'il ait la vie éternelle."
        self.home = 'http://localhost:8888/index.html'
        self.apropo = 'http://localhost:8888/prorpos.html'
        self.main_body(self.root)
        self.closed()

    def web_direct(self):
        self.server.contruction_server(self.server_adress)
        try:
            webbrowser.open_new(self.home)
            #self.root.quit()
        except:
            pass

    def web_direct2(self):
        try:
            webbrowser.open_new(self.apropo)
            #self.root.quit()
        except:
            pass


    def main_body(self, root):
        # creation d'un frame au dessus
        top_bar = Frame(root, bg='#2d2e30')
        # composant de la top bar
        name__ministys = Label(top_bar, text='.ministrys', fg='#ffffff', bg='#2d2e30', font=("Terminal", 25), padx=0)
        name__ministys.place(x=180, y=23)
        name__groupe = Label(top_bar, text="GEADV", fg='#919be0', bg="#2d2e30", font=("Terminal", 45), padx=0, pady=0,
                             justify='center')
        name__groupe.place(x=5, y=0)
        top_bar.place(relwidth=1.0, height=60)
        # creation du footer
        bottom_bar = Frame(root, bg='#ffffff')
        #  components of bottom_bar
        message = Label(bottom_bar, text=self.message, bg="#fffFff", font=('Terminal', 8), padx=0, pady=0, width=1,
                        justify="left")
        message.place(relwidth=1.0)
        bottom_bar.place(relwidth=1.0, y=780, height=20)
        # logo_canva
        logo_canva = Frame(root)
        # component of logo canva
        canva_img = Canvas(logo_canva, bg='#c8d7f1')
        canva_img.create_image(260, 360, image=self.logo)
        canva_img.place(relwidth=1.0, relheight=1.0)
        logo_canva.place(relwidth=0.52, x=0, y=60, height=720)

        # side_bar
        side_bar = Frame(root, bg='#ffffff')
        # compements
        bouton1 = Button(side_bar, text="Lancer GEADV.ministry", fg='#919be0', bg="#2d2e30", justify='center', padx=50, command=self.web_direct)
        bouton1.place(y=50, x=23, relwidth=0.9, height=50)
        bouton2 = Button(side_bar, text="A propos de l'application", fg='#919be0', bg="#2d2e30", justify='center',
                         padx=50, command=self.web_direct2)
        bouton2.place(y=350, x=23, relwidth=0.9, height=50)
        bouton3 = Button(side_bar, text="Quitter l'application", fg='#919be0', bg="#2d2e30", justify='center', padx=50,
                         command=self.quiter)
        bouton3.place(y=650, x=23, relwidth=0.9, height=50)
        side_bar.place(relwidth=0.48, x=520, y=60, height=720)

    def quiter(self):
        rep = askokcancel("confirmer la fermeture ", "voulez-vous vraiment quitter?")
        if rep:
            self.root.quit()


    def closed(self):
        self.root.mainloop()

class Server:
    def __init__(self):
        self.name = "server"

    def contruction_server(self, server_adresse):
        server = http.server.HTTPServer
        handler = http.server.CGIHTTPRequestHandler
        handler.cgi_directories = ["../web_view/html"]

        httpd = server(server_adresse, handler)
        #httpd.serve_forever()


if __name__ == '__main__':
    from tkinter import *
    import webbrowser
    from tkinter.messagebox import askokcancel
    import http.server
    launcher = Launcher()
