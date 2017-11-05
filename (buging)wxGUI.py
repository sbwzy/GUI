import wx
import turtle

class MyFrame:
       pass

class MyApp(wx.App):
       def OnInit(self):
              frame = wx.Frame(parent = None,
                               title = "SBW's tool",
                               size = (400,200),
                               pos = (300,300)
                               )                    #框架窗口对象
              
              panel = wx.Panel(frame,-1)
              
              self.buttonWJX = wx.Button(panel,
                                         -1,
                                         "五角星",
                                         size = (75,25),
                                         pos = (50,50)
                                         )
              
              self.buttonSJX = wx.Button(panel,
                                         -1,
                                         "三角形",
                                         size = (75,25),
                                         pos = (175,50)
                                         )
              
              self.Bind(wx.EVT_BUTTON,
                        self.OnButtonWJX,
                        self.buttonWJX
                        )

              self.Bind(wx.EVT_BUTTON,
                        self.OnButtonSJX,
                        self.buttonSJX
                        )
              
              frame.Show()                          #显示框架窗口
              return True

       def OnButtonWJX(self,event):
              for i in range(5):
                     turtle.forward(100)
                     turtle.right(144)

       def OnButtonSJX(self,event):
              for i in range(3):
                     turtle.forward(100)
                     turtle.right(120)




if __name__ == "__main__":
       app = MyApp()     #应用程序对象
       app.MainLoop()    #进入消息循环
