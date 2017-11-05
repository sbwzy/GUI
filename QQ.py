import wx
import time

class MyFrame(wx.Frame):
       def __init__(self):
              wx.Frame.__init__(self,
                                None,
                                -1,
                                "SBW's Chat",
                                size = (520,450)
                                )
              
              panel = wx.Panel(self)
              
              labelAll = wx.StaticText(panel,
                                       -1,
                                       "All Contents"
                                       )

              self.textAll = wx.TextCtrl(panel,
                                         -1,
                                         size = (480,200),
                                         style = wx.TE_MULTILINE | wx.TE_READLINE
                                         )

              labelIn = wx.StaticText(panel,
                                       -1,
                                       "You Say"
                                       )
              
              self.textIn = wx.TextCtrl(panel,
                                         -1,
                                         size = (480,100),
                                         style = wx.TE_MULTILINE
                                        )
              
              self.btnSent = wx.Button(panel,
                                       -1,
                                       "Sent",
                                       size = (75,25)
                                       )
              self.btnClear = wx.Button(panel,
                                        -1,
                                        "Clear",
                                        size = (75,25)
                                        )
              self.Bind(wx.EVT_BUTTON,
                        self.OnButtonSent,
                        self.btnSent)
              
              self.Bind(wx.EVT_BUTTON,
                        self.OnButtonClear,
                        self.btnClear)

              btnSizer = wx.BoxSizer()
              btnSizer.Add(self.btnSent,proportion = 0)
              btnSizer.Add(self.Clear,proportion = 0)

              mainSizer = wx.BoxSizer(wx.VERTICAL)
              mainSizer.Add(labalAll,proportion = 0)
              mainSizer.Add(self.textAll,proportion = 1)
              mainSizer.Add(labalIn,proportion = 0)
              mainSizer.Add(self.textIn,proportion = 0)
              mainSizer.Add(btnSizer,proportion = 0)

              panel.SetSizer(mainSizer)

       def OnButtonSent(self,event):
              userinput = self.textIn.GetValue()
              self.textIn.Clear()
              now = time.ctime()
              inmsg = "You (%s):\n%s \n" % (now,userinput)
              self.textAll.AppendText(inmsg)
              #self.textAll.SetValue(userinput)

       def OnButtonClear(self,event):
              pass
                                       

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
