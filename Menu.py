import wx

class MenuBar(wx.MenuBar):
    def __init__(self, frame, query_engine):
        super(MenuBar, self).__init__()

        self.frame = frame
        self.query_engine = query_engine

        # Create a settings menu
        settings_menu = wx.Menu()

        # Add items to the settings menu
        client_id_item = settings_menu.Append(wx.ID_ANY, "Set Client ID")
        client_secret_item = settings_menu.Append(wx.ID_ANY, "Set Client Secret")
        user_agent_item = settings_menu.Append(wx.ID_ANY, "Set User Agent")

        # Bind menu items to methods
        self.frame.Bind(wx.EVT_MENU, self.on_set_client_id, client_id_item)
        self.frame.Bind(wx.EVT_MENU, self.on_set_client_secret, client_secret_item)
        self.frame.Bind(wx.EVT_MENU, self.on_set_user_agent, user_agent_item)

        # Add settings menu to the menu bar
        self.Append(settings_menu, "&Settings")

    def on_set_client_id(self, event):
        """Handle setting the client ID."""
        dlg = wx.TextEntryDialog(self.frame, "Enter Client ID:", "Set Client ID")
        if dlg.ShowModal() == wx.ID_OK:
            client_id = dlg.GetValue()
            self.query_engine.config['client_id'] = client_id
            self.query_engine.save_config()

    def on_set_client_secret(self, event):
        """Handle setting the client secret."""
        dlg = wx.TextEntryDialog(self.frame, "Enter Client Secret:", "Set Client Secret")
        if dlg.ShowModal() == wx.ID_OK:
            client_secret = dlg.GetValue()
            self.query_engine.config['client_secret'] = client_secret
            self.query_engine.save_config()

    def on_set_user_agent(self, event):
        """Handle setting the user agent."""
        dlg = wx.TextEntryDialog(self.frame, "Enter User Agent:", "Set User Agent")
        if dlg.ShowModal() == wx.ID_OK:
            user_agent = dlg.GetValue()
            self.query_engine.config['user_agent'] = user_agent
            self.query_engine.save_config()
