import wx
class PyvaFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,
			pos = wx.DefaultPosition, size = wx.Size(450,100),
			style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
			wx.CLOSE_BOX | wx.CLIP_CHILDREN,
			title = "PyVa")
		panel = wx.Panel(self)
		my_sizer = wx.BoxSizer(wx.VERTICAL)
		lbl = wx.StaticText(panel,
			label = "How can I help U ?")
		my_sizer.Add(lbl,0,wx.ALL, 5)

		self.txt = wx.TextCtrl(panel,style = wx.TE_PROCESS_ENTER,
			size=(400,30))
		self.txt.SetFocus()
		self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
		my_sizer.Add(self.txt,0, wx.ALL, 5)
		panel.SetSizer(my_sizer)
		self.Show()
	
	def OnEnter(self, event):
		input = self.txt.GetValue()
		input = input.lower()
		print "Worked !"

if __name__ == "__main__":
	app = wx.App(True)
	frame = PyvaFrame()
	app.MainLoop()