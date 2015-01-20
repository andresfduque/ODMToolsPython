# -*- coding: utf-8 -*-############################################################################# Python code generated with wxFormBuilder (version Sep 12 2010)## http://www.wxformbuilder.org/#### PLEASE DO "NOT" EDIT THIS FILE!###########################################################################import wximport stringALPHA_ONLY = 1DIGIT_ONLY = 2class MyValidator(wx.PyValidator):    def __init__(self, flag=None, pyVar=None):        wx.PyValidator.__init__(self)        self.flag = flag        self.Bind(wx.EVT_CHAR, self.OnChar)    def Clone(self):        return MyValidator(self.flag)    def Validate(self, win):        tc = self.GetWindow()        val = tc.GetValue()        #if self.flag == ALPHA_ONLY:        #    for x in val:        #        if x not in string.letters:        #            return False        for x in val:            if x not in string.digits:                return False        return True    def OnChar(self, event):        key = event.GetKeyCode()        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:            event.Skip()            return        if self.flag == ALPHA_ONLY and chr(key) in string.letters:            event.Skip()            return        if self.flag == DIGIT_ONLY and chr(key) in string.digits + '.':            event.Skip()            return        if not wx.Validator_IsSilent():            wx.Bell()        # Returning without calling even.Skip eats the event before it        # gets to the text control        return    def TransferToWindow(self):        """ Transfer data from validator to window.            The default implementation returns False, indicating that an error            occurred.  We simply return True, as we don't do any data transfer.        """        return True # Prevent wxDialog from complaining.    def TransferFromWindow(self):        """ Transfer data from window to validator.            The default implementation returns False, indicating that an error            occurred.  We simply return True, as we don't do any data transfer.        """        return True # Prevent wxDialog from complaining.############################################################################# Class MyDialog1###########################################################################class MyDialog1 ( wx.Dialog ):    def __init__( self, parent ):        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Derive New Series", pos = wx.DefaultPosition, size = wx.Size( 775,350 ), style = wx.DEFAULT_DIALOG_STYLE )        self.SetSizeHintsSz( wx.Size( 600,350 ), wx.DefaultSize )        bSizer1 = wx.BoxSizer( wx.VERTICAL )        fgSizer1 = wx.FlexGridSizer( 4, 2, 0, 0 )        fgSizer1.SetFlexibleDirection( wx.BOTH )        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )        self.rbtn_derive_copy = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )        fgSizer1.Add( self.rbtn_derive_copy, 0, wx.ALL, 5 )        self.st_derive_copy = wx.StaticText( self, wx.ID_ANY, u"Derive A Copy Of Data For Editing", wx.DefaultPosition, wx.DefaultSize, 0 )        self.st_derive_copy.Wrap( -1 )        self.st_derive_copy.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )        fgSizer1.Add( self.st_derive_copy, 0, wx.ALL, 5 )        fgSizer3 = wx.FlexGridSizer( 2, 2, 0, 0 )        fgSizer3.SetFlexibleDirection( wx.BOTH )        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )        self.rbtn_agg_funtion = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )        fgSizer3.Add( self.rbtn_agg_funtion, 0, wx.ALIGN_TOP|wx.ALL, 5 )        fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )        fgSizer2 = wx.FlexGridSizer( 2, 1, 0, 0 )        fgSizer2.SetFlexibleDirection( wx.BOTH )        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )        self.st_agg_function = wx.StaticText( self, wx.ID_ANY, u"Derive Using Aggregate Function", wx.DefaultPosition, wx.DefaultSize, 0 )        self.st_agg_function.Wrap( -1 )        fgSizer2.Add( self.st_agg_function, 0, wx.ALL, 5 )        rb_agg_functionChoices = [ u"Daily", u"Monthly", u"Quarterly", u"Maximum", u"Minimum", u"Average", u"Sum" ]        self.rb_agg_function = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, rb_agg_functionChoices, 2, wx.RA_SPECIFY_ROWS )        self.rb_agg_function.SetSelection( 0 )        fgSizer2.Add( self.rb_agg_function, 0, wx.ALL, 5 )        fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )        self.m_radioBtn4 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )        fgSizer1.Add( self.m_radioBtn4, 0, wx.ALL, 5 )        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Derive Using Algebraic Equation", wx.DefaultPosition, wx.DefaultSize, 0 )        self.m_staticText9.Wrap( -1 )        fgSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )        fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )        fgSizer5 = wx.FlexGridSizer( 1, 13, 0, 0 )        fgSizer5.SetFlexibleDirection( wx.BOTH )        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Y =", wx.DefaultPosition, wx.DefaultSize, 0 )        self.m_staticText17.Wrap( -1 )        fgSizer5.Add( self.m_staticText17, 0, wx.ALL, 5 )        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, validator=MyValidator(DIGIT_ONLY) )        fgSizer5.Add( self.m_textCtrl2, 0, wx.ALL, 5 )        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )        self.m_staticText18.Wrap( -1 )        fgSizer5.Add( self.m_staticText18, 0, wx.ALL, 5 )        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, validator=MyValidator(DIGIT_ONLY) )        fgSizer5.Add( self.m_textCtrl3, 0, wx.ALL, 5 )        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"x +", wx.DefaultPosition, wx.DefaultSize, 0 )        self.m_staticText19.Wrap( -1 )        fgSizer5.Add( self.m_staticText19, 0, wx.ALL, 5 )        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, validator=MyValidator(DIGIT_ONLY) )        fgSizer5.Add( self.m_textCtrl4, 0, wx.ALL, 5 )        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"x^2 +", wx.DefaultPosition, wx.DefaultSize, 0 )        self.m_staticText20.Wrap( -1 )        fgSizer5.Add( self.m_staticText20, 0, wx.ALL, 5 )        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, validator=MyValidator(DIGIT_ONLY) )        fgSizer5.Add( self.m_textCtrl5, 0, wx.ALL, 5 )        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"x^3 +", wx.DefaultPosition, wx.DefaultSize, 0 )        self.m_staticText21.Wrap( -1 )        fgSizer5.Add( self.m_staticText21, 0, wx.ALL, 5 )        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, validator=MyValidator(DIGIT_ONLY) )        fgSizer5.Add( self.m_textCtrl6, 0, wx.ALL, 5 )        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"x^4 +", wx.DefaultPosition, wx.DefaultSize, 0 )        self.m_staticText22.Wrap( -1 )        fgSizer5.Add( self.m_staticText22, 0, wx.ALL, 5 )        self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, validator=MyValidator(DIGIT_ONLY) )        fgSizer5.Add( self.m_textCtrl7, 0, wx.ALL, 5 )        self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"x^5", wx.DefaultPosition, wx.DefaultSize, 0 )        self.m_staticText23.Wrap( -1 )        fgSizer5.Add( self.m_staticText23, 0, wx.ALL, 5 )        sbSizer2.Add( fgSizer5, 1, wx.EXPAND, 5 )        fgSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )        bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )        self.btn_newDataSeries = wx.Button( self, wx.ID_ANY, u"New Data Series", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )        bSizer3.Add( self.btn_newDataSeries, 0, wx.ALL, 5 )        self.btn_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )        bSizer3.Add( self.btn_cancel, 0, wx.ALL, 5 )        bSizer1.Add( bSizer3, 1, wx.ALL|wx.EXPAND, 5 )        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Derive Options" ), wx.VERTICAL )        bSizer1.Add( sbSizer5, 1, wx.EXPAND, 5 )        self.SetSizer( bSizer1 )        self.Layout()        self.Centre( wx.BOTH )    def __del__( self ):        pass