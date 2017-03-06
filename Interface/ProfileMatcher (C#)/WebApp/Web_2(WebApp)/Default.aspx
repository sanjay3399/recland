<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="Web_2_WebApp_.Default" EnableSessionState="false"%>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>My Site</title>
    <link rel="stylesheet" href="Content/Style.css" type="text/css"/>
    <style type="text/css">
        .auto-style1 {
            width: 217px;
        }
    </style>
</head>
<body>
    <div id="container">
        <div id="header">
            <h1>Profile Recommender</h1>
        </div>
        <div id="content">
            <div id="main">
                <h3 style="font-family: Calibri; font-size: x-large; font-weight: normal; font-style: normal; color: #000000">Enter job description</h3>
                <form id="form1" runat="server">
                    <div>
                        <table>
                            <tr>
                                <td>
                                    <asp:TextBox ID="txtQuery" runat="server" Font-Names="Calibri" Font-Size="Larger" Height="28px" Width="755px"></asp:TextBox>
                                    <br /><br /><br />
                                </td>
                                <td>&nbsp;</td>
                                <td>
                                    <asp:Button ID="btnSearch" runat="server" Text="Search" Height="34px" Width="100px" BackColor="#3399FF" Font-Names="Calibri" Font-Size="Large" ForeColor="White" OnClick="btnSearch_Click" />
                                    <br /><br /><br />
                                </td>
                            </tr>
                            <tr>
                                <asp:gridview ID="grdData" runat="server" 
                                    AutoGenerateColumns="False" CellPadding="4"
                                    ForeColor="#333333" GridLines="None" Width="769px" AllowPaging="True"
                                    OnPageIndexChanging="grdData_PageIndexChanging" Height="75px">
                                    <alternatingrowstyle BackColor="Silver" ForeColor="#284775"></alternatingrowstyle>
                                    <columns>
                                        <asp:boundfield DataField="Name" HeaderText="Name"></asp:boundfield>
                                        <asp:boundfield DataField="Title" HeaderText="Tilte"></asp:boundfield>
                                        <asp:boundfield DataField="CurrentLocation" HeaderText="Current Location"></asp:boundfield>
                                        <asp:BoundField DataField="Experience" HeaderText="Experience" />
                                        <asp:BoundField DataField="PayRate" HeaderText="Pay rate" />
                                        <asp:BoundField DataField="Relocate" HeaderText="Relocate" />
                                        <asp:BoundField DataField="URL" HeaderText="URL" />
                                    </columns>
                                    
                                    <editrowstyle BackColor="#999999"></editrowstyle>
                                    <footerstyle BackColor="#5D7B9D" Font-Bold="True" ForeColor="White"></footerstyle>
                                    <headerstyle BackColor="#808080" Font-Bold="True" ForeColor="White"></headerstyle>
                                    <pagerstyle BackColor="White" ForeColor="Blue" Font-Underline="True" HorizontalAlign="Center"></pagerstyle>
                                    <rowstyle BackColor="#F7F6F3" ForeColor="#333333"></rowstyle>
                                    
                                    <selectedrowstyle BackColor="#E2DED6" Font-Bold="True" ForeColor="#333333"></selectedrowstyle>
                                    <sortedascendingcellstyle BackColor="#E9E7E2"></sortedascendingcellstyle>
                                    <sortedascendingheaderstyle BackColor="#506C8C"></sortedascendingheaderstyle>
                                    <sorteddescendingcellstyle BackColor="#FFFDF8"></sorteddescendingcellstyle>
                                    <sorteddescendingheaderstyle BackColor="#6F8DAE"></sorteddescendingheaderstyle>
                                </asp:gridview>
                            </tr>
                        </table>
                    </div>
                </form>
            </div>
        </div>
        <div id="footer">
            <table>
                <tr><td class="auto-style1">&nbsp;</td></tr>
                <tr><td class="auto-style1">&nbsp;</td></tr>
                <tr><td class="auto-style1">&nbsp;</td></tr>
            </table>
            Copyright &copy; 2017 Saboor Ahmad. </div>
    </div>
    
</body>
</html>

