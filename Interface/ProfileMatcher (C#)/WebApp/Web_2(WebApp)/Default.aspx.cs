using System;
using System.Collections.Generic;
using System.Linq;
using System.Web.UI.WebControls;
using System.Data;

namespace Web_2_WebApp_
{
    public partial class Default : System.Web.UI.Page
    {
        private static List<RankedURL> URLFound = new List<RankedURL>();

        protected void Page_Load(object sender, EventArgs e)
        {
            LoadGridData(1);
        }

        private void LoadGridData(int state = 0)
        {
            DataTable dt = new DataTable();
            dt.Columns.Add("Name");
            dt.Columns.Add("Title");
            dt.Columns.Add("CurrentLocation");
            dt.Columns.Add("Experience");
            dt.Columns.Add("PayRate");
            dt.Columns.Add("Relocate");
            dt.Columns.Add("URL");
            if (state == 0)
            {
                if (URLFound.Count > 0)
                {
                    /*
                    for (int i = 0; i < URLFound.Count; i++)
                    {
                        DataRow dr = dt.NewRow();
                        dr["Sr"] = i + 1;
                        dr["URL"] = URLFound[i].WordPerURLCount.Keys.ToList<string>()[0] + "\r\n";
                        // String.Format("<a href=\"{0}\">{0}</a>")
                        foreach (KeyValuePair<string, Dictionary<string, int>> item2 in URLFound[i].WordPerURLCount)
                        {
                            foreach (KeyValuePair<string, int> item3 in item2.Value)
                            {
                                dr["Match"] += "\n(" + item3.Key + ":" + item3.Value + ") ";
                            }
                        }
                        dt.Rows.Add(dr);
                    }
                    */
                }
                else
                {
                    DataRow dr = dt.NewRow();
                    dr["CurrentLocation"] = "No results found";
                    dt.Rows.Add(dr);
                }
            }
            else
            {
                DataRow dr = dt.NewRow();
                dr["CurrentLocation"] = "Please do a search";
                dt.Rows.Add(dr);
            }
            grdData.DataSource = dt;
            grdData.DataBind();
        }
        protected void grdData_PageIndexChanging(object sender, GridViewPageEventArgs e)
        {
            grdData.PageIndex = e.NewPageIndex;
            LoadGridData();
        }

        protected void btnSearch_Click(object sender, EventArgs e)
        {
            Controller.Manager(txtQuery.Text);
            URLFound = new List<RankedURL>();
            URLFound = Controller.URLFOUND;
            LoadGridData();
        }
    }
}