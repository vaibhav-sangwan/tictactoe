
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
	#click()
	#incscore(ch : X/O)
	#self.scorex -> Label displaying score of X
	#self.scoreo -> Label displaying score of O
	#self.x -> Int containing score of X
	#self.o -> Int containing score of O
	#self.turn -> String denoting whose turn it is
	#self.turnview -> Label diplaying self.turn
	#self.storex -> Dict to track possible winnings of X
	#self.storeo -> Dict to track possible winnings of O
	#self.list -> 2-D list of the 9 buttons
	def __init__(self):
		Gtk.Window.__init__(self, title="Tic Tac Toe")
		vbox = Gtk.VBox(spacing = 20)
		self.add(vbox)
		
		self.turn = "X"
		self.turnview = Gtk.Label(label = self.turn+"'s turn")
		self.storex = {"dl":0,"dr":0,"v1":0,"v2":0,"v3":0, "h1":0,"h2":0, "h3":0}
		self.storeo = {"dl":0,"dr":0,"v1":0,"v2":0,"v3":0, "h1":0,"h2":0, "h3":0}
		self.list = [[],[],[]]
		self.scorex = Gtk.Label(label = "")
		self.scoreo = Gtk.Label(label = "")
		self.x = self.o = 0
		
		self.scorex.set_markup("<span font='12'> X:   0 </span>")
		self.scoreo.set_markup("<span font='12'> O:   0 </span>")
		hbox = Gtk.Box(spacing = 25)
		hbox.pack_start(self.scorex, True, True, 0)
		hbox.pack_start(Gtk.VSeparator(), 1, 1, 0)
		hbox.pack_start(self.scoreo, 1, 1, 0)
		label1 = Gtk.Label(label = "")
		label1.set_markup("<span font='15'> LEADERBOARD </span>")
		vbox.pack_start(label1, True, True, 0)
		vbox.pack_start(hbox, 1, 1, 0)
		
		
		
		
		vbox.pack_start(Gtk.HSeparator(), True, True, 0)
		self.turnview.set_markup("<span font='25'>"+self.turn+"'s turn</span>")
		
		vbox.pack_start(self.turnview, True, True, 0)
		l = b = 1
		grid = Gtk.Grid()
		vbox.pack_start(grid, True, True, 0)
		credits = Gtk.Label(label = "", xalign=1)
		credits.set_markup("<span font='10'> Made with ❤ by <a href='https://www.github.com/devmrfitz'> Aditya </a></span>")
		vbox.pack_start(credits, 1, 1, 0)
		
		for _ in range(3):
			for __ in range(3):
				self.list[_].append(Gtk.Button())
				self.list[_][__].connect("clicked",self.click,_,__)

		grid.attach(self.list[0][0], 0, 0, l, b)

		grid.attach_next_to(self.list[0][1], self.list[0][0], Gtk.PositionType.RIGHT, l, b)
		grid.attach_next_to(self.list[0][2], self.list[0][1], Gtk.PositionType.RIGHT, l, b)
		grid.attach_next_to(self.list[1][0], self.list[0][0], Gtk.PositionType.BOTTOM, l, b)
		grid.attach_next_to(self.list[1][1], self.list[1][0], Gtk.PositionType.RIGHT, l, b)
		grid.attach_next_to(self.list[1][2], self.list[1][1], Gtk.PositionType.RIGHT, l, b)
		grid.attach_next_to(self.list[2][0], self.list[1][0], Gtk.PositionType.BOTTOM, l, b)
		grid.attach_next_to(self.list[2][1], self.list[2][0], Gtk.PositionType.RIGHT, l, b)
		grid.attach_next_to(self.list[2][2], self.list[2][1], Gtk.PositionType.RIGHT, l, b)

		for li in self.list:
			for button in li:
				button.set_label("")
				button.get_child().set_markup("<span font='70'>     </span>")



	def click(self, widget, *uu):
		print("trigger")
		_ = int(uu[0])
		__ = int(uu[1])
		widget.get_child().set_markup("<span font='70'>  "+self.turn+"  </span>")
		if self.turn == "X":
			if _ == 0:
				if __ == 0:
					self.storex["dl"] += 1
					self.storex["v1"] += 1
					self.storex["h1"] += 1
				elif __ == 1:
                                        self.storex["v2"] += 1
                                        self.storex["h1"] += 1
				elif __ == 2:
                                        self.storex["v3"] += 1
                                        self.storex["h1"] += 1
                                        self.storex["dr"] += 1
			elif _ == 1:
                                if __ == 0:
                                        self.storex["v1"] += 1
                                        self.storex["h2"] += 1
                                elif __ == 1:
                                        self.storex["v2"] += 1
                                        self.storex["h2"] += 1
                                        self.storex["dl"] += 1
                                        self.storex["dr"] += 1
                                elif __ == 2:
                                        self.storex["v3"] += 1
                                        self.storex["h2"] += 1
			elif _ == 2:
                                if __ == 0:
                                        self.storex["v1"] += 1
                                        self.storex["h3"] += 1
                                        self.storex["dr"] += 1
                                elif __ == 1:
                                        self.storex["v2"] += 1
                                        self.storex["h3"] += 1
                                elif __ == 2:
                                        self.storex["v3"] += 1
                                        self.storex["h3"] += 1
                                        self.storex["dl"] += 1
			self.turn = "O"
		else:
                        if _ == 0:
                                if __ == 0:
                                        self.storeo["dl"] += 1
                                        self.storeo["v1"] += 1
                                        self.storeo["h1"] += 1
                                elif __ == 1:
                                        self.storeo["v2"] += 1
                                        self.storeo["h1"] += 1
                                elif __ == 2:
                                        self.storeo["v3"] += 1
                                        self.storeo["h1"] += 1
                                        self.storeo["dr"] += 1
                        elif _ == 1:
                                if __ == 0:
                                        self.storeo["v1"] += 1
                                        self.storeo["h2"] += 1
                                elif __ == 1:
                                        self.storeo["v2"] += 1
                                        self.storeo["h2"] += 1
                                        self.storeo["dl"] += 1
                                        self.storeo["dr"] += 1
                                elif __ == 2:
                                        self.storeo["v3"] += 1
                                        self.storeo["h2"] += 1
                        elif _ == 2:
                                if __ == 0: 
                                        self.storeo["v1"] += 1
                                        self.storeo["h3"] += 1
                                        self.storeo["dr"] += 1
                                elif __ == 1:
                                        self.storeo["v2"] += 1
                                        self.storeo["h3"] += 1
                                elif __ == 2:
                                        self.storeo["v3"] += 1
                                        self.storeo["h3"] += 1
                                        self.storeo["dl"] += 1
                        self.turn = "X"
		self.turnview.set_markup("<span font='25'>"+self.turn+"'s turn</span>")
		if 3 in self.storex.values():
			self.declare_winner("X")
		if 3 in self.storeo.values():
			self.declare_winner("O")

	def declare_winner(self, ch):
		self.incscore(ch)
		for li in self.list:
			for button in li:
				button.set_label("")
				button.get_child().set_markup("<span font='70'>     </span>")
		self.turn = ch.upper()
		self.turnview.set_markup("<span font='25'>"+self.turn+" wins!!! "+self.turn+"'s turn</span>")
		self.storex = {"dl":0,"dr":0,"v1":0,"v2":0,"v3":0, "h1":0,"h2":0, "h3":0}
		self.storeo = {"dl":0,"dr":0,"v1":0,"v2":0,"v3":0, "h1":0,"h2":0, "h3":0}
	
	def incscore(self, ch):
		if ch.upper() == "X":
			self.x += 1
			self.scorex.set_markup("<span font='12'> X:   "+str(self.x)+"</span>")
		elif ch.upper() == "O":
			self.o += 1
			self.scoreo.set_markup("<span font='12'> O:   "+str(self.o)+"</span>")	

		
		

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
