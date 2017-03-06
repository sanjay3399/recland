using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Web_2_WebApp_
{
    class URLEntries
    {
        string url;
        string word;
        int count;

        public URLEntries(string url, string word, int count)
        {
            this.url = url;
            this.count = count;
            this.word = word;
        }
        public int Count
        {
            get { return count; }
            set { count = value; }
        }
        public string Url
        {
            get { return url; }
            set { url = value; }
        }
        public string Word
        {
            get { return word; }
            set { word = value; }
        }
    }
}