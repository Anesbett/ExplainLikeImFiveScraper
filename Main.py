import wx
from WebScraperLogic import QueryEngine
from GUI import Frame

if __name__ == "__main__":
    app = wx.App()
    query_engine = QueryEngine()
    frm = Frame(query_engine, None)
    frm.Show()
    app.MainLoop()