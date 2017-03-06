using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Data;

namespace Web_2_WebApp_
{
    public class Controller
    {
        private static List<string> queryTokens = new List<string>();
        private static List<RankedURL> URLFound = new List<RankedURL>();

        private static DatabaseConnection objConnect;
        private static string conString;

        private static DataSet ds;
        private static DataRow dRow;

        public Controller()
        {
            try
            {
                objConnect = new DatabaseConnection();
                conString = Properties.Settings.Default.ConnectionString;

                objConnect.connection_string = conString;

                objConnect.Sql = Properties.Settings.Default.SQLWordCount;
                objConnect.TableName = "WordCount";
                ds = objConnect.GetConnection;
            }
            catch (Exception)
            {
                Console.WriteLine("ERROR INITIALIZING RESOURCES - in Controller()");
            }
        }

        internal static List<RankedURL> URLFOUND
        {
            get { return Controller.URLFound; }
            set { Controller.URLFound = value; }
        }

        public static void Manager(string query)
        {
            try
            {
                objConnect = new DatabaseConnection();
                conString = Properties.Settings.Default.ConnectionString;

                objConnect.connection_string = conString;

                objConnect.Sql = Properties.Settings.Default.SQLWordCount;
                objConnect.TableName = "WordCount";
                ds = objConnect.GetConnection;

                queryTokens.AddRange(query.Split(' '));
                for (int i = 0; i < queryTokens.Count; i++)
                {
                    queryTokens[i].ToLower();
                }
                URLFound = NavigateRecords();
            }
            catch (Exception)
            {
                Console.WriteLine("ERROR INITIALIZING RESOURCES - in Controller()");
            }
        }

        private static List<URLEntries> Navigate()
        {
            List<URLEntries> dataList = new List<URLEntries>();
            int i = 0;
            do
            {
                try
                {
                    dRow = ds.Tables[0].Rows[i];
                }
                catch (Exception)
                {
                    dRow = null;
                    break;
                }

                string url = dRow.ItemArray.GetValue(0).ToString();
                string word = dRow.ItemArray.GetValue(1).ToString();
                int count = Convert.ToInt32(dRow.ItemArray.GetValue(2).ToString());

                if (queryTokens.Contains(word))
                    dataList.Add(new URLEntries(url, word, count));
                ++i;
            }
            while (true);
            return dataList;
        }

        private static List<RankedURL> NavigateRecords()
        {
            // rank -> url -> word, count
            List<RankedURL> wordPerRankCount = new List<RankedURL>();
            Dictionary<string, Dictionary<string, int>> wordPerURLCount = new Dictionary<string, Dictionary<string, int>>();
            Dictionary<string, int> wordCount = new Dictionary<string, int>();
            List<string> urlDone = new List<string>();

            List<URLEntries> dataList = Navigate();

            int currCount = 0;
            foreach (URLEntries outerEntry in dataList)
            {
                if (!urlDone.Contains(outerEntry.Url))
                {
                    currCount = 0;
                    foreach (URLEntries innerEntry in dataList)
                    {
                        if (outerEntry.Url.Equals(innerEntry.Url))
                        {
                            wordCount.Add(innerEntry.Word, innerEntry.Count);
                            currCount += innerEntry.Count;
                        }
                    }
                    wordPerURLCount.Add(outerEntry.Url, wordCount);
                    urlDone.Add(outerEntry.Url);
                    wordPerRankCount.Add(new RankedURL(currCount, wordPerURLCount));

                    wordPerURLCount = new Dictionary<string, Dictionary<string, int>>();
                    wordCount = new Dictionary<string, int>();
                }
            }

            List<RankedURL> orderedByName = wordPerRankCount.OrderByDescending(item => item.Rank).ToList();
            return orderedByName;
        }
    }
}