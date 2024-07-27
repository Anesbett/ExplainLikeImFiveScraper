import wx
from webscraperLogic import QueryEngine
from Menu import MenuBar

class Frame(wx.Frame):
    def __init__(self, query_engine, *args, **kw):
        super(Frame, self).__init__(*args, **kw)
        
        # Store the query engine instance
        self.query_engine = query_engine
        
        # Create a panel to hold the UI elements
        pnl = wx.Panel(self)

        # Load sizes from the configuration file
        query_text_size = self.query_engine.config['query_text_size']
        result_text_size = self.query_engine.config['result_text_size']
        frame_size = self.query_engine.config['frame_size']
        
        # Create a static text control for the welcome message
        welcome_text = wx.StaticText(pnl, label="Welcome to the r/ExplainLikeImFive Scraper!")
        font = welcome_text.GetFont()
        font.PointSize += 10
        welcome_text.SetFont(font)
        
        # Create a static text control for the helper message
        helper_text = wx.StaticText(pnl, label="Please enter a query to search the r/ExplainLikeImFive subreddit...")
        font = helper_text.GetFont()
        font.PointSize += 1
        helper_text.SetFont(font)

        # Create the text control for user input
        self.query_text = wx.TextCtrl(pnl, style=wx.TE_MULTILINE, size=query_text_size)
        
        # Create the text control for displaying results
        self.result_text = wx.TextCtrl(pnl, style=wx.TE_MULTILINE | wx.TE_READONLY, size=result_text_size)
        
        # Create the search button and bind the click event to the search method
        search_button = wx.Button(pnl, label="Search")
        search_button.Bind(wx.EVT_BUTTON, self.on_search)
        
        # Create a vertical box sizer to manage the layout of the UI elements
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(welcome_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(helper_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.query_text, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(search_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.result_text, 2, wx.EXPAND | wx.ALL, 5)
        
        # Set the sizer for the panel
        pnl.SetSizer(sizer)
        
        # Set the frame size from the configuration file
        self.SetSize(frame_size)
        
        # Set the frame title
        self.SetTitle("Reddit Query App")
        
        self.SetMenuBar(MenuBar(self, query_engine))

    def on_search(self, event):
        """Handle the search button click event."""
        # Get the query from the user input text control
        query = self.query_text.GetValue()
        
        # Get the search results from the query engine
        results = self.query_engine.get_reddit_posts(query)
        
        # Format the results into a string
        result_text = "\n\n".join([f"Title: {post['title']}\nScore: {post['score']}\nURL: {post['url']}\n{'-'*20}" for post in results])
        
        # Display the results in the result text control
        self.result_text.SetValue(result_text)

if __name__ == "__main__":
    # Create the application instance
    app = wx.App()
    
    # Create the query engine instance
    query_engine = QueryEngine()
    
    # Create and show the main frame
    frm = Frame(query_engine, None)
    frm.Show()
    
    # Start the application main loop
    app.MainLoop()
